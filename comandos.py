import speech_recognition as sr
from gpiozero import LED
from selenium import webdriver
import os
import time
import re

def lista(text):
    os.system("aplay el.wav")
    rojo.on()
    verde.on()
    time.sleep(1)
    
    os.system("aplay al.wav")
    rojo.off()
    verde.off()
    time.sleep(1) 

    os.system("aplay rm.wav")
    os.system("aplay pista.wav")
    time.sleep(1)

    os.system("aplay dh.wav")
    os.system("python tiempo.py")
    
def musica(text):
    os.system("python YTMusic.py " + text)
    
def comandos(text):
    
    #¡Activar nova Nova!
    if text =="Hola Nova":
        os.system("aplay bn.wav")
    #Suspender Nova (Pendiente)
    
    #Presentación de nova
    if text == "preséntate Nova":
        os.system("aplay introduccion.wav")
    
    #Lista de lo que puede realizar
    if text =="Qué puedes hacer":
        os.system("aplay te.wav")
        lista(text)
    
    #Inicio de las instrucciones a realizar 
    if "Reproduce" in text:
       # text.split(" ",text)
        #print(re.split(r'\s+',text))
        palabras_array = re.split(r'\s+',text)
        cancion = ""
        #print(cancion_array)
        for palabra in palabras_array:
            if palabra != "Reproduce":
                cancion += palabra + " "      
        print(cancion)
        musica("\"" + cancion + "\"")
        os.system("aplay rcey.wav")  
    
    #Apagar musica
    if text == "Apagar música":
        os.system("pkill -3 chromium") 
        
    if text == "encender estelar":
        os.system("aplay ee.wav")
        rojo.on()
        verde.on()
                
    if text == "Apagar estelar":
        os.system("aplay ea.wav")
        rojo.off()
        verde.off()
        
    if text == "encender estelar 1":
        os.system("aplay e1e.wav")
        rojo.on()
                
    if text == "Apagar estelar 1":
        os.system("aplay e1a.wav")
        rojo.off()
    
    if text == "encender estelar 2":
        os.system("aplay e2e.wav")
        verde.on()
                
    if text == "Apagar estelar 2":
        os.system("aplay e2a.wav")
        verde.off()

        
    if text == "Cuál es la hora":
         os.system("python tiempo.py")
                   
    if text == "prueba":
        os.system('espeak -v mb-vz1 -s 130 "hola, puedo escucharte"')

rojo = LED(17)
verde = LED(27)

r=sr.Recognizer()
print(sr.Microphone.list_microphone_names())
while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
    # r.energy_threshold()
        print("di algo: ")
        audio= r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-MX")
            print(text)
            comandos(text)
        except:
            print("lo siento, no te entendi")
            os.system("aplay lsnte.wav")
#def opciones(TEXTO):
