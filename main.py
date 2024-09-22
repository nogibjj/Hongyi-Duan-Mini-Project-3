import matplotlib.pyplot as plt
import polars as pl

def get_mean(x):
    return x.mean()

def get_median(x):
    return x.median()

def get_std(x):
    return x.std()

def get_plot(x):
    plt.plot(x.to_list())  # Convert Polars Series to list for plotting
    plt.title(x.name)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
