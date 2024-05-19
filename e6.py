import streamlit as st
from collections import defaultdict

def horasXempleado(data):
    horas_por_empleado = defaultdict(int)
    for linea in data.splitlines():
        nombre, horas = linea.split(',')
        nombre = nombre.strip()
        horas = int(horas.strip())
        horas_por_empleado[nombre] += horas
    
    resultado = [f"{nombre}, Horas Totales: {horas}" for nombre, horas in horas_por_empleado.items()]
    return "\n".join(resultado)

st.title("Registro de Horas de Trabajo")

uploaded_file = st.file_uploader("Cargar archivo de registro de horas (formato .txt)", type="txt")

if uploaded_file is not None:
  
    data = uploaded_file.getvalue().decode("utf-8")
    
    resultado = horasXempleado(data)

    st.text_area("Informe de horas totales trabajadas por empleado:", resultado, height=200)
    
    output_data = resultado
    
    st.download_button(
        label="Descargar informe de horas",
        data=output_data,
        file_name="informe_horas.txt",
        mime="text/plain"
    )
