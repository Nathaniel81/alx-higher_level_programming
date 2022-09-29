import json
from platform import java_ver
"""
dictionary = {
	"name": "sathiyajith",
	"rollno": 56,
	"cgpa": 8.6,
	"phonenumber": "9976770500"
}

with open("sample.json", "w") as outfile:
	json.dump(dictionary, outfile)
"""
class A:
    def __init__(self, name, val):
        self.name = name
        self.val = val
    def  setttt(self, dic):
        for i in dic.keys():
            if i in self.__dict__.keys():
                self.__dict__[i] = dic[i]

x = A('Ab', 45)
dic1 = {'name': 'bb'}
x.setttt(dic1)
print(x.name)
