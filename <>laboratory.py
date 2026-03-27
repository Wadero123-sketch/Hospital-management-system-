from app.database import db, TimestampMixin
from enum import Enum

class LabTestStatus(Enum):
    ORDERED = "ordered"
    SAMPLE_COLLECTED = "sample_collected"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    REPORTED = "reported"

class LabTest(db.Model, TimestampMixin):
    __tablename__ = 'lab_tests'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    test_name = db.Column(db.String(120), nullable=False)
    test_code = db.Column(db.String(20), unique=True, nullable=False)
    ordered_date = db.Column(db.DateTime, nullable=False)
    sample_type = db.Column(db.String(50), nullable=True)  # e.g., "Blood", "Urine"
    status = db.Column(db.Enum(LabTestStatus), default=LabTestStatus.ORDERED)
    cost = db.Column(db.Float, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    
    # Results
    results = db.relationship('LabTestResult', backref='lab_test', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<LabTest {self.test_name} - {self.test_code}>'

class LabTestResult(db.Model, TimestampMixin):
    __tablename__ = 'lab_test_results'
    
    id = db.Column(db.Integer, primary_key=True)
    lab_test_id = db.Column(db.Integer, db.ForeignKey('lab_tests.id'), nullable=False)
    parameter_name = db.Column(db.String(120), nullable=False)
    result_value = db.Column(db.String(100), nullable=False)
    reference_range = db.Column(db.String(100), nullable=True)
    unit = db.Column(db.String(50), nullable=True)
    is_abnormal = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<LabTestResult {self.parameter_name}>'
