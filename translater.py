# algorithm of an online translater
t = int( input())# shows the number of words
c = 0 # the counter
d = {}

while c < t:
    word = input() 
    l = word.split()
    d[l[0]] = l[1]
    c += 1

jomle = input()
l2 = jomle.split() # spliting the words and putting it in a list
l3 = []


for kal in l2:
    if kal in d:
        l3.append(d[kal])
    else:
        l3.append(kal)


a = " ".join(l3)
print(a) # the final sentence including translated words and first words
