from calculaSolucion import ChequesSolver

print("Hola")
tipos = [
    (8),
    (3),
    (7)
]
cs =  ChequesSolver(tipos)
#print (cs.peso([(10,8),  (3, 3) ,(0, 2)]))
cantidad= 58
res= cs.calcula(cantidad)
print (cantidad,cs.peso(res), ": ", res)


cantidad= 8
res= cs.calcula(cantidad)
print (cantidad,cs.peso(res), ": ", res)


cantidad= 12
res= cs.calcula(cantidad)
print (cantidad,cs.peso(res), ": ", res)

cantidad= 13
res= cs.calcula(cantidad)
print (cantidad,cs.peso(res), ": ", res)





