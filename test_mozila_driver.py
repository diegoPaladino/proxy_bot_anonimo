#test_mozila_driver
#unsucessful test


import pyautogui as p
from selenium import webdriver
# import winsound
from selenium.webdriver.common.keys import Keys
import time as t
import schedule
import smtplib

operadriver='C://Users//diego//OneDrive//Desktop//DESKTOP//PROGRAMAS//MOZILA//geckodriver.exe'
driver = webdriver.Firefox()

#solicitando a abertura de uma página
driver.get('http://dashboard.tawk.to')
driver.set_window_position(166,-700)
driver.maximize_window()