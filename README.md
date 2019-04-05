# dp_seminar

UPDATE: for the Wishart Mechanism: it does NOT offer differential privacy. Due to that, the paper that proposed said mechanism was retracted, more information [here](https://ergodicity.net/2017/04/07/retraction-for-symmetric-matrix-perturbation-for-differentially-private-principal-component-analysis-icassp-2016/)

Repository for the course Seminar: Privacy Preserving Machine Learning, HY 2019  

- pca_linear_regression.ipynb and pca_logistic_regression.ipynb run simulations of the Gaussian Mechanism, Wishart Mechanism (that was retracted because it does not ensure privacy), and of the Laplace Mechanism 
- both these mechanisms are used to produce a noisy empirical covariance matrix of a data set  
- PCA is then applied on the noisy matrix, the highest resulting eigenvalues are then used to reduce the dimension of the data set   
- these lower dimensional data set are then used to train and test linear regressions and logistic regression(we train these for various privacy parameters, e.g., for various inputs for the Gaussian, Wishart and Laplace Mechanisms)  
- dp_algorithms.py contains the code for the Gaussian Mechanism, Laplace Mechanism and the Wishart Mechanism(partially for this one, we draw this one via R in create_wishart_matrix.R; for the Wishart symmetrical noise matrix we run the function from dp_algorithms, this functions invokes as a subprocess the R file create_wishart_matrix.R)  
