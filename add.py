import pandas as pd
import streamlit as st

df = pd.read_csv('12345.csv')
#Solo los estudiantes del colegio fe y alegria
st.text("Solo los estudiantes del colegio fe y alegria")

df1 = df[df["establecimiento"] == "col fe y alegria santa maria"]
st.table(df1.head(5))
#Solo los estudiantes que el puntaje de matematicas sea igual a 50.000
st.text("Solo los estudiantes que el puntaje de matematicas sea igual a 50.000")
df2 = df[df["puntaje_matematicas"] == 50.000]
st.table(df2.head(5))
#
st.text("Solo colegios con mas de 50.000 mil matriculados")
df3 = df[df["matriculados"] > 50.000]
st.table(df3.head(5))

st.text("Solo los estidiantes del 20162")
df4 = df[df["año_semestre"] == 20162]
st.table(df4.head(5))

st.text("Solo colegios con mas de 50 presentes")
df5 = df[df["presentes"] > 50]
st.table(df5.head(5))