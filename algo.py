import csv
from scipy.optimize import linear_sum_assignment

def str_to_float(value):
    try:
        return float(value)
    except Exception:
        return 7

first_cell = (2, 3)
people = []
groups = []
population = []
data = []
with open('input.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    i = 0
    for line in csv_reader:
        if i == first_cell[1] - 2:
            groups = line[first_cell[0]:]
        elif i == first_cell[1] - 1:
            population = list(map(int, line[first_cell[0]:]))
        elif i >= first_cell[1]:
            people.append(" ".join(line[:first_cell[0]]))
            values = list(map(str_to_float, line[first_cell[0]:]))
            populated_values = []
            for n, val in zip(population, values):
                populated_values += [val] * n
            data.append(populated_values)
        i += 1

populated_groups = []
for n, group in zip(population, groups):
    populated_groups += [group] * n

row_ind, col_ind = linear_sum_assignment(data)

for i, j in zip(row_ind, col_ind):
    print(f"{people[i]:25}\t{populated_groups[j]:10}\t{data[i][j]}")
