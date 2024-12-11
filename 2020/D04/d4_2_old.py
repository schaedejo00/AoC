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
        matches = re.findall("((byr:[0-9]{4})|(iyr:[0-9]{4})|(eyr:[0-9]{4})|(hgt:[0-9]{2,3}(cm|in))|hcl:#[0-9a-f]{6}|ecl:(amb|blu|brn|gry|grn|hzl|oth){1}|pid:[0-9]{9}){1}", line)
        #print(line)
        #print(matches)
        for tokens in matches:
            for token in tokens:
                if not( token in foundFields) and ':' in token:
                    foundFields.append(token)
                    #print(foundFields)
    else:
        # neuer Passport => alten prüfen
        total += 1

        isOk = all(elem in foundFields for elem in reqFields)

        for token in foundFields:
            if not(':' in token):
                continue

            tokenParts = token.split(':')

            #if(tokenParts[0]=='byr' and int(tokenParts[1]) not in range(1920, 2002):
             #       isOk = False

        if isOk:
            ok += 1
        else:
            notOk += 1


        print(foundFields)
        foundFields = []
        print("######next passport#######")

print('ok={}, notOk={}, total={}'.format(ok, notOk, total))
