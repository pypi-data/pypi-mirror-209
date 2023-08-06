from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='iva_order_selection',
      version='0.0.2',
      description='Implementation of CMI-IVA',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
      ],
      keywords='iva, model order selection, multiset analysis, common and distinct',
      url='https://mlsp.umbc.edu/Siddique',
      author='M. A. B. S. Akhonda',
      author_email='akhondams@nih.gov',
      license='LICENSE',
      packages=['iva_order_selection'],
      python_requires='>=3.6',
      install_requires=[
          'numpy',
          'scipy',
          'pytest',
          'joblib',
          'tqdm',
          'matplotlib',
      ],
      include_package_data=True,  # to include non .py-files listed in MANIFEST.in
      zip_safe=False)
