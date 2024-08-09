import streamlit as st
import plotly.express as px
from backend import get_data, get_city_name, get_images
import time

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for next {days} days in {place}")

try:
    data, dates = get_data(get_city_name(place), days, option)
    figure = px.line(x=dates, y=data, labels={"x": "Date", "y": "Temperature (C)"})

    if option == "Temperature":
        st.text(f"Current temperature is:")
        st.subheader(f":red-background[{int(data[0])}°C]")
        st.plotly_chart(figure)
    if option == "Sky":
        st.subheader(f"Now :red-background[{data[0]}]")

        images_data  = get_images()
        images = []

        for i in range(len(data)):
            for my_dict in images_data:
                if data[i] == my_dict["name"]:
                    img_path = my_dict["path"]
                    images.append(img_path)
        st.image(images, width=88, caption=dates)

        ##################################################################################

        # tabs_list = []
        #
        # columns_list = []
        # columns_list = st.columns(days)
        #
        # tabs_names = [f"Day {i + 1}" for i in range(days)]
        # tabs_list = st.tabs(tabs_names)
        # images_data = get_images()
        #
        #
        # start = 0
        # stop = 8
        # amount = days * 8
        # current_day = dates[0].strftime('%Y-%m-%d')
        # for tab in tabs_list:
        #     with tab:
        #         for i in range(start, stop):
        #             compare = current_day.split("-")
        #             compare = [int(i) for i in compare]
        #             for my_dict in images_data:
        #                 if data[i] == my_dict["name"]:
        #                     print(i)
        #                     img_path = my_dict["path"]
        #             st.image(img_path, width=150)
        #             st.text(f"{dates[i]}")
        #
        #             next_day = dates[i].strftime('%Y-%m-%d')
        #             compare2 = next_day.split("-")
        #             compare2 = [int(i) for i in compare2]
        #
        #             if compare[1] == compare2[1] or compare[2] == compare2[2]:
        #                 current_day = next_day
        #
        #             if stop == amount - 1:
        #                 break
        #             if i == stop - 1:
        #                 start = start + 8
        #                 stop = stop + 8
        #                 break

        ##################################################################################
except KeyError:
    time.sleep(10)
    st.info("You need to enter city to see weather forecast")
except IndexError:
    st.info("Unfortunately we have not data about this place")


