"""class Rectangle:
    def __init__(self, val, value):
        self.val = val
        self.value = value
    def __str__(self):
        return f'{self.val} - is the val'

r1 = Rectangle(10, 7)
r2 = Rectangle(2, 4)
list_rectangles_input = [r1, r2]
for i in list_rectangles_input:
    print(i)
"""
import csv

#with open("x.csv", 'r') as f:
#    mcs = csv.reader(f)
#    for i in mcs:
#        print(i)
#    with open("xx.csv", 'w') as ff:
#        mcs2 = csv.writer(ff, delimiter='\t ')
#        for i in mcs:
#            mcs2.writerow(i)

with open("x.csv", 'r') as f:
    mcs = csv.DictReader(f)
    with open("xx.csv", 'w') as ff:
        fld = ['Name', 'Sex', 'Age']
        mcs2 = csv.DictWriter(ff, fieldnames=fld, delimiter='\t')
        mcs2.writeheader()
        for i in mcs:
            mcs2.writerow(i)