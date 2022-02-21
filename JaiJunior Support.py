import PySimpleGUI as sg
import subprocess

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  
            [sg.Button('INTERNET'), sg.Button('DNS')],
            [sg.Button('DISCO'), sg.Button('SCAN')],
            [sg.Button('LIMPAR'),sg.Button('IMPRESSORA')],
            [sg.Button('Cancel')],
            [sg.Text('Desenvolvido por: Jairo Nonato Júnior')]],

# Create the Window
window = sg.Window('JaiJunior Suppport', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'INTERNET':
        subprocess.run('ipconfig /release',shell=True)
        subprocess.run('ipconfig /renew',shell=True)
    if event == 'DNS':
        subprocess.run('ipconfig /flushdns',shell=True)
    if event == 'DISCO':
        subprocess.run('chkdsk /f',shell=True)
    if event == 'SCAN':
        subprocess.run('sfc /scannow',shell=True)
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

    if event == 'IMPRESSORA':
        subprocess.run('wusa /uninstall /kb:5005565', shell=True) 
        subprocess.run('wusa /uninstall /kd:50006670', shell=True)
    
        
window.close()