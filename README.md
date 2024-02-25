# Logify
# 25 Feb 2024

Sign Language Recognition with Text-to-Speech


Documentation

Libraries Used
cvzone : 1.4.1
MediaPipe : 0.10.9
Pillow : 9.3.0
numpy : 1.23.5
opencv-python : 4.7.0.72
pandas : 2.0.1
tensorflow : 2.12.0
keras : 2.12.0
openai
Python Interpreter Version
Python 3.11

Working Logic
The data has been trained with the help of RoboFlow. We used the method of extracting keypoints and using them for training our data using the pre-built libraries by TensorFlow and Keras.

We set a fixed resolution of the image for collecting the dataset.
Once the dataset is collected in a specified directory, we extract the keypoints using MediaPipe.
Using MediaPipe, we extract the hand landmarks data from the dataset and convert that into an array, storing the data by creating a folder.
Training the Data
With the data in the form of arrays, we used Keras of TensorFlow for training the data and generating our own trained data model (Bhasha.h5).

GUI Interface
Our GUI interface includes features/buttons and guidelines that make it user-friendly. When the "Train My Model" button is pressed, it runs the file which can collect data and train the model.

The "Start" button opens our main app in another window for ease of use.

Project Vision
Our view towards this project is the implementation of sign language recognition with text-to-speech. If this idea is implemented within smartwatches using LIDARs and hand sign landmarks, and creating a real-time 3D mapping of hand landmarks, it can greatly improve the accuracy of the software and convert sign language into speech. This could help mute individuals express themselves verbally.



Overview

This project utilizes various libraries, including cvzone, MediaPipe, Pillow, numpy, opencv-python, pandas, tensorflow, and keras, along with Python 3.11, to recognize sign language and convert it to text-to-speech.

Functionality

Data is trained using RoboFlow, extracting keypoints and using pre-built TensorFlow and Keras libraries.
Images are collected at a fixed resolution and keypoints are extracted using MediaPipe.
Hand landmarks data is converted into arrays and stored in a folder.
Training is done using Keras to generate a trained data model (Bhasha.h5).
GUI Interface

The GUI interface includes buttons for data collection, training the model, and starting the main app in a separate window for user-friendly interaction.

Project Vision

The aim is to implement sign language recognition with text-to-speech, potentially for use in smartwatches with LIDAR technology for real-time 3D mapping of hand landmarks, enhancing communication for mute individuals.
