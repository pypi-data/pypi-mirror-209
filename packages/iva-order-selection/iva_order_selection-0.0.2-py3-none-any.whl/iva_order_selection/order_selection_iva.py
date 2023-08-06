#Implementation of complete model order selection using IVA (CMI-IVA)
# Developed by  M.A.B.S. Akhonda
# Coded by M.A.B.S. Akhonda (mo32 at umbc.edu)
 
# Reference:
#  M. A. B. S. Akhonda, B. Gabrielson, V. D. Calhoun and T. Adali,
#  "Complete Model Identification Using Independent Vector Analysis: Application to the Fusion of Task FMRI Data," 2021 
#  IEEE Data Science and Learning Workshop (DSLW), Toronto, ON, Canada, 2021, pp. 1-6, doi: 10.1109/DSLW51110.2021.9523414.

import numpy as np
from independent_vector_analysis import *

def order_selection_iva(X):
    """
    Input:
        X = np.ndarray containig K datasets (N x T), where N  = number of obervations(Subjects or timepoints), 
        T = Samples (voxels)
         
        Data observations are from K data sets, i.e., X[k] = A[k] @ S[k], where A[k] is an N x N
        unknown invertible mixing matrix, and S[k] is N x T matrix with the nth row corresponding to
        T samples of the nth source in the kth dataset. This enforces the assumption of an equal
        number of samples in each dataset.
       

    Output:
        iva_results: tuple
             -iva_results[0] = W : np.ndarray
                 The estimated demixing matrices of dimensions N x N x K so that ideally
                 W[k] @ A[k] = P @ D[k], where P is any arbitrary permutation matrix and D[k] is any
                 diagonal invertible (scaling) matrix. Note that P is common to all datasets. This is
                 to indicate that the local permutation ambiguity between dependent sources
                 across datasets should ideally be resolved by IVA.

             -iva_results[1] = cost : float
                 The cost for each iteration

             -iva_results[2] = Sigma_N : np.ndarray
                 Covariance matrix of each source component vector, with dimensions K x K x N

             -iva_results[3] = isi : float
         
        Order: dict
             -'mdl': int 
                  Common order estimated by the minimum description length (MDL) criteria 
             -'aic': int
                  Common order estimated by the akaike information criterion (AIC)
             -'mdl_results': np.ndarray
                  Number of subgroup in each SCV estimated by MDL (N)
             -'aic_results': np.ndarray
                  Number of subgroup in each SCV estimated by AIC (N)
        
        Corr_struct: dict
            -'eig': np.ndarray
                  Estimated eigenvalues for each SCV (K x N)
            -'eig_str': np.ndarray
                  Estimated correlation structire in each SCV (K x K x N)
    
    
    Information:
    # Developed by  M.A.B.S. Akhonda
    # Coded by M.A.B.S. Akhonda (mo32 at umbc.edu, akhondams@nih.gov)
 
    Reference:
        Plain text:
            M. A. B. S. Akhonda, B. Gabrielson, V. D. Calhoun and T. Adali,
            "Complete Model Identification Using Independent Vector Analysis: Application to the Fusion of Task FMRI Data," 2021 
            IEEE Data Science and Learning Workshop (DSLW), Toronto, ON, Canada, 2021, pp. 1-6, doi: 10.1109/DSLW51110.2021.9523414.
        
        BibTex:
            @INPROCEEDINGS{9523414,
            author={Akhonda, M. A. B. S. and Gabrielson, Ben and Calhoun, Vince D. and Adali, Tülay},
            booktitle={2021 IEEE Data Science and Learning Workshop (DSLW)}, 
            title={Complete Model Identification Using Independent Vector Analysis: Application to the Fusion of Task FMRI Data}, 
            year={2021},
            volume={},
            number={},
            pages={1-6},
            doi={10.1109/DSLW51110.2021.9523414}}
    """
    
    if X.ndim != 3:
        raise AssertionError('X must have dimensions N x T x K.')
    elif X.shape[2] == 1:
        raise AssertionError('There must be ast least K=2 datasets.')
    
    N,T,K = X.shape # Dimensions 
    
    # Run IVA step to maximize the correlation across modalities 
    iva_results = iva_g(X) # second order statistics used, replace it to use HOS
    de_scv_cov_mat = iva_results[2]; #Source component vector(SCV)
    
    # Common order estimation using eigen-based analysis and information theoretic critrion (ITC) 
    u_svd = np.zeros((K,K,N))
    s_svd = np.zeros((K,N))
    order_mdl = np.zeros(N)
    order_aic = np.zeros(N)
    for i in range(N):
        test_scv = de_scv_cov_mat[:,:,i]
        svd_results = np.linalg.svd(test_scv)
        u_svd[:,:,i] = np.array(svd_results[0])
        s_svd[:,i] = np.array(svd_results[1])


        lambda_s = s_svd[:,i]
        aic = np.zeros(N)
        mdl = np.zeros(N)
        penalty  = np.zeros(N)
        likelihood = np.zeros(N)
        for k in range(N):
            coef = 1/(N-k)
            dem = coef*(np.sum(lambda_s[k:N]))
            num = np.prod(lambda_s[k:N])**coef
            penalty[k] = 0.5*np.log(T)*(k*(2*N-k)+1)
            likelihood[k] = T*np.log(((num/dem)**(N-k)))
            aic[k] = -likelihood[k] + (k*(2*N-k)+1)
            mdl[k] = -likelihood[k] + penalty[k]

        order_mdl[i] = mdl.argmin()
        order_aic[i] = aic.argmin()

    Order = {'mdl':np.count_nonzero(order_mdl),'aic': np.count_nonzero(order_aic), 'mdl_results':order_mdl, 'aic_results':order_aic}
    
    # Common structure identification using eigenvectors
    eig_struc = np.zeros((K,K,N))
    if Order['mdl'] != 0: #Using MDL criteria for better results
        num_corr_comp = Order['mdl']
        for i in range(num_corr_comp):
            temp_eig = Order['mdl_results']
            loc_eig = np.argwhere(temp_eig>0)[:,0]
            num_eig_vec = int(temp_eig[loc_eig[i]])
            for j in range(num_eig_vec):
                temp_eig_vec = np.abs(u_svd[:,j,loc_eig[i]])
                temp_eig_vec = temp_eig_vec/np.max(temp_eig_vec)
                eig_struc[np.argwhere((temp_eig_vec)>0.7)[:,0],j,loc_eig[i]] = 1
    else:
        print('No correlation structure')

    Corr_struct = {'eig':s_svd, 'eig_str':eig_struc}
    
    return iva_results, Order, Corr_struct