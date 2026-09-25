import os
import torch
import torchvision.transforms as transforms
from PIL import Image
import timm
import numpy as np

# Dynamically locate the model relative to this file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "efficientnet_best.pth")

def load_model():
    # If your model architecture was trained as efficientnet_b2, change "tf_efficientnet_b0" to "tf_efficientnet_b2"
    model = timm.create_model("tf_efficientnet_b0", pretrained=False, num_classes=4)
    if os.path.exists(MODEL_PATH):
        model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    else:
        print(f"Warning: Model weights not found at {MODEL_PATH}")
    model.eval()
    return model

def predict(image_path):
    model = load_model()

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])

    try:
        img = Image.open(image_path).convert("RGB")
    except Exception as e:
        return "Error loading image", 0.0

    # Relaxed color variance check so valid ultrasound images aren't blocked
    np_img = np.array(img)
    diff_r_g = np_img[:, :, 0].astype("float32") - np_img[:, :, 1].astype("float32")
    diff_g_b = np_img[:, :, 1].astype("float32") - np_img[:, :, 2].astype("float32")
    color_variance = np.std(diff_r_g) + np.std(diff_g_b)

    # Increased threshold to avoid false rejections on clinical scans
    if color_variance > 60: 
        return "Not a thyroid ultrasound image", 0.0

    img_tensor = transform(img).unsqueeze(0)

    with torch.no_grad():
        output = model(img_tensor)
        probabilities = torch.nn.functional.softmax(output, dim=1)[0]
        max_prob = torch.max(probabilities).item()
        predicted_class = torch.argmax(probabilities).item()

    class_map = {
        0: "Benign",
        1: "Stage 1",
        2: "Stage 2",
        3: "Stage 3"
    }

    result_label = class_map.get(predicted_class, "Unknown")
    confidence = round(max_prob * 100, 2)

    return result_label, confidence