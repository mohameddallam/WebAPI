import streamlit as st
import requests

st.set_page_config(page_title="People in Space", layout="centered")

st.title("🚀 People in Space")
st.markdown("This app shows how many people are currently in space using a live Web API.")

# Get data from API
response = requests.get("http://api.open-notify.org/astros.json")

if response.status_code == 200:
    data = response.json()
    st.subheader(f"👩‍🚀 Number of people in space: {data['number']}")
    
    names = [person['name'] for person in data['people']]
    st.write("### Astronauts:")
    for name in names:
        st.markdown(f"- {name}")
else:
    st.error("Failed to fetch astronaut data.")

# Get ISS location
st.write("---")
st.write("### 🛰️ Current Location of the ISS")

loc_response = requests.get("http://api.open-notify.org/iss-now.json")

if loc_response.status_code == 200:
    loc_data = loc_response.json()
    latitude = float(loc_data['iss_position']['latitude'])
    longitude = float(loc_data['iss_position']['longitude'])
    st.map(data=[{"lat": latitude, "lon": longitude}])
else:
    st.error("Failed to fetch ISS location.")