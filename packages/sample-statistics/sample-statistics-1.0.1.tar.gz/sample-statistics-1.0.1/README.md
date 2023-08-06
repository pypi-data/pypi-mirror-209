# WeightedStatsCalculator

The WeightedStatsCalculator class is a tool for storing samples and calculating their weighted statistics. It calculates and stores the following statistics measures: weighted mean, weighted standard deviation, and standard error of the mean, for a set of weighted data points. 

## Installation

The WeightedStatsCalculator can be installed using pip:

```
pip install sample-statistics
```

The package is tested on Python 3.7, 3.8, 3.9 and 3.11.

## Getting started

To use the WeightedStatsCalculator, you first need to create an instance of the WeightedStatsCalculator class. You can do this by importing the library and calling the constructor:

```
from sample_statistics import WeightedStatsCalculator

wsc = WeightedStatsCalculator()
```

## Usage

You can then add weighted data points to the calculator using the add method. This method takes in a sample and its corresponding weights (if any), calculates its weighted statistics and returns a dictionary containing the statistics:

```
sample1 = np.array([1,2,3])
weights1 = np.array([1,2,0.5])

stats1 = wsc.add(sample=sample1, weights=weights1)

print(stats1)

# Output: {'sample': array([1, 2, 3]), 'weights': array([1. , 2. , 0.5]), 'weighted_mean': 1.8571428571428572, 'weighted_std': 0.7559289460184544, 'standard_error_mean': 0.4040610178208842}
```

You can add as many samples as you want using the add method.

```
sample2 = [4, 5, 6]

stats2 = wsc.add(sample=sample2)

print(stats2)

# Output: {'sample': array([4, 5, 6]), 'weights': array([1., 1., 1.]), 'weighted_mean': 5.0, 'weighted_std': 1.0, 'standard_error_mean': 0.5773502691896257}
```

The resulting dict (inner dict) of a sample is stored in a nested dict. You can access the current size of the nested dict and the stored inner dicts using the size and samples attributes, respectively:

```
print(wsc.size)

# Output: 2

print(wsc.samples)

# Output: {
0: {'sample': array([1, 2, 3]), 'weights': array([1. , 2. , 0.5]), 'weighted_mean': 1.8571428571428572, 'weighted_std': 0.7559289460184544, 'standard_error_mean': 0.4040610178208842}, 
1: {'sample': array([4, 5, 6]), 'weights': array([1., 1., 1.]), 'weighted_mean': 5.0, 'weighted_std': 1.0, 'standard_error_mean': 0.5773502691896257}
}

```

Alternatively, the nested dict can be also accessed by the __call__ method:

```
print(wsc.())

# Output: {
0: {'sample': array([1, 2, 3]), 'weights': array([1. , 2. , 0.5]), 'weighted_mean': 1.8571428571428572, 'weighted_std': 0.7559289460184544, 'standard_error_mean': 0.4040610178208842}, 
1: {'sample': array([4, 5, 6]), 'weights': array([1., 1., 1.]), 'weighted_mean': 5.0, 'weighted_std': 1.0, 'standard_error_mean': 0.5773502691896257}
}

```

You can update the statistics of a particular sample using the update method. This method takes in the index of the sample to update, and the new sample and weights (if any). It then calculates the new weighted statistics and returns a dictionary containing the updated statistics. If the sample (or weights) are not provided as arguments, the already stored sample (or weights) will be used in the calculation of the new statistics.

```
stats1_updated = wsc.update(index=0, sample=[1, 2, 3, 4, 5], weights=[1, 2, 1, 1, 1])

print(stats1_updated)

# Output: {'sample': array([1, 2, 3, 4, 5]), 'weights': array([1, 2, 1, 1, 1]), 'weighted_mean': 2.8333333333333335, 'weighted_std': 1.4719601443879744, 'standard_error_mean': 0.6009252125773314}
```

In the example above the new sample provided has a different size than the stored sample (len(new sample) = 5, len(old sample)= 3). It was therefore necessary to also provide new weights with the same size as the new sample. Calling the update method with just the new sample raises a type error as the calculator tries to get the statistics of the new sample using the old weights which have a different size. 

## How it works

The package stores samples and their corresponding weights into a nested dictionary. Each sample is stored into a separate inner dictionary. The assigned key to a new sample corresponds to the current size of the nested dictionary (e.g. new key = number of stored samples - 1). In addition, the package calculates the weighted mean, weighted standard deviation and the standard error of the mean of each sample by using the DescrStatsW class from statsmodels. These statistics are stored in each inner dictionary. Every inner dictionary has the following keys: "sample", "weights", "weighted_mean", "weighted_std" and "standard_error_mean". 

More on math?


## Requirements

This project uses the following third-party libraries:

* NumPy for simple data handling and data transformations.
* Statsmodels for calculating the weighted statistics.

API Documentation
================================================================================
The WeightedStatsCalculator class is a tool for storing samples and calculating their weighted statistics. It provides methods to add new samples, update existing samples, and retrieve the calculated statistics.

## `class sample_statistics.main.WeightedStatsCalculator`

A class for calculating weighted statistics on a set of samples.

Attributes:
-------------------------------------------------------
- `samples`: dict

   A nested dictionary containing dictionaries with the weighted statistics for each sample. Each inner dictionary has the following keys:

    - `sample`: numpy.ndarray

       The sample data.

    - `weights`: numpy.ndarray

       The weights for each data point in the sample.

    - `weighted_mean`: float

       The weighted mean of the sample.

    - `weighted_std`: float

       The weighted standard deviation of the sample.

    - `standard_error_mean`: float

       The standard error of the mean of the sample.

- `size`: int

  The number of samples in the calculator.

Methods:
-------------------------------------------------------
## `add(sample, weights=None)`

Adds a new sample to the nested dictionary and returns the dictionary of this added sample with its statistics.

### Parameters:

- `sample`: 1D array-like

    The sample data to add.

- `weights`: 1D array-like, optional

    The weights for each data point in the sample. Default is None, which gives equal weights to all data points.

### Returns:

- `dict`

    A dictionary containing the weighted statistics for the added sample.

## `update(index, sample=None, weights=None)`

Update the statistics of a particular sample and return its dictionary.

### Parameters:

- `index`: int

    The index of the sample to update.

- `sample`: 1D array-like, optional

    The new data to be used in the calculation of the sample statistics. If not provided, the existing sample data will be used. If provided, the     weights must also change to the same size.

- `weights`: 1D array-like, optional

    The new weights to be used in the calculation of the sample statistics. If not provided, the existing weights will be used. They must have     the same size as the sample. For the unweighted case, the input weights must be np.ones(len(sample)).

### Returns:

- `dict`:

    A dictionary containing the updated sample statistics.

## `__call__()`

### Returns:

- `dict`:

  The nested dictionary of samples and their statistics.
