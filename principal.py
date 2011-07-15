#!/usr/bin/python

import os
 
class ambprincipal():

  arquivos = []

  def __init__(self):
    lstArquivo = self.buscaArquivos()
    self.listaArquivos(lstArquivo)

  '''Retorna uma lista com os nomes dos arquivos em uma determinada pasta (servidor)'''	        
  def buscaArquivos(self):
    self.arquivos = os.listdir(os.path.expanduser('~/Documents/Projetos/AmbienteCol'))
    return self.arquivos

  def listaArquivos(self, lstArquivo):
    i = 1;
    for arquivo in lstArquivo:
      if arquivo[-4::] == '.txt':
        print "Arquivo numero", i, ":", arquivo
        i += 1
 
if __name__ == "__main__":
  ambprincipal()
  
