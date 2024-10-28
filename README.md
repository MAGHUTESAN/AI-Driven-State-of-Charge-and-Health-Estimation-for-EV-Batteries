# AI-Driven-State-of-Charge-and-Health-Estimation-for-EV-Batteries-
This repository contains code for a deep learning model using a **Multilayer Perceptron (MLP)** architecture to predict Ather battery health and performance metrics, including State of Charge (SoC), State of Health (SoH), Duration, and Speed.

![EV](https://static.vecteezy.com/system/resources/previews/025/733/581/original/electric-car-at-charging-station-abstract-electric-power-charger-ev-clean-energy-alternative-energy-electric-charger-concept-electronic-vehicle-power-dock-illustration-vector.jpg)





## Table of Contents
- [Overview](#overview)
- [Model Architecture](#model-architecture)
- [Dataset Description](#dataset-description)
- [Usage](#usage)
- [Future Work](#future-work)
- [Contributing](#contributing)

## Overview

This project leverages a **Multilayer Perceptron (MLP)** model to predict various Ather battery metrics:
- **State of Charge (SoC)** – Percentage of remaining charge
- **State of Health (SoH)** – Health status of the battery in percentage
- **Duration** – Expected operational time (in hours)
- **Speed** – Associated speed in km/h

## Model Architecture

The model uses a multi-input, multi-output **MLP** architecture with each branch dedicated to predicting one of the target variables (SoC, SoH, Duration, and Speed). Each branch includes:
- Dense layers with LeakyReLU activation functions for non-linearity
- Independent output layers for each target variable

## Dataset Description

The dataset used is based on **Ather Battery Specifications**, which includes the following features:
- **Voc**: Open-circuit voltage
- **Available Energy (kWh)**: Remaining energy in the battery
- **Battery Current (A)**: Current drawn from the battery
- **Duration (hrs)**: Expected duration of battery operation
- **Range150 (km)**, **Range145 (km)**, and **Range140 (km)**: Range of the battery at specific thresholds

### Additional Constant Values

Two additional constants are added to the dataset for improved feature representation:
- **Full Battery Voltage**: 58.8V
- **Minimum Battery Voltage**: 38.5V

Ensure your dataset is formatted with these features before running the model.

## Usage

1. **Prepare the Data**:
   Place your initial data in a CSV file named [`Dataset_of_Ather.csv`](Dataset_of_Ather.csv). This CSV file should include the columns specified above to match the Ather battery specifications. Missing values should be removed before loading the data.

2. **Run the Model**:
   - Execute the code cells in sequence in either a Jupyter Notebook or Python script. The code includes cells for:
      - Loading and preprocessing the dataset
      - Defining and compiling the MLP model
      - Training the model with an initial dataset
   - The code structure is divided into cells for easy execution and iterative improvements.

## Future Work

### Self-Training for Continuous Improvement

To enhance model performance over time, a self-training mechanism could be implemented, allowing the model to retrain on high-confidence predictions from new data. This process involves:
1. **Predicting on New Data**: Make predictions for each target variable (SoC, SoH, Duration, Speed) using the trained model on newly collected battery data.
2. **Filtering High-Confidence Predictions**: Use a confidence threshold to identify reliable predictions. For instance, predictions with a confidence level above 90% can be considered high-confidence.
3. **Retraining the Model**: Append high-confidence predictions to the training set and retrain the model, enabling it to learn from the latest data and improve its accuracy over time.

### App Deployment

Deploying the model as an application could enable users to input real-time battery data and receive predictions for SoC, SoH, Duration, and Speed. Possible deployment options include:
- **Web Application**: Build a front end using frameworks like Flask or Django to allow users to interact with the model.
- **Mobile App**: Integrate with a mobile app to provide on-the-go battery health insights.

## Contributing

Contributions are welcome! If you would like to propose improvements, add new features, or fix bugs, feel free to submit a pull request or open an issue.
