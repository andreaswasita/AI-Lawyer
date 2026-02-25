from flask import jsonify

class AppError(Exception):
    def __init__(self, message, status_code=400, error=None):
        self.message = message
        self.status_code = status_code
        self.error = error or message
        super().__init__(message)

def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({'success': False, 'error': 'Bad Request', 'message': str(e), 'status_code': 400}), 400
    
    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify({'success': False, 'error': 'Unauthorized', 'message': str(e), 'status_code': 401}), 401
    
    @app.errorhandler(403)
    def forbidden(e):
        return jsonify({'success': False, 'error': 'Forbidden', 'message': str(e), 'status_code': 403}), 403
    
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'success': False, 'error': 'Not Found', 'message': str(e), 'status_code': 404}), 404
    
    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({'success': False, 'error': 'Internal Server Error', 'message': str(e), 'status_code': 500}), 500
    
    @app.errorhandler(AppError)
    def handle_app_error(e):
        return jsonify({'success': False, 'error': e.error, 'message': e.message, 'status_code': e.status_code}), e.status_code
