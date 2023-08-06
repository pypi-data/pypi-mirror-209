# Comple Model Identification using Independent Vector Analysis (CMI-IVA)
   
This package contains the Python versions of CMI-IVA [1].

For CMI-IVA please visit:
- https://mlsp.umbc.edu/Siddique

For IVA please visit:
- http://mlsp.umbc.edu/jointBSS_introduction.html
- https://github.com/SSTGroup/independent_vector_analysis



Installing iva_order_selection	

	pip install independent_vector_analysis

####################################################

Pre-requisite:

Installing independent_vector_analysis

The only pre-requisite is to have **Python 3** (>= version 3.6) installed.
The iva package can be installed with

    pip install independent_vector_analysis

Required third party packages will automatically be installed.



################################################### 

First, the imports:

    import numpy as np
    from independent_vector_analysis import *
    from independent_vector_analysis.data_generation import MGGD_generation
	
Example:
	N = 10 # No. Sources
	T = 1000 # No. Samples
	K = 15 # No. datasets (subjects)
	rho = [0.9,0.8,0.7]
	
	# Common and distinct source generation
	source_mat = np.zeros((N,T,K))
	scv_cov_mat = np.zeros((K,K,N))
	
	# Common sources across K datasets
	for i in range(len(rho)):
		(temp,scv_cov_mat[:,:,i]) = MGGD_generation(T,K,'uniform',rho[i],0.5)
		source_mat[i,:,:] = temp.T
	
	# Common sources with sub-group structure across K datasets
	(temp,scv_cov_mat[:,:,len(rho)]) = MGGD_generation(T,K,'block',{'val': 0.01, 'blocks': [(0.9, 0, 3), (0.01, 3,14)]},0.5)
	source_mat[len(rho),:,:] = temp.T
	
	# Distinct sources across K datasets
	for i in range(len(rho)+1,N,1):
		(temp,scv_cov_mat[:,:,i]) = MGGD_generation(T,K,'ar',0.01,0.5)
		source_mat[i,:,:] = temp.T
	
	
	# Create datasets by mixing with randomly generated mixing matrices
	mix_mat = np.random.randn(N,N,K)
	data_mat = np.zeros((N,T,K))
	for k in range(K):
		data_mat[:,:,k] = mix_mat[:,:,k]@source_mat[:,:,k]
		
	# Apply CMI-IVA
	iva_results, Order, Corr_struct = order_selection_iva(data_mat)
	
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

## Contact

akhondams@nih.gov or mo32@umbc.edu

## Citing

If you use this package in an academic paper, please cite [1].

    @INPROCEEDINGS{9523414,
    author={Akhonda, M. A. B. S. and Gabrielson, Ben and Calhoun, Vince D. and Adali, Tülay},
    booktitle={2021 IEEE Data Science and Learning Workshop (DSLW)}, 
    title={Complete Model Identification Using Independent Vector Analysis: Application to the Fusion of Task FMRI Data}, 
    year={2021},
    volume={},
    number={},
    pages={1-6},
    doi={10.1109/DSLW51110.2021.9523414}}
    

[1]  M. A. B. S. Akhonda, B. Gabrielson, V. D. Calhoun and T. Adali,"Complete Model Identification Using Independent Vector Analysis: Application to the Fusion of Task FMRI Data," 2021 IEEE Data Science and Learning Workshop (DSLW), Toronto, ON, Canada, 2021, pp. 1-6, doi: 10.1109/DSLW51110.2021.9523414.

