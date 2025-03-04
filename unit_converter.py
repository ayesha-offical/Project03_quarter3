import streamlit as st

def converts_unit(value, unit_from, unit_to):
    conversion ={
        "meters_kilometers": 0.001, # meter = 0.001 kilometer
        "kilometers_meters": 1000, # kilometer = 1000 meter
        "grams_kilograms": 0.001, # gram = 0.001 kilogram
        "kilograms_grams": 1000, # kilogram = 1000 gram
    }

    key = f"{unit_from}{unit_to}" # Generate a key based on the input and output units

    if key in conversion: #all value of conversion is in the key word
        converts_unit = conversion[key]  #all value of conversion is convert in the converts_unit variable
        return value * converts_unit
    else:
        return "Invalid unit conversion"
    
st.title("Unit Converter ⚖️")
value = st.number_input("Enter the value you want to convert: ")
unit_from = st.selectbox("Convert From", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Convert To", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = converts_unit(value, unit_from, unit_to)
    st.success(f'Converted value: {result}')















import streamlit as st  # Import Streamlit for creating the web-based UI


# Function to convert units based on predefined conversion factors or formulas
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on input and output units
    if key in conversions:
        conversion = conversions[key]
        # If the conversion is a function (e.g., temperature conversion), call it
        return (
            conversion(value) if callable(conversion) else value * conversion
        )  # Otherwise, multiply by the conversion factor
    else:
        return "Conversion not supported"  # Return message if conversion is not defined


# Streamlit UI setup
st.title("Simple Unit Converter")  # Set title for the web app

# User input: numerical value to convert
value = st.number_input("Enter value:", min_value=1.0, step=1.0)

# Dropdown to select unit to convert from
unit_from = st.selectbox(
    "Convert from:", ["meters", "kilometers", "grams", "kilograms"]
)

# Dropdown to select unit to convert to
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)  # Call the conversion function
    st.write(f"Converted Value: {result}")  # Display the result