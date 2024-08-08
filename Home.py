import streamlit as st
import pandas

#df = pandas.read_csv("")

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for next {days} days in {place}")
#st.line_chart(df)
