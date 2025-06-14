# Model_deploy/apps.py

from django.apps import AppConfig
from django.conf import settings
import os
from tensorflow.keras.models import load_model

class ModelDeployConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Model_deploy'

    # This will hold the loaded model
    model = None

    def ready(self):
        """
        This method is called by Django when the app is ready.
        We load the model here to ensure it only happens once.
        """
        # Path to your Keras model file
        # IMPORTANT: Make sure the filename here is EXACTLY correct.
        model_path = os.path.join(settings.BASE_DIR, 'ResNet50_Transfer_Learning.keras')

        try:
            # Assign the loaded model to the class variable
            ModelDeployConfig.model = load_model(model_path, compile=False)
            print("✅ Django App: Model loaded successfully inside ready()!")
        except Exception as e:
            print(f"❌ Django App: Error loading model: {e}")
            ModelDeployConfig.model = None