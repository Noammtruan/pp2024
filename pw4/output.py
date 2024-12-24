import curses

class OutputHandler:
    @staticmethod
    def display_menu(stdscr, menu, current_row):
        stdscr.clear()
        for index, row in enumerate(menu):
            if index == current_row:
                stdscr.addstr(index, 0, row, curses.color_pair(1))
            else:
                stdscr.addstr(index, 0, row)
        stdscr.refresh()
