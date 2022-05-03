# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:23:57 2022

@author: maiury.nascimento
"""

# Importar pacotes necessarios
from time import sleep
from whatsapp_api import WhatsApp

# Inicializar o whatsapp
wp = WhatsApp()

# Esperar que enter seja pressionado
input("Pressione enter apos escanear o QR Code")

# Lista de nomes ou nomeros de telefone a serem pesquisados
# IMPORTANTE: O nome deve ser nao ambiguo pois ele retornara o primeiro resultado
nomes_palavras_chaves = ['MAYRAVILHOSA']

# Lista dos nomes que vou me referir na mensagem
# primeiros_nomes = ['Luciano', 'Aline', 'Beatriz', 'Joao', 'Maria', 'Pedro']

primeiros_nomes = [n.split(' ')[0] for n in nomes_palavras_chaves]

# Loop para mandar mensagens para os clientes
for primeiro_nome, nome_pesquisar in zip(primeiros_nomes, nomes_palavras_chaves):
    wp.search_contact(nome_pesquisar)
    
    # Mensagem a ser enviada
    mensagem = f"Olá, {primeiro_nome}. Seja bem vinde!"

    # Enviar mensagem
    sleep(2)
    wp.send_message(mensagem)
    
    # Esperar 10 segundos e fechar
    sleep(10)
    wp.driver.close()



