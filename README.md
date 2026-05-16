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

    🛠️ Tech Stack
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
