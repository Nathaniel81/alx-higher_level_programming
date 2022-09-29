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
d = [
    [1, 4, 6],
    [3, 5, 7]
]
"""
#for i in d:
#print('{}'.format(', '.join(i)))
#print('{}'.format(', '.join(map(str, d))))
#for row in d:
#       print("[{}]".format(",".join([str(x) for x in row])))
new_f = ""
with open("append_after_100.txt") as f:
    for stR in f.readlines():
        new_f += stR
        if 'Python' in stR:
            new_f += "\"C is fun!\"\n"
"""print(new_f)"""
with open("append_after_100.txt", "w") as f:
    f.write(new_f)
            
        















