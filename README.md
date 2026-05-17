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

    🛠️ **Tech Stack**
Frontend Framework: HTML5, CSS3, JavaScript

Backend Architecture: Flask (Python)

Database Engine: SQLite3

Deep Learning Ecosystem: TensorFlow, Keras, OpenCV

Core Model Architecture: EfficientNet-B0 + Custom Layer Grad-CAM

⚙️ Local Setup and Execution
Clone the repository:

Bash
git clone [https://github.com/PRANAV-MS25/Thyroid-dataset.git](https://github.com/PRANAV-MS25/Thyroid-dataset.git)
Install dependencies:

Bash
pip install -r requirements.txt
Initialize the relational database schema:

Bash
sqlite3 database/thyroid_app.db < database/schema.sql
Boot up the server:

Bash
python app.py

5. Scroll down to the bottom of the page, look for the green **"Commit changes..."** button, and click it. 

---

Go ahead and complete this step first on your browser. Let me know when you've committed the new README, and I will give you the exact next step to add the database folder and schema file!


🗄️ **Database Schema**
users
Field                Type
id             INT PK AUTOINCREMENT
username       VARCHAR(50) UNIQUE NOT NULL
email          VARCHAR(100) UNIQUE NOT NULL
password_hash  VARCHAR(255) NOT NULL
created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMPscan_recordsFieldTypeidINT PK AUTOINCREMENTuser_idINT FK → users(id) ON DELETE CASCADEimage_pathVARCHAR(255) NOT NULLprediction_labelVARCHAR(50) NOT NULLconfidence_scoreREAL NOT NULLgradcam_pathVARCHAR(255)scanned_atTIMESTAMP DEFAULT CURRENT_TIMESTAMP⚙️ Setup Instructions1. PrerequisitesPython 3.10+pip2. Clone / Extract ProjectDOScd thyroid-nodule-classification
3. Create Virtual EnvironmentDOSpython -m venv venv
venv\Scripts\activate
4. Install DependenciesDOSpip install -r requirements.txt
5. Run the ServerDOSpython app.py
Open: http://127.0.0.1:5000/🔄 System FlowUser visits page → Logs in or creates account at /login↓Logs in successfully → Redirected to dashboard at /↓Uploads ultrasound scan image via index.html panel↓System triggers modules/predict.py (EfficientNet evaluates features)↓System triggers modules/gradcam.py (Generates attention heatmaps)↓Scan results, score metrics, and image paths saved to 'scan_records' database↓Dashboard refreshes showing updated analysis logs with localized XAI metrics
#### **3. Commit Changes**
* Click **Commit changes...** at the top right.
* Select **"Commit directly to the `main` branch"**.
* Click the green **Commit changes** button.

Once you save this, click on your main repository tab to view the page—you'll see
