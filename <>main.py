from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.config import config
from app.database import db, migrate
import os

def create_app(config_name=None):
    """Application factory"""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    JWTManager(app)
    
    # Register blueprints
    from app.routes import auth, patients, doctors, appointments, billing, inventory, laboratory
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(patients.bp)
    app.register_blueprint(doctors.bp)
    app.register_blueprint(appointments.bp)
    app.register_blueprint(billing.bp)
    app.register_blueprint(inventory.bp)
    app.register_blueprint(laboratory.bp)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return jsonify({'error': 'Internal server error'}), 500
    
    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health():
        return jsonify({'status': 'healthy'}), 200
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
