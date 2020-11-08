class busca_Binaria():
        def __init__(self, lista, elemento):
                self.lista = lista
                self.elemento = elemento
        
        def buscar(self):
                try:
                        self.minimo = 0
                        self.maximo = len(self.lista) - 1
                        self.encontrado = False
                    
                        while self.minimo <= self.maximo and not self.encontrado:
                            self.meio_lista = (self.minimo + self.maximo)//2

                            if self.lista[self.meio_lista] == self.elemento:
                                self.encontrado = True
                                
                            elif self.elemento < self.lista[self.meio_lista]:
                                self.maximo = self.meio_lista - 1

                            else:
                                self.minimo = self.meio_lista + 1
                      
                        return self.encontrado
                finally:
                        self.mostrar()          

        def mostrar(self):
                
                if self.encontrado == True:
                        print('O elemento {} foi encontrado na lista!'.format(self.elemento))
                else:
                        print('O elemento {} não foi encontrado na lista!'.format(self.elemento))
lista = []

for x in range(1, 16):
    lista.append(x)

lista.sort()

print(lista)


pesquisa = busca_Binaria(lista, 20)
pesquisa.buscar()

pesquisa = busca_Binaria(lista, 15)
pesquisa.buscar()
