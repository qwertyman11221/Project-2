import PySimpleGUI as sg
import pyqrcode

sg.theme('DarkAmber')


layout = [
    [sg.Text('Enter text to convert to QR code:')],
    [sg.InputText()],
    [sg.Button('Generate QR Code'), sg.Button('Exit')]
]


window = sg.Window('QR Code Generator', layout)


while True:
    event, values = window.read()

    
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    
    if event == 'Generate QR Code':
        text = values[0]

        
        qr = pyqrcode.create(text)

        
        qr.png('qrcode.png', scale=20)

        
        layout2 = [[sg.Image(filename='qrcode.png')]]
        window2 = sg.Window('QR Code', layout2)
        event, values = window2.read()
        window2.close()


window.close()
