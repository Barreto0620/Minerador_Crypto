# coding: utf-8
import pyautogui
import time
import tkinter as tk
from datetime import datetime

pyautogui.PAUSE = 1  # Pausa de 1 segundo entre os comandos

# Função para exibir mensagens temporárias
def exibir_mensagem(mensagem):
    root = tk.Tk()
    root.title("Aviso")
    root.geometry("300x100")
    
    label = tk.Label(root, text=mensagem, font=("Arial", 12), pady=20)
    label.pack()
    
    root.after(3000, root.destroy)  # Fecha a janela após 3 segundos
    root.mainloop()  # Mantém a janela aberta corretamente

# Inicializa o contador de execuções
execucoes = 0

while True:
    try:
        inicio = time.time()  # Marca o início da execução
        
        # Exibe mensagem de início
        exibir_mensagem("Início da Automação")

        # Automação da Primeira Conta (Principal)
        pyautogui.hotkey('win')
        pyautogui.write('FreeBitco.in')
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.hotkey('win', 'up')
        time.sleep(5)
        for _ in range(3):
            pyautogui.click(x=1358, y=702)
        time.sleep(5)
        pyautogui.click(x=550, y=493)
        time.sleep(3)
        pyautogui.click(x=677, y=570)
        time.sleep(10)
        pyautogui.press('esc')
        time.sleep(5)
        pyautogui.hotkey('alt', 'f4')

        # Calcula o tempo total da execução
        fim = time.time()
        tempo_execucao = fim - inicio

        # Log da Primeira Conta
        execucoes += 1
        with open("minerador.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"PRINCIPAL: Execução {execucoes} realizada com sucesso em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Tempo: {tempo_execucao:.2f} segundos\n")

        # Exibe mensagem de fim
        exibir_mensagem(f"Fim da Automação\nTempo total: {tempo_execucao:.2f} segundos")

        # Aguardar 1 hora (3600 segundos) antes de repetir o processo
        time.sleep(3600)
        
    except Exception as e:
        # Grava qualquer erro no log
        with open("minerador.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"Erro na execução {execucoes + 1}: {str(e)} em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
