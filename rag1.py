import streamlit as st
import PyPDF2
import os
import base64
from io import BytesIO
import pandas as pd  # Add this line to import pandas

# Initialize session state to store PDF text
if 'pdf_text' not in st.session_state:
    st.session_state.pdf_text = ""

def save_uploadedfile(uploadedfile):
    with open(os.path.join("tempDir", uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = [page.extract_text() for page in reader.pages if page.extract_text() is not None]
    return "\n".join(text)

st.title('RAG Project Demo')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    st.session_state.pdf_text = extract_text_from_pdf(uploaded_file)
    st.text_area("Extracted Text", st.session_state.pdf_text, height=300)

query = st.text_input("Enter your query here")

if st.button('Retrieve Information'):
    if query and st.session_state.pdf_text:
        # Placeholder for retrieval logic
        st.write(f"Searching for: {query} in uploaded PDF...")
        # Imagine this is where you would have your retrieval logic
        st.write("This is a placeholder response based on the query.")
    else:
        st.warning("Please upload a PDF and enter a query.")

# Optional: Displaying a download link for debug purposes
def get_table_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="extracted_text.csv">Download csv file</a>'
    return href

if 'pdf_text' in st.session_state and st.session_state.pdf_text:
    st.markdown(get_table_download_link(pd.DataFrame([st.session_state.pdf_text], columns=["Extracted Text"])), unsafe_allow_html=True)

