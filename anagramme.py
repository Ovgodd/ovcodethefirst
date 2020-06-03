w = open("w.txt",'r')
l = []

for i in w:
    l+=i.split()


s = l[1]
s = ''.join(sorted(s))

i = 0
while i < (len(l)):
    u = ''.join(sorted(l[i]))
    if ( u == s ):
        print(l[i])
    i += 1
