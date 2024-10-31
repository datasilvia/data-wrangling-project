import streamlit as st
import pandas as pd
import os

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Título de la aplicación
st.title("Recomendador de Tarifas de Luz y Placas Solares")

# Añadir una imagen en la página principal
st.image(os.path.join(current_dir, "image.jpg"), use_column_width=True)

# Añadir una imagen en la parte superior del menú de navegación
st.sidebar.image(os.path.join(current_dir, "octocat.jpg"), use_column_width=True)

# Menú de navegación
st.sidebar.header("Menú de Navegación")
seccion = st.sidebar.radio("Ir a", ["Introducción", "Objetivos", "Metodología", "Visualizaciones", "Recomendador"])

# Sección de Introducción
if seccion == "Introducción":
    st.header("Introducción")
    st.write("""
    🌞 **Bienvenido al Recomendador de Tarifas de Luz y Placas Solares** 🌞

    En este proyecto, hemos desarrollado una aplicación web innovadora que recomienda tarifas de luz y placas solares basadas en los datos ingresados por el usuario. La aplicación utiliza datos actualizados de tarifas de luz y eficiencia de placas solares para proporcionar recomendaciones personalizadas que pueden ayudar a los usuarios a ahorrar en sus facturas de electricidad y a aprovechar la energía solar de manera eficiente. 💡🔋

    **¿Por qué es importante el ahorro energético?** 🌍

    El ahorro energético no solo tiene beneficios económicos, sino que también contribuye significativamente a la sostenibilidad del medio ambiente. Al reducir el consumo de energía y utilizar fuentes de energía renovable como la solar, podemos disminuir nuestra huella de carbono y ayudar a combatir el cambio climático. 🌱🌞

    **Beneficios del ahorro energético:**
    - **Ahorro económico:** Reducir el consumo de energía puede resultar en ahorros significativos en las facturas de electricidad. Esto libera recursos financieros que pueden ser utilizados para otras necesidades. 💰
    - **Sostenibilidad ambiental:** Utilizar energía renovable como la solar ayuda a reducir la dependencia de combustibles fósiles y disminuye las emisiones de gases de efecto invernadero. 🌍
    - **Independencia energética:** La instalación de placas solares permite a los usuarios generar su propia energía, reduciendo la dependencia de las compañías eléctricas y aumentando la resiliencia ante posibles fluctuaciones en los precios de la energía. ☀️🔋
    - **Innovación y tecnología:** Este proyecto fomenta el uso de tecnologías avanzadas como el web scraping, el análisis de datos y la visualización interactiva para proporcionar recomendaciones precisas y útiles. 🚀💡

    **¿Cómo funciona nuestra aplicación?** 🛠️

    Esta aplicación está diseñada para ser fácil de usar y accesible para todos. Simplemente ingrese sus datos en el formulario y obtenga recomendaciones personalizadas en cuestión de segundos. 🚀📊

    **Pasos para utilizar la aplicación:**
    1. **Ingrese sus datos:** Proporcione información sobre su consumo mensual de electricidad, la potencia contratada, las horas de sol disponibles y la superficie disponible para la instalación de placas solares.
    2. **Obtenga recomendaciones:** La aplicación analizará los datos ingresados y proporcionará recomendaciones personalizadas de tarifas de luz y placas solares.
    3. **Tome decisiones informadas:** Utilice las recomendaciones proporcionadas para elegir la tarifa de luz más adecuada y optimizar el uso de energía solar en su hogar.

    **Compromiso con la sostenibilidad:**

    Al utilizar esta aplicación, no solo está tomando decisiones informadas para ahorrar en sus facturas de electricidad, sino que también está contribuyendo a un futuro más sostenible. 🌱🔋

    ¡Gracias por utilizar nuestra aplicación y por su compromiso con el ahorro energético y la sostenibilidad ambiental! 🌍💡
    """)

# Sección de Objetivos
elif seccion == "Objetivos":
    st.header("Objetivos")
    st.write("""
    🎯 **Objetivos del Proyecto** 🎯

    Los objetivos principales de este proyecto son:

    1. **Proporcionar recomendaciones personalizadas de tarifas de luz**:
       - Analizar las tarifas de luz disponibles y recomendar la mejor opción basada en el consumo mensual y la potencia contratada del usuario. 💡
       - Ayudar a los usuarios a reducir sus facturas de electricidad eligiendo la tarifa más económica. 💰
       - Facilitar el acceso a información clara y precisa sobre las diferentes tarifas de luz disponibles en el mercado. 📊

    2. **Proporcionar recomendaciones personalizadas de placas solares**:
       - Evaluar la eficiencia de diferentes placas solares y recomendar la mejor opción basada en las horas de sol disponibles y la superficie disponible para la instalación. ☀️
       - Promover el uso de energía solar como una fuente de energía renovable y sostenible. 🌱
       - Ayudar a los usuarios a entender los beneficios económicos y ambientales de la instalación de placas solares. 🌍

    3. **Visualizar datos relevantes sobre tarifas de luz y energía solar**:
       - Crear gráficos y visualizaciones que faciliten la comprensión de los datos y las recomendaciones. 📊
       - Mostrar comparativas de tarifas y eficiencia de placas solares para ayudar a los usuarios a tomar decisiones informadas. 📈
       - Proporcionar herramientas interactivas que permitan a los usuarios explorar diferentes escenarios y opciones. 🛠️

    **Beneficios del Ahorro Energético y la Energía Sostenible**:

    🌟 **Ahorro Económico**: Al elegir la tarifa de luz más adecuada y optimizar el uso de energía solar, los usuarios pueden reducir significativamente sus facturas de electricidad. Esto no solo representa un ahorro económico, sino que también libera recursos financieros para otras necesidades. 💰

    🌟 **Sostenibilidad Ambiental**: La adopción de prácticas de ahorro energético y el uso de energía solar contribuyen a la reducción de la huella de carbono. Al disminuir el consumo de energía proveniente de fuentes no renovables, ayudamos a proteger el medio ambiente y a combatir el cambio climático. 🌍🌱

    🌟 **Independencia Energética**: La instalación de placas solares permite a los usuarios generar su propia energía, reduciendo la dependencia de las compañías eléctricas y aumentando la resiliencia ante posibles fluctuaciones en los precios de la energía. ☀️🔋

    🌟 **Innovación y Tecnología**: Este proyecto fomenta el uso de tecnologías avanzadas como el web scraping, el análisis de datos y la visualización interactiva para proporcionar recomendaciones precisas y útiles. Esto no solo mejora la experiencia del usuario, sino que también impulsa la innovación en el sector energético. 🚀💡

    Al alcanzar estos objetivos, esperamos contribuir al ahorro energético y a la adopción de prácticas sostenibles en el consumo de electricidad. 🌱🔋
    """)

# Sección de Metodología
elif seccion == "Metodología":
    st.header("Metodología")
    st.write("""
    🛠️ **Metodología del Proyecto** 🛠️

    La metodología utilizada en este proyecto incluye los siguientes pasos:

    1. **Recopilación de datos**:
       - Recopilamos datos de tarifas de luz de diferentes proveedores y datos de eficiencia de placas solares. 🌐
       - Utilizamos técnicas de web scraping para obtener datos actualizados de las páginas web de los proveedores de energía. 🕸️🔍
       - Los datos incluyen información sobre precios de energía, precios de potencia, eficiencia de placas solares, y más. 📊

    2. **Análisis de datos**:
       - Analizamos los datos recopilados para identificar las mejores opciones de tarifas de luz y placas solares. 📈
       - Utilizamos técnicas de análisis de datos para calcular los costos estimados y la energía generada por las placas solares. 💡

    3. **Desarrollo de la aplicación web**:
       - Desarrollamos una aplicación web utilizando Streamlit para proporcionar una interfaz fácil de usar. 💻
       - La aplicación permite a los usuarios ingresar sus datos y obtener recomendaciones personalizadas en tiempo real. ⏱️

    4. **Visualización de datos**:
       - Creamos gráficos y visualizaciones utilizando Seaborn y Matplotlib para mostrar comparativas de tarifas y eficiencia de placas solares. 📊
       - Las visualizaciones ayudan a los usuarios a comprender mejor los datos y las recomendaciones proporcionadas. 👁️

    5. **Validación y pruebas**:
       - Probamos la aplicación con diferentes conjuntos de datos para asegurarnos de que las recomendaciones sean precisas y útiles. ✅
       - Realizamos ajustes y mejoras basadas en los comentarios de los usuarios y los resultados de las pruebas. 🔧

    Al seguir esta metodología, hemos creado una herramienta poderosa que puede ayudar a los usuarios a tomar decisiones informadas sobre sus tarifas de luz y el uso de energía solar. 💡🔧
    """)

# Sección de Visualizaciones
elif seccion == "Visualizaciones":
    st.header("Visualizaciones")
    st.write("Seleccione el gráfico que desea ver:")

    # Menú de selección de gráficos
    grafico_seleccionado = st.selectbox("Seleccione un gráfico", [
        "Punta por Empresa", 
        "Punta por Tarifa", 
        "Llano por Empresa", 
        "Llano por Tarifa", 
        "Valle por Empresa", 
        "Valle por Tarifa", 
        "Dashboard Tarifas", 
        "Potencia por Empresas", 
        "Top Sol Ciudades", 
        "Bottom Sol Ciudades"
    ])

    # Mostrar el gráfico seleccionado y su explicación
    if grafico_seleccionado == "Punta por Empresa":
        st.image(os.path.join(current_dir, "punta_por_empresa.png"), caption="Punta por Empresa", use_column_width=True)
        st.write("Este gráfico muestra la tarifa de punta (P1) por empresa. La tarifa de punta se aplica durante las horas de mayor demanda de energía, generalmente durante el día. Este gráfico permite comparar las tarifas de punta ofrecidas por diferentes empresas.")

    elif grafico_seleccionado == "Punta por Tarifa":
        st.image(os.path.join(current_dir, "punta_por_tarifa.png"), caption="Punta por Tarifa", use_column_width=True)
        st.write("Este gráfico muestra la tarifa de punta (P1) por tarifa. La tarifa de punta se aplica durante las horas de mayor demanda de energía. Este gráfico permite comparar las diferentes tarifas de punta disponibles en el mercado.")

    elif grafico_seleccionado == "Llano por Empresa":
        st.image(os.path.join(current_dir, "llano_por_empresa.png"), caption="Llano por Empresa", use_column_width=True)
        st.write("Este gráfico muestra la tarifa de llano (P2) por empresa. La tarifa de llano se aplica durante las horas de demanda moderada de energía. Este gráfico permite comparar las tarifas de llano ofrecidas por diferentes empresas.")

    elif grafico_seleccionado == "Llano por Tarifa":
        st.image(os.path.join(current_dir, "llano_por_tarifa.png"), caption="Llano por Tarifa", use_column_width=True)
        st.write("Este gráfico muestra la tarifa de llano (P2) por tarifa. La tarifa de llano se aplica durante las horas de demanda moderada de energía. Este gráfico permite comparar las diferentes tarifas de llano disponibles en el mercado.")

    elif grafico_seleccionado == "Valle por Empresa":
        st.image(os.path.join(current_dir, "valle_por_empresa.png"), caption="Valle por Empresa", use_column_width=True)
        st.write("Este gráfico muestra la tarifa de valle (P3) por empresa. La tarifa de valle se aplica durante las horas de menor demanda de energía, generalmente durante la noche. Este gráfico permite comparar las tarifas de valle ofrecidas por diferentes empresas.")

    elif grafico_seleccionado == "Valle por Tarifa":
        st.image(os.path.join(current_dir, "valle_por_tarifa.png"), caption="Valle por Tarifa", use_column_width=True)
        st.write("Este gráfico muestra la tarifa de valle (P3) por tarifa. La tarifa de valle se aplica durante las horas de menor demanda de energía. Este gráfico permite comparar las diferentes tarifas de valle disponibles en el mercado.")

    elif grafico_seleccionado == "Dashboard Tarifas":
        st.image(os.path.join(current_dir, "dashboard tarifas.png"), caption="Dashboard Tarifas", use_column_width=True)
        st.write("Este dashboard muestra una visión general de las tarifas de luz, incluyendo las tarifas de punta, llano y valle por diferentes empresas y tarifas. Permite una comparación rápida y visual de las diferentes opciones disponibles en el mercado.")

    elif grafico_seleccionado == "Potencia por Empresas":
        st.image(os.path.join(current_dir, "potencia_por_empresas.png"), caption="Potencia por Empresas", use_column_width=True)
        st.write("Este gráfico muestra la potencia contratada por diferentes empresas. La potencia contratada es la cantidad de energía que una empresa puede suministrar a sus clientes. Este gráfico permite comparar la capacidad de suministro de energía de diferentes empresas.")

    elif grafico_seleccionado == "Top Sol Ciudades":
        st.image(os.path.join(current_dir, "top_sol_ciudades.png"), caption="Top Sol Ciudades", use_column_width=True)
        st.write("Este gráfico muestra las ciudades con más horas de sol al año. Las horas de sol son un factor importante a considerar al instalar placas solares, ya que determinan la cantidad de energía que se puede generar. Este gráfico permite identificar las mejores ciudades para la instalación de placas solares.")

    elif grafico_seleccionado == "Bottom Sol Ciudades":
        st.image(os.path.join(current_dir, "bottom_sol_ciudades.png"), caption="Bottom Sol Ciudades", use_column_width=True)
        st.write("Este gráfico muestra las ciudades con menos horas de sol al año. Las horas de sol son un factor importante a considerar al instalar placas solares. Este gráfico permite identificar las ciudades menos favorables para la instalación de placas solares.")

# Sección de Recomendador
elif seccion == "Recomendador":
    st.header("Recomendador")

    st.write("""
    Ingrese sus datos a continuación para obtener recomendaciones personalizadas de tarifas de luz y placas solares.
    """)

    # Formulario para ingresar datos del usuario
    consumo_mensual = st.number_input("Consumo mensual (kWh)", min_value=0)
    potencia_contratada = st.number_input("Potencia contratada (kW)", min_value=0.0, step=0.1)
    horas_sol = st.number_input("Horas de sol al día", min_value=0.0, step=0.1)
    superficie_placas = st.number_input("Superficie disponible para placas (m²)", min_value=0.0, step=0.1)

    # Datos de tarifas de ejemplo
    tarifas = {
        "Tarifa 1": {"precio_energia": 0.15, "precio_potencia": 0.10},
        "Tarifa 2": {"precio_energia": 0.20, "precio_potencia": 0.08},
        "Tarifa 3": {"precio_energia": 0.18, "precio_potencia": 0.09},
    }

    # Datos de placas solares de ejemplo
    placas = {
        "Placa 1": {"eficiencia": 0.18, "precio": 200},
        "Placa 2": {"eficiencia": 0.20, "precio": 250},
        "Placa 3": {"eficiencia": 0.22, "precio": 300},
    }

    # Función para recomendar tarifa
    def recomendar_tarifa(consumo, potencia):
        mejor_tarifa = None
        menor_costo = float('inf')
        for tarifa, datos in tarifas.items():
            costo = consumo * datos["precio_energia"] + potencia * datos["precio_potencia"]
            if costo < menor_costo:
                menor_costo = costo
                mejor_tarifa = tarifa
        return mejor_tarifa, menor_costo

    # Función para recomendar placas solares
    def recomendar_placas(horas_sol, superficie):
        mejor_placa = None
        mayor_energia = 0
        for placa, datos in placas.items():
            energia_generada = horas_sol * superficie * datos["eficiencia"]
            if energia_generada > mayor_energia:
                mayor_energia = energia_generada
                mejor_placa = placa
        return mejor_placa, mayor_energia

    # Mostrar recomendaciones
    if st.button("Recomendar"):
        tarifa, costo = recomendar_tarifa(consumo_mensual, potencia_contratada)
        placa, energia = recomendar_placas(horas_sol, superficie_placas)
        
        st.subheader("Recomendación de Tarifa de Luz")
        st.write(f"La mejor tarifa para usted es: **{tarifa}** con un costo mensual estimado de **{costo:.2f} €**.")
        
        st.subheader("Recomendación de Placas Solares")
        st.write(f"La mejor placa solar para usted es: **{placa}** que generará aproximadamente **{energia:.2f} kWh** al día.")
