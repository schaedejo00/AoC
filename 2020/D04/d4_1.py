import numpy as np
import re



with open('input_1.txt', 'r') as f:
    lines = f.readlines()
#([byr|iyr|eyr|hgt|hcl|ecl]+\:[0-9#a-z]+\s)

reqFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
foundFields = []
ok = 0
total = 0
notOk = 0

for line in lines:
    if (len(line)>1):
        tokens = re.findall("(byr|iyr|eyr|hgt|hcl|ecl|pid|cid){1}:", line)
        #print(line)
        #print(tokens)
        for token in tokens:
            foundFields.append(token)
            #print(foundFields)
    else:
        # neuer Passport => alten prüfen
        total += 1
        if all(elem in foundFields for elem in reqFields):
            ok += 1
        else:
            notOk += 1


        print(foundFields)
        foundFields = []
        print("######next passport#######")

print('ok={}, notOk={}, total={}'.format(ok, notOk, total))
