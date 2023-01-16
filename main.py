#!/usr/bin/env python
import PySimpleGUI as sg
import os


def LEDIndicator(key=None, radius=30):
    return sg.Graph(canvas_size=(radius, radius),
             graph_bottom_left=(-radius, -radius),
             graph_top_right=(radius, radius),
             pad=(0, 0), key=key)

def SetLED(window, key, color):
    graph = window[key]
    graph.erase()
    graph.draw_circle((0, 0), 25, fill_color=color, line_color='white')

sg.theme('DarkAmber')
# Define the window's contents
layout = [[sg.Text("Enter IP")],
          [sg.Input(key='-INPUT-'),LEDIndicator('_HOST1_')],
          [sg.Text(size=(40, 1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]


def HostPinger(host):
    response = int(os.system("ping -c1 " + host))
    return response

# Create the window
window = sg.Window('Host Checker', layout)

while True:
    event, value = window.read(timeout=2000)
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    if event == 'Ok':
        while True:
            event, value = window.read(timeout=2000)
            if event in (None, 'Quit'):
                break
            SetLED(window, '_HOST1_', 'red' if HostPinger(value['-INPUT-']) > 0 else 'green')


window.close()