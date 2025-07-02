import pandas as pd

from geopy.distance import geodesic

coordenadas = [
    (-33.47925751543143, -70.51879354219926),
    (-33.45480637803595, -70.66599587783907),
    (-33.450923361069634, -70.66134187719895),
    (-33.450923361069634, -70.65099965355424),

    # lista de coordenadas segun corresponda
]

# Función para contar 
def contar_lugares_cercanos(lat_casa, lon_casa, estaciones, umbral_metros=800):
    casa_coord = (lat_casa, lon_casa)
    return sum(1 for estacion in estaciones if geodesic(casa_coord, estacion).meters <= umbral_metros)

# leer archivo .csv
df = pd.read_csv("propiedades_geolocalizadas_final.csv")

# Crear la nueva columna segun corresponda
df['cercania_educacion'] = df.apply(
    lambda row: contar_lugares_cercanos(row['Latitud'], row['Longitud'], coordenadas), axis=1
)

# Guardar el nuevo archivo .csv
df.to_csv("propiedades_geo_final.csv", index=False)

print("csv guardado como 'propiedades_geo_final.csv'")
