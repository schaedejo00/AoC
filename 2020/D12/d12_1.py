from D12.actor import Actor

x = "halle"
x = 3


with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

actor = Actor(0, 0)
for line in lines:

    # print(line)
    action, amount = line[0], int(line[1:])
    if action == 'F':
        actor.moveForward(amount)
    if action in ['L', 'R']:
        actor.turn(amount, action)
    if action in ['N', 'S', 'E', 'W']:
        actor.move(amount, action)
    # print(actor.x, actor.y)

print(actor.manhattenDistanceTo(0, 0))

