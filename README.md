# 🩺 Thyroid Nodule Classification & Detection System

A CNN-based deep learning framework for automated thyroid nodule detection and classification using ultrasound images. The system combines **EfficientNet-B0, TensorFlow, Flask, Grad-CAM, and SQLite** to provide AI-assisted ultrasound image analysis, prediction confidence, explainable visualizations, and prediction history.

The project achieved approximately **95% classification accuracy** under the reported evaluation setup.

---

## 🎯 Project Overview

Thyroid nodules are commonly evaluated using ultrasound imaging, where accurate interpretation can assist in identifying potentially malignant cases.

This project implements an end-to-end AI-assisted workflow that allows a user to:

- Register and authenticate securely
- Upload a thyroid ultrasound image
- Preprocess the image for model inference
- Classify the uploaded image using a CNN
- Generate a prediction and confidence score
- Visualize model attention using Grad-CAM
- Store prediction results in SQLite
- Review previous predictions through prediction history

The system is designed as an **educational and research-oriented medical image classification application**.

---

## 📁 Project Structure

```text
Thyroid-Nodule-Classification/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   └── EfficientNet-B0 trained model
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
