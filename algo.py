import csv
from scipy.optimize import linear_sum_assignment

def str_to_float(value):
    """Convert a string to a float, with a default value to the maximum value
    in case the value is not a valid float."""
    try:
        return float(value)
    except Exception:
        return 100

# Define the first cell with data. It is assumed that previous cells
# on the left contain people names, and those above the group names.
# First column and first row are indexed at 0.
first_x = 2
first_y = 3

# Define lists
people = []
groups = []
population = []
populated_groups = []
data = []

# Read the csv file (exported from a gsheet or xslx), and store the data
# in the lists
with open('input.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for i, line in enumerate(csv_reader):
        # names of groups
        if i == first_y - 2:
            groups = line[first_x:]
        # number of people wanted per groups
        elif i == first_y - 1:
            population = [int(nb_people) for nb_people in line[first_x:]]
            # duplicate the columns n times
            for n, group in zip(population, groups):
                populated_groups += [group] * n
        # choices for each person
        elif i >= first_y:
            people.append(" ".join(line[:first_x]))
            values = [str_to_float(val) for val in line[first_x:]]
            # duplicate the columns n times
            populated_values = []
            for n, val in zip(population, values):
                populated_values += [val] * n
            data.append(populated_values)

# resolve the problem of assignment
row_ind, col_ind = linear_sum_assignment(data)

# print the solution
print(f"{'People':25}\t{'Group':10}\t{'Choice'}")
for i, j in zip(row_ind, col_ind):
    print(f"{people[i]:25}\t{populated_groups[j]:10}\t{data[i][j]}")
