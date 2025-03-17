import streamlit as st
import time as t

#set app name and layout 
st.set_page_config(page_title="Unit Converter",layout="centered",page_icon="💱")

# streamlit UI
st.title("🥰 Welcome To :blue[ Unit Converter]")
st.write("###### _This is a unit convertor app that converts units from one unit to another_.")

# category selected
def cate_selec():
        st.divider()
        category = st.selectbox("Select a category",["📏Length","⌚Time","⚖️ Weight","🌡Temperature","🏃Speed","🧪Volume"])
   
        if category =="⌚Time":
             time() 
        elif category == "🏃Speed":
             speed()
        elif category == "⚖️ Weight":
            weight()            
        elif category == "📏Length":
            lenght()
        elif category == "🌡Temperature":
            temperature()
        elif category == "🧪Volume":
            volume()
 
def factor (header,units):   
    
    st.subheader(f'{header} Converter')   

    value = st.number_input("Enter value:",min_value=0,value=1)
    
    from_unit = st.selectbox("From",list(units.keys()))
    To_unit = st.selectbox("TO",list(units.keys()))

    result = value * units[from_unit]/units[To_unit]

    if st.button("Convert",icon="♻"):
     # spinner loading 
     with st.spinner("converting.."): 
          #  t -> Time python module
           t.sleep(3)
     st.success(f'{value} {from_unit} = {result:.3f} {To_unit}')          
  
     # time function   
def time ():
     units = {
         "Seconds":1,
         "Minutes":60,
         "Hours":3600,
         "Days":86400,
         "Weeks": 604800.0,
         "Years": 31536000.0
         }  
     factor("⌚ Time",units)
     
# speed function
def speed ():
     units = {
        "Meters per second": 1,
        "Kilometers per hour": 0.2777777777777778,
        "Miles per hour": 0.44704,
        "Foot per second": 0.3048,
     }
     factor("🏃 Speed",units)

# Weight function
def weight ():
     units={
      "Kilograms": 1,
      "Grams": 0.001,
      "Pounds": 0.453592,
      "Ounces": 0.0283495
     } 
     factor("⚖️ Weight",units)

# lenght function
def lenght():
     units = {
      "Meters": 1,
      "Kilometers": 1000,
      "Centimeters": 0.01,
      "Millimeters": 0.001,
      "Miles": 1609.34,
      "Yards": 0.9144,
      "Feet": 0.3048,
      "Inches": 0.0254
    }
     factor("📏 Lenght",units)

# Volume function
def volume ():
     units={
        "litre":1,                  
        "Milli litre":0.001,         
        "Gallon": 3.78541,          
        "Cubic Meter": 1000.0, 
     }
     factor("🧪 Volume",units)

# temperature function
def temperature():
    st.subheader("🌡 Temperature Converter")
    value = st.number_input("Enter Value:", value=1 , min_value=0)

    from_unit = st.selectbox("From",["Celsius","Fahrenheit","kelvin"])
    To_unit = st.selectbox("To",["Celsius","Fahrenheit","Kelvin"])
  
    if from_unit ==To_unit:
       result = value  

    elif from_unit == "Celsius" and  To_unit == "Fahrenheit":
            result = (value * 9/5) + 32

    elif from_unit == "Celsius" and To_unit == "Kelvin":
         result = value + 273.15

    elif from_unit == "Fahrenheit" and To_unit == "Celsius":
         result = (value -32) * 5/9 

    elif from_unit == "Fahrenheit" and To_unit == "Kelvin":
         result = (value -32) * 5/9 + 273.15

    elif from_unit == "Kelvin" and To_unit =="Celsius":
         result = value - 273.15
    
    elif from_unit == "Kelvin" and To_unit =="Fahrenheit":
         result = (value - 273.15 ) * 9/5 + 32

# spinner loading 
    if st.button("Convert"):
        with st.spinner("converting.."):
            t.sleep(3)
        st.success(f"{value} {from_unit} = {result} {To_unit}")    

cate_selec()

# footer 
st.markdown("<hr style='margin-top:5rem'>",unsafe_allow_html=True)

st.markdown("<p style='text-align:center; font-family:sans-serif;font-style:italic;'>Developed by <span style='color: #2e8f90' >Hammad Iqbal</span></p>",unsafe_allow_html=True)
    
   