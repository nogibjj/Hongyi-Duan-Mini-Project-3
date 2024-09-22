import matplotlib.pyplot as plt
import polars as pl

def get_mean(df, column_name):
    # Calculate mean using Polars for a given column
    return df.select(pl.col(column_name).mean()).item()

def get_median(df, column_name):
    # Calculate median using Polars for a given column
    return df.select(pl.col(column_name).median()).item()

def get_std(df, column_name):
    # Calculate standard deviation using Polars for a given column
    return df.select(pl.col(column_name).std()).item()

def get_plot(df, column_name):
    # Convert the column to a list and plot it
    x = df.select(pl.col(column_name)).to_series()
    plt.plot(x.to_list())
    plt.title(column_name)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

