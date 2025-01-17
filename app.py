import pandas as pd
import pickle as pk
import streamlit as st

# Load the model
try:
    model = pk.load(open('C:\\Users\\jayam\\House Price prediction project\\House_prediction_model.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.header('House Price Predictor')
data = pd.read_csv('C:\\Users\\jayam\\House Price prediction project\\Cleaned_data.csv')

beds = st.selectbox('Choose the beds', data['beds'])
size = st.number_input('Enter Total size')
bath = st.number_input('Enter number of bathrooms')
zip_code = st.number_input('Enter zip code')

input_data = pd.DataFrame({'beds': [beds], 'baths': [bath], 'size': [size], 'zip_code': [zip_code]})

if st.button('Predict'):
    try:
        prediction = model.predict(input_data)
        st.write(f'Predicted house price: ${prediction[0]:.2f}')
    except Exception as e:
        st.error(f"Error making prediction: {e}")