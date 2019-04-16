import bmV2

filename = input("Nama file : ")
file = open(filename)
q={}

for line in file:
    x = line.split("?")
    a =x[0]
    b =x[1]
    q[a] =b
#list pertanyaan
for c in q:
    print(c)

# T = input()
P = input()
# print ("T  \t:",T)
print ("Pattern \t:",P)
for c in q:
    found =bmV2.BM(c,P)
    if found:
        print(q[c])
        break
