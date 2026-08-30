# Allows us to see keycodes of any key. Couldn't find good docs, so this is the solution.

import hpprime as h


def main():
    print("Press any key:")
    while True:
        code = h.eval('getkey')
        if code != -1:
            print(int(code))
            h.eval('wait(0.25)')   # let the key settle before polling again
            while h.eval('getkey') != -1:
                pass                # drain any repeat/bounce events
        else:
            h.eval('wait(0.03)')

main()