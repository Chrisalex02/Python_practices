#importando librerias basicas
import streamlit as st #Para desplegar y formatear la app
import pandas as pd #Para manipular datos
import numpy as np #Para operaciones de algebra lineal

st.title('Uber pickups in NYC') #titulo de la app
# Nota: para visualizar la pagina hay que dar en el boton open in browser 
# cualquier otra opcion da error

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

#Trayendo datos
@st.cache_data #Guardando los datos en cache
def load_data(nrows): #Cargando datos
    data = pd.read_csv(DATA_URL, nrows=nrows) #Convirtiendolos a CSV
    lowercase = lambda x: str(x).lower() #Normalizandolos a minusculas
    data.rename(lowercase, axis='columns', inplace=True) #Eliminado el indice?
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN]) #Extreyendo la fecha
    return data #Devolver el arreglo con los datos

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
#data_load_state.text('Loading data...done!')
data_load_state.text("Done! (using st.cache_data)")

#st.subheader('Raw data')
#st.write(data)
#Use a button to toggle data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')

#Use NumPy to generate a histogram that breaks down pickup times binned by hour:
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

#Now, let's use Streamlit's st.bar_chart() method to draw this histogram.
st.bar_chart(hist_values)

#Add a subheader for the section:
#st.subheader('Map of all pickups')

#Use the st.map() function to plot the data:
#st.map(data)

#After drawing your histogram, you determined that the busiest hour for Uber pickups was 17:00. 
# Let's redraw the map to show the concentration of pickups at 17:00.
#hour_to_filter = 17
#Locate hour_to_filter and replace it with this code snippet:
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

