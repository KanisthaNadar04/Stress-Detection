"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Stress Level Detector")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
         Stress level detection is the process of using technology or methods to measure and analyze an individual's stress level. The goal of stress level detection is to provide an accurate assessment of a person's stress level, which can be used to guide interventions and treatments to help manage stress. An edge processor with a model analyzing the physiological changes that occur during sleep along with the sleeping habits is proposed. Based on these changes during sleep, stress prediction for the following day is proposed. A user interface is provided allowing the user to control the data accessibility and visibility. The importance of stress level detection lies in the fact that high levels of stress can have negative effects on physical and mental health, including cardiovascular disease, anxiety, and depression. By detecting stress levels, individuals can take steps to manage stress and improve their overall well-being.
        </p>
    """, unsafe_allow_html=True)

    st.markdown(""" <style>
     #MainMenu {visibility: hidden;}
     footer {visibility: hidden;}
     </style> """, unsafe_allow_html=True)