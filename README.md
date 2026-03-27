# Hospital-management-system

A comprehensive full-stack hospital management system built with Python Flask, SQLAlchemy, PostgreSQL, and React.

## Features

- **Patient Management**: Complete patient profiles, medical history, and insurance information
- **Doctor Management**: Manage doctors, specializations, and availability
- **Appointment Scheduling**: Book and manage patient appointments with doctors
- **Electronic Health Records (EHR)**: Maintain detailed medical records for each patient
- **Billing & Invoicing**: Generate and manage bills with payment tracking
- **Medicine Inventory**: Track medicines, stock levels, and expiry dates
- **Equipment Management**: Manage hospital equipment and maintenance
- **Laboratory Services**: Order and track lab tests with results
- **User Authentication**: Secure JWT-based authentication
- **Role-Based Access Control**: Different roles (Admin, Doctor, Patient, Receptionist, etc.)

## Project Structure

```
hospital-management-system/
├── backend/                 # Flask API
│   ├── app/
│   │   ├── models/         # Database models
│   │   ├── routes/         # API endpoints
│   │   ├── services/       # Business logic
│   │   ├── schemas/        # Request/response schemas
│   │   └── utils/          # Utilities
│   ├── migrations/         # Database migrations
│   ├── requirements.txt
│   └── .env.example
├── frontend/               # React web application
│   ├── public/
│   └── src/
├── docker-compose.yml
└── README.md
```

## Prerequisites

- Python 3.9+
- Node.js 14+
- PostgreSQL 12+
- Docker & Docker Compose (optional)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Wadero123-sketch/hospital-management-system.git
cd hospital-management-system
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your configuration
```

### 3. Database Setup

```bash
# Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Run Backend

```bash
python -m app.main
```

The API will be available at `http://localhost:5000`

### 5. Frontend Setup

```bash
cd frontend
npm install
npm start
```

The application will be available at `http://localhost:3000`

## Docker Deployment

```bash
docker-compose up -d
```

This will start:
- PostgreSQL database on port 5432
- Backend API on port 5000
- Frontend on port 3000

## API Documentation

### Authentication Endpoints

- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get JWT tokens
- `POST /api/auth/refresh` - Refresh access token
- `GET /api/auth/me` - Get current user info

### Patient Endpoints

- `GET /api/patients` - List all patients
- `POST /api/patients` - Create a new patient
- `GET /api/patients/<id>` - Get patient details
- `PUT /api/patients/<id>` - Update patient
- `DELETE /api/patients/<id>` - Delete patient

### Doctor Endpoints

- `GET /api/doctors` - List all doctors
- `POST /api/doctors` - Create a new doctor
- `GET /api/doctors/<id>` - Get doctor details
- `PUT /api/doctors/<id>` - Update doctor
- `DELETE /api/doctors/<id>` - Delete doctor

### Appointment Endpoints

- `GET /api/appointments` - List appointments
- `POST /api/appointments` - Book a new appointment
- `GET /api/appointments/<id>` - Get appointment details
- `PUT /api/appointments/<id>` - Update appointment
- `DELETE /api/appointments/<id>` - Cancel appointment

### Billing Endpoints

- `GET /api/billing` - List billing records
- `POST /api/billing` - Create billing record
- `GET /api/billing/<id>` - Get billing details
- `POST /api/billing/<id>/payments` - Record payment

### Inventory Endpoints

- `GET /api/medicines` - List medicines
- `POST /api/medicines` - Add medicine
- `GET /api/medicines/<id>` - Get medicine details
- `PUT /api/medicines/<id>` - Update medicine

### Laboratory Endpoints

- `GET /api/lab-tests` - List lab tests
- `POST /api/lab-tests` - Order new lab test
- `GET /api/lab-tests/<id>` - Get lab test details
- `POST /api/lab-tests/<id>/results` - Add lab results

## Configuration

Edit `.env` file to configure:

- Database connection details
- JWT secret keys
- Email settings
- API port and host

## Testing

```bash
python -m pytest tests/
```

## Contributing

1. Create a feature branch (`git checkout -b feature/AmazingFeature`)
2. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email support@hospitalms.com or open an issue on GitHub.
