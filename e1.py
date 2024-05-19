import streamlit as st

def mostrarCorreo(archivo, archivoSalida):
    with open(archivo, 'r') as file:
        lines = file.readlines()

    correos_mayores = []
    for line in lines:
        nombre, edad, correo = line.split(',')
        if int(edad.strip()) > 18:
            correos_mayores.append(correo.strip())

    with open(archivoSalida, 'w') as file:
        for correo in correos_mayores:
            file.write(correo + '\n')

    return correos_mayores


st.title("Correos de Personas Mayores de Edad")


uploaded_file = st.file_uploader("Cargar archivo de entrada", type=["txt"])

if uploaded_file is not None:
    correos_mayores = mostrarCorreo(uploaded_file.name, "correos_mayores.txt")

    
    st.subheader("Correos de Personas Mayores de 18 Años:")
    for correo in correos_mayores:
        st.write(correo)

   
    if st.button("Descargar correos filtrados"):
        with open("correos_mayores.txt", 'r') as file:
            data = file.read()
        st.download_button(
            label="Haz clic aquí para descargar",
            data=data,
            file_name="correos_mayores.txt",
            mime="text/plain"
        )
