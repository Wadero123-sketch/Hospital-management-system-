from app.database import db, TimestampMixin
from enum import Enum

class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    NO_SHOW = "no_show"

class Appointment(db.Model, TimestampMixin):
    tablename = 'appointments'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False, index=True)
    duration_minutes = db.Column(db.Integer, default=30)
    reason = db.Column(db.Text, nullable=True)
    status = db.Column(db.Enum(AppointmentStatus), default=AppointmentStatus.SCHEDULED)
    notes = db.Column(db.Text, nullable=True)
    consultation_mode = db.Column(db.String(20), default="in-person")  # in-person or online
    
    # Relationships
    medical_record = db.relationship('MedicalRecord', backref='appointment', uselist=False, cascade='all, delete-orphan')
    billing_record = db.relationship('BillingRecord', backref='appointment', uselist=False, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Appointment {self.id} - {self.appointment_date}>'
