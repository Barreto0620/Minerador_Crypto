import pyautogui
import time

# Aguarda 3 segundos antes de capturar a posição
time.sleep(3)

# Obtém a posição atual do cursor do mouse
x, y = pyautogui.position()

print(f"A posição atual do mouse é: X={x}, Y={y}")
