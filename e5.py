import streamlit as st

def procesar_ventas(data):
    lines = data.strip().split('\n')
    total_ventas = 0
    num_ventas = 0
    max_venta = None
    min_venta = None
    
    for line in lines:
        fecha, venta = line.split()
        venta = float(venta)
        total_ventas += venta
        num_ventas += 1
        
        if max_venta is None or venta > max_venta[1]:
            max_venta = (fecha, venta)
        
        if min_venta is None or venta < min_venta[1]:
            min_venta = (fecha, venta)
    
    promedio_ventas = total_ventas / num_ventas if num_ventas > 0 else 0
    
    resultados = {
        "total_ventas": total_ventas,
        "promedio_ventas": promedio_ventas,
        "max_venta_fecha": max_venta[0],
        "max_venta_valor": max_venta[1],
        "min_venta_fecha": min_venta[0],
        "min_venta_valor": min_venta[1]
    }
    
    return resultados

st.title("Procesamiento de Ventas")

uploaded_file = st.file_uploader("Elige un archivo TXT", type="txt")

if uploaded_file is not None:

    data = uploaded_file.getvalue().decode("utf-8")
    
    resultados = procesar_ventas(data)
    
    st.write(f"**Venta total:** {resultados['total_ventas']}")
    st.write(f"**Promedio de ventas:** {resultados['promedio_ventas']:.2f}")
    st.write(f"**Día de mayor venta:** {resultados['max_venta_fecha']} con {resultados['max_venta_valor']} ventas")
    st.write(f"**Día de menor venta:** {resultados['min_venta_fecha']} con {resultados['min_venta_valor']} ventas")
    
    output_data = (
        f"Venta total: {resultados['total_ventas']}\n"
        f"Promedio de ventas: {resultados['promedio_ventas']:.2f}\n"
        f"Día de mayor venta: {resultados['max_venta_fecha']} {resultados['max_venta_valor']}\n"
        f"Día de menor venta: {resultados['min_venta_fecha']} {resultados['min_venta_valor']}\n"
    )
    
    st.download_button(
        label="Descargar archivo de salida",
        data=output_data,
        file_name="5salida.txt",
        mime="text/plain"
    )
