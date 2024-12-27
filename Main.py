import pandas as pd
import os

# Caminho relativo para o ficheiro
file_path = os.path.join("original_data", "jobs_in_data.csv")

# Ler os dados do ficheiro CSV
data = pd.read_csv(file_path)

# Eliminar as colunas irrelevantes
columsn_to_drop = ["work_year", "salary", "salary_currency", "job_title"]
data = data.drop(columns=columsn_to_drop)


