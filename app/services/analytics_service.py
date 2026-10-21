import os
import pandas as pd
import numpy as np

class RiskAnalyticsService:
    def __init__(self, file_path=None):

        if not file_path:
            self.file_path = os.path.join(os.getcwd(), 'data', 'insurance_data.xlsx')
        else:
            self.file_path = file_path

    def load_and_process_data(self):
        """
        Loads the insurance excel sheet, cleans columns, handles missing values,
        and computes portfolio risk metrics using Pandas and NumPy.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Dataset not found at {self.file_path}")

        df = pd.read_excel(self.file_path)

        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

        for col in df.select_dtypes(include=[np.number]).columns:
            df[col] = df[col].fillna(df[col].median())
        
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].fillna('Unknown')

        metrics = {
            "total_records": int(len(df)),
            "columns": list(df.columns),
        }

        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        if numeric_cols:
            metrics["summary_statistics"] = df[numeric_cols].agg(['sum', 'mean', 'std']).to_dict()

        return metrics