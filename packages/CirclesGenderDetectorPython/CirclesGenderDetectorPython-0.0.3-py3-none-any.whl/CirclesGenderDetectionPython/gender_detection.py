import numpy as np
import tensorflow as tf
import os
from tensorflow.keras.utils import Sequence
from keras.models import load_model
from tensorflow.keras import Sequential,Model,Input
from tensorflow.keras.layers import Conv2D,MaxPool2D,Flatten,Dense,Dropout,GlobalAveragePooling2D
from keras.regularizers import l2
import cv2
from cv2 import VideoCapture,imshow,imwrite,waitKey

from tensorflow import keras
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.optimizers import SGD
from keras.applications.inception_v3 import InceptionV3

import random
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import pandas as pd
from keras.preprocessing.image import ImageDataGenerator as Imgen
from keras.models import Model,Sequential
import keras.layers as layers
from keras.layers import Input,Conv2D,MaxPooling2D,Dropout,Flatten,Dense,GlobalAveragePooling2D,BatchNormalization
from dotenv import load_dotenv
load_dotenv()
from CirclesLocalLoggerPython.LoggerServiceSingleton import LoggerServiceSingleton







def create_model(input_shape):
    """
    Function to create a CNN model with multiple Convolutional, MaxPooling, and Dense layers. The model takes
    as input an image tensor of shape (input_shape) and outputs a prediction vector of shape (1,). 

    Args:
        input_shape (tuple): A tuple representing the shape of input tensor of an image.
                             (height, width, channel)

    Returns:
        keras.Sequential: A compiled CNN model instance. 
    """
    CNNmodel = keras.Sequential([
        layers.Conv2D(16, (3, 3), input_shape=input_shape, activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2,2)),
        layers.Dropout(0.2),
        
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2,2)),
        layers.Dropout(0.2),

        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2,2)),
        layers.Dropout(0.2),

        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2,2)),
        layers.Dropout(0.2),

        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.2),  
        layers.Dense(128, activation = 'relu'),
        layers.Dropout(0.2), 
        layers.Dense(64, activation = 'relu'),
        layers.Dropout(0.2), 
        layers.Dense(32, activation = 'relu'),
        layers.Dropout(0.2), 
        layers.Dense(16, activation = 'relu'),
        layers.Dense(1, activation = 'sigmoid')
    ])

    return CNNmodel

def capture_write(filename="image.jpeg", port=0, ramp_frames=30, x=178, y=218):
    """
    Captures an image using the webcam and saves it to a file.
    
    Args:
        filename (str): The name of the file to save the image to. Default is "image.jpeg".
        port (int): The port number of the camera to use. Default is 0.
        ramp_frames (int): The number of frames to skip before capturing the image. Default is 30.
        x (int): The width of the image in pixels. Default is 178.
        y (int): The height of the image in pixels. Default is 218.
    
    Returns:
        numpy.ndarray: The captured image as a NumPy array.
    """
    camera = cv2.VideoCapture(port)

    # Set Resolution
    camera.set(3, x)
    camera.set(4, y)

    # Adjust camera lighting
    for i in range(ramp_frames):
        temp = camera.read()
    retval, im = camera.read()
    
    del(camera)
    return im


class GenderClassifier:
    def __init__(self):
        """
        GenderClassifier is a class that detects the gender of a person through webcam images.

        Args:
            train (bool): a boolean indicating whether to train the model or not. Defaults to False.
            predict (bool): a boolean indicating whether to predict the gender or not. Defaults to True.
        """
        self.logger = LoggerServiceSingleton()
        self.lgrins = self.logger.get_instance()

    def predict_gender(self,model_path,image_path=None):
        """
        This function captures an image from the webcam and predicts the gender of the person.

        Returns:
            str: a string indicating the predicted gender ('Male' or 'Female').
        """

        # Test Functionality
        if image_path is not None:
           # Read the contents of the image file
           image = tf.io.read_file(image_path)

           # Decode the JPEG-encoded image into a tensor
           image = tf.image.decode_jpeg(image)
       
           image = tf.image.resize(image, (178,218))
        else:
           # Permission to use webcam and work on singular image
           inquiry = input("""
           This script will take a picture with your webcam, 
           this will only be for the purposes for determining your gender. 
           Proceed? (Y/n) """)

           if inquiry.lower()!="y" and inquiry.lower!="yes":
              self.lgrins.log("\nAborting\n")
              exit()

           # Capture Image from Webcam
           image = tf.image.resize(capture_write(), (178, 218))

        # Rescale the pixel values to a range of [0, 1]
        image = image / 255.0

        # Apply data augmentation
        if np.random.rand() < 0.5:
            image = tf.image.flip_left_right(image)

        model = load_model(model_path)
        prediction = model.predict(tf.expand_dims(image, axis=0))[0]
        self.lgrins.log("Prediction Confidence (>0.5 Male,<=0.5 Female)",prediction)
        if prediction > 0.5:
            #print("Male")
            return "Male"
        else:
            #print("Female")
            return "Female"






    def train_model(self, save=True):
        """
        This function trains a model to detect the gender of a person through images.

        Args:
            save (bool): a boolean indicating whether to save the trained model or not. Defaults to True.
        """
        # Build Model With Transfer Learning from Pre-Trained VGG-Face
        model = create_model((178, 218, 3))

        train = tf.keras.utils.image_dataset_from_directory("./Train", image_size=(178, 218))
        validation = tf.keras.utils.image_dataset_from_directory("./Validation", image_size=(178, 218))
        test = tf.keras.utils.image_dataset_from_directory("./Test", image_size=(178, 218))

        model.compile(loss='binary_crossentropy', optimizer="adam", metrics='accuracy')

        # Train your model using the custom early stopping callback
        model.fit(train, epochs=10, batch_size=32, validation_data=validation)

        # Evaluate the performance of the model on a validation set
        loss, accuracy = model.evaluate(test)
        self.lgrins.log(loss, accuracy)
        if save is True:
            model.save("gender_detection", save_format='h5')
            
            
  

