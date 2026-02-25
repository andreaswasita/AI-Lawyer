from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    jwt_required, get_jwt_identity, get_jwt
)
from marshmallow import ValidationError
from app.extensions import db, token_blacklist
from app.models.user import User
from app.schemas.user import UserRegistrationSchema, UserLoginSchema
from app.utils.security import hash_password, check_password

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    schema = UserRegistrationSchema()
    try:
        data = schema.load(request.get_json() or {})
    except ValidationError as e:
        return jsonify({'success': False, 'error': 'Validation error', 'message': str(e.messages), 'status_code': 400}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'success': False, 'error': 'Email already exists', 'message': 'A user with this email already exists', 'status_code': 409}), 409
    
    user = User(
        email=data['email'],
        hashed_password=hash_password(data['password']),
        name=data['name']
    )
    db.session.add(user)
    db.session.commit()
    
    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))
    
    return jsonify({
        'success': True,
        'data': {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': user.to_dict()
        },
        'message': 'User registered successfully'
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    schema = UserLoginSchema()
    try:
        data = schema.load(request.get_json() or {})
    except ValidationError as e:
        return jsonify({'success': False, 'error': 'Validation error', 'message': str(e.messages), 'status_code': 400}), 400
    
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password(data['password'], user.hashed_password):
        return jsonify({'success': False, 'error': 'Invalid credentials', 'message': 'Email or password is incorrect', 'status_code': 401}), 401
    
    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))
    
    return jsonify({
        'success': True,
        'data': {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': user.to_dict()
        },
        'message': 'Login successful'
    })

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify({
        'success': True,
        'data': {'access_token': access_token},
        'message': 'Token refreshed'
    })

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    token_blacklist.add(jti)
    return jsonify({'success': True, 'message': 'Logged out successfully'})

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))
    if not user:
        return jsonify({'success': False, 'error': 'User not found', 'status_code': 404}), 404
    return jsonify({'success': True, 'data': user.to_dict()})
