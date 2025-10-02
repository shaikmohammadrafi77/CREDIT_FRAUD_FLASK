import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os
import logging

logger = logging.getLogger(__name__)

class FraudDetectionModel:
    def __init__(self, model_path, scaler_path):
        self.model_path = model_path
        self.scaler_path = scaler_path
        self.model = None
        self.scaler = None
        self.load_model()
    
    def load_model(self):
        """Load the trained model and scaler"""
        try:
            if os.path.exists(self.model_path):
                with open(self.model_path, 'rb') as f:
                    self.model = pickle.load(f)
                logger.info("Model loaded successfully")
            else:
                logger.warning("Model file not found, using default model")
                self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            
            if os.path.exists(self.scaler_path):
                with open(self.scaler_path, 'rb') as f:
                    self.scaler = pickle.load(f)
                logger.info("Scaler loaded successfully")
            else:
                logger.warning("Scaler file not found, using StandardScaler")
                from sklearn.preprocessing import StandardScaler
                self.scaler = StandardScaler()
                
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise e
    
    def predict(self, features):
        """Make prediction on features"""
        try:
            # Ensure features are in correct format
            if isinstance(features, list):
                features = np.array(features).reshape(1, -1)
            elif isinstance(features, pd.DataFrame):
                features = features.values
            
            # Scale features
            features_scaled = self.scaler.transform(features)
            
            # Make prediction
            probability = self.model.predict_proba(features_scaled)[0][1]
            prediction = probability > 0.5
            
            return prediction, probability
            
        except Exception as e:
            logger.error(f"Error making prediction: {str(e)}")
            raise e
    
    def save_model(self):
        """Save the model and scaler"""
        try:
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            
            with open(self.model_path, 'wb') as f:
                pickle.dump(self.model, f)
            
            with open(self.scaler_path, 'wb') as f:
                pickle.dump(self.scaler, f)
                
            logger.info("Model and scaler saved successfully")
            
        except Exception as e:
            logger.error(f"Error saving model: {str(e)}")
            raise e

# Global model instance
fraud_model = None

def init_model(app):
    """Initialize the fraud detection model"""
    global fraud_model
    try:
        fraud_model = FraudDetectionModel(
            model_path=app.config['MODEL_PATH'],
            scaler_path=app.config['SCALER_PATH']
        )
        return fraud_model
    except Exception as e:
        logger.error(f"Failed to initialize model: {str(e)}")
        raise e

def get_model():
    """Get the global model instance"""
    if fraud_model is None:
        raise RuntimeError("Model not initialized. Call init_model first.")
    return fraud_model
