import matplotlib.pyplot as plt
import numpy as np


def plot_histogram_with_mean_median(data):
    
    # Check if numpy is imported
    if 'numpy' not in globals():
        raise ImportError("numpy package is not imported")

    # Check if matplotlib is imported
    if 'matplotlib' not in globals():
        raise ImportError("matplotlib package is not imported")
    
    # Check if input is a numpy array
    if not isinstance(data, np.ndarray):
        # Check if input can be converted to a numpy array
        try:
            data = np.array(data)
        except:
            raise ValueError("Input must be a numpy array or convertible to a numpy array")
    
    plt.hist(data, bins='auto')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram with Mean and Median')

    mean = np.mean(data)
    median = np.median(data)

    plt.axvline(mean, color='r', linestyle='dashed', linewidth=1, label=f'Mean: {mean:.2f}')
    plt.axvline(median, color='g', linestyle='dashed', linewidth=1, label=f'Median: {median:.2f}')

    plt.legend()
    plt.xticks(np.arange(np.min(data), np.max(data), 3)  , rotation=45, ha='right')
    plt.show()
