import time

import pyautogui #para clicar
from PIL import ImageGrab  #vai pegar imagens da tela
#vai ficar tirando fotos e comparando as imagens quando aparecer o objeto//descobrindo pela cor///dai faz algo
cor_fundo= (32,33,36)
cor_dino=(172,172,172)
cor_inimigo=(172,172,172)

#310 430  388 430
#310 475  388 475
def capturar_tela():
    screen = ImageGrab.grab() #printou
    return screen   #returnando a image

def detectar(image):   #aqui vai pegar uma parte dos pixeis
    for x in range(310, 388):
        for y in range(430, 475):
            color = screen.getpixel((x, y))

            if color == (172,172,172):
                return True
def pular():
    pyautogui.press("space")
time.sleep(2)
pular()
while True:           
    screen = capturar_tela()
    
    if detectar(screen):
        pular()