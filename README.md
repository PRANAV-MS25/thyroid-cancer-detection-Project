# thyroid-nodule-classification
A CNN-based deep learning framework for automated thyroid nodule detection and classification using ultrasound images. Implemented using EfficientNet-B0, TensorFlow, and Flask with ~95% accuracy.


# Thyroid Nodule Classification & Detection System

A CNN-based deep learning framework for automated thyroid nodule detection and classification using ultrasound images. Implemented using EfficientNet-B0, TensorFlow, and Flask.

---

## 🔑 Default Credentials

| Role | Username | Password |
| :--- | :--- | :--- |
| **User** | `user@gmail.com` | `password` |

---

## 🔄 System Flow

1. User lands on **Login / Register** page.
2. Authenticates via **Flask-Login** backend session.
3. Navigates to **Dashboard / Home**.
4. Uploads a thyroid ultrasound image.
5. **CNN model** processes image through **EfficientNet-B0**.
6. Prediction generated (Benign vs Malignant/Stage).
7. **Grad-CAM** heatmap generated for explainability.
8. Prediction stored in **SQLite database**.
9. User views diagnosis result + confidence score.

---

## ✅ Features Implemented

* User authentication system
* Thyroid ultrasound image upload
* CNN-based thyroid nodule classification
* Benign vs Malignant prediction
* EfficientNet-B0 deep learning architecture
* Grad-CAM explainable AI visualization
* Confidence score generation
* SQLite database integration
* Flask backend integration
* Responsive frontend UI
* Prediction history management
* Secure image upload handling
* Real-time AI inference engine

---

## 📸 App Interface Gallery

| Login Page | Home / Dashboard |
| :---: | :---: |
| ![Login](login.png) | ![Home](home.png) |

| Upload Scan | Diseases Info |
| :---: | :---: |
| ![Upload](upload.png) | ![Diseases](diseases.png) |

| Patient History | Developer Profile |
| :---: | :---: |
| ![History](history.png) | ![Profile](profile.png) |

| About Page | |
| :---: | :---: |
| ![About](about.png) | |
