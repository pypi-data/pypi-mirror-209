import numpy as np
import unittest
from sample_statistics import main

class TestWeightedStatsCalculator(unittest.TestCase):
    """
    Unit tests for the WeightedStatsCalculator class in sample_statistics.py.

    The WeightedStatsCalculator class is responsible for calculating various statistics
    (e.g. mean, standard deviation, standard error of the mean) for a given set of samples
    and their corresponding weights. These tests cover various edge cases and scenarios
    to ensure that the WeightedStatsCalculator class performs as expected.

    To run these tests, execute this module.
    """
    # Set up the test before each test method
    def setUp(self):

        # Create an instance of the WeightedStatsCalculator
        self.calculator = main.WeightedStatsCalculator()

        # Define some sample arrays
        self.samples = [
            np.array([1,2,3,4]),
            np.array([5,6,7,8]),
            np.array([]),
            np.array([13,13,13,13]),
            np.ones(15)
        ]

        # Define some weight arrays
        self.weights = [
            np.array([1,1,1,1]),
            np.array([2,2,2,2]),
            np.array([]),
            np.array([4,4,4,4]),
            None
        ]

    def test_add(self):

        # Add first sample in the dict
        sample = self.samples[0]
        weights = self.weights[0]
        result = self.calculator.add(sample, weights)

        # Test the statistics and the added sample
        self.assertIn(0, self.calculator.samples)
        self.assertEqual(1, self.calculator.size)
        self.assertEqual(result['sample'].tolist(), sample.tolist())
        self.assertEqual(result['weights'].tolist(), weights.tolist())
        self.assertAlmostEqual(result['weighted_mean'], 2.5)
        self.assertAlmostEqual(result['weighted_std'], (5/3)**0.5)
        self.assertAlmostEqual(result['standard_error_mean'], (5/3)**0.5/2)

        # Add and test second sample
        sample_2 = self.samples[1]
        weights_2 = self.weights[1]
        result_2 = self.calculator.add(sample_2, weights_2)
        self.assertIn(1, self.calculator.samples)
        self.assertEqual(2, self.calculator.size)
        self.assertEqual(result_2['sample'].tolist(), sample_2.tolist())
        self.assertEqual(result_2['weights'].tolist(), weights_2.tolist())

        # Test adding an empty sample and weight
        empty_sample = self.samples[2]
        empty_weights = self.weights[2]
        with self.assertRaises(TypeError):
            self.calculator.add(empty_sample, empty_weights)

        # Test adding a sample and weight of different lengths
        short_sample = np.array([1, 2, 3])
        long_weights = np.array([1, 2, 3, 4, 5])
        with self.assertRaises(TypeError):
            self.calculator.add(short_sample, long_weights)

        # Test adding a sample with negative weights
        neg_weights = np.array([-1, -2, -3, -4])
        with self.assertRaises(ValueError):
            self.calculator.add(sample, neg_weights)

        # Test adding a sample with zero weight
        zero_weights = np.array([0, 0, 0, 0])
        with self.assertRaises(ValueError):
            self.calculator.add(sample, zero_weights)

    # Define a test method for updating a sample and its weights in the dict
    def test_update(self):

        # Add a sample and weights to the calculator
        sample = self.samples[0]
        weights = self.weights[0]
        self.calculator.add(sample, weights)

        # Update the sample and weights in the dict
        new_sample = self.samples[1]
        new_weights = self.weights[1]
        result = self.calculator.update(0, new_sample, new_weights)

        # Test the updated statistics
        self.assertEqual(result['sample'].tolist(), new_sample.tolist())
        self.assertEqual(result['weights'].tolist(), new_weights.tolist())
        self.assertAlmostEqual(result['weighted_mean'], 6.5)
        self.assertAlmostEqual(result['weighted_std'], (10/7)**0.5)
        self.assertAlmostEqual(result['standard_error_mean'], (10/7/8)**0.5)

    # Define a test method for calculating the statistics of a sample and its weights
    def test_calculate_statistics(self):

        # Choose sample and weights
        sample = self.samples[0]
        weights = self.weights[0]

        sample_2 = self.samples[3]
        weights_2 = self.weights[3]

        sample_3 = self.samples[0]
        weights_3 = self.weights[4]

        # Test the statistics of the sample and its weights
        mean, std, sem = self.calculator._calculate_statistics(sample, weights)
        self.assertAlmostEqual(mean, 2.5)
        self.assertAlmostEqual(std, (5/3)**0.5)
        self.assertAlmostEqual(sem, (5/3)**0.5/2)

        # Test sample with identical points
        mean_2, std_2, sem_2 = self.calculator._calculate_statistics(sample_2, weights_2)
        self.assertAlmostEqual(mean_2, 13)
        self.assertAlmostEqual(std_2, 0)
        self.assertAlmostEqual(sem_2, 0)

        # Test sample with no weights
        mean_3, std_3, sem_3 = self.calculator._calculate_statistics(sample_3, weights_3)
        self.assertAlmostEqual(mean_3, 2.5)
        self.assertAlmostEqual(std_3, (5/3)**0.5)
        self.assertAlmostEqual(sem_3, (5/3)**0.5/2)

if __name__ == '__main__':
    unittest.main()
