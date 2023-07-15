import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config("Dashboard votação lei da improbidade")

with st.container():
    st.title("Dashboard votação lei da improbidade")

@st.cache_data
def get_data():
    data = pd.read_csv('././Dados/df_completo.csv', index_col=0)

    return data

def get_data_map():
    data = pd.read_csv('././Dados/df_prop.csv', index_col=0)

    return data

def create_map():
    state_geo = (
        'https://raw.githubusercontent.com/luizpedone/municipal-brazilian-geodata/master/data/Brasil.json'
        )
    
    df_prop = get_data_map()
    
    m = folium.Map(location=[-16.490371, -50.294348], zoom_start=4)
    
    choropleth = folium.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        data=df_prop,
        columns=["UF", "Proporcao"],
        key_on="properties.UF",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="proporção de votos (%)",
        highlight=True,
        vmin=df_prop["Proporcao"].min(),
        vmax=df_prop["Proporcao"].max()

    )
    choropleth.add_to(m)
    choropleth.geojson.add_child(
        folium.GeoJsonTooltip(['ESTADO'], labels=False)
    )

    folium.LayerControl().add_to(m)

    return m


with st.container():
    st.write('---')
    
    m = create_map()
    
    st.subheader('Proporção de votos sim por estado')
    st_data = st_folium(m, width=700, height=450)

def count_plot(df, column):
  fig = plt.figure(figsize=(12,8))
  sns.countplot(x=column, data=df, palette='flare', hue='Voto')

  font1 = {'family':'serif','color':'black','size':20}
  font2 = {'family':'serif','color':'purple','size':15}

  title = f'Divisão de votos por {column}'

  plt.title(title, fontdict=font1)
  plt.ylabel('Quantidade', fontdict=font2)
  plt.xlabel(column, fontdict=font2)
  plt.xticks(rotation=45)

  st.pyplot(fig)

with st.container():
    st.write('---')

    st.subheader('Plotagem de um countplot')

    df = get_data()

    select_box_axisx = st.selectbox('Selecione a variavel do eixo x', df.columns[1:], index=0)
    count_plot(df, select_box_axisx)
    
    st.write('Primeiras 5 linhas do DataFrame')
    st.write(df.head())

