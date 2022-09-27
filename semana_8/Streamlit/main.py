import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import webbrowser
import urllib.request
st.set_page_config(layout='centered', page_icon='src/images/ih.png', page_title='Streamlit Workshop')

st.title('STREAMLIT WORKSHOP')

st.header('METODOS PARA INTRODUCIR TEXTO EN LA PAGINA')
st.subheader('Existen varios metodos para introducir texto')
st.write('Con el método write podemos introducir texto de forma normal y podemos darle formato')
st.write('''
    # Si ponemos '#' delante del texto lo interpretará como H1
    ## Si ponemos '##' delante del texto lo interpretará como H2
    ### Si ponemos '###' delante del texto lo interpretará como H3
''')

st.info('Con el método info podemos resaltar información')
st.success('Con el método success podemos indicar la conclusión de un proceso de manera satisfactoria')
st.warning('Con el método warning podemos mostrar mensajes de alerta')
st.error ('Con el metodo error podemos mostrar mensajes de error en la página')

df = pd.read_csv('src/data/comunio_J6.csv')
st.caption('# Podemos cargar un dataframe y mostrarlo')

st.warning('Podemos introducir métodos para filtrar el dataframe')

filtros, equipos, pos, goles = st.columns(4)

with filtros:
    columnas = df.columns
    selection = st.multiselect('Filtrar Columnas', columnas, default=['Team','Player', 'Position', 'Matchs', 'Goals',
                                                                      'Total_Points'])

with equipos:
    equipo = st.selectbox('Filtrar Equipos', df.Team.unique())

with pos:
    player_pos = st.selectbox('Filtrar Posicion', df.Position.unique())

with goles:
    gol_min, gol_max = st.select_slider('Filtrar por Goles', options=[i for i in range(0, df.Goals.max()+1)],
                                        value=[0, df.Goals.max()])
st.sidebar.header('Menú Lateral')
st.sidebar.subheader('Streamlit Workshop for IH')
st.sidebar.image(Image.open('src/images/ih.png'))
st.sidebar.info('Aquí puedes poner una barra de navegación o zonas para cargar archivos')
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
upload_image = st.sidebar.file_uploader('Upload an Image', type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)
else:
    df1 = df[selection]

    var = df1[(df1.Team == equipo) &
              (df1.Goals >= gol_min) &
              (df1.Goals <= gol_max) &
              (df1.Position == player_pos)]

    st.dataframe(var)

    df_plot = df1[(df1.Team == equipo) &
        (df1.Goals >= gol_min) &
        (df1.Goals <= gol_max) &
        (df1.Position == player_pos)]
    fig, ax = plt.subplots()
    plt.title(f'Puntos Totales del {equipo} por Jugador - Posición {player_pos}')
    ax.barh(y=df_plot.Player, width=df_plot.Total_Points)
    st.caption('## También podemos mostrar gráficos')
    st.pyplot(fig)

st.caption('## Imágenes')
if upload_image is not None:
    st.image(upload_image)
else:
    st.image(Image.open('src/images/ih.png'))

st.caption('# Podemos incluir botones de redirección')
url = 'https://www.ironhack.com/en?utm_campaign=MAD_Spain_Madrid_Global_Search_Brand_EN&utm_source=google&utm_medium=cpc&utm_content=search-brand&utm_term=ironhack%20madrid&gclid=CjwKCAjwrNmWBhA4EiwAHbjEQH2Jk5GIClZTxrUGqBIismRC9suomZJPbeej70o0UCKznHoVPPGyNRoCymkQAvD_BwE'


if st.button('Web Ironhack'):
    webbrowser.open_new_tab(url)

st.caption('## Cargar imágenes desde una url')

url = st.form('template2')

image_url = url.text_input('Introduce la url de la imagen')

submit = url.form_submit_button('Enviar')

if submit:
    urllib.request.urlretrieve(
        image_url,
        "image.png")
    image_player = Image.open("image.png")
    st.image(image_url)

else:
    st.warning('Introduce una url de imagen para mostrar')

st.caption('## Busqueda en Google')

url2 = st.form('template')

query = url2.text_input('Introduce la búsqueda')

search_query = url2.form_submit_button('Buscar')

if search_query:
    url_query = 'https://www.google.com/search?q='+query
    webbrowser.open_new_tab(url_query)

st.caption('## Busqueda en Youtube')

url3 = st.form('template3')

query2 = url3.text_input('Introduce la búsqueda')

search_query2 = url3.form_submit_button('Buscar')

if search_query2:
    url_query2 = 'https://www.youtube.com/results?sp=mAEB&search_query='+'+'.join(query2.split())+'&sp=mAEB'
    webbrowser.open_new_tab(url_query2)

st.caption('# Y para finalizar, también se pueden incluir vídeos')

st.video('https://www.youtube.com/watch?v=Yem_iEHiyJ0')

st.caption('# Si aún os quedan dudas')
help_kike = 'https://docs.streamlit.io/library/api-reference'


if st.button('Kike Help me Please'):
    webbrowser.open_new_tab(help_kike)
