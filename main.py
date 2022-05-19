from calculaSolucion import ChequesSolver

print("Hola")
tipos = [
    (8),
    (3),
    (2)
]
cs =  ChequesSolver(tipos)
#print (cs.peso([(10,8),  (3, 3) ,(0, 2)]))
cantidad= 20
res= cs.calcula(cantidad)
print (cantidad,res.peso(), ": ", res.elementos)
print ("Soluciones analizadas: ", cs.soluciones_analizadas)

