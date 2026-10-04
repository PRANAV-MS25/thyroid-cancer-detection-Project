# 🩺 Thyroid Nodule Classification & Detection System

A CNN-based deep learning framework for automated thyroid nodule detection and classification using ultrasound images. The system combines **EfficientNet-B0, TensorFlow, Flask, Grad-CAM, and SQLite** to provide AI-assisted thyroid image analysis with prediction confidence and explainable visualizations.

---

## 📁 Project Structure

```text
Thyroid-Nodule-Classification/
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   └── EfficientNet-B0 trained model files
│
├── data/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   ├── upload.html
│   ├── diseases.html
│   ├── history.html
│   ├── profile.html
│   └── about.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── db/
│   └── database.py
│
├── uploads/
│   └── Uploaded ultrasound images
│
├── login.png
├── home.png
├── upload.png
├── diseases.png
├── history.png
├── profile.png
└── about.png

Note: The structure above represents the logical organization of the application. Keep the filenames and folders aligned with the actual repository structure when deploying or running the project.

🗄️ Core Components & Architecture
app.py — Flask Application & Backend
Component	Description
Flask Application	Initializes and manages the web application
Authentication	Handles user login, registration, logout, and session management
Image Upload	Receives and validates thyroid ultrasound images
Model Inference	Processes uploaded images through the trained CNN model
Prediction	Generates thyroid nodule classification results
Confidence Score	Calculates and displays prediction confidence
Grad-CAM	Generates visual explanations highlighting important image regions
Database Operations	Stores users, predictions, and history using SQLite
Dashboard	Provides access to upload, results, history, and application features
🧠 Deep Learning Pipeline
Stage	Implementation
Image Acquisition	Thyroid ultrasound images
Preprocessing	Image resizing, normalization, and preparation for inference
Feature Extraction	EfficientNet-B0 convolutional feature extraction
Classification	CNN-based thyroid nodule classification
Prediction	Benign / Malignant or configured disease-stage prediction
Explainability	Grad-CAM heatmap generation
Confidence	Prediction probability/confidence calculation
Result Storage	Prediction information stored in SQLite
🗃️ db/ — Database Layer
Component	Purpose
SQLite	Lightweight relational database for application data
User Records	Stores registered user information
Prediction Records	Stores classification results
Prediction History	Allows users to review previous analyses
Database Access	Provides backend functions for database operations
🔐 Authentication & Access

The application uses Flask-based authentication and session management.

Default Credentials
Role	Username	Password
User	user@gmail.com	password

For production deployment, replace the default credentials and use securely hashed passwords and environment-based configuration.

🔄 System Flow
User
 │
 ▼
Login / Register
 │
 ▼
Flask Authentication
 │
 ▼
Dashboard / Home
 │
 ▼
Upload Thyroid Ultrasound
 │
 ▼
Image Validation & Preprocessing
 │
 ▼
EfficientNet-B0 CNN Model
 │
 ▼
Feature Extraction
 │
 ▼
Classification
 │
 ├───────────────┐
 ▼               ▼
Benign       Malignant / Stage
 │               │
 └───────┬───────┘
         ▼
   Confidence Score
         │
         ▼
      Grad-CAM
         │
         ▼
Explainable Prediction
         │
         ▼
SQLite Database
         │
         ▼
Prediction History
🧠 Model Architecture
EfficientNet-B0

The classification engine is built around EfficientNet-B0, a convolutional neural network architecture designed to achieve strong image-classification performance while maintaining computational efficiency.

Component	Description
Architecture	EfficientNet-B0
Framework	TensorFlow
Input	Thyroid ultrasound image
Processing	Image preprocessing and normalization
Feature Extraction	EfficientNet convolutional layers
Classification	Thyroid nodule classification
Output	Predicted class and confidence score
Explainability	Grad-CAM visualization
🔬 Explainable AI — Grad-CAM

The application integrates Grad-CAM (Gradient-weighted Class Activation Mapping) to provide a visual explanation of the CNN prediction.

The generated heatmap highlights image regions that contributed most strongly to the model's prediction, allowing users to better understand the areas considered important by the model.

Ultrasound Image
       ↓
EfficientNet-B0
       ↓
Model Prediction
       ↓
Gradient Calculation
       ↓
Grad-CAM
       ↓
Activation Heatmap
       ↓
Explainable Result
📦 Main Technologies
Category	Technologies / Tools
Programming Language	Python
Deep Learning	TensorFlow
CNN Architecture	EfficientNet-B0
Explainable AI	Grad-CAM
Backend	Flask
Authentication	Flask-Login
Database	SQLite
Image Processing	OpenCV / PIL
Frontend	HTML5, CSS3, JavaScript
Model Inference	TensorFlow / Keras
Version Control	Git, GitHub
⚙️ Setup & Local Development
1. Prerequisites
Python 3.x
pip
Git
Modern web browser
Recommended: Virtual environment
Sufficient system resources for TensorFlow model inference
2. Clone the Repository
git clone <YOUR-REPOSITORY-URL>
cd Thyroid-Nodule-Classification
3. Create a Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
macOS / Linux
python3 -m venv venv
source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Configure the Model

Place the trained EfficientNet-B0 model in the expected model directory and ensure the filename/path matches the configuration used by the Flask application.

6. Run the Application
python app.py

The Flask development server will start locally.

Open the displayed local URL in your browser.

🚀 Application Features
🔐 User authentication and registration
🩺 Thyroid ultrasound image upload
🧠 CNN-based thyroid nodule classification
⚡ EfficientNet-B0 inference
📊 Prediction confidence score
🔬 Grad-CAM explainable AI visualization
🗃️ SQLite database integration
📜 Prediction history
🖼️ Secure image upload handling
🌐 Flask backend
📱 Responsive frontend interface
⚙️ Real-time AI inference
👤 User profile management
📚 Thyroid disease information section
🔄 User Interaction Flow
User opens application
        ↓
Login / Register
        ↓
Dashboard
        ↓
Upload ultrasound scan
        ↓
AI image preprocessing
        ↓
EfficientNet-B0 inference
        ↓
Classification result
        ↓
Confidence score + Grad-CAM
        ↓
Save prediction
        ↓
View result
        ↓
Prediction History
📸 App Interface Gallery
1. Authentication & Dashboard
Login Page	Home / Dashboard

	
2. Image Analysis
Upload Scan	Disease Information

	
3. User & Prediction Management
Patient History	Developer Profile

	
4. About
About Page

📊 Model Performance

The project achieved approximately 95% classification accuracy under the reported evaluation setup.

Model performance can vary depending on the dataset split, preprocessing pipeline, training configuration, and evaluation methodology.

🔒 Security Considerations
Validate uploaded image file types.
Restrict upload sizes where appropriate.
Avoid storing sensitive patient information unnecessarily.
Use secure password hashing for production systems.
Store secret configuration values using environment variables.
Replace the default credentials before deployment.
Use HTTPS when deploying the application publicly.
⚠️ Medical Disclaimer

This project is intended for educational and research purposes and demonstrates an AI-assisted medical image classification workflow.

It should not be used as a substitute for professional medical diagnosis or clinical decision-making. Predictions should be reviewed by qualified medical professionals.

🌐 Project Links
Resource	Link
GitHub Repository	Add repository URL
Documentation	This README
Application	Local Flask application
🏆 Key Highlights
CNN-based medical image classification
EfficientNet-B0 transfer-learning architecture
Explainable AI using Grad-CAM
Flask-based full-stack implementation
SQLite-backed prediction history
User authentication and session management
Confidence-based prediction results
Responsive web interface
End-to-end image upload → inference → visualization workflow

© 2026 Pranav Matham. All rights reserved.
