# coding: utf-8
# Configuração de Monitor - 1920x1080 *
# Configuração da Página - Zoom 100% *

import pyautogui
import time

pyautogui.PAUSE = 1  # Pausa de 1 segundo entre os comandos

# Inicializa o contador de execuções
execucoes = 0

while True:  # Loop infinito
    try:
        # Executando as ações
        pyautogui.hotkey('win')  # Abre o menu Iniciar
        pyautogui.write('FreeBitco.in')  # Digita "FreeBitco.in"
        pyautogui.press('enter')  # Pressiona Enter para abrir
        time.sleep(5)  # Aguarda 5 segundos
        pyautogui.hotkey('win', 'up')  # Maximiza a janela
        time.sleep(5)  # Aguarda 5 segundos
        for _ in range(3):  # Repete o clique 3 vezes
            pyautogui.click(x=1910, y=1012)
        time.sleep(5)  # Aguarda 5 segundos para a página carregar
        pyautogui.click(x=950, y=762)  # Clique nas coordenadas específicas
        time.sleep(5)  # Aguarda 5 segundos
        pyautogui.press('esc')  # Pressiona a tecla Esc
        time.sleep(5)  # Aguarda 5 segundos
        pyautogui.hotkey('alt', 'f4')  # Fecha a janela

        # Incrementa o contador antes de gravar no log
        execucoes += 1
        with open("minerador.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"Execução {execucoes} realizada com sucesso em {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

        # Aguardar 1 hora (3600 segundos) antes de repetir o processo
        time.sleep(3600)  # Aguardar 1 hora
    except Exception as e:
        # Grava qualquer erro no log
        with open("minerador.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"Erro na execução {execucoes + 1}: {str(e)} em {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
