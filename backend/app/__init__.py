from flask import Flask
from app.extensions import db, jwt, cors, migrate
from app.config import config_by_name
from app.utils.exceptions import register_error_handlers

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": app.config.get('ALLOWED_ORIGINS', '*')}})
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.api.v1 import v1_bp
    app.register_blueprint(v1_bp, url_prefix='/api/v1')
    
    # Register error handlers
    register_error_handlers(app)
    
    return app
