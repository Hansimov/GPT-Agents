# python -m pip install windows-curses
import curses


def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)

    # Get screen height and width
    height, width = stdscr.getmaxyx()

    # Create a new window
    win = curses.newwin(height, width, 0, 0)

    # Enable keypad input for the window
    win.keypad(1)

    # Turn off input echoing
    curses.noecho()

    # Start color in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    # Print text with color attribute
    win.addstr(0, 0, "Hello, World!", curses.color_pair(1))

    # Refresh the screen
    win.refresh()

    # Wait for user input
    win.getch()


curses.wrapper(main)
