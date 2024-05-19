import streamlit as st
import pandas as pd

def convertirdolares(soles):
    conversion = 1 / 3.85
    return soles * conversion


st.title("Conversión de Precios de Soles a Dólares")


uploaded_file = st.file_uploader("Elige un archivo ", type="txt")

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file, header=None, names=["Producto", "Precio en Soles"])

    
    df["Precio en Dólares"] = df["Precio en Soles"].apply(convertirdolares)

    
    st.write(df)

   
    output_csv = df.to_csv(index=False)
    st.download_button(
        label="Descargar archivo convertido",
        data=output_csv,
        file_name="3salida.txt",
        mime="text/csv"
    )
