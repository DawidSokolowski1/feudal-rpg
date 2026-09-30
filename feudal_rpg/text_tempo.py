"""Printing text slowly, letter by letter, like a narrator.

Pressing any key while the text is printing skips the delay and shows
the rest at once. On macOS/Linux this uses termios/tty; those don't exist
on Windows, so there msvcrt (Windows only) is used instead.
"""
import time
import sys

# Windows has no termios/tty, so the right modules are imported per system
IS_WINDOWS = sys.platform == "win32"
if IS_WINDOWS:
    import msvcrt
else:
    import select
    import tty
    import termios


def windows_print(text, delay):
    """Letter-by-letter printing for Windows, used by the functions below.

    time.sleep() makes the delay. msvcrt.kbhit() is True when a key has
    been pressed; the key is then read with getwch() (so it doesn't show
    up later) and the rest of the text is printed without waiting.
    """
    skip = False
    for char in text:
        print(char, end="", flush=True)
        if not skip:
            time.sleep(delay)
            if msvcrt.kbhit():
                msvcrt.getwch()
                skip = True
    print()


def fight_print(text, delay=0.03):
    """Print fight messages letter by letter (0.03 s per letter).

    How it works:
    - tty.setcbreak() makes key presses readable immediately, without
      waiting for Enter. The old terminal settings are saved first.
    - select.select() waits up to `delay` seconds for a key press. If
      none comes, the next letter is printed; this wait is the delay.
    - If a key was pressed, it is read (so it doesn't show up later) and
      skip = True prints the rest without waiting.
    - finally always restores the old terminal settings, even if an
      error happens.
    """
    if IS_WINDOWS:
        return windows_print(text, delay)
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
    """Print the enemy table quickly (0.008 s per letter).

    Works exactly like fight_print(), only with a shorter delay.
    """
    if IS_WINDOWS:
        return windows_print(text, delay)
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
    """Print story text slowly (0.05 s per letter).

    Works exactly like fight_print(), only with a longer delay.
    """
    if IS_WINDOWS:
        return windows_print(text, delay)
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
    """Stop the game for a number of seconds (currently not used)."""
    time.sleep(seconds)
