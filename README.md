# Thyroid Nodule Detection & Classification using Deep Learning

An advanced, end-to-end medical image analysis web application designed to automate the detection and classification of thyroid nodules from ultrasound imagery. Powered by a Convolutional Neural Network (CNN) architecture optimized with EfficientNet-B0 and integrated with Explainable AI (Grad-CAM) to visualize clinical focus points.

## 🚀 Key Features
- **Automated Classification:** Processes ultrasound scans to classify nodules with ~95% model accuracy.
- **Explainable AI (XAI):** Generates Grad-CAM visual heatmaps highlighting the exact regions triggering the model's prediction.
- **User Authentication:** Complete secure registration and login management system for clinicians.
- **Patient Scan History:** Relational storage tracking historical diagnostic outcomes and confidence metrics per user.

## 📁 System Architecture & Directory Layout
```text
thyroid-nodule-classification/
│
├── .gitignore                      # Excludes large database binaries and cache files
├── README.md                       # Comprehensive project documentation
├── requirements.txt                # Python dependencies (TensorFlow, Flask, OpenCV)
├── app.py                          # Main Flask application engine
│
├── database/                       # Database layer
│   ├── schema.sql                  # Structured table layouts
│   └── thyroid_app.db              # Active SQLite database file
│
├── models/                         # Model registry
│   └── efficientnet_b0_weights.h5  # Pre-trained deep learning weights
│
├── modules/                        # Backend business logic
│   ├── predict.py                  # Core CNN inference logic
│   └── gradcam.py                  # Heatmap & explainable AI layers
│
├── static/                         # Web assets
│   ├── css/                        # Frontend styling
│   └── uploads/                    # Folder where uploaded ultrasound scans are saved
│
└── templates/                      # Flask HTML structural pages
    ├── index.html                  # Main dashboard / scan uploader
    └── login.html                  # User login / signup page


    ### `core_patientscan`

| Field | Type | Value |
| :--- | :--- | :--- |
| `scan_id` | INT PK | Scan analysis transaction key |
| `patient_name` | VARCHAR | Name of patient under analysis |
| `ultrasound_image` | VARCHAR | Server path to the uploaded image file |
| `prediction_label` | VARCHAR | Model output (Benign / Malignant) |
| `confidence_score` | DECIMAL | Precision metric percentage |
| `analyzed_at` | DATETIME | Execution timestamp |

   
