from pynput import keyboard
 
def write_file(key_char):
    with open("minLineLength.txt","w") as f:
        f.write(str(int(key_char) * 10))

def write_up():
    with open("minLineLength.txt", "r") as f:
        data = f.readline()
        data = int(int(data) + 1)
    with open("minLineLength.txt","w") as f:
        f.write(str(int(data)))
        print(data)

def write_down():
    with open("minLineLength.txt", "r") as f:
        data = f.readline()
        data = int(int(data) - 1)
    with open("minLineLength.txt","w") as f:
        f.write(str(int(data)))
        print(data)

def on_press(key):
    try:
        # print('alphanumeric key {0} pressed'.format(key.char))
        if key.char == '0' or key.char == '1' or key.char == '2' or key.char == '3' or key.char == '4' or key.char == '5' or key.char == '6' or key.char == '7' or key.char == '8' or key.char == '9' :
            write_file(str(key.char))
    except AttributeError:
        # print('special key {0} pressed'.format(key))
        if key == keyboard.Key.up:
            # print('up000000000000000000')
            write_up()
        if key == keyboard.Key.down:
            # print('down---------------')
            write_down()
 
def on_release(key):
    # print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False
 
while True:
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()