import pandas as pd
class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold
        return
        
     
    def is_safe(self, row: pd.Series) -> bool:
        """
        Determine if  row of water data is safe.
        """
        return (
            self.ph_range[0] <= row["pH"] <= self.ph_range[1]
            and row["turbidity"] <= self.turbidity_threshold
        )

    def evaluate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add a 'Safe' column to the DataFrame indicating whether each row is safe.
        """
        df = df.copy()
        df["Safe"] = df.apply(self.is_safe, axis=1)
        return df

            


