import pandas as pd  

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.

    Returns:
        pd.DataFrame: Cleaned data.
    """

    df = df.copy()


    if 'pH' in df.columns:
        df['pH'] = pd.to_numeric(df['pH'], errors='coerce')
        df['pH'] = df['pH'].fillna(df['pH'].median())

 
    if 'turbidity' in df.columns:
        df['turbidity'] = pd.to_numeric(df['turbidity'], errors='coerce')
        df['turbidity'] = df['turbidity'].fillna(df['turbidity'].mean())


    return df

