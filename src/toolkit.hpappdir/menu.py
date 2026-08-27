from uio import *
from math import *
from urandom import *
from hpprime import *
import builtins

#Constants
MENU = [
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]
VISIBLE = 10
selected = 0
top = 0


def draw_menu():
  global selected, top

  # Clear screen
  dimgrob(1, 320, 240, 0xFFFFFF)

  # Draw title
  eval('textout_p("MENU",G1,10,8,6,#000000)')

  # Draw menu items
  for i in range(VISIBLE):
    index = top + i

    if index >= len(MENU):
      break

    y = 40 + i * 24

    # Highlight selected item
    if index == selected:
      fillrect(1, 5, y - 2, 310, 22, 0xCCCCCC, 0xCCCCCC)
      eval(
        'textout_p(">{0}",G1,15,{1},4,#000000)'.format(
          MENU[index], y
        )
      )
    else:
      eval(
        'textout_p("{0}",G1,25,{1},4,#000000)'.format(
          MENU[index], y
        )
      )

  # Simple scroll indicators
  if top > 0:
    eval('textout_p("^",G1,305,35,3,#000000)')

  if top + VISIBLE < len(MENU):
    eval('textout_p("v",G1,305,225,3,#000000)')

  blit(0, 0, 0, 1)


def run_script(number):
  #print(f"Selected: {number}") # Are f strings genuinally not supported :/
  print("Selected: " + str(number)) # Thanks autocomplete


dimgrob(1, 320, 240, 0xFFFFFF) # Create the weird graphics buffer

# Clear any previously pressed keys
while eval('getkey') != -1:
  pass


while True:

  draw_menu()

  key = eval('getkey')

  # UP
  if key == 2:
    if selected > 0:
      selected -= 1

      # Scroll upward
      if selected < top:
        top = selected

  # DOWN
  elif key == 12:
    if selected < len(MENU) - 1:
      selected += 1

      # Scroll downward
      if selected >= top + VISIBLE:
        top = selected - VISIBLE + 1

  # SELECT / CENTER
  elif key == 4:
    run_script(MENU[selected])

  # Wait for key release
  while eval('getkey') != -1:
    pass