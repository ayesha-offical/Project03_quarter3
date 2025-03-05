import streamlit as st


# Function to convert units based on predefined conversion factors or formulas
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on the input and output units
    # logical units
    if key in conversions: #all value of conversion is in the key word
       converts_unit = conversions[key] #all value of conversion is convert in the converts_unit variable
       return (
            converts_unit(value) if callable(converts_unit) else value * converts_unit
        )  # Otherwise, multiply by the conversion facto
    else:
        return "Conversion not supported"  #  message if conversion is not defined


# Streamlit UI
st.title("Unit Converter ⚖️")  # Set title for the web 

# User input: numerical value to convert
value = st.number_input("Enter value:", min_value=1.0, step=1.0)

unit_from = st.selectbox(
    "Convert from:", ["meters", "kilometers", "grams", "kilograms"]
)

unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

#button to trigger the button functionality

if st.button("Convert🔄"):
    result = convert_units(value, unit_from, unit_to)  # Call the conversion function
    st.write(f"Converted Value🔢: {result}")  # Display the result
    st.write("-------------------------")
    st.write("Build by ❤️ [Ayesha Faisal] (https://github.com/ayesha-offical)")