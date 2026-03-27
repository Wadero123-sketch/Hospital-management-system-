from app.database import db, TimestampMixin

class Doctor(db.Model, TimestampMixin):
    __tablename__ = 'doctors'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    license_number = db.Column(db.String(50), unique=True, nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    qualification = db.Column(db.Text, nullable=True)
    experience_years = db.Column(db.Integer, nullable=True)
    consultation_fee = db.Column(db.Float, default=0.0)
    available_from = db.Column(db.Time, nullable=True)
    available_to = db.Column(db.Time, nullable=True)
    available_days = db.Column(db.String(50), nullable=True)  # e.g., "Mon,Tue,Wed,Thu,Fri"
    is_available = db.Column(db.Boolean, default=True)
    
    # Relationships
    appointments = db.relationship('Appointment', backref='doctor', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Doctor {self.user.first_name} - {self.specialization}>'
