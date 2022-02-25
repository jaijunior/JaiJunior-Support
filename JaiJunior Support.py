from tkinter import INSERT
import webbrowser
import PySimpleGUI as sg
import subprocess
import os, sys

# Layouts
def window1():
    largura = 17
    altura = 2
    sg.theme('LightGrey2')  
    layout = [  
                [sg.Button('INTERNET',size=(largura,altura),) , sg.Button('DNS',size=(largura,altura))],
                [sg.Button('DISCO',size=(largura,altura)), sg.Button('SCAN',size=(largura,altura))],
                [sg.Button('LIMPAR',size=(largura,altura)),sg.Button('REMOVER ATUALIZAÇÕES 65/70',size=(largura,altura))],
                [sg.Button('BACKUP',size=(largura,altura)),sg.Button('INSTALAR PROGRAMA', size=(largura,altura))],
                [sg.Button('SAIR',size=(36,1), focus=True),],            
                [sg.Text('Desenvolvido por: Jairo Nonato Júnior \nVersão: 0.0.3')],
                [sg.Text('GitHub: JaiJunior', enable_events=True, key='github')]
                ],
    return sg.Window('JaiJunior Support',layout, finalize=True)

def instalar():
    altura = 2
    largura= 15
    layout = [
        [sg.Text('COMUNS', size=(largura, altura)), sg.Text('TRATAMENTO DE IMAGEM', size=(largura, altura)), sg.Text('UTILITÁRIOS', size=(largura,altura))],
        [sg.Check('Firefox', key='FF', size=(largura, altura)), sg.Check('GIMP', key='GIMP',size=(largura,altura)), sg.Check('Java jre8', key='JAVA8', size=(largura,altura))],
        [sg.Check('Google Chrome', key='GC',size=(largura,altura))],
        [sg.Check('Winrar',  key='WR')],
        [sg.Check('MS Office',  key='MO')],
        [sg.Check('OnlyOffice',  key='OO')],
        [sg.Check('Adobe Reader',  key='AR')],
        [sg.Check('Driver Booster', key='DB')],
        [sg.Check('MalwareBytes',  key='MB')],
        [sg.Check('Zoom',  key='ZM')],
        [sg.Check('MS Teams',  key='MT')],
        [sg.Button('Instalar'),sg.Button('Voltar')]        
    ]
    return sg.Window('JaiJunior Support - INSTALAR PROGRAMAS',layout, finalize=True)


# JANELAS PRINCIPAIS

janela1 = window1()
janela2 = None

# Loop de Leitura de Eventos
while True:
    window, event, values = sg.read_all_windows()
    #jANELA VAI VOLTA E FECHA
    if window == janela1 and event == sg.WIN_CLOSED or event == 'SAIR': # if user closes window or clicks cancel
        break
    if window == janela1 and event == 'INSTALAR PROGRAMA':
        janela2 = instalar()
        janela1.hide()
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    
    # EVENTOS DA PAGINA PRINCIPAL
    if event == 'INTERNET':
        subprocess.run('ipconfig /release',shell=True)
        subprocess.run('ipconfig /renew',shell=True)
        sg.popup_ok('Processo Finalizado')

    if event == 'DNS':
        subprocess.run('ipconfig /flushdns', shell=True)
        sg.popup_ok('Processo Finalizado')
    if event == 'DISCO':
        subprocess.run('chkdsk /f',shell=True)                
        window1.bring_to_front()
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
        if pasta =='':
            sg.popup_ok('Insira uma pasta válida\nProcesso Finalizado')
        else:
            subprocess.run(f'7z a -t7z  "\\\suporte03\PROGRAMAS\BKP\%username%_%date:~6,4%-%date:~3,2%_%date:~0,2%" "{pasta}"', shell=True)
            sg.popup_ok('Processo Finalizado') 
     
    ## EVENTOS DA SEGUNDA PÁGINA

    if window == janela2 and event == 'Instalar':
        subprocess.run("powershell Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))", shell=True)
        if values['FF'] == True:
            subprocess.run('choco install firefox -y', shell=True)
        if values['WR'] == True:       
            subprocess.run('choco install winrar -y', shell=True)
        if values['MO'] == True:
            subprocess.run('choco install officeproplus2013 -y', shell=True)
        if values['OO'] == True:
            subprocess.run('choco install onlyoffice -y', shell=True)
        if values['AR'] == True:
            subprocess.run('choco install adobereader -y', shell=True)
        if values['DB'] == True:
            subprocess.run('choco install driverbooster -y', shell=True)
        if values['MB'] == True:             
            subprocess.run('choco install malwarebytes -y', shell=True)
        if values['MT'] == True:
            subprocess.run('choco install microsoft-teams -y', shell=True)
        if values['ZM'] == True:
            subprocess.run('choco install zoom -y', shell=True)
        if values['GIMP'] == True:
            subprocess.run('choco install gimp -y', shell=True)
        if values['GC'] == True:
            subprocess.run('choco install googlechrome -y', shell=True)
        sg.popup('Processo Finalizado')

