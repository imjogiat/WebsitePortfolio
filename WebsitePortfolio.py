import streamlit as smlt
import pandas


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

#writes the content above under my background information
smlt.write(content)

#import that data file into a table/data frame object through pandas function
project_table=pandas.read_csv("appsdata.csv",sep=",")

# column3, column4= smlt.columns(2)

#below code defines the width of  the actual columns and sets the width of space column to half
column3, empty_column, column4= smlt.columns([1.5, 0.5, 1.5])

#in each column, iterate through the rows of the data frame and display the title
with column3:
    #Data frame type is already enumerated
    #for loop to iterate through the rows of the datafram/table (have to use iterrows())
    #print the element in the row with the key value "title"
    for index,row in project_table[:10].iterrows():
        smlt.header(row["title"])
        smlt.write(row["description"])
        #image function in streamlit takes the file location argument and returns an image object that is displayed in webpage
        smlt.image("AppImages/"+row["image"])
        #the below format of string is the convention for URL links. What follows the square brackets in parentheses is what is linked in the hypertext
        smlt.write("[Source Code]("+row["url"]+")")

with column4:
    for index,row in project_table[10:].iterrows():
        smlt.header(row["title"])
        smlt.write(row["description"])
        smlt.image("AppImages/"+row["image"])
        smlt.write("[Source Code]("+row["url"]+")")