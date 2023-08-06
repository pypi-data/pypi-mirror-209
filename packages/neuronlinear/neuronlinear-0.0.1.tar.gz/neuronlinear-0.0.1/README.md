# Perceptron Package - neuronlinear



![Perceptron](https://images.deepai.org/glossary-terms/perceptron-6168423.jpg)

Welcome to the neuronlinear ! This package is designed to provide a simple and efficient implementation of the Perceptron algorithm for binary classification tasks. Whether you are new to machine learning or an experienced practitioner, the Perceptron Package offers a versatile and easy-to-use tool for your classification needs.

## Features

* Lightweight and efficient implementation of the Perceptron algorithm
* Supports both online and batch learning modes
* Flexible customization options for data preprocessing and feature engineering
* Simple and intuitive API for training and inference
Compatible with Python 3.x

## Installation

You can easily install the Perceptron Package using pip:

```pip install neuronlinear```

## Quick Start
Using the neuronlinear Package is straightforward. Here's a simple example to get you started:

```
from neuronlinear.model import Perceptron, prepare_data


ETA = 0.1 #leaning rate
EPOCHS = 10 #epochs count

# Create a Perceptron object
perceptron = Perceptron(eta=ETA, epochs=EPOCHS)

data = {"x1":[0, 0, 1, 1], "x2" : [0, 1, 0, 1], "y" : [0, 1, 1, 1]}

X, y = prepare_data(data)

perceptron.fit(X, y)
print(f"Prediction for > 0, 1 is {perceptron.predict([0, 1])}")

print(f"Total loss is {model.total_loss}")

```

## Contributing
We welcome contributions from the community! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on our GitHub repository.

## License

The neuronlinear Package is licensed under the MIT License.

## Acknowledgments
We would like to express our gratitude to the contributors and supporters who have helped make this package possible.

If you find the Perceptron Package useful, please consider giving it a star on GitHub. Your support is greatly appreciated!

> Note: The neuronlinear Package is provided as-is without any warranty. Use at your own risk.