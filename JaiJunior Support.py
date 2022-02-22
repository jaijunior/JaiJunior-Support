from tkinter import INSERT
import webbrowser
import PySimpleGUI as sg
import subprocess
import os, sys

largura = 17
altura = 2
sg.theme('DarkAmber')   # Add a touch of color

# All the stuff inside your window.
layout = [  
            [sg.Button('INTERNET',size=(largura,altura),) , sg.Button('DNS',size=(largura,altura))],
            [sg.Button('DISCO',size=(largura,altura)), sg.Button('SCAN',size=(largura,altura))],
            [sg.Button('LIMPAR',size=(largura,altura)),sg.Button('REMOVER ATUALIZAÇÕES 65/70',size=(largura,altura))],
            [sg.Button('BACKUP',size=(36,2),),],
            [sg.Button('SAIR',size=(36,1),button_color='#FFAAAA'),],            
            [sg.Text('Desenvolvido por: Jairo Nonato Júnior')],
            [sg.Text('GitHub: JaiJunior', enable_events=True, key='github')]
            ],

# Create the Window
window = sg.Window('JaiJunior Support', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'SAIR': # if user closes window or clicks cancel
        break
    if event == 'INTERNET':
        subprocess.run('ipconfig /release',shell=True)
        subprocess.run('ipconfig /renew',shell=True)
        sg.popup_ok('Processo Finalizado')

    if event == 'DNS':
        subprocess.run('ipconfig /flushdns', shell=True)
        sg.popup_ok('Processo Finalizado')
    if event == 'DISCO':
        subprocess.run('chkdsk /f',shell=True)                
        window.bring_to_front()
        sg.popup_ok('Processo Finalizado')
    if event == 'SCAN':
        subprocess.run('sfc /scannow',shell=True)
        sg.popup_ok('Processo Finalizado')
    if event == 'LIMPAR':
        subprocess.run('DEL /F /S /Q %HOMEPATH%\Config~1\Temp\*.*',shell=True)
        subprocess.run('DEL /F /S /Q C:\WINDOWS\Temp\*.* ',shell=True)
        subprocess.run('DEL /F /S /Q C:\WINDOWS\Prefetch\*.*',shell=True)
        subprocess.run('DEL "%WINDIR%\Tempor~1\*.*" /F /S /Q',shell=True)
        subprocess.run('RD /S /Q "%HOMEPATH%\Config~1\Temp"',shell=True)
        subprocess.run('MD "%HOMEPATH%\Config~1\Temp"',shell=True)
        subprocess.run('RD /S /Q C:\WINDOWS\Temp\ ',shell=True)
        subprocess.run('MD C:\WINDOWS\Temp',shell=True)
        subprocess.run('RD /S /Q C:\WINDOWS\Prefetch\ ',shell=True)
        subprocess.run('MD C:\WINDOWS\Prefetch',shell=True)
        sg.popup_ok('Processo Finalizado') 
        
        
    if event == 'REMOVER ATUALIZAÇÕES 65/70':
        subprocess.run('wusa /uninstall /kb:5005565', shell=True) 
        subprocess.run('wusa /uninstall /kb:50006670', shell=True)
        sg.popup_ok('Processo Finalizado') 

    if event == 'BACKUP':
        pasta = sg.popup_get_folder('Escolha a Pasta Para Backup')
        subprocess.run(f'7z a -t7z  "\\\suporte03\PROGRAMAS\BKP\%username%_%date:~6,4%-%date:~3,2%_%date:~0,2%" "{pasta}"', shell=True)                  
        sg.popup_ok('Processo Finalizado') 

window.close()