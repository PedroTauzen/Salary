import pandas as pd
import os

# Caminho relativo para o ficheiro
file_path = os.path.join("original_data", "jobs_in_data.csv")

# Ler os dados do ficheiro CSV
data = pd.read_csv(file_path)

# Imprimir os primeiros registos
print(data.head())
