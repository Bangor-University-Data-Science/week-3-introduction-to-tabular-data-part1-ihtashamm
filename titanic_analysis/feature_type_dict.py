def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],
            'discrete': []
        },
        'categorical': {
            'nominal': [],
            'ordinal': []
        }
    }
    
    # Example list of known ordinal features
    ordinal_features = ['Fare', 'Class']  # Adjust as necessary based on your dataset

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            # Classify numerical features
            if df[column].nunique() > 10:  # Example threshold for continuous
                feature_types['numerical']['continuous'].append(column)
            else:
                feature_types['numerical']['discrete'].append(column)
        elif isinstance(df[column].dtype, pd.CategoricalDtype) or df[column].dtype == 'object':
            # Classify categorical features
            if column in ordinal_features:
                feature_types['categorical']['ordinal'].append(column)
            else:
                feature_types['categorical']['nominal'].append(column)  # Default to nominal

    return feature_types