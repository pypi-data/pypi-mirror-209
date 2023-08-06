import cv2
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import time

# Initiate all session states used
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0
if 'frames' not in st.session_state:
    st.session_state['frames'] = []

# Use a callback to display the current value of the slider when changed


def display_value():
    st.session_state['counter'] = st.session_state.myslider

# Function to display video in the Streamlit app


def display_video(video_path, alerts, data):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    i = 0

    resume = False
    column1, column2, column3 = st.columns([1, 1.5, 1])
    with column1:
        # zone to display images
        stframe = st.empty()
    with column3:
        # Display the table
        df = pd.DataFrame(alerts)
        options_builder = GridOptionsBuilder.from_dataframe(df)
        options_builder.configure_selection(
            selection_mode="single", use_checkbox=True)
        grid_options = options_builder.build()
        grid_return = AgGrid(df, grid_options)
        selected_rows = grid_return["selected_rows"]
        # Buttons and zone of display
    col1, col2, col3, col4, col5 = st.columns(
        [1, 4, 1, 1.5, 0.5])
    with col1:
        st.write('')
        st.write('')
        container_2 = st.empty()
        pause = container_2.button('⏸')

    with col2:
        widget = st.empty()
        # Create a Streamlit slider for navigating the video
        widget.slider("", min_value=0, max_value=int(
            cap.get(cv2.CAP_PROP_FRAME_COUNT)), value=st.session_state['counter'], key="myslider", on_change=display_value)
        st.session_state['counter'] = st.session_state.myslider
    with col3:
        st.write('')
        st.write('')
        replay = st.button("↻")
    with col4:
        st.write('')
        st.write('')
        plus = st.button("➕")
    with col5:
        st.write('')
        st.write('')
        minus = st.button("➖")
    if minus:
        st.session_state['counter'] = st.session_state['counter']-1
        # the first frame
    if replay:
        st.session_state['counter'] = 0
        st.session_state['frames'] = []
    if selected_rows:
        selected_rows = grid_return["selected_rows"][0]["Alerts"]

        if plus:
            st.session_state['counter'] = st.session_state['counter']+1
        else:
            st.session_state['counter'] = selected_rows
        widget.slider("", min_value=0, max_value=int(
            cap.get(cv2.CAP_PROP_FRAME_COUNT)), value=st.session_state['counter'], on_change=display_value)
        container_2.empty()
        pause = container_2.button('▶')
        resume = True
        # get all the frames from video when the list is empty
    if not st.session_state['frames']:
        while True:
            successs, frames = cap.read()
            if successs:
                frames = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
                st.session_state['frames'].append(frames)
            else:
                break
        cap.release()
    # back to the first frame if the video is finished
    if st.session_state['counter'] == len(st.session_state['frames']):
        st.session_state['counter'] = 0
    stframe.image(st.session_state['frames']
                  [st.session_state['counter']], caption='', width=450)
    try:
        while st.session_state['counter'] < len(st.session_state['frames']):
            if not resume:

                stframe.image(
                    st.session_state['frames'][st.session_state['counter']], caption='', width=500)
                time.sleep(0.08)
                st.session_state['counter'] += 1
                # update slider value

                frame_num = widget.slider("", min_value=0, max_value=int(
                    cap.get(cv2.CAP_PROP_FRAME_COUNT)), value=st.session_state['counter'], on_change=display_value)

                if st.session_state.myslider > frame_num:
                    del st.session_state.myslider
                    #st.session_state.clear()
                    st.session_state['counter'] = frame_num
                    #st.session_state['counter'] = 0
                    resume = True
                    # st.experimental_rerun() #remove cache
                    break

                if pause:
                    resume = True
                    break
                if plus:
                    resume = True
                    break
                if minus:
                    st.session_state['counter'] -= 1
                    resume = True
                    break
                st.session_state['counter'] = frame_num
    except Exception as e:
        st.write('')
    if resume:
        container_2.empty()
        pause = container_2.button('▶')
        resume = False

# Run the Streamlit app


def main():

    alerts = {"Alerts": [43, 64]}
    data = [[[10, 100, 290, 200], 0.82, 0, "Class 0"],
            [[55, 22, 100, 120], 0.9, 1, "Class 1"]]
    video_path = "https://cvlogger.blob.core.windows.net/clientsample/1678352121.8713963_1678352127.8713963.webm?se=2023-05-22T15%3A52%3A24Z&sp=r&sv=2021-08-06&sr=b&sig=wUTiwlgqE9cWJrAWELquNAimEahYFcd0cdGhIiFZ4ko%3D"
    if video_path is not None:
        display_video(video_path, alerts, data)


if __name__ == "__main__":
    main()
