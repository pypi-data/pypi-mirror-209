import os
import joblib
import numpy as np
import logging
import pandas as pd

def prepare_data(data, target_col="y"):
    """It returns features and label for the given dataset

    Args:
        df (pd.DataFrame): This is a dataframe
        target_col (str, optional): label or targel column. Defaults to "y".

    Returns:
        tuple: features and label
    """
    df = pd.DataFrame(data)
    logging.info("preparing data for training")
    x = df.drop(columns=target_col)
    y = df[target_col]

    return x, y

class Perceptron:
    def __init__(self, eta=None, epochs=None):
        """Constructor for the Perceptron class

        Args:
            eta (int, optional): ETA value. Defaults to None.
            epochs (int, optional): number of epochs. Defaults to None.
        """
        if (eta is not None) and (epochs is not None):
            self.eta=eta
            self.epochs = epochs

            self.weights = np.random.rand(3)*1e-4

            logging.info("Initial weights are \n")
            logging.info(self.weights)
        
    def _z_value(self, inputs, weights):
        """computes z value for the given inputs and weights

        Args:
            inputs (np.array): inputs 
            weights (np.array): weights

        Returns:
            np.array: returns the z value
        """
        return np.dot(inputs, weights)
        
    def _activation_func(self, z):
        """Activation function / decision function of perceptron

        Args:
            z (np.array): z value

        Returns:
            np.array: value after applying activation
        """
        return np.where(z>=0, 1, 0)
    
    def fit(self, x, y):
        """fits the model for the given data

        Args:
            x (np.array): features
            y (np.array): label
        """
        self.x = x
        self.y = y
        
        x_with_bias = np.c_[x, -np.ones((len(x), 1))]
        
        for epoch in range(1, self.epochs+1):
            logging.info("#"*50)
            logging.info(f"\n Epoch {epoch}/{self.epochs}\n")
            
            z = self._z_value(x_with_bias, self.weights)
            y_hat = self._activation_func(z)
            logging.info(f"Prediction is : is {y_hat}\n")
            
            error = y - y_hat
            logging.info(f"Error : is\n{error}\n")
            
            self.weights = self.weights + self.eta * np.dot(x_with_bias.T, error)
            logging.info(f"Updated weights are  : \n{self.weights}\n")
        
        self.error = error
        # logging.info(f"Total loss is {self.error.sum()}")
        logging.info("model fitting complete")
    
    def predict(self, x):
        """prediction for the given input

        Args:
            x (np.array): input

        Returns:
            np.array: prediction for given x
        """
        x.append(-1)
        z = np.dot(x, self.weights)
        y_hat = self._activation_func(z)
        return y_hat
    
    @property
    def total_loss(self):
        """calculates total loss

        Returns:
            int: error value after training
        """
        return self.error.sum()
    
    def save(self, filename, model_dir="Perceptron models"):
        """saves the model

        Args:
            filename (str): file name to save model
            model_dir (str, optional): folder to save the model. Defaults to "model".
        """
        os.makedirs(model_dir, exist_ok=True)
        file_path = os.path.join(model_dir, filename)
        joblib.dump(self, file_path)
        logging.info(f"Model is save to {file_path}")
        
    def load(self, filename, model_dir="model"):
        """method for loading the model with the path of saved model

        Args:
            filename (str): file name for the model to load
            model_dir (str, optional): models. Defaults to "model".

        Returns:
            Perceptron: instance of Perceptron class
        """
        file_path = os.path.join(model_dir, filename)
        return joblib.load(file_path)
