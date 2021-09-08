def pas(a, b, c):
    import pyperclip, keyboard, time

    def paste(text: str):
        buffer = pyperclip.paste()
        pyperclip.copy(text)
        keyboard.press_and_release('ctrl + v')
        pyperclip.copy(buffer)


    def type(text: str, interval=0.0):
        if interval == None:
            paste(text)
            return

        buffer = pyperclip.paste()
        for char in text:
            pyperclip.copy(char)
            keyboard.press_and_release('ctrl + v')
            time.sleep(interval)
        pyperclip.copy(buffer)
    time.sleep(c)
    if c == None:
        pass
    else:
        time.sleep(c)
    type(a, b)
    keyboard.press("enter")