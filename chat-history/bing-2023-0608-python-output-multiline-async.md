# I would like to use Pytho...

> I would like to use Python to develop a multiple line output program.
> When the program output texts to windows terminal, it can update multiple lines asyncly at the same time.
> Please search the web, and list several high-quality solutions for my requirement.

There are several ways to achieve your goal of updating multiple lines asynchronously in a Python program. One way is to use the `reprint` module for Python 2/3 which allows you to print and refresh multi-line output contents in the terminal[1](https://stackoverflow.com/questions/14300770/how-to-refresh-the-multi-line-output-dynamically). You can treat the output instance as a normal dict or list (depending on which mode you use) and when you modify the content in the output instance, the output in the terminal will automatically refresh[1](https://stackoverflow.com/questions/14300770/how-to-refresh-the-multi-line-output-dynamically).

Another way is to use `curses` module on Unix systems or `PDCurses` on Windows systems[2](https://stackoverflow.com/questions/6840420/rewrite-multiple-lines-in-the-console). You can also use ANSI control codes to move the cursor up and update multiple lines[3](https://stackoverflow.com/questions/39455022/python-3-print-update-on-multiple-lines).

Would you like more information on any of these methods?

1. [python - How to refresh the multi-line output dynamically - Stack Overflow](https://stackoverflow.com/questions/14300770/how-to-refresh-the-multi-line-output-dynamically)
2. [python - Rewrite multiple lines in the console - Stack Overflow](https://stackoverflow.com/questions/6840420/rewrite-multiple-lines-in-the-console)
3. [Python 3 Print Update on multiple lines - Stack Overflow](https://stackoverflow.com/questions/39455022/python-3-print-update-on-multiple-lines)
4. [](https://bing.com/search?q=python+multiple+line+output+program+update+asyncly)
5. [python - Multiple async requests simultaneously - Stack Overflow](https://stackoverflow.com/questions/53021448/multiple-async-requests-simultaneously)