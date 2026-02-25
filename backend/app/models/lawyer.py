from datetime import datetime
from app.extensions import db

class Lawyer(db.Model):
    __tablename__ = 'lawyers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100))
    rating = db.Column(db.Float, default=0.0)
    bio = db.Column(db.Text)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    consultations = db.relationship('Consultation', backref='lawyer', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'specialization': self.specialization,
            'rating': self.rating,
            'bio': self.bio,
            'email': self.email,
            'phone': self.phone,
        }
