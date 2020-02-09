from operator import attrgetter

class Magic:
    def __init__(self, attack, mp):
        self.attack = attack
        self.mp = mp
        self.ratio = float(attack) / float(mp)
    
    def __repr__(self):
        return "%d, %d, %f" % (self.attack, self.mp, self.ratio)

val = input().split(' ')
h = int(val[0])
n = int(val[1])
magics = []
for i in range(n):
    val = input().split(' ')
    magics.append(Magic(int(val[0]), int(val[1])))

magics = sorted(magics, key=attrgetter('mp'))
magics = sorted(magics, key=attrgetter('ratio'), reverse=True)

counter = 0
for i, magic in enumerate(magics):
    count = h / magic.attack
    h -= magic.attack * count
    counter = magic.mp * count
    if h < 0:
        break
    
print(counter)
