from uio import *
from math import *
from urandom import *
from hpprime import *
import builtins

selected = 0
top = 0


class UI:
  INPUT_VAR = "PyInputStr"

  @staticmethod
  def getinput(message="", title="Input", default=""): # Abstraction for getting user input
    while eval('getkey') != -1:
      pass
    eval('{0}:="{1}"'.format(UI.INPUT_VAR, default))
    ok = eval('INPUT({0},"{1}","{2}","ENTER to confirm, ESC to cancel")'.format(
      UI.INPUT_VAR, title, message
    ))

    if not ok:
      return default

    return eval(UI.INPUT_VAR)

  @staticmethod
  def sendNotification(message: str): # Sends notifcations. 
    while eval('getkey') != -1: #Wait till enter is released or we'll immediately close the popup
      pass

    # Draw the popup background
    # fillrect(grob, x, y, width, height, edge_color, fill_color)
    fillrect(1, 60, 90, 200, 60, 0x000000, 0xEEEEEE)
    
    # Write text
    msg = message
    eval('textout_p("{0}",G1,75,100,4,#000000)'.format(msg))
    eval('textout_p("Press any key to dismiss",G1,75,125,2,#555555)')
    
    #Push the buffer to the screen
    blit(0, 0, 0, 1)

    # Close when use presses a key
    while eval('getkey') == -1:
      pass

  @staticmethod
  def draw_menu(VISIBLE, MENU):
    global selected, top

    # Clear screen
    dimgrob(1, 320, 240, 0xFFFFFF)

    # Draw title
    eval('textout_p("Dev Menu",G1,10,8,6,#000000)')

    # Draw menu items
    for i in range(VISIBLE):
      index = top + i

      if index >= len(MENU):
        break

      y = 25 + i * 20 # Difference in y position for each item
      item = MENU[index]

      # Highlight selected item
      if index == selected:
        fillrect(1, 5, y - 2, 310, 22, 0xCCCCCC, 0xCCCCCC)
        eval(
          'textout_p(">{0}",G1,15,{1},4,#000000)'.format(
            item.display, y
          )
        )
      else:
        eval(
          'textout_p("{0}",G1,25,{1},4,#000000)'.format(
            item.display, y
          )
        )

    # Simple scroll indicators
    if top > 0:
      eval('textout_p("^",G1,305,35,3,#000000)')

    if top + VISIBLE < len(MENU):
      eval('textout_p("v",G1,305,225,3,#000000)')

    blit(0, 0, 0, 1)