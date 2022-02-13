# IMPORTS
import streamlit as st
from PIL import Image
import os

### MAIN - HEADER ###
st.title("Zoom Background Downloader") # Title
st.markdown("Zoom meetings can be boring.  Let's spice them up a bit!") # Description


### SIDEBAR ###

# Sidebar Title
st.sidebar.title('Select A Background') # Sidebar title

# Use the os.listdir() function to view the folder 'images', add the file names to a list, and store the list in a variable called 'image_list'
image_list = os.listdir('images')

# Use the image names in image list to populate a streamlit dropdown menu and set it equal to a variable called 'image_name' 
image_name = st.sidebar.selectbox("Select a virtual background from the menu below,  then click the Download Background button.", image_list) 

# Download button.
with open(f"images/{image_name}", "rb") as file: #Use an f-string to define the path to the image, and the functin 'open' to open the image and store it as 'file'
     btn = st.sidebar.download_button( #Create an instance of Streamlit's 'download_button' function
             label="Download Background", # Text displayed on the button 
             data=file, # The contents of the file to be downloaded.  Out image was saved as 'file' above
             file_name=f"{image_name}", # An optional string to use as the name of the file to be downloaded 
             mime="image/jpg"  # The type of the data. If None, defaults to "text/plain" or "application/octet-stream" depending on the data type.
           )


### MAIN - VIEW IMAGE ###

# Use a f-string to define the path to the image, open it with the open function, and set it equal to the variable 'image'
image = Image.open(f"images/{image_name}")
# Use the streamlit image function to call on the image
st.image(image)
st.text('\n') # Spacer
st.text('\n') # Spacer
st.write("Curious how this was built?  Visit my [GitHub page](https://github.com/brianwetzel/image_downloader)")  # Text with a url embedded
