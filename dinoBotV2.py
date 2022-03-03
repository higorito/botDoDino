import time
#este codigo nao ta muito otimizado//ainda perde para o outro v1

import pyautogui #para clicar
from PIL import ImageGrab  #vai pegar imagens da tela
#vai ficar tirando fotos e comparando as imagens quando aparecer o objeto//descobrindo pela cor///dai faz algo
cor_fundo= (32,33,36)
cor_dino=(172,172,172)
cor_inimigo=(172,172,172)
#X1=310
#X2=388
X=310.0

#310 430  388 430
#310 475  388 475
def capturar_tela():
    screen = ImageGrab.grab() #printou
    return screen   #returnando a image

def detectar(image):   #A DIFERENÇA para o outro é que pega pixel por pixel e compara com o anterior
    aux_color = screen.getpixel((int(X), 430))
    for x in range(int(X), int(X+5)):
        for y in range(430, 450):  #diminui aq pa tava pegando no chao
            color = screen.getpixel((x, y))

            if color !=aux_color:
                return True
            else:
                aux_color = color
def pular():
    global X
    pyautogui.press("space")
    X+=0.4

time.sleep(2)
pular()
while True:           
    screen = capturar_tela()
    
    if detectar(screen):
        pular()