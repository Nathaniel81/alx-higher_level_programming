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
with open("fj.json", "r") as F:
    aa = json.load(F)
print(aa)