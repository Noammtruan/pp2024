import curses
from domains.manager import Manager

def main():
    curses.wrapper(manager.curses_ui)

if __name__ == "__main__":
    main()
