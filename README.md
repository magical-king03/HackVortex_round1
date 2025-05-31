# Student Engagement Detection using Bagging Ensemble Deep Learning

This project presents a deep learning-based system to automatically detect student engagement in virtual learning environments. It utilizes a bagging ensemble framework combining Convolutional Neural Networks (CNN) and Residual Networks (ResNet) to classify engagement levels from facial expressions.

## 📌 Problem Statement
Traditional observation methods are ineffective in online education, and existing engagement detection approaches often require additional hardware or suffer from low accuracy. This project addresses the issue by providing an efficient, accurate, and non-intrusive solution using only facial video data.

## 🎯 Objective
To build a scalable and real-time engagement detection system using ensemble deep learning techniques, enhancing classification accuracy across various engagement levels.

## 🧠 Technologies and Tools Used
Python, TensorFlow, Keras, OpenCV, Haar Cascade, SVD, One-Hot Encoding, DAiSEE, FER2013, Jupyter Notebook, Google Colab

## 🗂️ Dataset
- **DAiSEE**: A dataset for affective state recognition in e-learning.
- **FER2013**: Facial Emotion Recognition dataset for training emotion-aware models.

## 🔧 Preprocessing Steps
- Frame extraction using OpenCV
- Label mapping and one-hot encoding
- Feature reduction using SVD
- Face detection using Haar Cascade
- Image normalization and reshaping

## 🧪 Model Architecture
- **CNN**: For local feature extraction with Conv1D layers and pooling
- **ResNet**: For deep hierarchical learning using residual blocks
- **Ensemble**: Combines CNN and ResNet outputs using bagging strategy and softmax fusion for final prediction

## 📊 Evaluation
- Training and validation across multiple epochs with categorical crossentropy loss
- Accuracy assessment using confusion matrix
- Live emotion detection via webcam input

## 🌟 Key Features
- Real-time engagement monitoring
- Multi-class classification (Very Low, Low, High, Very High)
- No additional hardware required
- Bagging ensemble for higher accuracy

## 👥 Beneficiaries
- Educators and Instructors
- Students
- E-learning platforms
- Educational Institutions
- EdTech Researchers

## 🚀 How to Run
1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Run `preprocessing.py` to prepare the dataset
4. Train the models using `cnn_model.py`, `resnet_model.py`, and `ensemble_model.py`
5. Execute `live_tracking.py` for real-time engagement prediction via webcam

## 📚 References
- Santoni, M. M., Basaruddin, T., Junus, K., & Lawanto, O. (2024). *Automatic Detection of Students Engagement During Online Learning: A Bagging Ensemble Deep Learning Approach*. IEEE Access.
- DAiSEE Dataset - https://www.iitg.ac.in/daisee/
- FER2013 Dataset - Available on Kaggle

---
