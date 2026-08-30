from uio import *
from math import *
from urandom import *
from hpprime import *
import builtins
import ui
from ui import UI

# Constants
class MenuItem:
  def __init__(self, name, display, action):
    self.name = name
    self.display = display
    self.action = action


def input_test():
  UI.getinput("This is a test of the input box. Type something and press Enter.", "Input Test", "Default text")
  sendNotification("Input test completed. You typed: " + eval(UI.INPUT_VAR)) # TODO: Fix text overflowing


def notif_test():
  sendNotification("Notification test selected")


MENU = [
  MenuItem("input_test", "Input test", input_test),
  MenuItem("notif_test", "Notification test", notif_test),
]

VISIBLE = 10 # Number of items visible at once


draw_menu = UI.draw_menu
getinput = UI.getinput
sendNotification = UI.sendNotification

def run_script(number):
  #print(f"Selected: {number}") # Are f strings genuinally not supported :/
  sendNotification("You selected" + str(number))


dimgrob(1, 320, 240, 0xFFFFFF) # Create the weird graphics buffer

# Clear any previously pressed keys
while eval('getkey') != -1:
  pass


while True:

  draw_menu(VISIBLE=VISIBLE, MENU=MENU)

  key = eval('getkey')

  # UP
  if key == 2:
    if ui.selected > 0:
      ui.selected -= 1

      # Scroll upward
      if ui.selected < ui.top:
        ui.top = ui.selected

  # DOWN
  elif key == 12:
    if ui.selected < len(MENU) - 1:
      ui.selected += 1

      # Scroll downward
      if ui.selected >= ui.top + VISIBLE:
        ui.top = ui.selected - VISIBLE + 1

  # SELECT / CENTER
  elif key == 30:
    MENU[ui.selected].action()

  # Wait for key release
  while eval('getkey') != -1:
    pass