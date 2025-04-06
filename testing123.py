import streamlit as st
import os
import uuid

st.title("Photo upload")

# Upload image
img = st.file_uploader("Image upload", type=["jpg", "jpeg", "png"])

if img is not None:
    # Generate a unique filename
    unique_filename = f"{uuid.uuid4()}.png"  # or keep img.name.split('.')[-1] to retain original extension

    # Define the path to save
    save_path = os.path.join("uploaded_images", unique_filename)
    os.makedirs("uploaded_images", exist_ok=True)  # Ensure directory exists

    # Save the file
    with open(save_path, "wb") as f:
        f.write(img.getbuffer())

    st.success(f"Image saved as {unique_filename}")
    st.image(save_path)


