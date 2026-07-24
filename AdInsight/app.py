import streamlit as st

st.set_page_config(
    page_title="AdInsight",
    page_icon="📢",
    layout="wide"
)

st.title("📢 AdInsight")
st.subheader("NLP-Based Multimedia Advertisement Content Analysis and Persuasion Detection System")

st.divider()

st.write("### Upload Advertisement")

input_type = st.selectbox(
    "Select Advertisement Type",
    [
        "Text",
        "PDF",
        "DOCX",
        "TXT",
        "Image",
        "Video"
    ]
)

uploaded_file = st.file_uploader(
    "Choose a file",
    type=[
        "pdf",
        "docx",
        "txt",
        "jpg",
        "jpeg",
        "png",
        "mp4",
        "avi",
        "mov"
    ]
)

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write("Filename:", uploaded_file.name)

st.divider()
st.info("Analysis results will appear here.")