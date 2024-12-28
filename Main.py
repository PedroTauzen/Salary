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
        return "Low"
    elif q1 < salary <= q3:
        return "Medium"
    else:
        return "High"

# Cria uma coluna para a classificação de salários
data["salary_classification"] = data[salary_classification].apply(classify_salary)

# Selecionar as colunas para listar os valores únicos
columns_to_check = ['company_location', 'job_category', 'employee_residence']

# Criar um dicionário com os valores únicos e as suas quantidades
for col in columns_to_check:
    unique_values = data[col].unique()
    print(f"Coluna: {col}")
    print(f"Valores únicos ({len(unique_values)}): {unique_values}")
    print("\n")

# Mapeamento de países para continentes
continent_mapping = {
    # Europa
    'Germany': 'Europe', 'United Kingdom': 'Europe', 'France': 'Europe', 'Spain': 'Europe',
    'Ireland': 'Europe', 'Portugal': 'Europe', 'Netherlands': 'Europe', 'Luxembourg': 'Europe',
    'Lithuania': 'Europe', 'Poland': 'Europe', 'Romania': 'Europe', 'Slovenia': 'Europe',
    'Greece': 'Europe', 'Italy': 'Europe', 'Czech Republic': 'Europe', 'Estonia': 'Europe',
    'Latvia': 'Europe', 'Denmark': 'Europe', 'Sweden': 'Europe', 'Finland': 'Europe', 'Bulgaria': 'Europe',
    'Switzerland': 'Europe', 'Belgium': 'Europe', 'Austria': 'Europe', 'Andorra': 'Europe',
    'Malta': 'Europe', 'Bosnia and Herzegovina': 'Europe', 'Gibraltar': 'Europe', 'Moldova': 'Europe',
    'Croatia': 'Europe', 'Serbia': 'Europe', 'Georgia': 'Europe', 'Armenia': 'Europe',  'Jersey': 'Europe',

    # América do Norte
    'United States': 'North America', 'Canada': 'North America', 'Mexico': 'North America',
    'Puerto Rico': 'North America', 'American Samoa': 'North America', 'Bahamas': 'North America',

    # América do Sul
    'Brazil': 'South America', 'Colombia': 'South America', 'Argentina': 'South America',
    'Ecuador': 'South America', 'Peru': 'South America', 'Honduras': 'South America',
    'Chile': 'South America', 'Bolivia': 'South America',

    # África
    'South Africa': 'Africa', 'Mauritius': 'Africa', 'Kenya': 'Africa', 'Ghana': 'Africa',
    'Nigeria': 'Africa', 'Tunisia': 'Africa', 'Egypt': 'Africa', 'Algeria': 'Africa',
    'Central African Republic': 'Africa',

    # Ásia
    'India': 'Asia', 'China': 'Asia', 'Japan': 'Asia', 'Thailand': 'Asia', 'Philippines': 'Asia',
    'Pakistan': 'Asia', 'Turkey': 'Asia', 'Russia': 'Asia', 'Saudi Arabia': 'Asia', 'Qatar': 'Asia',
    'Indonesia': 'Asia', 'Malaysia': 'Asia', 'Singapore': 'Asia', 'Iran': 'Asia', 'Israel': 'Asia',
    'United Arab Emirates': 'Asia', 'Vietnam': 'Asia', 'Uzbekistan': 'Asia', 'Hong Kong': 'Asia',

    # Oceania
    'Australia': 'Oceania', 'New Zealand': 'Oceania'
}


# Caminho para o novo ficheiro
output_dir = "transformed_data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_file = os.path.join(output_dir, "jobs_in_data.csv")

# Gravar os dados transformados em CSV
data.to_csv(output_file, index=False)

print(f"Ficheiro transformado gravado com sucesso em: {output_file}")
