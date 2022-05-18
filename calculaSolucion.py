


from tabnanny import check

def reset(n, lista):
        for e in range(n, len(lista)):
            lista[e] = (0,0)

class ChequesSolver:
    cheques = 0
    niveles= 0

    def __init__(self, cheques):
        self.cheques = cheques
        #print("Tipos de cheques: ", self.cheques)        


    def peso(self, mochila):
        peso=0
        for elem in mochila:
            peso += elem[0] * elem [1]
        return peso

    def papeles(self, mochila):
        papeles=0
        for elem in mochila:
            papeles += elem[0]
        return papeles

    def calculaRec(self, cantidad, nivel, mochila, mochilaCand):
        if nivel == self.niveles:
            #print ("Caso base", mochilaCand)
            
            pCand= self.peso(mochilaCand)
            pMochila= self.peso(mochila)
            if pCand > cantidad:
                return mochila
            if pCand > pMochila:
                #mochila= mochilaCand
                return mochilaCand
            else:
                if pCand == pMochila:
                    nCand= self.papeles(mochilaCand)
                    nMochila= self.papeles(mochila)
                    if nCand < nMochila:
                        #mochila= mochilaCand
                        return mochilaCand
            return mochila
        else:
            #print ("Caso recursivo")
            pesoCand = self.peso(mochilaCand)
            maxCheques= int((cantidad - pesoCand) / self.cheques[nivel]) 
            temp = mochilaCand.copy()
            for i in range(maxCheques+1):
                #reset(nivel, mochilaCand)                                
                mochilaCand.append((i, self.cheques[nivel]))
                mochila = self.calculaRec(cantidad, nivel + 1, mochila, mochilaCand)
                mochilaCand= temp.copy()
        return mochila



    

    def calcula(self,cantidad):
        mochila= []
        mochilaCand = []
        self.niveles= len(self.cheques)
        mochila= self.calculaRec(cantidad, 0, mochila, mochilaCand)
        return mochila
    
    





    


