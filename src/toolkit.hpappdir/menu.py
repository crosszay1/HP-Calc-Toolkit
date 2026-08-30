from uio import *
from math import *
from urandom import *
from hpprime import *
import builtins

#Constants
MENU = {
  1: "1",
  2: "2",
  3: "3",
  4: "4",
  5: "5",
  6: "6",
  7: "7",
  8: "8",
  9: "9",
  10: "10"
}

import ui
from ui import UI

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

  draw_menu(VISIBLE=10, MENU=MENU)

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
    items = list(MENU.keys())
    run_script(MENU[items[ui.selected]])

  # Wait for key release
  while eval('getkey') != -1:
    pass