import numpy as np
import re



with open('input_1valid.txt', 'r') as f:
    lines = f.readlines()
#([byr|iyr|eyr|hgt|hcl|ecl]+\:[0-9#a-z]+\s)

reqFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
okFields = []
ok = 0
total = 0
notOk = 0
inputLines = ""

for line in lines:
    if not(line == '\n'):
        inputLines += line
        matches = re.findall(
            "((byr:[0-9]{4})|(iyr:[0-9]{4})|(eyr:[0-9]{4})|(hgt:[0-9]{2,3}(cm|in))|hcl:#[0-9a-f]{6}|ecl:(amb|blu|brn|gry|grn|hzl|oth){1}|pid:[0-9]{9}){1}",
            line)
        for tokens in matches:
            for token in tokens:
                if ':' in token:
                    field, value = token.split(':')
                    if field in okFields:
                        continue

                    if(field=='byr'):
                        value = int(value)
                        if(1920 <= value and value <= 2002):
                            okFields.append(field)
                    if (field == 'iyr'):
                        value = int(value)
                        if (2010 <= value and value <= 2020):
                            okFields.append(field)
                    if (field == 'eyr'):
                        value = int(value)
                        if (2020 <= value and value <= 2030):
                            okFields.append(field)
                    if (field == 'hgt'):
                        #print(field + "_" + value)
                        unit = value[len(value)-2:len(value)]
                        value = int(value[0:len(value)-2])
                        #print(unit + "_" + str(value))
                        if (unit=='cm' and 150 <= value and value <= 193):
                            okFields.append(field)
                        if (unit == 'in' and 59 <= value and value <= 76):
                            okFields.append(field)
                    if (field == 'ecl'):
                        if (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                            okFields.append(field)
                    if (field == 'hcl' or field == 'pid' or field == 'cid'):
                        okFields.append(field)
    else:
        # neuer Passport => alten prüfen
        total += 1
        if all(elem in okFields for elem in reqFields):
            ok += 1
            isOk=True
        else:
            notOk += 1
            isOk=False

        if isOk:
            print(inputLines)
            print(okFields)
            print("######next passport#######" + str(isOk))

        okFields = []
        inputLines = ""

print('ok={}, notOk={}, total={}'.format(ok, notOk, total))
