l=lambda a: a*5
f=[n*4 for n in range(30)]
print("mapeo")
f0= list(map(l,f))
print(f)
print(f0)
print("filtrado")
f1=list(filter(lambda e: e>99,f0))
print(f1)