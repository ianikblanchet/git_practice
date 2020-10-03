import random
maliste = [[1,2,3,4],[12,2,3,4]]
print(maliste)
del maliste[0][1]
#del (random.choice(maliste))
print(maliste)
print(random.choice(maliste))

maliste2 = ['01h','02h','01d','02d','01c','02c','01s','02s']
carte1 = random.choice(maliste2)
maliste2.remove(carte1)
carte2 = random.choice(maliste2)
print(carte1[0:2])
print(carte2)
valeur1 = int(carte1[0:2])
print(valeur1)

print("testgit")
