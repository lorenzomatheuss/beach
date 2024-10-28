# utils/helpers.py

import os

def log_to_file(message, filepath='data/logs/bot_log.txt'):
    """
    Função para gravar mensagens de log em um arquivo.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'a') as file:
        file.write(message + "\n")
