import csv
import math
from collections import defaultdict

def is_perfect_square(n):
    return int(math.sqrt(n)) ** 2 == n

def is_palindrome(s):
    return s == s[::-1]

candidates = []
with open('Academy_Candidates.txt', 'r') as file:
    next(file)  
    for line in file:
        name, age, position, state = line.strip().split(';')
        age = int(age.replace(' anos', '').strip())
        candidates.append({
            'Name': name,     
            'Position': position,
            'Age': age,
            'State': state
        })

position_count = defaultdict(int)
position_age_sum = defaultdict(int)
position_ages = defaultdict(list)
states = set()

for candidate in candidates:
    position = candidate['Position']
    age = candidate['Age']
    state = candidate['State']
    
    position_count[position] += 1
    position_age_sum[position] += age
    position_ages[position].append(age)
    states.add(state)

total_candidates = len(candidates)
position_percentage = {position: (count / total_candidates) * 100 for position, count in position_count.items()}

position_average_age = {position: position_age_sum[position] / position_count[position] for position in position_count}
position_oldest_age = {position: max(ages) for position, ages in position_ages.items()}
position_youngest_age = {position: min(ages) for position, ages in position_ages.items()}
position_total_age_sum = position_age_sum

distinct_states_count = len(states)

with open('Sorted_Academy_Candidates.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Position', 'Age', 'State']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for candidate in sorted(candidates, key=lambda x: x['Name']):
        writer.writerow({
            'Name': candidate['Name'],
            'Position': candidate['Position'],
            'Age': candidate['Age'],
            'State': candidate['State']
        })

qa_instructor = None
for candidate in candidates:
    if candidate['Position'] == "QA" and candidate['State'] == "SC":
        if 18 <= candidate['Age'] <= 30 and is_perfect_square(candidate['Age']) and is_palindrome(candidate['Name'].split()[0]):
            qa_instructor = candidate['Name']
            break

mobile_instructor = None
for candidate in candidates:
    if candidate['Position'] == "Mobile" and candidate['State'] == "PI":
        if 30 < candidate['Age'] < 40 and candidate['Age'] % 2 == 0 and candidate['Name'].split()[-1].startswith('C'):
            mobile_instructor = candidate['Name']
            break

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
