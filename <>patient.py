from app.database import db, TimestampMixin
from enum import Enum

class BloodType(Enum):
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"

class Patient(db.Model, TimestampMixin):
    __tablename__ = 'patients'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    blood_type = db.Column(db.Enum(BloodType), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    postal_code = db.Column(db.String(20), nullable=True)
    emergency_contact_name = db.Column(db.String(120), nullable=True)
    emergency_contact_phone = db.Column(db.String(20), nullable=True)
    allergies = db.Column(db.Text, nullable=True)
    medical_history = db.Column(db.Text, nullable=True)
    insurance_provider = db.Column(db.String(120), nullable=True)
    insurance_policy_number = db.Column(db.String(50), nullable=True)
    
    # Relationships
    appointments = db.relationship('Appointment', backref='patient', cascade='all, delete-orphan')
    medical_records = db.relationship('MedicalRecord', backref='patient', cascade='all, delete-orphan')
    billing_records = db.relationship('BillingRecord', backref='patient', cascade='all, delete-orphan')
    lab_tests = db.relationship('LabTest', backref='patient', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Patient {self.user.first_name} {self.user.last_name}>'
