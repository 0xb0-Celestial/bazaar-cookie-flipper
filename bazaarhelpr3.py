import pyautogui as pg,keyboard,win32gui,win32con,os,ctypes,time
from colorama import Fore,Back,Style,init

def z(seconds): # ease of access :yawn:
    time.sleep(seconds) 
def mc(x, y): # ease of access :yawn:
    pg.moveTo(x, y)
    pg.click(x, y)
    z(1)
def mt(x, y): # ease of access :yawn:

    pg.moveTo*(x, y)
    z(1)
def openbz(): # ease of access :yawn:
    pg.press('t')
    pg.write("/bz")
    pg.press('enter')
    print(f"{Fore.LIGHTWHITE_EX}[STATUS] Opened bazaar.")
    z(1)
def cls(): # ease of access :yawn:
    os.system('cls')
def startup(): # some config needed at script startup
    init(convert=True) # goofy shit for colorama
    hwnd = win32gui.GetForegroundWindow() 
    win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,560,300,0) # width(560) and length(300)
    ctypes.windll.kernel32.SetConsoleTitleW('Bazaar helpr - pydattyko') # console title('self explanatory')

startup()

f = 0 # idk why this is here, i think it helps?
def ststage(): # 1st stage for buying cookies
    global f # local variable to check if script has ran once or not
    if f == 0:
        print(f"{Fore.LIGHTWHITE_EX}Please select how many {Fore.YELLOW}Cookies {Fore.LIGHTWHITE_EX}you want to buy.")
        print(f"{Fore.LIGHTRED_EX}1 = Just one! {Fore.LIGHTWHITE_EX}|{Fore.LIGHTMAGENTA_EX} 2 = A half-dozen! (6) {Fore.LIGHTWHITE_EX}|{Fore.LIGHTCYAN_EX} 3 = Get me a dozen! (12){Fore.LIGHTWHITE_EX}")
        localx = 0
        while localx == 0:
            if keyboard.is_pressed('1'):
                print("Option 1 selected.")
                opt=1
                amount = 1
                localx = 1
            if keyboard.is_pressed('2'):
                print("Option 2 selected.")
                opt=2
                amount = 6
                localx = 1
            if keyboard.is_pressed('3'):
                print("Option 3 selected.")
                opt=3
                amount = 12
                localx = 1
            if keyboard.is_pressed('4'):
                print("Skipping.")
                localx = 1
                opt=0
        if opt > 0:
            z(2) #
            cls() # some fancy sleep zzz
            z(3) #
            if opt==1:
                c = f"{Fore.LIGHTRED_EX}1, Just one!{Fore.LIGHTWHITE_EX}"
            elif opt==2 :
                c = f"{Fore.LIGHTMAGENTA_EX}2, A half-dozen! (6){Fore.LIGHTWHITE_EX}" # why aren't u using switch cases? 
            elif opt==3:
                c = f"{Fore.LIGHTCYAN_EX}3, Get me a dozen! (12){Fore.LIGHTWHITE_EX}"

            print(f"Great. The script will get right to it. You've selected option:\n{c}")
            print("Please make sure to have MINECRAFT selected.")
            z(3)
            cls()
            
            def buyorders(): # buy order action
                if opt==1:
                    openbz() # buy just one cookie
                    mc(890,400)
                    mc(1030,430)
                    mc(850,430)
                    mc(850,430)
                    mc(960,430)
                    print(f"{Fore.LIGHTWHITE_EX}[STATUS] Attempted to buy one cookie.")
                if opt==2:
                    openbz() # buy a half-dozen cookies (6)
                    mc(890,400)
                    mc(1030,430)
                    mc(920,430)
                    mc(850,430)
                    mc(960,430)
                    print(f"{Fore.LIGHTWHITE_EX}[STATUS] Attempted to buy a half-dozen cookies.")
                if opt==3:
                    openbz() # buy a dozen cookies (12)
                    mc(890,400)
                    mc(1030,430)
                    mc(1000,430)
                    mc(850,430)
                    mc(960,430)
                    print(f"{Fore.LIGHTWHITE_EX}[STATUS] Attempted to buy a dozen cookies.")
            buyorders()
            z(2)
            cls()

            f = 1

            ststage()
        elif opt == 0:
            f = 1
            ststage()
    elif f == 1:
        def sndstage(): # 2nd stage for relisting buy/sell orders, claim orders, and returning to the 1st stage
            print("This is the second stage of the script.\nNow, you will have to manually press buttons.")
            z(3)
            cls()
            print("[1] to relist buy order\n[2] to relist sell order\n[3] to claim order\n[4] to return to the normal page")
            localy = 0 # local variable for a loopdy loop
            def routine(): # routine for re buying cooki
                        if amount > 0:
                            mc(890,400)
                            mc(1030,430)
                            mc(1070,430)
                            pg.write(amount)
                            pg.press('enter')
                            mc(860,430)
                            mc(960,430)
            while localy == 0: # cute ahh loop
                if keyboard.is_pressed('1'):
                    print("Option 1 selected.")
                    z(2)
                    cls()
                    openbz()
                    mc(1000,540)
                    mc(860,460)
                    mc(860,460)
                    mc(890,430)
                    mc(965,500)
                    print("Please now press how many cookies (if) you have claimed from the order:")
                    print("0,1,2,3,4,5,6,7,8,9")
                    sndstage()
                    locald = 0
                    while locald != 1:
                        if keyboard.is_pressed('1'):
                            amount = amount -1
                            locald = 1
                            routine()
                        if keyboard.is_pressed('2'): # use switch cases for gods sakeeeeeeeeeeeeeeeeeee
                            amount = amount -2
                            locald = 1
                            routine()
                        if keyboard.is_pressed('3'):
                            amount = amount -3
                            locald = 1
                            routine()
                        if keyboard.is_pressed('4'):
                            amount = amount -4
                            locald = 1
                            routine()
                        if keyboard.is_pressed('5'):
                            amount = amount -5
                            locald = 1
                            routine()
                        if keyboard.is_pressed('6'):
                            amount = amount -6
                            locald = 1
                            routine()
                        if keyboard.is_pressed('7'):
                            amount = amount -7
                            locald = 1
                            routine()
                        if keyboard.is_pressed('8'):
                            amount = amount -8
                            locald = 1
                            routine()
                        if keyboard.is_pressed('9'): #
                            amount = amount -9
                            locald = 1
                            routine()
                        if keyboard.is_pressed('0'):
                            locald = 1
                            routine()
                    pg.press('esc')
                    localy = 1

                if keyboard.is_pressed('2'):
                    print("Option 2 selected.")
                    z(2)
                    cls()
                    openbz()
                    mc(1000,540)
                    mc(860,430)
                    mc(860,430)
                    mc(960,430)
                    mc(960,500)
                    mc(888,400)
                    mc(1065,430)
                    mc(850,430)
                    mc(960,430)
                    localy = 1
                    sndstage()
                    
                if keyboard.is_pressed('3'):
                    print("Option 3 selected.")
                    z(2)
                    cls()
                    openbz()
                    mc(1000,540)
                    mc(850,430)
                    pg.press('esc')
                    localy = 1
                    sndstage()

                if keyboard.is_pressed('4'):
                    print("Option 4 selected.")
                    z(2)
                    cls()
                    sndstage.bye = 0 # this is returniiiiiiiiiiiiiiiiing
                    localy = 1
        sndstage()
        if sndstage.bye == 0:
            f = 0
            ststage()

ststage()