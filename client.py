#!/usr/bin/python

import Pyro.core

import pygtk
pygtk.require("2.0")
import gtk, gtk.glade
 
class interface():
  #lstArquivos = []
  def __init__(self, procedimentos, arvore): 
    self.procedimentos = procedimentos
    self.arvore = arvore
    janela = self.arvore.get_widget('janelaPrincipal')
    self.arvore.signal_autoconnect(self)
    janela.show_all()
    janela.connect("destroy",gtk.main_quit)
    
    gtk.mainloop()    

  def sair(self, widget):
    gtk.main_quit()

  def sobre(self, widget):
    self.about = self.arvore.get_widget('aboutdialog1')
    self.about.show_all() 

  def sairSobre(self, widget):
    self.about.hide()

  def abrir(self, widget):
    self.abrir = self.arvore.get_widget('janelaAbreArquivo')

    #lstArquivos = self.procedimentos.buscaArquivos()
    #Preciso que seja uma lista onde eu possa jogar os itens da lstArquivos e selecionar um - existe??
    telaNomesArquivos = self.arvore.get_widget('treeview1')
    
    self.abrir.show_all()
    
  def abrirArquivo(self, widget):
    self.abrir.hide()
    
    #essa seria a variavel para onde iria o nome do arquivo - o caminho eu deixo fixo mesmo :P
    arquivoParaAbrir = "/home/ubuntu/Documents/Projetos/AmbienteCol/texto.txt"
    
    self.textArea = self.arvore.get_widget('textview1')
    
    #hora de pegar o conteudo do arquivo(1)!
    arq = file(arquivoParaAbrir)
    conteudo = arq.read()    
    abreBuffer = self.textArea.get_buffer()
    abreBuffer.set_text(conteudo)
    
    #apos aberto, deve ser verificado se houve mudancas (a nao ser que esteja bloqueado para outro usuario)

  def sairAbrirArquivo(self, widget):
    self.abrir.hide()

  def salvar(self,widget):
    #essa seria a variavel para onde iria o nome do arquivo - o caminho eu deixo fixo mesmo :P
    arquivoParaAbrir = "/home/ubuntu/Documents/Projetos/AmbienteCol/texto.txt"
    arq = file(arquivoParaAbrir,"w",0)
    salvaBuffer = self.textArea.get_buffer()
    conteudo = salvaBuffer.get_text(*salvaBuffer.get_bounds())
    arq.write(conteudo)
    
if __name__ == "__main__":
  Pyro.core.initClient()
  proc=Pyro.core.getProxyForURI('PYRONAME://:Default.AmbienteColaborativo')  

  arvoreDeWidgets = gtk.glade.XML('InterfaceAmbiente.glade')
  interface(proc, arvoreDeWidgets)
