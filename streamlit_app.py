import streamlit as st
from PIL import Image

# Judul Aplikasi
st.title("Image Scaling App")

# Mengunggah file gambar
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Input untuk faktor scaling
scale_factor = st.slider("Scaling Factor", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

# Proses jika ada file yang diunggah
if uploaded_file is not None:
    # Membaca file gambar
    img = Image.open(uploaded_file)
    st.image(img, caption="Original Image", use_column_width=True)

    # Mendapatkan ukuran asli
    original_width, original_height = img.size

    # Menghitung ukuran baru
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    # Mengubah ukuran gambar
    scaled_img = img.resize((new_width, new_height), Image.ANTIALIAS)

    # Menampilkan gambar hasil scaling
    st.image(scaled_img, caption=f"Scaled Image (Factor: {scale_factor})", use_column_width=True)

    # Tombol untuk mengunduh gambar hasil scaling
    scaled_img_path = "scaled_image.png"
    scaled_img.save(scaled_img_path)

    with open(scaled_img_path, "rb") as file:
        btn = st.download_button(
            label="Download Scaled Image",
            data=file,
            file_name="scaled_image.png",
            mime="image/png"
        )
