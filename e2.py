import streamlit as st

def calcularPromedios(data):
    lines = data.strip().split('\n')
    resultados = []
    
    for line in lines:
        parts = line.split(',')
        nombre = parts[0].strip()
        total_notas = 0
        num_notas = 0
        
        for part in parts[1:]:
            if ':' in part:
                _, nota = part.split(':')
                total_notas += float(nota)
                num_notas += 1
        
        promedio = total_notas / num_notas if num_notas > 0 else 0
        resultados.append(f"{nombre}, Promedio: {promedio:.2f}")
    
    return "\n".join(resultados)


st.title("Calcular Promedio de Estudiantes")

uploaded_file = st.file_uploader("Elige un archivo TXT", type="txt")

if uploaded_file is not None:
   
    data = uploaded_file.getvalue().decode("utf-8")
    
    promedios = calcularPromedios(data)
     
    st.text_area("Promedios calculados:", promedios, height=200)
    
    st.download_button(
        label="Descargar archivo de promedios",
        data=promedios,
        file_name="promedios.txt",
        mime="text/plain"
    )
