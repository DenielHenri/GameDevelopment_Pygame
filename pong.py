import pygame
import random

#Inicializar a biblioteca e configurar o tamanho da nossa tela
pygame.init()

#Configuração da janela
LARGURA_TELA = 800
ALTURA_TELA = 600

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pong!")

#cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

#-------- Constante em jogo --------
LARGURA_RAQUETE = 15
ALTURA_RAQUETE = 100
VELOCIDADE_RAQUETE = 7

RAIO_BOLA = 10
VELOCIDADE_BOLA_X = 5
VELOCIDADE_BOLA_Y = 5

#-------- Classes do jogo --------
class Raquete:
    # O 'construtor': é chamado quando criamos uma Raquete
    # 'self' se refere ao próprio objeto
    def __init__(self, x, y):
        # O 'rect' armazena a posição (x,y) e o tamanho
        self.rect = pygame.Rect(x, y, LARGURA_RAQUETE, ALTURA_RAQUETE)

    #Método utilizado para desenhar a raquete 
    def desenhar(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect)
    
    #Método para mover a raquete
    def mover(self, tecla_cima, tecla_baixo):
        #Captura um dicionário de todas as teclas que estão pressionadas
        teclas = pygame.key.get_pressed()

        #Verificar se a tecla foi pressionada
        if teclas[tecla_cima] and self.rect.top > 0:
            self.rect.y -= VELOCIDADE_RAQUETE

        if teclas[tecla_baixo] and self.rect.bottom < ALTURA_TELA:
            self.rect.y += VELOCIDADE_RAQUETE


class Bola:
    def __init__(self, x, y):
        self.rect = pygame.rect(x - RAIO_BOLA, RAIO_BOLA * 2, RAIO_BOLA * 2)

        #Velocidades/direção para X e Y
        self.vel_x = VELOCIDADE_BOLA_X * random.choice((1, -1))
        self.vel_y = VELOCIDADE_BOLA_Y * random.choice((1, -1))

    def desenhar(self, tela):
        pygame.draw.ellipse(tela, BRANCO, self.rect) #Desenhando um Círculo
    
    def mover(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def verificar_colisao(self, raquete1, raquete2):
        #verificação da colisão com as paredes

        if self.rect.top <= 0 or self.rect.bottom >= ALTURA_TELA:
            self.val_y *= -1 #Inverter a direção da variável minha_bola

        if self.rect.colliderect(raquete1) or self.rect.colliderect(raquete2):
            self.vel_x *= -1 #Inverte a direção X
    

    def resetar(self):
        #Mover a bola de volta para o centro 
        self.rect.x = LARGURA_TELA / 2 - RAIO_BOLA 
        self.rect.y = ALTURA_TELA / 2 - RAIO_BOLA

        self.vel_x *= -1
        self.vel_y = VELOCIDADE_BOLA_Y * random.choice((1, -1))

        pygame.time.delay(500) #0.5 seg

#Criar o fluxo principal

relogio = pygame.time.Clock()
rodando = True


#Criando a raquete 01 a partir da classe raquete
#Posição: 10 Pixels a esquerda, e centralizada na altura
raquete1 = Raquete(10, ALTURA_TELA / 2 - ALTURA_RAQUETE / 2)
raquete2 = Raquete(LARGURA_TELA - LARGURA_RAQUETE - 10, ALTURA_TELA / 2 - ALTURA_RAQUETE / 2)

minha_bola = bola(LARGURA_TELA / 2, ALTURA_TELA / 2)

while rodando:
    #------ 1. Eventos ------
    for event in pygame.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    #-------- 2. Tela --------
    #Criação da Tela (preto)
    tela.fill(PRETO)

    #-------- 2.1 A primeira raquete --------
    raquete1.desenhar(tela)
    raquete2.desenhar
    minha_bola.desenhar(tela)

    #-------- 3. Atualização da Tela --------
    pygame.display.flipp()
    relogio.tick(60)

    #-------- 4. movendo a raquete --------
    raquete1.mover(pygame.K_w, pygame.K_s)
    raquete2.mover(pygame.K_UP, pygame.K_DOWN)
    minha_bola.mover()

    #-------- Verificar solisões --------
    minha_bola.verificar_solisao(raquete1.rect, raquete2.rect)

    if minha_bola.rect.left < 0:
        pontos_j2 += 1
        minha_bola.resetar()

    if minha_bola.rect.right > LARGURA_TELA:
        pontos_
        minha_bola.resetar()


pygame.quit()
