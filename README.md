# Automação com PyAutoGUI para FreeBitco.in  

## Descrição  
Este script em Python utiliza a biblioteca **PyAutoGUI** para automatizar ações relacionadas ao uso do software **FreeBitco.in** no sistema operacional Windows. Ele realiza uma sequência de ações que incluem abrir o programa, executar cliques em áreas específicas da tela e registrar logs sobre cada execução bem-sucedida ou falha em um arquivo de texto.  

O script foi projetado para funcionar em monitores com a resolução de **1920x1080** e o zoom da interface do sistema configurado em **100%**.  

## Requisitos  
- **Python 3.6 ou superior** instalado no sistema.  
- Biblioteca **PyAutoGUI** instalada.  
  - Instalação: `pip install pyautogui`  
- O software **FreeBitco.in** deve estar instalado e configurado no computador para que o script funcione corretamente.  
- Sistema operacional **Windows**.  

## Configuração Inicial  
1. Certifique-se de que o FreeBitco.in está instalado e acessível pelo menu Iniciar do Windows.  
2. Verifique se a resolução do monitor está configurada para **1920x1080** e o zoom do sistema está em **100%**.  
3. Ajuste os parâmetros de coordenadas dos cliques no código para refletirem a posição exata dos elementos de interação em seu sistema. Para localizar as coordenadas:  
   - Execute o seguinte código para capturar as posições do cursor:  
     ```python
     import pyautogui
     import time
     
     time.sleep(5)
     print(pyautogui.position())
     ```  
   - Passe o mouse sobre os elementos e anote as coordenadas fornecidas no console.

## Personalização  
O campo de coordenadas de clique (`pyautogui.click(x, y)`) precisa ser ajustado para refletir as posições específicas no seu computador. Substitua as coordenadas de exemplo fornecidas no script (`x=1910, y=1012` e `x=950, y=762`) pelas coordenadas corretas obtidas conforme descrito acima.  

## Logs  
Todos os resultados das execuções (sucessos ou falhas) são registrados no arquivo `minerador.txt`.  
- Cada execução bem-sucedida será registrada no formato:  
  ```  
  Execução X realizada com sucesso em [DATA e HORA]  
  ```  
- Qualquer erro será registrado no formato:  
  ```  
  Erro na execução X: [DESCRIÇÃO DO ERRO] em [DATA e HORA]  
  ```  

## Estrutura do Script  
1. **Inicialização**: Define uma pausa entre os comandos para evitar problemas de sincronização.  
2. **Execuções Automatizadas**:  
   - Abre o FreeBitco.in via menu Iniciar.  
   - Maximiza a janela e realiza cliques nas áreas definidas.  
   - Fecha o programa ao final de cada ciclo.  
3. **Contador e Log**:  
   - Incrementa o número de execuções realizadas.  
   - Grava os resultados no arquivo de log (`minerador.txt`).  
4. **Intervalo**: Aguarda uma hora (3600 segundos) antes de iniciar novamente.  

## Atenção  
- **Não utilize este script para finalidades que possam infringir os termos de uso de softwares ou serviços.**  
- Certifique-se de que o script seja usado dentro dos limites da ética e da legalidade.  

## Suporte  
Caso encontre problemas ou tenha dúvidas, consulte a [documentação oficial do PyAutoGUI](https://pyautogui.readthedocs.io/) para referência ou ajuste do código.  

---  
Este arquivo README foi criado para orientar a configuração e utilização adequada do script.
