import streamlit as st

def mostrarCorreo(data):
    lines = data.splitlines()
    correos_mayores = []
    for line in lines:
        nombre, edad, correo = line.split(',')
        if int(edad.strip()) > 18:
            correos_mayores.append(correo.strip())

    archivoSalida = "\n".join(correos_mayores)
    return correos_mayores, archivoSalida

st.title("Correos de Personas Mayores de Edad")

uploaded_file = st.file_uploader("Cargar archivo de entrada", type=["txt"])

if uploaded_file is not None:
    
    data = uploaded_file.getvalue().decode("utf-8")

    correos_mayores, archivoSalida = mostrarCorreo(data)

    st.subheader("Correos de Personas Mayores de 18 Años:")
    for correo in correos_mayores:
        st.write(correo)
        
    st.download_button(
        label="Haz clic aquí para descargar",
        data=archivoSalida,
        file_name="correos_mayores.txt",
        mime="text/plain"
    )
