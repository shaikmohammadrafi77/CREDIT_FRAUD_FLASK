from flask import Flask, render_template, request, redirect, url_for, flash
import random
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-123'

class SimpleFraudDetector:
    def predict(self, data):
        """Simple rule-based fraud detection for demo"""
        amount = float(data.get('amount', 0))
        time = float(data.get('time', 0))
        
        # Simple fraud rules
        fraud_indications = 0
        
        # Rule 1: Large amount
        if amount > 1000:
            fraud_indications += 2
        
        # Rule 2: Unusual time
        if time < 0 or time > 24:
            fraud_indications += 1
        
        # Rule 3: Very small amount (card testing)
        if 0 < amount < 1:
            fraud_indications += 1
        
        # Rule 4: Round numbers (common in fraud)
        if amount % 100 == 0 and amount > 0:
            fraud_indications += 1
        
        # Calculate probability
        base_prob = fraud_indications * 0.2
        random_factor = random.uniform(0.05, 0.15)
        probability = min(0.95, base_prob + random_factor)
        
        is_fraud = probability > 0.5
        
        return is_fraud, probability

# Initialize detector
detector = SimpleFraudDetector()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form
        
        # Make prediction
        is_fraud, probability = detector.predict(data)
        
        # Generate ID
        analysis_id = f"TXN_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        return render_template('result.html',
                            is_fraud=is_fraud,
                            probability=probability,
                            amount=float(data.get('amount', 0)),
                            time=float(data.get('time', 0)),
                            analysis_id=analysis_id)
        
    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('upload'))

@app.route('/upload-file', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            flash('No file selected', 'error')
            return redirect(url_for('upload'))
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(url_for('upload'))
        
        if file and file.filename.endswith('.csv'):
            # For demo, use sample data from file upload
            sample_data = {
                'amount': 150.0,
                'time': 12.5,
                'v1': -1.2,
                'v2': 0.5,
                'v3': -0.8,
                'v4': 1.1,
                'v5': -0.3,
                'v6': 0.7
            }
            
            is_fraud, probability = detector.predict(sample_data)
            analysis_id = f"FILE_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            return render_template('result.html',
                                is_fraud=is_fraud,
                                probability=probability,
                                amount=sample_data['amount'],
                                time=sample_data['time'],
                                analysis_id=analysis_id)
        else:
            flash('Please upload a CSV file', 'error')
            return redirect(url_for('upload'))
            
    except Exception as e:
        flash(f'Error processing file: {str(e)}', 'error')
        return redirect(url_for('upload'))

if __name__ == '__main__':
    print("🚀 Fraud Detection App Starting...")
    print("📊 Access at: http://localhost:5000")
    print("💡 This is a demo version with rule-based detection")
    app.run(debug=True, port=5000)