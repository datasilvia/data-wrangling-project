import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import requests
import calendar

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
    st.header("🛠️ Metodología del Proyecto 🛠️")
    st.write("""
    En este proyecto, hemos seguido una metodología estructurada para garantizar la precisión y la utilidad de nuestras recomendaciones. A continuación, se detallan los pasos clave que hemos seguido:

    1. **Recopilación de Datos** 🌐:
       - Recopilamos datos de tarifas de luz de diferentes proveedores y datos de eficiencia de placas solares. 📊
       - Utilizamos técnicas de web scraping para obtener datos actualizados de las páginas web de los proveedores de energía. 🕸️🔍
       - Los datos incluyen información sobre precios de energía, precios de potencia, eficiencia de placas solares, y más. 💡

    2. **Análisis de Datos** 📈:
       - Analizamos los datos recopilados para identificar las mejores opciones de tarifas de luz y placas solares. 🔍
       - Utilizamos técnicas de análisis de datos para calcular los costos estimados y la energía generada por las placas solares. 💡

    3. **Desarrollo de la Aplicación Web** 💻:
       - Desarrollamos una aplicación web utilizando Streamlit para proporcionar una interfaz fácil de usar. 🚀
       - La aplicación permite a los usuarios ingresar sus datos y obtener recomendaciones personalizadas en tiempo real. ⏱️

    4. **Visualización de Datos** 👁️:
       - Creamos gráficos y visualizaciones utilizando Seaborn y Matplotlib para mostrar comparativas de tarifas y eficiencia de placas solares. 📊
       - Las visualizaciones ayudan a los usuarios a comprender mejor los datos y las recomendaciones proporcionadas. 📈

    5. **Validación y Pruebas** ✅:
       - Probamos la aplicación con diferentes conjuntos de datos para asegurarnos de que las recomendaciones sean precisas y útiles. 🔧
       - Realizamos ajustes y mejoras basadas en los comentarios de los usuarios y los resultados de las pruebas. 🛠️

    Al seguir esta metodología, hemos creado una herramienta poderosa que puede ayudar a los usuarios a tomar decisiones informadas sobre sus tarifas de luz y el uso de energía solar. 🌞🔋
    """)

# Sección de Visualizaciones
elif seccion == "Visualizaciones":
    st.header("📊 Visualizaciones 📊")
    st.write("""
    Bienvenido a la sección de visualizaciones. Aquí podrás explorar diferentes gráficos que te ayudarán a entender mejor los datos relacionados con las tarifas de luz y la energía solar. 📈📉

    Selecciona el gráfico que deseas ver a continuación y obtén una visión detallada de la información. ¡Esperamos que estas visualizaciones te sean útiles para tomar decisiones informadas! 💡🔍
    """)

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
    🌞 **¡Bienvenido al Recomendador de Tarifas de Luz y Placas Solares!** 🌞

    Por favor, complete el siguiente formulario para recibir recomendaciones personalizadas que le ayudarán a ahorrar en su factura de electricidad y a aprovechar la energía solar de manera eficiente. 💡🔋

    **¡Hagamos un mundo más sostenible juntos!** 🌍✨
    """)

    # Función para cargar tarifas desde un archivo CSV

    import csv
    def cargar_tarifas():
        tarifas = []
        with open(os.path.join(current_dir, 'tarifas_nosolar.csv'), 'r') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            for fila in lector:
                tarifa = {
                    "compañia": fila['Empresa'],
                    "nombre": fila['Tarifa'],
                    "punta": float(fila['Punta']),
                    "llano": float(fila['Llano']),
                    "valle": float(fila['Valle']),
                    "P1": float(fila['P1']) if 'P1' in fila else 0,
                    "P3": float(fila['P3']) if 'P3' in fila else 0,
                    "batería": 0
                }
                tarifas.append(tarifa)
        return tarifas

    def obtener_incremento_por_habitante(num_personas):
        if num_personas == 1:
            return 1.0
        elif num_personas == 2:
            return 1.25
        elif num_personas == 3:
            return 1.45
        elif num_personas == 4:
            return 1.60
        else:
            return 1.60 + 0.1 * (num_personas - 4)

    # Función para ajustar el consumo en función del número de habitantes
    def ajustar_consumo_por_habitantes(consumo, num_personas):
        incremento = obtener_incremento_por_habitante(num_personas)
        return consumo * incremento

    # Diccionario de meses y días
    dias_por_mes = {
        "enero": 31, "febrero": 28, "marzo": 31, "abril": 30,
        "mayo": 31, "junio": 30, "julio": 31, "agosto": 31,
        "septiembre": 30, "octubre": 31, "noviembre": 30, "diciembre": 31
    }

    # Comparativa de tarifas
    def calcular_mejor_tarifa(datos_consumo, tarifas):
        mes = datos_consumo["mes"]
        if mes is None:
            st.error("El mes no ha sido proporcionado correctamente.")
            return
        dias = dias_por_mes.get(mes.lower(), 30)  # Usar 30 días si el mes es inválido o no está en el diccionario
        excedentes = 0
        potencia = datos_consumo['potencia']
        iva = 1.21
        bono_social = 0.006282
        impuesto = 3.8 / 100
        equipos = 0.82

        comparativa = []
        for empresa in tarifas:
            consumo_total = (empresa["punta"] * datos_consumo["punta"] +
                             empresa["llano"] * datos_consumo["llano"] +
                             empresa["valle"] * datos_consumo["valle"])
            potencia_total = potencia * dias * (empresa["P1"] + empresa["P3"])
            
            precionormal = ((potencia_total + bono_social * dias + consumo_total) * (1 + impuesto) +
                            equipos) * iva 
            
            calculado = {
                "Empresa": empresa["compañia"],
                "Tarifa": empresa["nombre"],
                "Precio": precionormal
            }
            comparativa.append(calculado)

        comparativa.sort(key=lambda x: x["Precio"])
        mejor_tarifa = comparativa[0]

        st.write("\nComparativa de tarifas:")
        for tarifa in comparativa:
            st.write(f"{tarifa['Empresa']} - {tarifa['Tarifa']}: {tarifa['Precio']:.2f} €")

        st.write(f"\nLa tarifa más económica es la de {mejor_tarifa['Empresa']} - {mejor_tarifa['Tarifa']} con un precio de {mejor_tarifa['Precio']:.2f} €.")

    # Formulario para ingresar datos del usuario
    st.header("Formulario de Consumo")
    mes = st.selectbox("¿Para qué mes deseas hacer la comparativa?", list(dias_por_mes.keys()))
    provincia = st.text_input("¿En qué provincia te encuentras?")
    num_personas = st.number_input("¿Cuántas personas viven en tu domicilio?", min_value=1, step=1)

    conoce_consumo = st.radio("¿Conoces tu consumo en kWh para los periodos de Valle, Llano y Punta?", ('Sí', 'No'))

    if conoce_consumo == 'Sí':
        consumo_valle = st.number_input("Introduce tu consumo en kWh para el periodo Valle:", min_value=0.0, step=0.1)
        consumo_llano = st.number_input("Introduce tu consumo en kWh para el periodo Llano:", min_value=0.0, step=0.1)
        consumo_punta = st.number_input("Introduce tu consumo en kWh para el periodo Punta:", min_value=0.0, step=0.1)
        potencia = st.number_input("Introduce tu potencia en kW:", min_value=0.0, step=0.1)

        # Mostrar gráfico de franjas horarias
        discriminacion = {
            "00": 'valle', "01": 'valle', "02": 'valle', "03": 'valle',
            "04": 'valle', "05": 'valle', "06": 'valle', "07": 'valle',
            "08": 'llano', "09": 'llano', "10": 'punta', "11": 'punta',
            "12": 'punta', "13": 'punta', "14": 'llano', "15": 'llano',
            "16": 'llano', "17": 'llano', "18": 'punta', "19": 'punta',
            "20": 'punta', "21": 'punta', "22": 'llano', "23": 'llano',
        }

        # Crear un pie chart simulando las 24 horas de un reloj
        labels = list(discriminacion.keys())
        sizes = [1] * 24  # Cada hora tiene el mismo tamaño
        colors = ['#2ca02c' if discriminacion[hora] == 'valle' else '#ffdd44' if discriminacion[hora] == 'llano' else '#d62728' for hora in labels]

        fig, ax = plt.subplots(figsize=(6, 6))  # Ajustar el tamaño del gráfico
        ax.pie(sizes, labels=labels, colors=colors, startangle=90, counterclock=False)
        ax.axis('equal')  # Para asegurar que el pie chart es un círculo
        ax.set_title('Distribución de las Franjas Horarias', pad=20)  # Ajustar el padding del título

        # Añadir leyenda
        custom_lines = [plt.Line2D([0], [0], color='#2ca02c', lw=4),
                        plt.Line2D([0], [0], color='#ffdd44', lw=4),
                        plt.Line2D([0], [0], color='#d62728', lw=4)]
        ax.legend(custom_lines, ['Valle', 'Llano', 'Punta'], loc='upper right', bbox_to_anchor=(1.1, 1), fontsize='x-small')

        st.pyplot(fig)

        # Ajustar el consumo en función del número de habitantes
        consumo_valle = ajustar_consumo_por_habitantes(consumo_valle, num_personas)
        consumo_llano = ajustar_consumo_por_habitantes(consumo_llano, num_personas)
        consumo_punta = ajustar_consumo_por_habitantes(consumo_punta, num_personas)
        
        datos_consumo = {"valle": consumo_valle, "llano": consumo_llano, "punta": consumo_punta, "potencia": potencia, "mes": mes}

    elif conoce_consumo == 'No':
        consumo_estimado = 0
        electrodomesticos = {
            "Frigorífico": 1.2, "Lavadora": 0.9, "Lavavajillas": 0.85,
            "Televisor": 0.2, "Aire Acondicionado": 3.0, "Vitroceramica": 1.5,
            "Horno": 1.0, "Calefactores eléctricos": 2.0, "Microondas": 0.2,
            "Ordenador": 0.5, "Plancha de ropa": 0.3, "Algún otro electrodomestico": 0.5
        }
        
        st.write("Vamos a estimar tu consumo. Por favor, indica si tienes los siguientes electrodomésticos:")
        for electrodomestico, consumo in electrodomesticos.items():
            respuesta = st.radio(f"¿Tienes {electrodomestico}?", ('Sí', 'No'))
            if respuesta == 'Sí':
                consumo_estimado += consumo

        consumo_valle = consumo_estimado * 0.4 * 30
        consumo_llano = consumo_estimado * 0.3 * 30
        consumo_punta = consumo_estimado * 0.3 * 30
        potencia = st.number_input("Introduce tu potencia en kW:", min_value=0.0, step=0.1)

        # Ajuste del consumo basado en habitantes
        consumo_valle = ajustar_consumo_por_habitantes(consumo_valle, num_personas)
        consumo_llano = ajustar_consumo_por_habitantes(consumo_llano, num_personas)
        consumo_punta = ajustar_consumo_por_habitantes(consumo_punta, num_personas)

        st.write("\nEstimación de consumo:")
        st.write(f"Consumo estimado en Valle: {consumo_valle:.2f} kWh")
        st.write(f"Consumo estimado en Llano: {consumo_llano:.2f} kWh")
        st.write(f"Consumo estimado en Punta: {consumo_punta:.2f} kWh")

        datos_consumo = {"valle": consumo_valle, "llano": consumo_llano, "punta": consumo_punta, "potencia": potencia, "mes": mes}

    # Botón para calcular la mejor tarifa
    if st.button("Calcular Mejor Tarifa"):
        tarifas = cargar_tarifas()
        calcular_mejor_tarifa(datos_consumo, tarifas)

        # Preguntar al usuario si le interesa saber si le compensa poner placas solares
        interes_placas = st.radio("¿Te interesa saber si te compensa poner placas solares?", ('Sí', 'No'))

        if interes_placas == 'Sí':

            # Función para sacar datos horarios por provincia
            def sacar_datos_horarios(ciudad):
                ciudad = ciudad.capitalize()  # Asegurarse de que la primera letra de la ciudad esté en mayúscula
                url = f'https://cdn.mitma.gob.es/portal-web-drupal/salidapuestasol/2024/{ciudad}-2024.txt'
                response = requests.get(url)
                response.encoding = 'ISO-8859-1'
                content = response.text

                # Mostrar la URL y las primeras líneas del contenido para depuración
                st.write(f"URL: {url}")
                st.write("Primeras líneas del contenido descargado:")
                st.write(content.splitlines()[:10])

                lines = content.splitlines()[7:]  # Saltar las primeras 7 líneas de encabezado
                data = [line.split() for line in lines]

                # Mostrar las primeras líneas de los datos para depuración
                st.write("Primeras líneas de los datos procesados:")
                st.write(data[:10])

                def adjust_days(data):
                    for sublist in data:
                        if not sublist:
                            continue
                        elif sublist[0] == '30':
                            sublist.insert(3, '0000')
                            sublist.insert(4, '0000')
                        elif sublist[0] == '31':
                            sublist.insert(3, '0000')
                            sublist.insert(4, '0000')
                            sublist.insert(7, '0000')
                            sublist.insert(8, '0000')
                            sublist.insert(11, '0000')
                            sublist.insert(12, '0000')
                            sublist.insert(17, '0000')
                            sublist.insert(18, '0000')
                            sublist.insert(21, '0000')
                            sublist.insert(22, '0000')
                    return data

                data = adjust_days(data)
                columnas = ['Dia', 'Ene_Ort', 'Ene_Ocas', 'Feb_Ort', 'Feb_Ocas', 'Mar_Ort', 'Mar_Ocas', 'Apr_Ort', 'Apr_Ocas',
                            'May_Ort', 'May_Ocas', 'Jun_Ort', 'Jun_Ocas', 'Jul_Ort', 'Jul_Ocas', 'Aug_Ort', 'Aug_Ocas',
                            'Sep_Ort', 'Sep_Ocas', 'Oct_Ort', 'Oct_Ocas', 'Nov_Ort', 'Nov_Ocas', 'Dec_Ort', 'Dec_Ocas']
                
                # Verificar si data no está vacío y si el número de columnas coincide con el esperado
                if not data:
                    st.error("Los datos descargados están vacíos.")
                    return None
                if len(data[0]) != len(columnas):
                    st.error(f"El número de columnas no coincide con el esperado. Esperado: {len(columnas)}, Obtenido: {len(data[0])}")
                    st.write("Contenido de data[0]:")
                    st.write(data[0])
                    return None

                try:
                    df = pd.DataFrame(data).iloc[:-4].dropna(axis=1, how='all')
                    df.columns = columnas
                    df = df.iloc[2:].reset_index(drop=True)
                except Exception as e:
                    st.error(f"Error al crear el DataFrame: {e}")
                    return None

                def format_time(value):
                    if isinstance(value, str):
                        if len(value) == 3:
                            value = '0' + value
                        value = value[:-2] + ':' + value[-2:]
                    return value

                try:
                    df.iloc[:, 1:] = df.iloc[:, 1:].applymap(format_time)
                    for col in df.columns[1:]:
                        df[col] = pd.to_timedelta(df[col] + ':00')
                except Exception as e:
                    st.error(f"Error al formatear las horas: {e}")
                    return None

                meses = ["Ene", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                nuevo_df = pd.DataFrame()
                nuevo_df['Dia'] = df['Dia']
                nuevo_df['Ciudad'] = ciudad

                try:
                    for mes in meses:
                        nuevo_df[mes] = (df[f'{mes}_Ocas'] - df[f'{mes}_Ort']).apply(lambda x: x.total_seconds() / 3600)
                except Exception as e:
                    st.error(f"Error al calcular las horas de sol: {e}")
                    return None

                return nuevo_df

            # Función para prorratear el consumo
            def prorrateo_consumo(mesecito, consumito):
                year = 2024
                mes = {
                    'enero': 'Ene', 'febrero': 'Feb', 'marzo': 'Mar', 'abril': 'Apr', 'mayo': 'May', 'junio': 'Jun',
                    'julio': 'Jul', 'agosto': 'Ago', 'septiembre': 'Sep', 'octubre': 'Oct', 'noviembre': 'Nov', 'diciembre': 'Dic'
                }
                month = mes.get(mesecito.lower())
                if month is None:
                    st.error(f"Mes no válido: {mesecito}")
                    return None

                discriminacion = {
                    "00": 'valle', "01": 'valle', "02": 'valle', "03": 'valle',
                    "04": 'valle', "05": 'valle', "06": 'valle', "07": 'valle',
                    "08": 'llano', "09": 'llano', "10": 'punta', "11": 'punta',
                    "12": 'punta', "13": 'punta', "14": 'llano', "15": 'llano',
                    "16": 'llano', "17": 'llano', "18": 'punta', "19": 'punta',
                    "20": 'punta', "21": 'punta', "22": 'llano', "23": 'llano',
                }

                horas_llano_lab = sum(1 for h in discriminacion if discriminacion[h] == 'llano')
                horas_punta_lab = sum(1 for h in discriminacion if discriminacion[h] == 'punta')
                num_dias_mes = calendar.monthrange(year, month)[1]
                dias_finde = sum(1 for d in range(1, num_dias_mes + 1) if calendar.weekday(year, month, d) >= 5)
                dias_laborables = num_dias_mes - dias_finde
                horas_llano_totales = horas_llano_lab * dias_laborables
                horas_punta_totales = horas_punta_lab * dias_laborables

                c_p = consumito[0] * 8 / horas_punta_totales
                c_l = consumito[1] * 8 / horas_llano_totales
                c_v = (sum(consumito) - c_p * num_dias_mes - c_l * num_dias_mes) / num_dias_mes

                c_totales = [c_p * num_dias_mes, c_l * num_dias_mes, c_v * num_dias_mes]
                return c_totales

            # Función para calcular el número de placas solares
            def calcular_placas(ciudad, mes, potencia, consumo):
                consumo_total = prorrateo_consumo(mes, consumo)
                if consumo_total is None:
                    return "No se pudo prorratear el consumo debido a un mes no válido."
                df_ciudad = sacar_datos_horarios(ciudad)
                if df_ciudad is None:
                    return "No se pudo obtener los datos horarios para la ciudad especificada."

                factor_solar = 0.8
                pot_placa = 0.455
                dias = {'Ene': 31, 'Feb': 29, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Ago': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dic': 31}

                meses = df_ciudad.columns.difference(['Dia', 'Ciudad'])
                horas_sol = {mes: df_ciudad[mes].sum() * factor_solar for mes in meses}
                c_total = sum(consumo_total)
                n_placas = int(c_total / (pot_placa * 0.7 * horas_sol[mes] * 0.8))

                if n_placas < 2:
                    return "Tu consumo es muy bajo para poder beneficiarte de una instalación de placas solares. ¡Gracias por ser un consumidor eficiente!"
                else:
                    return f"Con los datos de consumo suministrados, ¡Te podría interesar instalar hasta {n_placas} placas! Ten en cuenta que la mejor estimación del número de placas se realiza con el consumo en verano, además de ser donde te beneficiarás del mayor ahorro."

            recomendacion_placas = calcular_placas(provincia, mes, datos_consumo["potencia"], [datos_consumo["punta"], datos_consumo["llano"], datos_consumo["valle"]])
            st.write(recomendacion_placas)
        else:
            st.write("Gracias por usar esta aplicación.")
