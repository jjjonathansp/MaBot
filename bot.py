# -*- coding: utf-8 -*-

import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time
from datetime import datetime, date, timedelta
import calendar
import os, shutil
import random



TOKEN = '597540172:AAFiMDuQVG60AjB_EJvRnv2HWeznopqhZos' # Nuestro tokken del bot (el que @BotFather nos dió).
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        cid = m.chat.id # Almacenaremos el ID de la conversación.
        #print ("[" + str(cid) + "]: " + m.text) # Y haremos que imprima algo parecido a esto -> [52033876]: /start
        #print ("[" + str(m.from_user.username) + "] ") # Y haremos que imprima algo parecido a esto -> [52033876]: /start
        #print('id-chat:'+str(cid)+' usuario:'+str(m.from_user.username)+' mensaje:'+m.text)
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
#############################################
#Funciones
@bot.message_handler(commands=['problema'])
def command_problema(m):
    cid = m.chat.id
    desde = m.from_user.username
    bot.send_sticker( cid, 'CAADBAADlgUAArVKywFuQm1R0ewLhAI')

@bot.message_handler(commands=['huevos'])
def command_huevos(m):
    cid = m.chat.id
    desde = m.from_user.username
    bot.send_sticker( cid, 'CAADBAADlQUAArVKywHTzJa3Zg7N0gI')

@bot.message_handler(commands=['money'])
def command_money(m):
    cid = m.chat.id
    desde = m.from_user.username
    try:
	    bot.send_video( cid, open('gifs/imanol.mp4', 'rb'))
    except Exception as e:
	    bot.send_message( cid, 'Pidiendo prestamo a Imanol OMG...')

@bot.message_handler(commands=['imanol']) 
def command_soydios(m):
    cid = m.chat.id
    desde = m.from_user.username
    try:
        bot.send_video( cid, open('gifs/imimanol.mp4', 'rb'))
    except Exception as e:
        bot.send_message( cid, 'Imanol no esta disponible')

@bot.message_handler(commands=['lohepetado'])
def command_liada(m):
    cid = m.chat.id
    desde = m.from_user.username
    try:
        bot.send_video( cid, open('gifs/liada.mp4', 'rb'))
    except Exception as e:
	    bot.send_message( cid, 'La he liao gente!')

@bot.message_handler(commands=['rayao'])
def command_rayao(m):
    cid = m.chat.id
    desde = m.from_user.username
    try:
        bot.send_video( cid, open('gifs/rayao.mp4', 'rb'))
    except Exception as e:
	    bot.send_message( cid, 'La he liao gente!')

@bot.message_handler(commands=['galder'])
def command_galder(m):
    cid = m.chat.id
    desde = m.from_user.username
    bot.send_message( cid, 'Es mala gente, no os fieis de él...')

@bot.message_handler(commands=['dieginho'])
def command_dieginho(m):
    cid = m.chat.id
    desde = m.from_user.username
    bot.send_message( cid, 'Tsss callaros, que llega el gerente')
	
@bot.message_handler(commands=['yao'])
def command_yao(m):
    cid = m.chat.id
    desde = m.from_user.username
    bot.send_sticker( cid, 'BQADBAADDgUAApv7sgABzHBUSmMoLrsC')

@bot.message_handler(commands=['misterio'])
def command_misterio(m):
    cid = m.chat.id
    bot.send_voice( cid, open( 'sonidos/WTF.ogg', 'rb'))

@bot.message_handler(commands=['volo'])
def command_volo(m):
    cid = m.chat.id
    bot.send_voice( cid, open( 'sonidos/volo.ogg', 'rb'))

@bot.message_handler(commands=['sparta'])
def command_sparta(m):
    cid = m.chat.id
    bot.send_voice( cid, open( 'sonidos/sparta.ogg', 'rb'))

@bot.message_handler(commands=['gay'])
def command_gay(m):
    cid = m.chat.id
    bot.send_voice( cid, open( 'sonidos/gay.ogg', 'rb'))

@bot.message_handler(commands=['subnormal'])
def command_subnormal(m):
    cid = m.chat.id
    bot.send_voice( cid, open( 'sonidos/subnormal.mp3', 'rb'))


@bot.message_handler(commands=['roto'])
def command_roto(m):
    cid = m.chat.id
    bot.send_photo( cid, open( 'roto2.png', 'rb'))

@bot.message_handler(commands=['tonto'])
def command_tonto(m):
    cid = m.chat.id
    bot.send_message( cid, "'Cuando un tonto sigue un camino, el camino se acaba pero el tonto sigue.'\nby MABot, 2015.")
    bot.send_sticker( cid, 'BQADBAADqgQAAhIwUAQ22UqcGHnjuwI')

@bot.message_handler(commands=['leviosa'])
def command_leviosa(m):
    cid = m.chat.id
    bot.send_sticker( cid, 'BQADAgADFQADlQSwBXpE-yUfhXUOAg')
    bot.send_voice( cid, open( 'sonidos/leviosa.ogg', 'rb'))

@bot.message_handler(commands=['tontopasiempre'])
def command_tontopasiempre(m):
    cid = m.chat.id
    bot.send_voice( cid, open( 'sonidos/tontopasiempre.ogg', 'rb'))

@bot.message_handler(commands=['hermione'])
def command_stopit(m):
    cid = m.chat.id
    bot.send_sticker( cid, 'BQADAgADEwADlQSwBTg5G6s7CLNXAg')
    bot.send_voice( cid, open( 'sonidos/hermione.ogg', 'rb'))

@bot.message_handler(commands=['snape'])
def command_snape(m):
    cid = m.chat.id
    bot.send_sticker( cid, 'BQADAgADGQADlQSwBbZCafQNvAPlAg')
    bot.send_voice( cid, open( 'sonidos/snape.ogg', 'rb'))

@bot.message_handler(commands=['cage'])
def command_cage(m):
    cid = m.chat.id
    numeroRandom=random.randint(1,14)
    bot.send_photo( cid, open( 'cage/'+str(numeroRandom)+'cage.jpg', 'rb'))

@bot.message_handler(commands=['omg'])
def command_omg(m):
    cid = m.chat.id
    bot.send_sticker( cid,'BQADBAADrAUAApv7sgABKxDLwbtomX0C')
    
@bot.message_handler(commands=['hagay'])
def command_hagay(m):
    cid = m.chat.id
    bot.send_sticker( cid,'BQADBAADcAQAApv7sgABhhsOY--uNgUC')


@bot.message_handler(commands=['pideperdon'])
def command_pideperdon(m):
    cid = m.chat.id
    valorperdon = str(m.text).replace('/pideperdon','')
    bot.send_message( cid, valorperdon+' pide perdon por tu retraso! pero ya!')
	
@bot.message_handler(commands=['poltergeist'])
def command_pideperdon(m):
    cid = m.chat.id
    valorperdon = str(m.text).replace('/pideperdon','')
    bot.send_message( cid, 'No es mi poltergeist')

@bot.message_handler(commands=['entrega'])
def command_euskal(m):
    cid = m.chat.id
    fecha1= datetime.now()
    fecha2=datetime(2018,12,20,16,00,0,00000)
    diff=fecha2-fecha1
    hours = diff.days * 24 + diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60
    if hours>24:
        bot.send_message( cid, 'Cuenta atras para la entrega:\n'+str(diff))
    else:
        bot.send_message( cid, 'BRACE YOURSELVES, ENTREGA IS COMING: '+str(hours)+' horas, '+str(minutes)+' minutos y '+str(seconds)+' segundos' )


@bot.message_handler(commands=['perdon'])
def command_perdon(m):
    cid = m.chat.id
    desdeperdon = m.from_user.username
    bot.send_message( cid, str(desdeperdon)+' ha pedido perdon por su retraso')

@bot.message_handler(commands=['perfect'])
def command_perfect(m):
    cid = m.chat.id
    idmensaje = m.message_id
    try:
        bot.send_video( cid, open('ok.gif.mp4', 'rb'))
    except Exception as e:
        bot.send_message(cid, 'Pos vale...','true',idmensaje)
    
#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.