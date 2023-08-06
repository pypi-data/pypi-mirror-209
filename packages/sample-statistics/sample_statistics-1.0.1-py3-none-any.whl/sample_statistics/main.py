import numpy as np
import statsmodels.stats.api as sms

# The WeightedStatsCalculator class is a tool for calculating weighted statistics on a set of samples.
# It calculates and stores the following statistics measures:
# weighted mean, weighted standard deviation, and standard error of the mean, for a set of weighted data points.
#
# Both add and update methods run in O(n) time. 

class WeightedStatsCalculator:
    """
    A class for calculating weighted statistics on a set of samples.

    Attributes:
    -----------
    samples : dict
        A nested dictionary containing dictionaries with the weighted statistics for each sample.
        Each inner dictionary has the following keys:
        'sample': numpy.ndarray
            The sample data.
        'weights': numpy.ndarray
            The weights for each data point in the sample.
        'weighted_mean': float
            The weighted mean of the sample.
        'weighted_std': float
            The weighted standard deviation of the sample.
        'standard_error_mean': float
            The standard error of the mean of the sample.
    size : int
        The number of samples in the calculator.
    """
    def __init__(self):
        """
        Initializes the WeightedStatsCalculator object with an empty dictionary to store samples and their statistics.
        """
        self.samples = {}
        self.size = 0

    def add(self, sample, weights=None):
        """
        Adds a new sample to the nested dictionary and
        returns the dictionary of this added sample with its statistics.

        Parameters:
        -----------
        sample : 1D array-like
            The sample data to add.
        weights : 1D array-like, optional
            The weights for each data point in the sample. Default is None,
            which gives equal weights to all data points.

        Returns:
        --------
        dict
            A dictionary containing the weighted statistics for the added sample.
        """
        # Check validity of sample and weights
        sample, weights = self._check_sample_and_weights(sample, weights)

        # Calculate weighted statistics
        weighted_mean, weighted_std, sem = self._calculate_statistics(sample=sample, weights=weights)

        # Supress large size samples
        np.set_printoptions(threshold=10, edgeitems=5)

        # Store sample statistics as a dict in the nested dictionary
        # with key name the [current size of the nested dict -1]
        self.samples[self.size]= {
            'sample': sample,
            'weights': weights,
            'weighted_mean': weighted_mean,
            'weighted_std': weighted_std,
            'standard_error_mean': sem
        }

        self.size += 1

        return self.samples[self.size-1]

    def _check_sample_and_weights(self, sample, weights):
        """
        Check the validity of a sample and its corresponding weights and
        return them as 1D numpy arrays.

        Parameters:
        -----------
        sample : 1D array-like
            An array of sample values.
        weights : 1D array-like
            An array of corresponding weights. If None it returns equal weights to all data points.

        Raises:
        -------
        TypeError:
            If the sample is not a 1D array with at least 2 elements or if the weights
            are not a 1D array or if the sample and weights arrays have different sizes.
        ValueError:
            If any weight is not positive.

        Returns:
        --------
        tuple:
            Returns a tuple containing two 1D numpy arrays representing the input
            'sample' and 'weights' after checking their validity.

        """
        # Make sample input a numpy
        sample = np.asarray(sample)

        # Make weights input a numpy
        if weights is None:
            weights = np.ones(len(sample))
        else:
            weights = np.asarray(weights)

        # Check sample validity
        if sample.ndim != 1 or len(sample)<1:
            raise TypeError("Sample must be 1D array with at least 2 elements")

        # Check weights validity
        if weights.ndim != 1:
            raise TypeError("Weights must be a 1D array")

        if np.any(weights <= 0):
            raise ValueError("All weights must be positive and non-zero")

        if len(sample) != len(weights):
            raise TypeError("Sample and Weights must have the same size")

        return sample, weights

    def _calculate_statistics(self, sample, weights=None):
        """
        Calculates the weighted statistics of a sample.

        Parameters:
        -----------
        sample : 1D numpy.ndarray
            The sample to calculate statistics for.
        weights : 1D numpy.ndarray, optional
            The weights for each data point in the sample.

        Returns:
        --------
        tuple of floats
            The weighted mean, weighted standard deviation, and standard error of the mean of the sample, respectively.
        """
        # Calculate statistics
        descr_stats = sms.DescrStatsW(sample, weights=weights, ddof=1)

        return descr_stats.mean, descr_stats.std, descr_stats.std_mean

    def update(self, index, sample=None, weights=None):
        """
        Update the statistics of a particular sample and return its dictionary.

        Parameters:
        -----------
        index : int
            The index of the sample to update.
        sample : 1D array-like, optional
            The new data to be used in the calculation of the sample statistics.
            If not provided, the existing sample data will be used.
            If provided, the weights must also change to the same size.
        weights : 1D array-like, optional
            The new weights to be used in the calculation of the sample statistics.
            If not provided, the existing weights will be used.
            They must have the same size as the sample.
            For the unweighted case, the input weights must be np.ones(len(sample)).

        Returns:
        --------
        dict:
            A dictionary containing the updated sample statistics.
        """
        if index not in self.samples:
            raise IndexError("Sample index not found")

        if sample is None:
            sample = self.samples[index]['sample']

        if weights is None:
            weights = self.samples[index]['weights']

        # Check validity of input
        sample, weights = self._check_sample_and_weights(sample, weights)

        # Calculate statistics
        weighted_mean, weighted_std, sem = self._calculate_statistics(sample=sample, weights=weights)

        # Update the inner dict
        self.samples[index]['sample'] = sample
        self.samples[index]['weights'] = weights
        self.samples[index]['weighted_mean'] = weighted_mean
        self.samples[index]['weighted_std'] = weighted_std
        self.samples[index]['standard_error_mean'] = sem

        return self.samples[index]

    def __call__(self):
        """
        Returns the nested dictionary of samples and their statistics.

        Returns:
        --------
        self.samples : dict
            The nested dictionary of samples and their statistics.
        """
        return self.samples
