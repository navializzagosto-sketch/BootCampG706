import pandas as pd
 # crear datos (simulación estudiantes)
datos={
    "nombre":["Ana","Luis","carlos","sofia","pedro"],
    "edad":[30,70,18,21,22],
    "nota":[3.5,4.2,2.8,4.8,3.0]
}
df = pd.DataFrame(datos)
print(df)
#proemdio de notas
print("promedio de notas:",df["nota"].mean())
#promedio edad 
print("promedio de edad:",df["edad"].mean())