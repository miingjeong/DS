import pandas as pd
import folium

class Visualization:

    def __init__(self):
        self.df=pd.read_csv('./data/older_population.csv')
        self.geo_data ='./data/seoul-dong.geojson'

    def get_figure(self, area):
        center=[37.541, 126.986]
        m=folium.Map(location=center, zoom_start=10)

        if area is None or area =='동':
            folium.Choropleth(
                geo_data=self.geo_data,
                data=self.df,
                columns=('동','인구'),
                key_on='feature.properties.동',
                fill_color='BuPu',
                legend_name='노령 인구수',
            ).add_to(m)
        else:
            df_adm = self.df.groupby(['구'])(['인구']).to_frame().reset_index()

            folium.Choropleth(
                geo_data=self.geo_data,
                data=df_adm,
                columns=('구', '인구'),
                key_on='feature.properties.구',
                fill_color='BuPu',
                legend_name='노령 인구수',
            ).add_to(m)

        figure = folium.Figure()
        m.add_to(figure)
        figure.render()

        return figure