# AI-Driven-State-of-Charge-and-Health-Estimation-for-EV-Batteries-
ML model for predicting SoC, SoH, Duration &amp; Speed in batteries with self-training for high-confidence continuous learning.This repository contains code for a deep learning model that predicts battery health and performance metrics, including SoC, SoH, Duration, and Speed. The model incorporates a self-training loop to continuously improve its accuracy by retraining on high-confidence predictions from new data.

![EV](https://static.vecteezy.com/system/resources/previews/025/733/581/original/electric-car-at-charging-station-abstract-electric-power-charger-ev-clean-energy-alternative-energy-electric-charger-concept-electronic-vehicle-power-dock-illustration-vector.jpg)

## Table of Contents
- [Overview](#overview)
- [Model Architecture](#model-architecture)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview

This project leverages a multi-branch deep learning model to predict various battery metrics:
- **State of Charge (SoC)** – Remaining charge percentage of the battery
- **State of Health (SoH)** – Overall health of the battery in percentage
- **Duration** – Estimated operational time (in hours)
- **Speed** – Associated speed in km/h

### Self-Training for Continuous Improvement

The model includes a self-training mechanism. After making predictions on new data, high-confidence predictions are identified and added to the training dataset, allowing the model to continuously learn from new data.

## Model Architecture

The model uses a multi-input, multi-output architecture with each branch focused on predicting a specific target variable (SoC, SoH, Duration, and Speed). Each branch includes:
- Dense layers with LeakyReLU activation functions
- Separate output layers for each target variable

The self-training loop filters high-confidence predictions from new data, which are appended to the training dataset and used for retraining.


## Usage

1. **Prepare the Data**:
   Place your initial data in a CSV file (e.g., `Final_pred.csv`). The CSV should include columns such as `Voc`, `Available Energy`, `Battery Current`, `Duration`, and range columns (e.g., `Range150`).

2. **Run the Model**:
   You can execute the code in a Jupyter Notebook or as a Python script with cells containing the following:
   - Data loading and preprocessing
   - Model definition and training
   - Self-training with new data

3. **Add New Data for Self-Training**:
   To add new data for self-training, structure it similarly to the initial data. High-confidence predictions from new data will be appended to the training set and used to retrain the model.



## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements, bug fixes, or feature requests.


