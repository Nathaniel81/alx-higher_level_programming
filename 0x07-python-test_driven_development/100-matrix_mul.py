#!/usr/bin/python3
"""Documentation for a simple matmul function"""


def matrix_mul(m_a, m_b):
	"""Computes the multiplication of m_a by m_b."""

if m_a == [[]]:
raise ValueError("m_a can't be empty")
if m_b == [[]]:
raise ValueError("m_b can't be empty")

if not type(m_a) == list:
raise TypeError("m_a must be a list")
if not type (m_b) == list:
raise TypeError("m_b must be a list") 

for i in m_a:
if not type(i) == list:
raise TypeError("m_a must be a list")
if len(i) == 0:
raise ValueError("m_a can't be empty")
if len(i) != len(m_a[0]):
raise TypeError("each row of m_a must be of the same size")
for j in i:
if type(j) not in [int, float]:
raise TypeError("m_a should contain only integers or floats")

for i in m_b:
if not type(i) == list:
raise TypeError("m_b must be a list")
if len(i) == 0:
raise ValueError("m_b can't be empty")
if len(i) != len(m_b[0]):
raise TypeError("each row of m_b must be of the same size")
for j in i:
if type(j) not in [int, float]:
raise TypeError("m_b should contain only integers or floats")

if len(m_a[0]) != len(m_b):
raise ValueError("m_a and m_b can't be multiplied")

transp = []
for r in range(len(m_b[0])):
new_row = []
for c in range(len(m_b)):
new_row.append(m_b[c][r])
transp.append(new_row)

new_matrix = []
for row in m_a:
new_row = []
for col in transp:
prod = 0
for i in range(len(transp[0])):
prod += row[i] * col[i]
new_row.append(prod)
new_matrix.append(new_row)

return new_matrix