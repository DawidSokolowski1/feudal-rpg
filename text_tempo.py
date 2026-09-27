import time
import sys
import select
import tty
import termios

def fight_print(text, delay=0.03):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        skip = False
        for char in text:
            if not skip:
                print(char, end="", flush=True)
                ready, _, _ = select.select([sys.stdin], [], [], delay)
                if ready:
                    sys.stdin.read(1)
                    skip = True
            else:
                print(char, end="", flush=True)
        print()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def enemy_stats_print(text, delay=0.008):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        skip = False
        for char in text:
            if not skip:
                print(char, end="", flush=True)
                ready, _, _ = select.select([sys.stdin], [], [], delay)
                if ready:
                    sys.stdin.read(1)
                    skip = True
            else:
                print(char, end="", flush=True)
        print()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def story_print(text, delay=0.05):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        skip = False
        for char in text:
            if not skip:
                print(char, end="", flush=True)
                ready, _, _ = select.select([sys.stdin], [], [], delay)
                if ready:
                    sys.stdin.read(1)
                    skip = True
            else:
                print(char, end="", flush=True)
        print()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def pause(seconds=8.0):
    time.sleep(seconds)