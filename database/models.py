from datetime import datetime
from .database import db

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(100), unique=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    time = db.Column(db.Float, nullable=False)
    v1 = db.Column(db.Float, nullable=False)
    v2 = db.Column(db.Float, nullable=False)
    v3 = db.Column(db.Float, nullable=False)
    v4 = db.Column(db.Float, nullable=False)
    v5 = db.Column(db.Float, nullable=False)
    v6 = db.Column(db.Float, nullable=False)
    v7 = db.Column(db.Float, nullable=True)
    v8 = db.Column(db.Float, nullable=True)
    v9 = db.Column(db.Float, nullable=True)
    v10 = db.Column(db.Float, nullable=True)
    v11 = db.Column(db.Float, nullable=True)
    v12 = db.Column(db.Float, nullable=True)
    v13 = db.Column(db.Float, nullable=True)
    v14 = db.Column(db.Float, nullable=True)
    v15 = db.Column(db.Float, nullable=True)
    v16 = db.Column(db.Float, nullable=True)
    v17 = db.Column(db.Float, nullable=True)
    v18 = db.Column(db.Float, nullable=True)
    v19 = db.Column(db.Float, nullable=True)
    v20 = db.Column(db.Float, nullable=True)
    v21 = db.Column(db.Float, nullable=True)
    v22 = db.Column(db.Float, nullable=True)
    v23 = db.Column(db.Float, nullable=True)
    v24 = db.Column(db.Float, nullable=True)
    v25 = db.Column(db.Float, nullable=True)
    v26 = db.Column(db.Float, nullable=True)
    v27 = db.Column(db.Float, nullable=True)
    v28 = db.Column(db.Float, nullable=True)
    prediction = db.Column(db.Float, nullable=False)  # Probability
    is_fraud = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'transaction_id': self.transaction_id,
            'amount': self.amount,
            'time': self.time,
            'prediction': self.prediction,
            'is_fraud': self.is_fraud,
            'created_at': self.created_at.isoformat()
        }

class AnalysisResult(db.Model):
    __tablename__ = 'analysis_results'
    
    id = db.Column(db.Integer, primary_key=True)
    analysis_id = db.Column(db.String(100), unique=True, nullable=False)
    total_transactions = db.Column(db.Integer, nullable=False)
    fraud_count = db.Column(db.Integer, nullable=False)
    fraud_percentage = db.Column(db.Float, nullable=False)
    average_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'analysis_id': self.analysis_id,
            'total_transactions': self.total_transactions,
            'fraud_count': self.fraud_count,
            'fraud_percentage': self.fraud_percentage,
            'average_amount': self.average_amount,
            'created_at': self.created_at.isoformat()
        }
    