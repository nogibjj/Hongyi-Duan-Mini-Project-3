from main import *
import polars as pl

df = None
try:
    df = pl.read_excel("Project-Management-Sample-Data.xlsx")
except FileNotFoundError:
    pass

column_name = 'Progress'
print(df[column_name].describe())

def test_df_exists():
    assert df is not None, "DataFrame was not loaded, check if it exists."
    
def test_mean():
    assert round(get_mean(df, column_name), 5) == round(df[column_name].mean(), 5)
    
def test_median():
    assert round(get_median(df, column_name), 5) == round(df[column_name].median(), 5)
    
def test_std():
    assert round(get_std(df, column_name), 5) == round(df[column_name].std(), 5)

if __name__ == "__main__":
    test_df_exists()
    test_mean()
    test_median()
    test_std()
    get_plot(df, column_name)
