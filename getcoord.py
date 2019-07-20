from pynput import mouse


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
def on_scroll(x, y, dx, dy):
    return False


# Collect events until released
with mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
