from io import BytesIO
from tensorflow._api.v2.image import rgb_to_grayscale, resize
from keras.models import load_model
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os

class AIModelLoader:
    _instance = None
    __current_dir = os.path.dirname(os.path.abspath(__file__))

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._model = cls._instance._load_model()
        return cls._instance

    def _load_model(self):
        model_path = os.path.join(self.__current_dir, "best_1600_epochs_model.keras")
        return load_model(model_path)

    def predict_image(self, image):
        image_data = image.read()
        image.seek(0)  
        image_pil = Image.open(BytesIO(image_data))
        image_array = np.array(image_pil)
        
        if len(image_array.shape)  == 2:
            image_array = np.stack((image_array, image_array, image_array), axis=-1)

        image_tensor = np.expand_dims(image_array, axis=0)
        
        if image_tensor.shape[-1] == 4:
            image_tensor = image_tensor[:, :, :, :3]

        bw_image = rgb_to_grayscale(image_tensor)

        size = 200
        bw_image = resize(bw_image, [size, size])
        result = self._model.predict(bw_image)
        class_names = ['adenocarcinoma', 'large cell carcinoma', 'normal', 'squamous cell carcinoma']
        return class_names[np.argmax(result)], np.round(result)