# Face Mask Detection with Live Alert System

This project uses computer vision and deep learning to detect whether a person is wearing a face mask in real-time using a webcam. It promotes health and safety by providing instant visual alerts.

## 🔍 Features

- Real-time webcam face mask detection
- Trained Convolutional Neural Network (CNN) using TensorFlow
- Face detection using OpenCV Haar Cascades
- Visual alerts for "Mask 😷" or "No Mask ❌"

## 🛠️ Tools and Technologies

- Python 3.10.11
- TensorFlow 2.11.0
- OpenCV 4.12.0.88
- NumPy 1.25.0
- scikit-learn 1.1.3
- VS Code
- Webcam

## 📂 Project Structure
<pre>
Face Mask Detection with Live Alert System/
├── train_model.py # Script to train the CNN model
├── realtime_mask_detection.py # Real-time mask detection using webcam
├── mask_detector_model.h5 # Saved trained model
├── observations/ # Dataset folders (with_mask / without_mask)
  └── experiements/data/
├── README.md # This file
├── Face_Mask_Detection_Report.pdf # Final 2-page report
</pre>  



## 🚀 How to Run

1. Clone the repo or download the files
2. Install requirements:
   ```bash
   pip install tensorflow==2.11.0 opencv-python numpy scikit-learn
3. Train model (optional):
   ```bash
   python train_model.py
4. Run real-time detection:
   ```bash
   python realtime_mask_detection.py


## 🙏 Acknowledgements
* Dataset source: [GitHub - prajnasb/observations](https://github.com/prajnasb/observations)

* Developed as part of Elevate Labs Internship Project Phase
