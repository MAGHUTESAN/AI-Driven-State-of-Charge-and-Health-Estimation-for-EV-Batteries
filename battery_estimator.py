import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the pre-trained MLP model
model = tf.keras.models.load_model('battery_prediction_model.h5')  # Replace with the path to your model

# Initialize Streamlit app
st.title("EV Battery Health and Performance Estimator")

# Allow user to set constants
FULL_BATTERY_VOLTAGE = st.number_input("Full Battery Voltage (V)", min_value=0.0, value=58.8, format="%.2f")
MINIMUM_BATTERY_VOLTAGE = st.number_input("Minimum Battery Voltage (V)", min_value=0.0, value=38.5, format="%.2f")
FULL_CHARGE_CAPACITY = st.number_input("Full Charge Battery Capacity (kWh)", min_value=0.0, value=3.183216, format="%.6f")
CHARGE_CURRENT_CAPACITY = st.number_input("Charge Current Capacity (Ah)", min_value=0.0, value=54.5, format="%.2f")
RANGE_CONSTANT = st.number_input("Range Constant (km)", min_value=0.0, value=150.0, format="%.2f")

# Option for user to choose between single entry or CSV file upload
input_type = st.radio("Choose input type", ('Single Entry', 'CSV File'))

if input_type == 'Single Entry':
    # User inputs for Battery Pack Voltage, Battery Current, and Internal Resistance
    voltage = st.number_input("Battery Pack Voltage (V)", min_value=0.0, format="%.2f")
    current = st.number_input("Battery Current (A)", min_value=0.0, format="%.2f")
    resistance = st.number_input("Internal Resistance (Ω)", min_value=0.0, format="%.9f")

    # Check if all inputs are provided
    if st.button("Predict"):
        # Process input and prepare it for prediction
        input_data = np.array([[voltage, current, resistance]])
        
        # Scale the input using the same method as during training
        scaler = StandardScaler()
        input_data_scaled = scaler.fit_transform(input_data)  # Ensure to use the original scaler from training

        # Make predictions
        predictions = model.predict(input_data_scaled)
        soc_pred, soh_pred, duration_pred, speed_pred = predictions[0]

        # Calculations for correct values
        voc = voltage + (current * resistance)
        soc = 100 * (voc - MINIMUM_BATTERY_VOLTAGE) / (FULL_BATTERY_VOLTAGE - MINIMUM_BATTERY_VOLTAGE)
        available_energy = (soc / 100) * FULL_CHARGE_CAPACITY
        soh = 100 * available_energy / FULL_CHARGE_CAPACITY
        duration = CHARGE_CURRENT_CAPACITY / current
        speed = RANGE_CONSTANT / duration

        st.subheader("Predicted Values")
        st.write(f"SoC (%): {soc:.2f}")
        st.write(f"SoH (%): {soh:.2f}")
        st.write(f"Duration (hrs): {duration:.2f}")
        st.write(f"Speed (km/hr): {speed:.2f}")

elif input_type == 'CSV File':
    # CSV file upload
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the CSV file
        data = pd.read_csv(uploaded_file)
        
        # Ensure the CSV file has the required columns
        if {'voltage', 'current', 'resistance'}.issubset(data.columns):
            scaler = StandardScaler()
            input_data = data[['voltage', 'current', 'resistance']]
            input_data_scaled = scaler.fit_transform(input_data)  # Scale using original scaler from training
            
            # Predict for each row
            predictions = model.predict(input_data_scaled)
            results = []
            
            for i, pred in enumerate(predictions):
                soc_pred, soh_pred, duration_pred, speed_pred = pred
                voltage = data['voltage'][i]
                current = data['current'][i]
                resistance = data['resistance'][i]
                
                voc = voltage + (current * resistance)
                soc = 100 * (voc - MINIMUM_BATTERY_VOLTAGE) / (FULL_BATTERY_VOLTAGE - MINIMUM_BATTERY_VOLTAGE)
                available_energy = (soc / 100) * FULL_CHARGE_CAPACITY
                soh = 100 * available_energy / FULL_CHARGE_CAPACITY
                duration = CHARGE_CURRENT_CAPACITY / current
                speed = RANGE_CONSTANT / duration
                
                results.append({
                    "Voltage (V)": voltage,
                    "Current (A)": current,
                    "Resistance (Ω)": resistance,
                    "SoC (%)": soc,
                    "SoH (%)": soh,
                    "Duration (hrs)": duration,
                    "Speed (km/hr)": speed
                })
                
            results_df = pd.DataFrame(results)
            st.subheader("Predicted Values")
            st.dataframe(results_df)
            
            # Option to download results
            csv = results_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download predictions as CSV",
                data=csv,
                file_name='predictions.csv',
                mime='text/csv',
            )
        else:
            st.error("CSV file must contain 'voltage', 'current', and 'resistance' columns.")

# Instructions to run on a network
st.write("To access this app on another device, use the command below:")
st.code("streamlit run app.py --server.address 0.0.0.0 --server.port 8501", language="bash")
