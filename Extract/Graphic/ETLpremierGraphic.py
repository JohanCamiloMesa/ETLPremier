
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Config.config import Config

def grafica_promedio_goles_liverpool(df):
	# Promedio de goles de local y visitante del Liverpool
	goles_local = df[df['HomeTeam'] == 'Liverpool']['FTH Goals'].mean()
	goles_visitante = df[df['AwayTeam'] == 'Liverpool']['FTA Goals'].mean()
	plt.figure(figsize=(6, 5))
	sns.barplot(x=['Local', 'Visitante'], y=[goles_local, goles_visitante], palette=['blue', 'red'])
	plt.title('Promedio de Goles de Liverpool')
	plt.xlabel('Condición')
	plt.ylabel('Promedio de Goles')
	plt.tight_layout()
	plt.show()

def grafica_promedio_tarjetas_por_equipo(df):
	# Promedio de tarjetas amarillas y rojas por equipo local
	amarillas = df.groupby('HomeTeam')['H Yellow'].mean()
	rojas = df.groupby('HomeTeam')['H Red'].mean()
	equipos = amarillas.index
	plt.figure(figsize=(12, 6))
	sns.barplot(x=equipos, y=amarillas.values, color='yellow', label='Amarillas')
	sns.barplot(x=equipos, y=rojas.values, color='red', label='Rojas', alpha=0.7)
	plt.title('Promedio de Tarjetas Amarillas y Rojas por Equipo Local')
	plt.xlabel('Equipo Local')
	plt.ylabel('Promedio de Tarjetas')
	plt.xticks(rotation=90)
	plt.legend(['Amarillas', 'Rojas'])
	plt.tight_layout()
	plt.show()

def grafica_promedio_goles_por_equipo(df):
	plt.figure(figsize=(10, 6))
	goles_por_equipo = df.groupby('HomeTeam')['FTH Goals'].mean().sort_values(ascending=False)
	sns.barplot(x=goles_por_equipo.index, y=goles_por_equipo.values, palette='viridis')
	plt.title('Promedio de Goles por Equipo Local')
	plt.xlabel('Equipo Local')
	plt.ylabel('Promedio de Goles')
	plt.xticks(rotation=90)
	plt.tight_layout()
	plt.show()

