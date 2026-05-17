# Thyroid Nodule Detection & Classification using Deep Learning

An advanced, end-to-end medical image analysis web application designed to automate the detection and classification of thyroid nodules from ultrasound imagery. Powered by a Convolutional Neural Network (CNN) architecture optimized with EfficientNet-B0 and integrated with Explainable AI (Grad-CAM) to visualize clinical focus points.

## 🚀 Key Features
- **Automated Classification:** Processes ultrasound scans to classify nodules with ~95% model accuracy.
- **Explainable AI (XAI):** Generates Grad-CAM visual heatmaps highlighting the exact regions triggering the model's prediction.
- **User Authentication:** Complete secure registration and login management system for clinicians.
- **Patient Scan History:** Relational storage tracking historical diagnostic outcomes and confidence metrics per user.

## 📂 System Architecture & Directory Layout

```bash
mybuspass_project/
│
├── manage.py                     # Django project manager
├── db.sqlite3                    # SQLite database
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
│
├── static/
│   └── style.css                 # Complete UI stylesheet
│
├── templates/
│   ├── admin_dashboard.html
│   ├── admin_applications.html
│   ├── admin_routes.html
│   ├── admin_route_form.html
│   └── admin_students.html
│
├── buspass/
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Main URL routing
│   └── wsgi.py                   # WSGI configuration
│
└── core/
    ├── models.py                 # Database models
    ├── views.py                  # Business logic
    ├── urls.py                   # App routes
    └── forms.py                  # Django forms
```

---

# 🗄️ Database Schema

### `auth_user` (Django built-in)

| Field      | Type              |
|------------|-------------------|
| id         | INT PK            |
| username   | VARCHAR           |
| email      | VARCHAR           |
| first_name | VARCHAR           |
| last_name  | VARCHAR           |
| password   | VARCHAR (hashed)  |
| is_staff   | BOOLEAN           |

### `core_studentprofile`

| Field      | Type                |
|------------|---------------------|
| id         | INT PK              |
| user_id    | FK → auth_user      |
| roll_number| VARCHAR UNIQUE      |
| department | VARCHAR             |
