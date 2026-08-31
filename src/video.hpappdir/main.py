# Idea from https://www.cemetech.net/forum/viewtopic.php?t=19174

import hpprime as h

def dvidW():
    h.eval('DIMGROB_P(G4,30000,240)')
    h.eval('G4:=AFiles("demo.png")')

    H = 0
    done = False
    while not done:
        h.eval('BLIT_P(G0,0,0,320,240,G4,{0},0,{1},240)'.format(H, 320 + H))
        H += 320
        if H > 29670:
            H = 0
        h.eval('WAIT(0.04)')
        if h.eval('ISKEYDOWN(4)'):
            done = True

dvidW()