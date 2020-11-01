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
                        print('O elemento {} foi encontrado na lista'.format(self.elemento))
                else:
                        print('Elemento não pertence a lista')
    

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

pesquisa = busca_Binaria(lista, 20)
pesquisa.buscar()
