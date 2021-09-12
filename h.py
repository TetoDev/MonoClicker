from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import Key
from pynput import keyboard
from os import system, sys, _exit
import time
import random
from functools import partial
import threading

k = Controller()
c = []

def vary (x, y, button, pressed):
    
    lastwasntrelease = True
    while(True):
        print(c)
        if (button == Button.left and pressed and lastwasntrelease and c[1]==1):
            random.seed(time.time()**2/4 -2)
            m = random.randint(0,100)
            r = 1000 /c[0]
            if m > 95:     
                v = r + random.randint(int(-23*r/100),int(75*r/100))
            else:
                v = r + random.randint(int(-9*r/100),int(27*r/100))
            time.sleep(v/1000)
            
            k.press(Button.left)
            time.sleep(random.randint(3,5)/1000)
            k.release(Button.left)
            lastwasntrelease = False
        else :
            break

def gsg (d):
    
    if d == Key.scroll_lock:
        _exit(0)
        system.exit("Terminated by operator")
    
    if d == Key.end:
        if not (c[0]-3) < 1:
            c[0]= c[0]-3
            print(c[0])
    if d == Key.home:
        c[0] = c[0] + 3
        print(c[0])
    
    if d == Key.page_down:
        if c[1] == 1:
            c.insert(1,0)
            print("Stop")
    
    if d == Key.page_up:
        if c[1] == 0:
            c.insert(1,1)
            print("Start")

def dlis ():
    with keyboard.Listener(
            on_press=gsg
    ) as listenerk:
        print("Enabled")
        listenerk.join()

def main ():
    c.append(17)
    c.append(1)
    f = open("/home/teto/.bash_history",'w')
    fr = open("/home/teto/.bash_history",'r')
    x = fr.read().split('\n')
    for i in range(len(x)):
        if x[i] == "python main.py":
            x.pop(i)
        elif x[i]== "screen -S h":
            x.pop(i)
        elif x[i] == "cd hanger":
            x.pop(i)
        elif x[i] =="./hhh":
            x.pop(i)
    f.writelines(x)
    f.close()
    fr.close()

    t=threading.Thread(target=dlis)
    
    t.start()
    
    
    

    with Listener(
        on_click=vary,
    ) as listener:
        listener.join()
    
    

main()
