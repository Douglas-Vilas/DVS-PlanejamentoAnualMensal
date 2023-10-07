import datetime
import time

# Dicionário para armazenar os eventos
eventos = {}

# Função para adicinar um evento
def adicionar_evento(nome, mes, dia):
    ano_atual = datetime.date.today().year
    eventos[nome] = datetime.date(ano_atual, mes, dia)

# Função para remover um evento
def remover_evento(nome):
    if nome in eventos:
        del eventos[nome]

# Função para verificar os eventos 
def verificar_eventos():
    hoje = datetime.date.today()
    for nome, data in list(eventos.items()): # Usei list() para evitar erros de modificação durante a interação
        if data < hoje:
            # Atualiza o ano do evento para o próximo ano
            eventos[nome] = datetime.date(hoje.year + 1, data.month, data.day)
        elif data == hoje:
            print(f"Hoje é o {nome}!")

# Adicionando alguns eventos
adicionar_evento("Lei da Libras", 4, 24)
adicionar_evento("Dia Nacional do Surdo", 9, 26)
adicionar_evento("Dia Teste", 10, 7)

while True:
    verificar_eventos()
    time.sleep(86400) # Esperar por um dia
