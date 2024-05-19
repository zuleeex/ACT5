import streamlit as st
import pandas as pd

def errores(data):
    
    df = pd.DataFrame(data, columns=["Error"])
    
    conteo_errores = df["Error"].value_counts().reset_index()
    conteo_errores.columns = ["Error", "Frecuencia"]
    
    return conteo_errores

st.title("Resumen de Errores")

uploaded_file = st.file_uploader("Cargar archivo de errores", type="log")

if uploaded_file is not None:
   
    data = uploaded_file.readlines()
    data = [x.decode("utf-8").strip() for x in data]
    
    df_resumen = errores(data)
    
    st.write(df_resumen)
