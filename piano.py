from pynput.mouse import Button, Controller
import PIL.ImageGrab as imG
import time
from pynput import keyboard

running= True

mouse = Controller()

def on_press(key):
    if key == keyboard.Key.esc:
        print("EXIT\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        exit()
        running = False
        return False

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.space:
        # Stop listener
        return False

with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()


print("HOWDY")
1920,1080
#mouse.position = (1440,860)

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()



lasttime=time.perf_counter()
print(lasttime)
image = imG.grab()
coords=[1100,1000,900,800]
y=690
while running:# and time.perf_counter()<20:
    image = imG.grab()
    for x in coords:
        color = image.getpixel((x, y))
        if color[0]<40 and color[1] <40 and color[2] <40: #and time.perf_counter()-lasttime>0.1:#color[0]>100 and color[1] <20:
            color2 = image.getpixel((x, y-5))
            if color ==color2:
                mouse.position = (1600*x/1920-20,900*y/1080+80)
                mouse.press(Button.left)
                time.sleep(0.03)
                mouse.release(Button.left)
                #lasttime=time.perf_counter()
                print(color,x,y)


    
'''# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

# Set pointer position
mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(
    mouse.position))

# Move pointer relative to current position
mouse.move(5, -5)

# Press and release
mouse.press(Button.left)
mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on Mac OSX
mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)
'''
