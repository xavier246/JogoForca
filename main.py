import pygame
import random
width = 1000
height = 800
size = (width, height)


def verificar_letra(evento):
	if evento.key==ord('a'):
		return 'a'
	if evento.key==ord('b'):
		return 'b'
	if evento.key==ord('c'):
		return 'c'
	if evento.key==ord('d'):
		return 'd'
	if evento.key==ord('e'):
		return 'e'
	if evento.key==ord('f'):
		return 'f'
	if evento.key==ord('g'):
		return 'g'
	if evento.key==ord('h'):
		return 'h'
	if evento.key==ord('i'):
		return 'i'
	if evento.key==ord('j'):
		return 'j'
	if evento.key==ord('k'):
		return 'k'
	if evento.key==ord('l'):
		return 'l'
	if evento.key==ord('m'):
		return 'm'
	if evento.key==ord('n'):
		return 'n'
	if evento.key==ord('o'):
		return 'o'
	if evento.key==ord('p'):
		return 'p'
	if evento.key==ord('q'):
		return 'q'
	if evento.key==ord('r'):
		return 'r'
	if evento.key==ord('s'):
		return 's'
	if evento.key==ord('t'):
		return 't'
	if evento.key==ord('u'):
		return 'u'
	if evento.key==ord('v'):
		return 'v'
	if evento.key==ord('w'):
		return 'w'
	if evento.key==ord('x'):
		return 'x'
	if evento.key==ord('y'):
		return 'y'
	if evento.key==ord('z'):
		return 'z'







palavras=[]
dicas=[]
letras_digitadas=[]
acertos=0
erros=0
arquivo=open('palavras.txt','r')
for linha in arquivo:
	elementos=linha.split(',')
	palavras.append(elementos[0].rstrip("\n").lower())
	dicas.append(elementos[1].rstrip("\n"))

indice=random.randint(0,len(palavras)-1)
pygame.display.set_caption("Prepare-se para o Jogo da Forca!")
janela = pygame.display.set_mode(size)
forca=pygame.image.load("imagens/forca.png")
cabeca=pygame.image.load("imagens/cabeca.png")
corpo=pygame.image.load("imagens/corpo.png")
braco_e=pygame.image.load("imagens/braco_e.png")
braco_d=pygame.image.load("imagens/braco_d.png")
perna_e=pygame.image.load("imagens/perna_e.png")
perna_d=pygame.image.load("imagens/perna_d.png")
txt='Dica: '+dicas[indice]
pygame.font.init()                                
fonte=pygame.font.get_default_font()              
fontesys=pygame.font.SysFont(fonte, 30)           
txttela = fontesys.render(txt, 1, (255,255,255))  
janela.blit(txttela,(50,50))
txt='Digite uma letra: '
pygame.font.init()                                
fonte=pygame.font.get_default_font()              
fontesys=pygame.font.SysFont(fonte, 30)           
txttela = fontesys.render(txt, 1, (255,255,255))  
janela.blit(txttela,(50,90))
posica_traco=230
for i in range(len(palavras[indice])):
	txt='__'
	pygame.font.init()                                
	fonte=pygame.font.get_default_font()              
	fontesys=pygame.font.SysFont(fonte, 30)           
	txttela = fontesys.render(txt, 1, (255,255,255))  
	janela.blit(txttela,(posica_traco,90))
	posica_traco=posica_traco+30
janela.blit(forca,(20,150))
pygame.display.flip()
while acertos<=len(palavras[indice]):
	if acertos==len(palavras[indice]):
		txt1='Parabens, voce ganhou!!!!'
		pygame.font.init()                                
		fonte=pygame.font.get_default_font()              
		fontesys=pygame.font.SysFont(fonte, 30)           
		txttela = fontesys.render(txt1, 1, (255,255,255))  
		janela.blit(txttela,(posicao_letra,690))
		pygame.display.flip()
		pygame.time.wait(2000)
		acertos=acertos+1
	elif erros==6:
		txt1='Voce perdeu!!!!'
		pygame.font.init()                                
		fonte=pygame.font.get_default_font()              
		fontesys=pygame.font.SysFont(fonte, 30)           
		txttela = fontesys.render(txt1, 1, (255,255,255))  
		janela.blit(txttela,(posicao_letra,690))
		janela.blit(braco_d,(425,580))
		pygame.display.flip()
		pygame.time.wait(5000)
		exit()
	else:	
		txt1=''
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.quit()
				exit()
			if evento.type == pygame.KEYDOWN:
				posicao_letra=235
				txt1=verificar_letra(evento)
				if letras_digitadas.count(txt1)==0:
					letras_digitadas.append(txt1)
					indice_letra=99
					for i in range(len(palavras[indice])):
						if palavras[indice][i] == txt1:
							posicao_letra=235
							acertos=acertos+1
							posicao_letra=posicao_letra+30*i
							indice_letra=i
							txt_escrever=txt1.upper()
							pygame.font.init()                                
							fonte=pygame.font.get_default_font()              
							fontesys=pygame.font.SysFont(fonte, 30)           
							txttela = fontesys.render(txt_escrever, 1, (255,255,255))  
							janela.blit(txttela,(posicao_letra,90))
							pygame.display.flip()
					if indice_letra==99:
						erros=erros+1
					if erros==1:
						janela.blit(cabeca,(350,300))
						pygame.display.flip()
					elif erros==2:
						janela.blit(corpo,(380,404))
						pygame.display.flip()
					elif erros==3:
						janela.blit(braco_e,(295,404))
						pygame.display.flip()
					elif erros==4:
						janela.blit(braco_d,(425,404))
						pygame.display.flip()
					elif erros==5:
						janela.blit(perna_e,(325,580))
						pygame.display.flip()

					
					
					
					
					
					
					
					


	

