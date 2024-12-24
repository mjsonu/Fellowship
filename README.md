# Flower Classification using ResNet50

This project uses a pre-trained ResNet50 model to classify images of flowers into 102 categories from the **102 Flowers Dataset**. The model is fine-tuned on the dataset to achieve accurate predictions.

---
![Example Result](https://github.com/mjsonu/Fellowship/blob/main/pic1.png)

## Project Overview

1. **Dataset**:
   - The dataset contains images of flowers belonging to 102 categories.
   - Includes segmentation images, labels, and predefined train/validation/test splits.

2. **Model**:
   - ResNet50, a deep residual network, is used for training.
   - Fine-tuned to adapt to the flower dataset.

3. **Steps**:
   - Load and preprocess the dataset.
   - Train ResNet50 on the training set.
   - Evaluate the model on the test set.
   - Predict and visualize flower types on sample test images.

---

## How It Works

1. **Training**:
   - The model learns patterns like colors, shapes, and textures from the training images.
2. **Prediction**:
   - Given a new flower image, the model predicts its category with high accuracy.
3. **Visualization**:
   - Displays test images with their true and predicted labels.

---

## How to Run

1. **Install Dependencies**:
   ```bash
   pip install tensorflow matplotlib numpy
2. **Download and save the follwing files in current directory:**
   Dataset images
   Image segmentations
   The image labels
   The data splits
2. **Run the ipynb file**
