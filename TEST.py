import pyautogui as gui
import time
import webbrowser
from pynput.mouse import Controller, Button
import tkinter as tk
from tkinter import simpledialog


ROOT = tk.Tk()
ROOT.withdraw()

time.sleep(4)
SC2= (gui.locateOnScreen("SC2.PNG"))
gui.click(SC2)#run
time.sleep(1)
gui.click()
gui.click()
gui.click()
gui.click()
gui.click()
gui.click()
gui.click()
gui.click()