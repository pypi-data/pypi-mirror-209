#!/usr/bin/env python
# coding: utf-8
# Author : Rahul Bhadani
# Initial Date: 2023-05-17
__author__ = 'Rahul Bhadani'
__email__  = 'rahulbhadani@email.arizona.edu'


import numpy as np
from numpy import pi
from numpy import cos
from numpy import sin

import tensorflow as tf
from tensorflow.keras import layers

class RNNModel(tf.keras.Model):
    """
    Recurrent Neural Network Model Implementation using Tensorflow 2

    Parameters
    ------------
    hidden_units: `int`
        Number of hidden units

    input_size: `int`
        Sizr of the input to the first layer


    """
    def __init__(self, hidden_units, input_size, *args, **kwargs):
        super(RNNModel, self).__init__()
        self.hidden_units = hidden_units
        self.input_size = input_size
        self.rnn = layers.SimpleRNN(hidden_units, activation='relu', input_shape=(None, input_size))
        self.dense = layers.Dense(1)  # Output layer with single unit for speed prediction



    def call(self, inputs):
        x = self.rnn(inputs)
        output = self.dense(x)
        return output

    def compile_model(self, optimizer, loss_fn):
        """
        Compile the model

        Parameters
        -----------
        optimizer: `object`
            Specify the optimizer algorithms such as adam

        loss_fn: `string` | `object`
            Specify the loss function
        """
        self.compile(optimizer=optimizer, loss=loss_fn)

    def train_model(self, input_X, labels_y, epochs, batch_size):
        """
        Train the model

        Parameters
        ----------------
        `input_X`:
            training dataset

        `labels_y`:
            labels or the ground truth

        `epochs`:
            For how many epochs to train

        `batch_size`:
            Batch size to use for every training iteration
        """

        self.fit(input_X, labels_y, epochs=epochs, batch_size=batch_size)

    def model_predict(self, new_data):
        """
        Make predictions from the trained model

        Parameters
        -----------
        `new_data`:
            New data on which prediction needs to be made

        Returns
        ---------

        Predicted Values
        """
        predictions = self.predict(new_data)
        return predictions


