import streamlit as st

def temperaturas(data):
    lines = data.strip().split('\n')
    max_temp = None
    min_temp = None
    
    for line in lines:
        fecha, temp = line.split()
        temp = float(temp)
        
        if max_temp is None or temp > max_temp[1]:
            max_temp = (fecha, temp)
        
        if min_temp is None or temp < min_temp[1]:
            min_temp = (fecha, temp)
    
    return max_temp, min_temp


st.title("Procesamiento de Temperaturas Extremas")

uploaded_file = st.file_uploader("Elige un archivo TXT", type="txt")

if uploaded_file is not None:
   
    data = uploaded_file.getvalue().decode("utf-8")
    
    max_temp, min_temp = temperaturas(data)
    
    st.write(f"**Día de temperatura máxima:** {max_temp[0]} con {max_temp[1]}°C")
    st.write(f"**Día de temperatura mínima:** {min_temp[0]} con {min_temp[1]}°C")

    output_data = f"Día de temperatura máxima: {max_temp[0]} {max_temp[1]}°C\n"
    output_data += f"Día de temperatura mínima: {min_temp[0]} {min_temp[1]}°C\n"
    
    st.download_button(
        label="Descargar archivo de salida",
        data=output_data,
        file_name="4salida.txt",
        mime="text/plain"
    )
