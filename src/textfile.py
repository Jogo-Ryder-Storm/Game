# Imports
import pygame, sys
from pygame.locals import *


class TextFile():
    def __init__(self, fileName):
       self.file = fileName

    def writePlayer(self, name, time, life):
        arquivo = open(self.file, "w")
        
        arquivo.write(name)
        arquivo.write(", ")
        arquivo.write(time)
        arquivo.write(", ")
        arquivo.write(life)
                
        arquivo.close()
    
    def readFile(self):
        # Abrir o arquivo em modo de append
        arquivo = open(self.file, "r")

        conteudo = arquivo.read()
        
        # Fechar o arquivo
        arquivo.close()

        # Exibir o conteúdo lido
        #print(conteudo)