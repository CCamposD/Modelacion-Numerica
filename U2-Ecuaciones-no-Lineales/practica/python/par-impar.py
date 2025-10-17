print("\nPar")
a = 27.00472
b = 27.00534

M = (a + b) / 2 
R = (b - a) / 2

print("\nSalida en bruto")
print(M)    
print(R) 

#  Errores 
M_prima = round(M, 1)
R_prima = round(R, 1)

print("\nTolerancia")
print(M_prima)
print(R_prima)

print("\nCota")
print(M_prima - R_prima)

print("\nImpar")

a = 1.230987
b = 1.230995

M = (a + b) / 2 
R = (b - a) / 2

print("\nSalida en bruto")
print(M)     
print(R)    

#  Errores 
M_prima = round(M, 1)
R_prima = round(R, 1)

print("\nTolerancia")
print(M_prima)
print(R_prima)

print("\nCota")
print(M_prima - R_prima)