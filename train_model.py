import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import pickle
import os

def train_fraud_detection_model():
    """
    Train a fraud detection model using credit card data
    Note: You'll need to provide your own dataset
    """
    
    # Load your dataset
    # Replace this with your actual data loading code
    try:
        # Example: df = pd.read_csv('creditcard.csv')
        # For now, we'll create a dummy dataset for demonstration
        print("Creating dummy dataset for demonstration...")
        
        n_samples = 10000
        np.random.seed(42)
        
        # Create dummy features (V1-V28) and target
        X = np.random.normal(0, 1, (n_samples, 30))  # Time + V1-V28 + Amount
        y = np.random.binomial(1, 0.0017, n_samples)  # Rare fraud cases
        
        # Make some features correlated with fraud
        fraud_indices = np.where(y == 1)[0]
        X[fraud_indices, 1] += 2  # V1 higher for fraud
        X[fraud_indices, 2] -= 2  # V2 lower for fraud
        
    except Exception as e:
        print(f"Error loading data: {e}")
        return
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    print("Training Random Forest model...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=10,
        min_samples_leaf=5,
        random_state=42,
        class_weight='balanced'
    )
    
    model.fit(X_train_scaled, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
    
    print("\nModel Evaluation:")
    print(f"AUC Score: {roc_auc_score(y_test, y_pred_proba):.4f}")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save model and scaler
    os.makedirs('models', exist_ok=True)
    
    with open('models/fraud_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    with open('models/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    
    print("\nModel and scaler saved to 'models/' directory")

if __name__ == '__main__':
    train_fraud_detection_model()
    