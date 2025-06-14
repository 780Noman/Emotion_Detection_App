# FER_deploy/Model_deploy/views.py

from django.shortcuts import render
import numpy as np
import cv2
from .apps import ModelDeployConfig # Import the app config to access the model

# NOTE: These labels will be used, but the model's predictions will be random.
EMOTION_LABELS = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def preprocess_image_for_generic_resnet(image_bytes):
    """
    This function is now changed to match the generic ResNet50 model's requirements.
    It will prepare a 224x224 color image.
    """
    # Decode the image from bytes
    nparr = np.frombuffer(image_bytes, np.uint8)
    # The image is read as BGR (3-channel color) by default
    img_color = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # --- CHANGED: Resize to the model's expected input size (224x224) ---
    resized_img = cv2.resize(img_color, (224, 224))

    # --- CHANGED: We are NOT converting to grayscale ---

    # Normalize pixel values to be between 0 and 1
    normalized_img = resized_img / 255.0

    # Expand dimension to create a "batch" of 1 image
    # The shape will be (1, 224, 224, 3)
    processed_img = np.expand_dims(normalized_img, axis=0)

    return processed_img

def predict_emotion(request):
    """
    This is the main view that handles file uploads and predictions.
    """
    context = {'prediction': "None"}

    if request.method == 'POST':
        if 'image_file' in request.FILES:
            uploaded_file = request.FILES['image_file']

            if ModelDeployConfig.model:
                img_bytes = uploaded_file.read()

                # Use the new preprocessing function
                processed_image = preprocess_image_for_generic_resnet(img_bytes)

                # Make a prediction. The error will be gone, but the result is not meaningful.
                prediction = ModelDeployConfig.model.predict(processed_image)
                
                # This part will run, but the logic is flawed because the model
                # wasn't trained for emotions. We just pick an emotion label randomly
                # based on the output of a generic object-detection model.
                predicted_index = np.argmax(prediction)

                # To prevent an index out of bounds error if the generic model
                # has more than 7 outputs, we use a failsafe.
                if predicted_index < len(EMOTION_LABELS):
                    predicted_emotion = EMOTION_LABELS[predicted_index]
                else:
                    predicted_emotion = "Unknown (Model Output Mismatch)"

                context['prediction'] = predicted_emotion

    return render(request, 'index.html', context)