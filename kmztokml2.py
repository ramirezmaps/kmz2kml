import streamlit as st
from zipfile import ZipFile
import simplekml
from io import BytesIO

def kmz_to_kml(kmz_content):
    with ZipFile(BytesIO(kmz_content), 'r') as kmz:
        kml_file = [f for f in kmz.namelist() if f.endswith('.kml')][0]
        kml_content = kmz.read(kml_file)
        return kml_content

def main():
    st.title("KMZ 2 KML ")

    uploaded_file = st.file_uploader("Cargar archivo KMZ", type=["kmz"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        if st.button("Convertir"):
            kmz_content = uploaded_file.read()
            kml_content = kmz_to_kml(kmz_content)

            # Download the converted KML file
            st.download_button(
                label="Descargar KML",
                data=kml_content,
                file_name="converted_file.kml",
                key="kml_download_button"
            )

    st.text("")

if __name__ == "__main__":
    main()
