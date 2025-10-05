import pandas as pd
def load_csv(filepath: str) -> pd.DataFrame:
    
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print("File not found. Check your filepath.")
        return None



 

   
    
