def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    unique_values = {}
    for feature in categorical_features:
        if feature in df.columns:
            unique_values[feature] = df[feature].unique().tolist()  # Get unique values as a list
        else:
            unique_values[feature] = None 
    return unique_values  
