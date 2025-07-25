import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

IMG_SIZE = 100  # image size for resizing
data = []
labels = []

# Load images from with_mask and without_mask folders
with_mask_path = "observations/experiements/data/with_mask"
without_mask_path = "observations/experiements/data/without_mask"

for category, label in [(with_mask_path, 1), (without_mask_path, 0)]:
    for img_name in os.listdir(category):
        try:
            img_path = os.path.join(category, img_name)
            img = cv2.imread(img_path)
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            data.append(img)
            labels.append(label)
        except:
            pass  # skip broken images

# Convert to NumPy arrays and normalize
data = np.array(data) / 255.0  # scale pixels between 0 and 1
labels = np.array(labels)

# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)

# Build Convolutional Neural Network (CNN)
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')  # output: 1 neuron for binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Show model summary (optional)
model.summary()

# Train the model
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))


# Save the trained model to a file
model.save("mask_detector_model.h5")

