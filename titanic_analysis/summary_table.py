import pandas as pd
def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary_data = {
        'Feature Name': [],
        'Data Type': [],
        'Has Missing Values?': [],
        'Number of Unique Values': []
    }
    
    for column in df.columns:
        summary_data['Feature Name'].append(column)
        summary_data['Data Type'].append(str(df[column].dtype))
        summary_data['Has Missing Values?'].append(df[column].isnull().any())
        summary_data['Number of Unique Values'].append(df[column].nunique())
    
    return pd.DataFrame(summary_data)
