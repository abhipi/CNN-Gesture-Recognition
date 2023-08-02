# CNN based Hand Gesture Recognition
This repository, abhipi/CNN-Gesture-Recognition, contains code and model files for hand gesture recognition using a 7-layer convolutional neural networks (CNN). The main functionality of the code directory includes:
1. Collecting data: The "collect_data.py" script captures images of hand gestures using a webcam and saves them in separate directories for training and testing.
2. Training the model: The "train_data.py" script builds and trains a CNN model using the collected data.
3. Making predictions: The "predict.py" script uses the trained CNN model to make predictions on hand gestures captured from a webcam.
Please refer to the individual script files for more details on their functionalities and usage.
Additionally, this repository includes the following model files:
* "model-bw.json": a JSON representation of the CNN model architecture.
* "model-bw.h5": contains the weights of the trained CNN model.
# Workflow
1. Data Collection: Use the collect_data.py script to capture images of hand gestures using a webcam. The captured images are saved in separate directories for training and testing.

2. Model Training: Run the train_data.py script to build and train a Convolutional Neural Network (CNN) model using the collected data. The script defines the CNN model architecture and compiles it with the Adam optimizer and categorical cross-entropy loss. It uses an ImageDataGenerator to preprocess the training data and augments it with transformations like rescaling, shearing, zooming, and horizontal flipping. The training set is then used to fit the model with a specified number of epochs and steps per epoch. After training, the model architecture is saved in a JSON file (model-bw.json) and the model weights are saved in an h5 file (model-bw.h5).

3. Prediction: Execute the predict.py script to use the trained CNN model for gesture recognition. The script loads the saved model architecture and weights from the JSON and h5 files. It sets up a video capture using the default webcam and enters a loop that continuously captures images, processes them, and predicts the gesture using the loaded model until the 'q' key is pressed. The captured frames are preprocessed by flipping, region of interest selection, cropping, and thresholding to enhance gesture visibility. The processed image is resized to 64x64 pixels and passed through the model's predict method to obtain predicted probabilities for each gesture category. The predicted probabilities are then converted to a list of integers, and the corresponding category names for probabilities equal to 1 are printed. The loop breaks when the 'q' key is pressed.

Overall, the workflow involves collecting hand gesture data, training a CNN model using the data, and then using the trained model for real-time gesture recognition using a webcam.

