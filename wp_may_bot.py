# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 15:29:41 2022

@author: maiury.nascimento
"""

from time import sleep
from whatsapp_api import WhatsApp

# Inicializar o whatsapp
wp = WhatsApp()

# Esperar que enter seja pressionado
input("Pressione enter apos escanear o QR Code")

wp.search_contact('MAYRAVILHOSA')
 
message = "Oi, obrigada por comparecer hoje"
 
wp.search_contact('MAYRAVILHOSA')

sleep(2)
 
wp.send_message(message)
 
 #Esperar 10 segundaos e fechar
sleep(10)
wp.driver.close()