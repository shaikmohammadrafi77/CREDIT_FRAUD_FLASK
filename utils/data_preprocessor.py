import pandas as pd
import numpy as np
import logging
from typing import Dict, List, Union
import io

logger = logging.getLogger(__name__)

class DataPreprocessor:
    def __init__(self):
        self.required_columns = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'Amount']
        self.all_columns = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
    
    def validate_csv(self, file_content) -> tuple:
        """Validate CSV file and return DataFrame"""
        try:
            # Read CSV file
            df = pd.read_csv(io.StringIO(file_content.decode('utf-8')))
            
            # Check required columns
            missing_columns = [col for col in self.required_columns if col not in df.columns]
            if missing_columns:
                return None, f"Missing required columns: {', '.join(missing_columns)}"
            
            # Check for empty file
            if df.empty:
                return None, "CSV file is empty"
            
            # Validate data types
            for col in self.required_columns:
                if col in ['Time', 'Amount'] + [f'V{i}' for i in range(1, 7)]:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                    if df[col].isna().any():
                        return None, f"Column {col} contains non-numeric values"
            
            return df, "Valid CSV file"
            
        except Exception as e:
            logger.error(f"Error validating CSV: {str(e)}")
            return None, f"Error reading CSV file: {str(e)}"
    
    def preprocess_single_transaction(self, data: Dict) -> np.ndarray:
        """Preprocess single transaction data for prediction"""
        try:
            # Create feature array in correct order
            features = []
            
            # Add time and amount
            features.append(float(data.get('time', 0)))
            
            # Add V1-V28 features (fill missing with 0)
            for i in range(1, 29):
                feature_name = f'v{i}'
                features.append(float(data.get(feature_name, 0)))
            
            # Add amount at the end
            features.append(float(data.get('amount', 0)))
            
            return np.array(features).reshape(1, -1)
            
        except Exception as e:
            logger.error(f"Error preprocessing transaction: {str(e)}")
            raise e
    
    def preprocess_batch(self, df: pd.DataFrame) -> np.ndarray:
        """Preprocess batch data for prediction"""
        try:
            # Ensure all V columns are present
            for i in range(1, 29):
                col_name = f'V{i}'
                if col_name not in df.columns:
                    df[col_name] = 0.0
            
            # Reorder columns to match training format
            df_processed = df[self.all_columns]
            
            return df_processed.values
            
        except Exception as e:
            logger.error(f"Error preprocessing batch data: {str(e)}")
            raise e
    
    def generate_analysis_id(self) -> str:
        """Generate unique analysis ID"""
        from datetime import datetime
        import random
        import string
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return f"ANL_{timestamp}_{random_str}"

    def generate_transaction_id(self) -> str:
        """Generate unique transaction ID"""
        from datetime import datetime
        import random
        import string
        
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_str = ''.join(random.choices(string.digits, k=4))
        return f"TXN_{timestamp}_{random_str}"
    