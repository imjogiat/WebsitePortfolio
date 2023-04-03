import streamlit as smlt
import os
import cv2

smlt.set_page_config(layout="wide")

#creates column objects
column1, column2 = smlt.columns(2)

#with first column, display my picture
with column1:
    
    smlt.image("photo.jpg")

#with second column, display information
with column2:
    smlt.title("Ismail Jogiat")
    my_descrip="""
    Hello, my name is Ismail Jogiat. I am currently learning Python Programming. 
    I am currently working as a Network Support Analyst for iTel Networks and I have previously worked as an 
    IT Coordinator for Practic Consulting. My goal is to create projects and display them below in order to showcase my progress and ability. I live in Calgary, Alberta, Canada and originally from Durban, South Africa.
    """
    smlt.info(my_descrip)

content="Here are the projects that I have worked on so far. Feel free to contact me if you have any questions! "

smlt.write(content)