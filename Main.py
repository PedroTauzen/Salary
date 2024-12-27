import pandas as pd
import os

# Caminho relativo para o ficheiro
file_path = os.path.join("original_data", "jobs_in_data.csv")

# Ler os dados do ficheiro CSV
data = pd.read_csv(file_path)

# Eliminar as colunas irrelevantes
columns_to_drop = ["work_year", "salary", "salary_currency", "job_title"]
data = data.drop(columns=columns_to_drop)

# Manter a coluna original de salário e criar uma coluna categorizada
salary_classification = "salary_in_usd"

# Calcular os quartis
q1 = data[salary_classification].quantile(0.25)
q3 = data[salary_classification].quantile(0.75)

# Definir as classes de salários com base nos quartis
def classify_salary(salary):
    if salary <= q1:
        return "low_salary"
    elif q1 < salary <= q3:
        return "medium_salary"
    else:
        return "high_salary"

# Cria uma coluna para a classificação de salários
data["salary_classification"] = data[salary_classification].apply(classify_salary)

# Caminho para o novo ficheiro
output_dir = "transformed_data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_file = os.path.join(output_dir, "jobs_in_data.csv")

# Gravar os dados transformados em CSV
data.to_csv(output_file, index=False)

print(f"Ficheiro transformado gravado com sucesso em: {output_file}")
