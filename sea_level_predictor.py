import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot using the Year and CSIRO Adjusted Sea Level columns
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", s=10)
    
    # Create first line of best fit using the entire dataset
    slope_all, intercept_all, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    # Create an array of years from the minimum year in the data through 2050
    years_all = np.arange(df["Year"].min(), 2051)
    predicted_all = intercept_all + slope_all * years_all
    plt.plot(years_all, predicted_all, color="red", label="Best Fit Line (All Data)")
    
    # Create second line of best fit using data from year 2000 onward
    df_2000 = df[df["Year"] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    # Create an array of years from 2000 to 2050 for this regression
    years_2000 = np.arange(2000, 2051)
    predicted_2000 = intercept_2000 + slope_2000 * years_2000
    plt.plot(years_2000, predicted_2000, color="green", label="Best Fit Line (2000 Onward)")
    
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()