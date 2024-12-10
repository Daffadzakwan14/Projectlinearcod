import streamlit as st
from PIL import Image

# Judul Aplikasi
st.title("Image Scaling App")

# Instruksi pengguna
st.write("Unggah gambar, pilih faktor scaling, dan unduh hasilnya.")

# Mengunggah gambar
uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

# Slider untuk memilih faktor scaling
scale_factor = st.slider(
    "Select Scaling Factor",
    min_value=0.1, 
    max_value=5.0, 
    value=1.0, 
    step=0.1,
    help="Pilih faktor untuk memperbesar atau memperkecil gambar (1.0 = ukuran asli)."
)

if uploaded_file is not None:
    # Membaca gambar yang diunggah
    img = Image.open(uploaded_file)
    
    # Menampilkan gambar asli
    st.subheader("Original Image")
    st.image(img, caption="Original Image", use_column_width=True)
    
    # Mendapatkan ukuran asli
    original_width, original_height = img.size
    
    # Menghitung ukuran baru berdasarkan faktor scaling
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    
    # Melakukan scaling pada gambar
    scaled_img = img.resize((new_width, new_height), Image.NTIALIAS)
    
    # Menampilkan gambar hasil scaling
    st.subheader("Scaled Image")
    st.image(scaled_img, caption=f"Scaled Image (Factor: {scale_factor})", use_column_width=True)
    
    # Menyediakan gambar untuk diunduh
    st.subheader("Download Scaled Image")
    scaled_img_path = "scaled_image.png"
    scaled_img.save(scaled_img_path)
    
    with open(scaled_img_path, "rb") as file:
        st.download_button(
            label="Download Scaled Image",
            data=file,
            file_name="scaled_image.png",
            mime="image/png"
        )
