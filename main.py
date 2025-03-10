import json
from sympy import symbols, expand
from itertools import combinations

def lagrange_interpolation(points):
    x = symbols('x')
    polynomial = 0
    for i in range(len(points)):
        xi, yi = points[i]
        term = yi
        for j in range(len(points)):
            if i != j:
                xj, _ = points[j]
                term *= (x - xj) / (xi - xj)
        polynomial += term
    return expand(polynomial)

with open('input.json') as file:
    data = json.load(file)

n = data['keys']['n']
k = data['keys']['k']

points = []
for key, value in data.items():
    if key.isdigit():
        base = int(value['base'])
        decimal_value = int(value['value'], base)
        points.append((int(key), decimal_value))

print("Points:", points)

combinations_of_points = combinations(points, k)
polynomials = []

for combo in combinations_of_points:
    polynomial = lagrange_interpolation(combo)
    polynomials.append(polynomial)
    print(f'Polynomial for {combo}: {polynomial.simplify()}')
    # print(f'Coefficents for {combo}: {polynomial.as_coefficients_dict()}')

print("Generated polynomials:", polynomials)

x_test, y_test = 1, 4  #example
x = symbols('x')
for poly in polynomials:
    if poly.subs(x, x_test) == y_test:
        print("Found the correct polynomial:", poly)
        break