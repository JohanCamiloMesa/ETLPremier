# importación de librerías
import pandas as pd

# Clase para limpieza de datos
class SpotifyandYoutubeClean:
	def __init__(self, df):
		self.df = df.copy()

	def verificar_nulos_ceros(self):
		"""
		Retorna un DataFrame con el conteo de nulos y ceros por columna
		"""
		nulos = self.df.isnull().sum()
		ceros = (self.df == 0).sum()
		return pd.DataFrame({'Nulos': nulos, 'Ceros': ceros})

	def limpiar_columnas(self):
		"""
		Elimina columnas irrelevantes y filas con nulos, pero conserva los ceros.
		"""
		# Eliminar columnas irrelevantes (ajusta según tu necesidad)
		columnas_a_eliminar = ['Referee', 'Display_Order']
		df_limpio = self.df.drop(columns=[col for col in columnas_a_eliminar if col in self.df.columns], errors='ignore')

		# Eliminar filas con nulos
		df_limpio = df_limpio.dropna()

		# Conservar los ceros, no eliminar filas con ceros
		df_limpio = df_limpio.reset_index(drop=True)
		return df_limpio
