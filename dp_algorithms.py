import subprocess
import numpy as np

def gaussian_mechanism(data_matrix, epsilon, delta):

    variance = 2 * np.log(1.25 / delta) / (epsilon ** 2)

    if variance <= 0:

        print("This is not going to work, the variance needs to be bigger than 0")
        print("Bye!")

        return -1

    else:

        # calculate the empirical covariance matrix
        empirical_covariance_matrix = np.matmul(data_matrix.transpose(), data_matrix)
        empirical_covariance_matrix /= len(data_matrix)

        # draw the noise and construct the symmetrical noise matrix
        noise = np.random.normal(0, variance, (len(empirical_covariance_matrix), len(empirical_covariance_matrix)))
        noise_matrix = np.tril(noise) + np.tril(noise, -1).T

        empirical_covariance_matrix += noise_matrix

        return empirical_covariance_matrix


def laplace_mechanism(data_matrix, epsilon):

    variance = 2 * data_matrix.shape[1] / (data_matrix.shape[0] * epsilon)

    if variance <= 0:

        print("This is not going to work out well for you so I am just going to stop now ...")
        print("Variance needs to be bigger than 0")
        print("Bye")

        return -1

    else:

        # calculate the empirical covariance matrix
        empirical_covariance_matrix = np.matmul(data_matrix.transpose(), data_matrix)
        empirical_covariance_matrix /= len(data_matrix)

        # draw the noise and construct the symmetrical noise matrix
        noise = np.random.laplace(0, variance, (len(empirical_covariance_matrix), len(empirical_covariance_matrix)))
        noise_matrix = np.tril(noise) + np.tril(noise, -1).T

        empirical_covariance_matrix += noise_matrix

        return empirical_covariance_matrix


def wishart_mechanism(data_matrix, epsilon):
    '''
        The code works BUT, the mechanism in itself does NOT offer differencial privacy;
        the paper that proposed said mechanism was retracted, more information here:
        https://ergodicity.net/2017/04/07/retraction-for-symmetric-matrix-perturbation-for-differentially-private-principal-component-analysis-icassp-2016/
    '''

    # the data matrix is a pandas frame

    n = data_matrix.shape[1]
    c_value = 3 / (2 * len(data_matrix) * epsilon)

    # draw the wishart matrix using R
    command = 'Rscript'
    path    = 'create_wishart_matrix.R'
    args    = [str(n), str(c_value)]
    cmd     = [command, path] + args

    output = subprocess.check_output(cmd, universal_newlines = True)

    numerical = [float(value) for value in output.split(" ")]
    numerical = np.array(numerical)
    numerical = numerical.reshape([n, n])

    # calculate the noisy empirical covariance matrix
    empirical_covariance_matrix = np.matmul(data_matrix.transpose(), data_matrix)
    empirical_covariance_matrix /= len(data_matrix)
    empirical_covariance_matrix += numerical

    return empirical_covariance_matrix
