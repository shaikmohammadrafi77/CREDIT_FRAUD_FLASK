from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    """Initialize the database with the Flask app"""
    db.init_app(app)
    
    with app.app_context():
        # Create all tables
        db.create_all()
        
def get_db_session():
    """Get database session"""
    return db.session

def close_db_session(exception=None):
    """Close database session"""
    db.session.remove()
    