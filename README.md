# dp_seminar
Repository for the course Seminar: Privacy Preserving Machine Learning, HY 2019  

- pca_linear_regression.ipynb and pca_logistic_regression.ipynb run simulations of the Gaussian Mechanism and the Wishart Mechanism  
- both these mechanisms are used to produce a noisy empirical covariance matrix of a data set  
- PCA is then applied on the noisy matrix, the highest resulting eigenvalues are then used to reduce the dimension of the data set   
- these lower dimensional data set are then used to train and test linear regressions and logistic regression(we train these for various privacy parameters, e.g., for various inputs for the Gaussian and the Wishart Mechanisms)  
- dp_algorithms.py contains the code for the Gaussian Mechanism and the Wishart Mechanism(partially for this one, we draw this one via R in create_wishart_matrix.R; for the Wishart symmetrical noise matrix we run the function from dp_algorithms, this functions invokes as a subprocess the R file create_wishart_matrix.R)  
