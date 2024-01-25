a = [5,4,3,2,1]
print (a)
b = []
c = []
while len (a):
    b.append (a.pop())
while len (b):
    c.append (b.pop())
print (c)
