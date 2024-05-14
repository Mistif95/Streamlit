import streamlit as st
from PIL import Image

# Title of the dashboard
st.title('Simple Image Display in Streamlit')

# Load an image using PIL
image = Image.open('path_to_your_image.jpg')

# Display the image
st.image(image, caption='This is a sample image.', use_column_width=True)
