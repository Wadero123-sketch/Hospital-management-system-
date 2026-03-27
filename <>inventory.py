from app.database import db, TimestampMixin

class MedicineCategory(db.Model, TimestampMixin):
    __tablename__ = 'medicine_categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    medicines = db.relationship('Medicine', backref='category', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<MedicineCategory {self.name}>'

class Medicine(db.Model, TimestampMixin):
    __tablename__ = 'medicines'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('medicine_categories.id'), nullable=False)
    generic_name = db.Column(db.String(120), nullable=True)
    manufacturer = db.Column(db.String(120), nullable=True)
    strength = db.Column(db.String(50), nullable=True)  # e.g., "500mg"
    unit = db.Column(db.String(20), nullable=True)  # e.g., "tablet", "ml"
    cost_per_unit = db.Column(db.Float, nullable=False)
    selling_price = db.Column(db.Float, nullable=False)
    quantity_in_stock = db.Column(db.Integer, default=0)
    minimum_stock_level = db.Column(db.Integer, default=10)
    expiry_date = db.Column(db.Date, nullable=True)
    batch_number = db.Column(db.String(50), nullable=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=True)
    
    prescriptions = db.relationship('PrescriptionItem', backref='medicine', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Medicine {self.name}>'

class Supplier(db.Model, TimestampMixin):
    __tablename__ = 'suppliers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    contact_person = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    address = db.Column(db.Text, nullable=True)
    
    medicines = db.relationship('Medicine', backref='supplier', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Supplier {self.name}>'

class Equipment(db.Model, TimestampMixin):
    __tablename__ = 'equipment'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    cost = db.Column(db.Float, nullable=False)
    maintenance_date = db.Column(db.Date, nullable=True)
    is_functional = db.Column(db.Boolean, default=True)
    location = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return f'<Equipment {self.name}>'
