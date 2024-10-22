import csv
import math
from collections import defaultdict

# Função para verificar se um número é quadrado perfeito
def is_perfect_square(n):
    return int(math.sqrt(n)) ** 2 == n

# Função para verificar se uma string é um palíndromo
def is_palindrome(s):
    return s == s[::-1]

# Lendo os dados do arquivo Academy_Candidates.txt
candidates = []
with open('Academy_Candidates.txt', 'r') as file:
    next(file)  # Ignora o cabeçalho, se houver
    for line in file:
        # Agora a ordem é Nome;Idade;Vaga;Estado
        name, age, position, state = line.strip().split(';')
        # Remove qualquer texto extra e converte a idade para inteiro
        age = int(age.replace(' anos', '').strip())
        candidates.append({
            'Name': name,      # Ajustando a chave para "Name"
            'Position': position,  # Ajustando a chave para "Position"
            'Age': age,          # Ajustando a chave para "Age"
            'State': state       # Ajustando a chave para "State"
        })

# Inicializando variáveis
position_count = defaultdict(int)
position_age_sum = defaultdict(int)
position_ages = defaultdict(list)
states = set()

# Processando os candidatos
for candidate in candidates:
    position = candidate['Position']
    age = candidate['Age']
    state = candidate['State']
    
    position_count[position] += 1
    position_age_sum[position] += age
    position_ages[position].append(age)
    states.add(state)

# Calculando porcentagem de candidatos por vaga
total_candidates = len(candidates)
position_percentage = {position: (count / total_candidates) * 100 for position, count in position_count.items()}

# Calculando idade média por vaga e outras informações
position_average_age = {position: position_age_sum[position] / position_count[position] for position in position_count}
position_oldest_age = {position: max(ages) for position, ages in position_ages.items()}
position_youngest_age = {position: min(ages) for position, ages in position_ages.items()}
position_total_age_sum = position_age_sum

# Determinando o número de estados distintos
distinct_states_count = len(states)

# Criando o arquivo Sorted_Academy_Candidates.csv
with open('Sorted_Academy_Candidates.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Position', 'Age', 'State']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for candidate in sorted(candidates, key=lambda x: x['Name']):  # Ordenando por nome
        writer.writerow({
            'Name': candidate['Name'],
            'Position': candidate['Position'],
            'Age': candidate['Age'],
            'State': candidate['State']
        })

# Encontrando o instrutor de QA
qa_instructor = None
for candidate in candidates:
    if candidate['Position'] == "QA" and candidate['State'] == "SC":
        if 18 <= candidate['Age'] <= 30 and is_perfect_square(candidate['Age']) and is_palindrome(candidate['Name'].split()[0]):
            qa_instructor = candidate['Name']
            break

# Encontrando o instrutor de Mobile
mobile_instructor = None
for candidate in candidates:
    if candidate['Position'] == "Mobile" and candidate['State'] == "PI":
        if 30 < candidate['Age'] < 40 and candidate['Age'] % 2 == 0 and candidate['Name'].split()[-1].startswith('C'):
            mobile_instructor = candidate['Name']
            break

# Exibindo os resultados
print("Proporção de candidatos por vaga (porcentagem):")
for position, percentage in position_percentage.items():
    print(f"{position}: {percentage:.2f}%")

print("\nIdade média dos candidatos de QA:", position_average_age.get("QA", 0))
print("Idade do candidato mais velho de Mobile:", position_oldest_age.get("Mobile", 0))
print("Idade do candidato mais novo de Web:", position_youngest_age.get("Web", 0))
print("Soma das idades dos candidatos de QA:", position_total_age_sum.get("QA", 0))
print("Número de estados distintos presentes entre os candidatos:", distinct_states_count)
print("Arquivo Sorted_Academy_Candidates.csv foi criado.")
print("Instrutor de QA:", qa_instructor)
print("Instrutor de Mobile:", mobile_instructor)
