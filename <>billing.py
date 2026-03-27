from app.database import db, TimestampMixin
from enum import Enum

class PaymentStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    PARTIALLY_PAID = "partially_paid"
    OVERDUE = "overdue"

class PaymentMethod(Enum):
    CASH = "cash"
    CARD = "card"
    INSURANCE = "insurance"
    BANK_TRANSFER = "bank_transfer"

class BillingRecord(db.Model, TimestampMixin):
    __tablename__ = 'billing_records'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'), nullable=True)
    consultation_fee = db.Column(db.Float, default=0.0)
    lab_fees = db.Column(db.Float, default=0.0)
    medication_fees = db.Column(db.Float, default=0.0)
    other_charges = db.Column(db.Float, default=0.0)
    discount = db.Column(db.Float, default=0.0)
    tax = db.Column(db.Float, default=0.0)
    total_amount = db.Column(db.Float, nullable=False)
    amount_paid = db.Column(db.Float, default=0.0)
    payment_status = db.Column(db.Enum(PaymentStatus), default=PaymentStatus.PENDING)
    payment_method = db.Column(db.Enum(PaymentMethod), nullable=True)
    invoice_number = db.Column(db.String(50), unique=True, nullable=False)
    due_date = db.Column(db.Date, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    
    # Relationships
    payments = db.relationship('Payment', backref='billing_record', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<BillingRecord {self.invoice_number}>'

class Payment(db.Model, TimestampMixin):
    __tablename__ = 'payments'
    
    id = db.Column(db.Integer, primary_key=True)
    billing_record_id = db.Column(db.Integer, db.ForeignKey('billing_records.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.Enum(PaymentMethod), nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    transaction_id = db.Column(db.String(100), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return f'<Payment {self.id} - ${self.amount}>'
