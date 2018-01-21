from pynput.keyboard import Key, Controller
import os, time

keyboard = Controller()

tokens = []
files = open("choose.txt", "r").read()

def open_file(filename):
    data = open(filename, "r").read()
    data += "<EOF>"
    return data

def lex(filecontents):
    tok = ""
    state = 0
    string = ""
    expr = ""
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        if tok == " ":
            if state == 0:
                tok = ""
            else:
                tok = " "
        elif tok == "\n" or tok == "<EOF>":
            if expr != "":
                tokens.append("NUM:" + expr)
                expr = ""
            tok = ""
        elif tok.upper() == "PRINT":
            tokens.append("PRINT")
            tok = ""
        elif tok.upper() == "TYPE":
            tokens.append("TYPE")
            tok = ""
        elif tok.upper() == "STRING":
            tokens.append("KEYSSTRING")
            tok = ""
        elif tok.upper() == "DELAY":
            tokens.append("DELAY")
            tok = ""
        elif tok.upper() == "REM":
            tokens.append("REM")
            tok = ""
        elif tok in map(str, range(0, 10)):
            if state == 0:
                expr += tok
            else:
                string += tok
            tok = ""
        elif tok == "\"":
            if state == 0:
                state = 1
                tok = ""
            elif state == 1:
                tokens.append("STRING:" + string)
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""
    return tokens

def parse(toks):
    i = 0
    while(i < len(toks)):
        if(toks[i] + " " + toks[i+1][0:3] == "DELAY NUM"):
            delay = int(toks[i+1][4:])
            delay /= 1000
            time.sleep(delay)
            i += 2
        elif(toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:6] == "KEYSSTRING STRING STRING"):
            dir = str(os.popen('<nul set /p =%cd%').read())

            if toks[i+1][7:] == "EXTENSION":
                keyboard.type(dir + "\\extension")
            elif toks[i+1][7:] == "SCRIPT":
                keyboard.type(dir + "\\scripts\\" + files)
            elif toks[i+1][7:] == "PYTHON":
                keyboard.type("python.exe ")
            else:
                keyboard.type(toks[i+1][7:])
            
            if toks[i+2][7:] == "EXTENSION":
                keyboard.type(dir + "\\\\extension")
            elif toks[i+2][7:] == "SCRIPT":
                keyboard.type(dir + "\\scripts\\" + files)
            elif toks[i+1][7:] == "PYTHON":
                keyboard.type("python.exe ")
            else:
                keyboard.type(toks[i+2][7:])
            i += 3
        elif(toks[i] + " " + toks[i+1][0:6] == "KEYSSTRING STRING"):
            dir = str(os.popen('<nul set /p =%cd%').read())

            if toks[i+1][7:] == "EXTENSION":
                keyboard.type(dir + "\\extensions")
            elif toks[i+1][7:] == "SCRIPT":
                keyboard.type(dir + "\\scripts\\" + files)
            elif toks[i+1][7:] == "PYTHON":
                keyboard.type("python.exe ")
            else:
                keyboard.type(toks[i+1][7:])
            i += 2
        elif(toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:6] == "TYPE STRING STRING"):
            if toks[i+1][7:] == "GUI":
                with keyboard.pressed(Key.cmd):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "CTRL":
                with keyboard.pressed(Key.ctrl):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "ALT":
                with keyboard.pressed(Key.alt):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "SHIFT":
                with keyboard.pressed(Key.shift):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "TAB":
                with keyboard.pressed(Key.tab):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "ENTER":
                with keyboard.pressed(Key.enter):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "F1":
                with keyboard.pressed(Key.f1):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "F2":
                with keyboard.pressed(Key.f2):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "F3":
                with keyboard.pressed(Key.f3):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "F4":
                with keyboard.pressed(Key.f4):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "F5":
                with keyboard.pressed(Key.f5):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "F6":
                with keyboard.pressed(Key.f6):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "F7":
                with keyboard.pressed(Key.f7):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "F8":
                with keyboard.pressed(Key.f8):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "F9":
                with keyboard.pressed(Key.f9):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "F10":
                with keyboard.pressed(Key.f10):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "F11":
                with keyboard.pressed(Key.f11):
                    keyboard.type(toks[i+2][7:])
            elif toks[i+2][7:] == "F12":
                with keyboard.pressed(Key.f12):
                    keyboard.type(toks[i+2][7:])
            i += 3
        elif(toks[i] + " " + toks[i+1][0:6] == "TYPE STRING"):
            if toks[i+1][7:] == "GUI":
                keyboard.press(Key.cmd)
                keyboard.release(Key.cmd)
            elif toks[i+1][7:] == "CTRL":
                keyboard.press(Key.ctrl)
                keyboard.release(Key.ctrl)
            elif toks[i+1][7:] == "ALT":
                keyboard.press(Key.alt)
                keyboard.release(Key.alt)
            elif toks[i+1][7:] == "SHIFT":
                keyboard.press(Key.shift)
                keyboard.release(Key.shift)
            elif toks[i+1][7:] == "TAB":
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
            elif toks[i+1][7:] == "ENTER":
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            elif toks[i+1][7:] == "F1":
                keyboard.press(Key.f1)
                keyboard.release(Key.f1)
            elif toks[i+1][7:] == "F2":
                keyboard.press(Key.f2)
                keyboard.release(Key.f2)
            elif toks[i+1][7:] == "F3":
                keyboard.press(Key.f3)
                keyboard.release(Key.f3)
            elif toks[i+1][7:] == "F4":
                keyboard.press(Key.f4)
                keyboard.release(Key.f4)
            elif toks[i+1][7:] == "F5":
                keyboard.press(Key.f5)
                keyboard.release(Key.f5)
            elif toks[i+1][7:] == "F6":
                keyboard.press(Key.f6)
                keyboard.release(Key.f6)
            elif toks[i+1][7:] == "F7":
                keyboard.press(Key.f7)
                keyboard.release(Key.f7)
            elif toks[i+1][7:] == "F8":
                keyboard.press(Key.f8)
                keyboard.release(Key.f8)
            elif toks[i+1][7:] == "F9":
                keyboard.press(Key.f9)
                keyboard.release(Key.f9)
            elif toks[i+1][7:] == "F10":
                keyboard.press(Key.f10)
                keyboard.release(Key.f10)
            elif toks[i+1][7:] == "F11":
                keyboard.press(Key.f11)
                keyboard.release(Key.f11)
            elif toks[i+1][7:] == "F12":
                keyboard.press(Key.f12)
                keyboard.release(Key.f12)
            i += 2
        elif(toks[i] + " " + toks[i+1][0:6] == "REM STRING"):
            i += 2

def run():
    print ""
    print "  _____       _     _               _____             _          "
    print " |  __ \     | |   | |             |  __ \           | |         "
    print " | |__) |   _| |__ | |__   ___ _ __| |  | |_   _  ___| | ___   _ "
    print " |  _  / | | | '_ \| '_ \ / _ \ '__| |  | | | | |/ __| |/ / | | |"
    print " | | \ \ |_| | |_) | |_) |  __/ |  | |__| | |_| | (__|   <| |_| |"
    print " |_|  \_\__,_|_.__/|_.__/ \___|_|  |_____/ \__,_|\___|_|\_\\\__, |"
    print "                                                            __/ |"
    print "   Running Script!                                         |___/ "
    print ""

    if os.path.isdir(".\\scripts\\" + files):
        data = open_file(".\\scripts\\" + files + "\\script.txt")
        toks = lex(data)
        parse(toks)
    else:
        print("That script is unavailble!")

run()
