
with open('input.txt', 'r') as f:
    lines = f.readlines()

maxSeatID = 0
ids = list()
for line in lines:
    line = line.replace('F', '0')
    line = line.replace('B', '1')

    line = line.replace('L', '0')
    line = line.replace('R', '1')

    row = int('0b' + line[0:7], 2)
    column = int('0b' + line[7:10], 2)
    seatID = row * 8 + column

    print(line[0:len(line)-1] + ":" + str(row) + "/" + str(column) + ", seatID=" + str(seatID))

    ids.append(seatID)



ids.sort()
print("max=" + str(ids[len(ids)-1]))