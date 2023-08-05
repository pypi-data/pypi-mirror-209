"""Customer Segmentation Package.

This package provides functions for customer data analysis and segmentation.

Functions:
- load_data(file_path): Loads customer data from a CSV file.
- find_missing_values(data): Finds the number of missing values in each column of the customer data.
- perform_eda(data): Performs exploratory data analysis on the customer data.
- plot_histograms(data, columns, figsize=(10, 12)): Plots histograms for specified columns in the customer data.
- plot_pairplot(data, columns=None): Generates a pairplot for specified columns in the customer data.
- convert_to_datetime(data, column_name): Converts a string column to a datetime object and creates a new date column.
- customer_data_clusters(data, num_clusters): Performs K-means clustering on customer data.
- customer_segmentation(data, num_clusters): Performs customer segmentation using the K-means clustering algorithm.
- plot_cluster_scatter(data, column1, column2, num_clusters): Creates scatter plots for each cluster based on two columns of data.

"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def load_data(file_path):
    """
    Loads customer data from a CSV file provided by user.
    
    Args:
        file_path(str): The path of CSV file(data).
    
    Returns:
        DataFrame: The loaded customer data as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def find_missing_values(data):
    """
    Find the number of missing values in each column of the customer data.

    Args:
        data(DataFrame): The customer data as a DF.

    Returns:
        pandas.Series: The number of missing values in each column.
    """
    
    missing_values_count = data.isnull().sum()
    return missing_values_count

def perform_eda(data):
    """
    Perform exploratory data analysis on the customer data.

    Args:
        data(DataFrame): The customer data as a DF.
    """
    
        
    #Summary statistics of the data 
    summary_stats = data.describe()
    print(summary_stats)

    #Correlation matrix to visualize the correlation between variables
    correlation_matrix = data.corr()
    plt.figure(figsize=(14, 12))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

def plot_histograms(data, columns, figsize=(10, 12)):
    """
    Plots histograms for the specified columns in the customer data.

    Args:
        data(DataFrame): The customer data as a DF.
        columns(list): The list of columns which the user want to plot in the histograms.
        figsize(tuple): This part is optional. The figure size of the histogram plot. Default is (10, 12).
    """
    data[columns].hist(figsize=figsize)
    plt.show()
 
def plot_pairplot(data, columns=None):
    
    """
    Generate a pairplot for the specified columns in the customer data.

    Args:
        data (pandas.DataFrame): The customer data as a DataFrame.
        columns (list): Optional. The list of columns to include in the pairplot. 
                        If not specified, all numeric columns will be used.
    """
    if columns is None:
        columns = data.select_dtypes(include='number').columns
    sns.pairplot(data[columns])
    plt.show()
    

def convert_to_datetime(data, column_name):
    """
    Convert a string column to a datetime object and create a new date column.

    Args:
        data (pandas.DataFrame): The data as a DataFrame.
        column_name (str): The name of the column to convert.

    Returns:
        pandas.DataFrame: The data with the converted datetime column and new date column.
    """
    data[column_name] = pd.to_datetime(data[column_name])
    data['date'] = data[column_name].apply(lambda x: x.date())
    return data

def customer_data_clusters(data, num_clusters):
    """
    Perform K-means clustering on customer data.

    Parameters:
        data (pandas.DataFrame): The input data containing numeric columns.
        num_clusters (int): The number of clusters to create.

    Returns:
        pandas.DataFrame: A DataFrame containing the cluster labels for each data point.

    """
    # Exclude non-numeric columns
    numeric_cols = data.select_dtypes(include='number').columns
    data_numeric = data[numeric_cols]

    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    data_imputed = pd.DataFrame(imputer.fit_transform(data_numeric), columns=data_numeric.columns)

    # Standardize the data
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data_imputed)

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(data_scaled)

    # Convert data_scaled back to DataFrame
    data_scaled_df = pd.DataFrame(data_scaled, columns=data_numeric.columns)

    # Compute cluster statistics
    cluster_data = data_scaled_df.copy()
    cluster_data['cluster'] = cluster_labels

    return cluster_data

def customer_segmentation(data, num_clusters):
    """
    Perform customer segmentation using the K-means clustering algorithm and provide cluster statistics.

    Args:
        data (pandas.DataFrame): The customer data as a DataFrame.
        num_clusters (int): The number of clusters to create.

    Returns:
        pandas.DataFrame: The cluster statistics with columns for clusters, min, max, mean, std, and quantiles.
    """
    # Exclude non-numeric columns
    numeric_cols = data.select_dtypes(include='number').columns
    data_numeric = data[numeric_cols]

    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    data_imputed = pd.DataFrame(imputer.fit_transform(data_numeric), columns=data_numeric.columns)

    # Standardize the data
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data_imputed)

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(data_scaled)

    # Convert data_scaled back to DataFrame
    data_scaled_df = pd.DataFrame(data_scaled, columns=data_numeric.columns)
    data_scaled_df["kmeans_clusters"] = kmeans.labels_
    cluster_stats = data_scaled_df.groupby(['kmeans_clusters']).describe()
   
    return cluster_stats

def plot_cluster_scatter(data, column1, column2, num_clusters):
    """
    Create scatter plots for each cluster based on two columns of data.

    Args:
        data (pandas.DataFrame): The input data containing the cluster labels.
        column1 (str): The name of the column to be plotted on the x-axis.
        column2 (str): The name of the column to be plotted on the y-axis.
        num_clusters (int): The number of clusters.

    """
    
    df = customer_data_clusters(data, num_clusters)

    fig, axes = plt.subplots(nrows=num_clusters, figsize=(8, 6*num_clusters))

    for cluster, ax in zip(range(num_clusters), axes):
        cluster_data = df[df['cluster'] == cluster]
        ax.scatter(cluster_data[column1], cluster_data[column2], label=f'Cluster {cluster}')
        ax.set_xlabel(column1)
        ax.set_ylabel(column2)
        ax.set_title(f'Scatter Plot for Cluster {cluster}')

    plt.tight_layout()
    plt.show()

