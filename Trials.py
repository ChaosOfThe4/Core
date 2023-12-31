import sys
import math
import time
import ctypes
import keyboard
import memprocfs
import threading 
import tkinter as tk
from tkinter import *
import concurrent.futures

from Helper import (
    ACVars, CSVars, TFVars,
)

global vmm,base,process_Main,local_Player,integer_val,integer_val1,bytes_val,bytes_val1, feature2

feature2 = {
    'infHealth' : False,
    'infAmmo' : False,
    'infArmor' : False,
    'infGrenades' : False,
    'speedHack' : False,
}

def FindDMAAddy(vHandle, base, offsets, arch = 64):
    size = 8
    if (arch == 32): size = 4
    
    bases = int.from_bytes(vHandle.memory.read(base, 0x04), "little")
    print(bases)
    test  = vHandle.memory.read(base+bases, 0x0)
    print(int.from_bytes(test, "little"))
    
    """for offset in offsets:
                    addy = vHandle.memory.read(bases + offset, 0x04)
                    print(vmm.hex(addy))
                    bases = int.from_bytes(addy, "little")
                    print(bases)"""

    return bases

def  unhex(h3x):
    return int(str(h3x), 16)

def check(features, feat):
    for x,y in features.items():
        if x == feat:
            return y

###Need to make function check game to get right class then each feature set from each class

def runner(features, feat, game):
    for x,y in game.items():
        if x == game:
            is_On = check(y.features, feat)
        if (not is_On):
            features.update({str(feat): not is_On})
            h = threading.Thread(target=y.feat, args=[], daemon=True)
            h.run()

"""def manager(features):
    for x, y in features.items():
        if (y):"""
            


menu_options = {
    1: 'Assault Cube',
    2: 'CS:GO',
    3: 'SoTF',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )



"""def init(processz, clasz):
    base = {}

    vmm = memprocfs.Vmm(['-device', 'fpga'])
    process_Main = vmm.process(processz)

    print("\n(-----------------------------------)\n")
    print("Initializing DMA connection...\n")
    if vmm:
        print("DMA connected!...\n")
        print("Collecting process id of " + processz)

        if process_Main:

            print("Got process id: " + str(process_Main))
            for each in clasz.modules:
                print("Collecting modules: ")
            
                trial  = process_Main.module(each)
                base[each] = trial.base

                print("\t" + each + ":" + str(base[each]))
    return vmm, process_Main"""

class AC_Client:
        #inUse = boolean
    integer_val = 1100000000 #int
    integer_val1 = 999 #int
    bytes_val = integer_val.to_bytes(4, 'little') #int to proper bytes for memory
    bytes_val1 = integer_val1.to_bytes(4, 'little') #int to proper bytes for memory
        #age = age


    def Innit():   
        base = {}

        vmm = memprocfs.Vmm(['-device', 'fpga'])
        process_Main = vmm.process("ac_client.exe")

        print("\n(-----------------------------------)\n")
        print("Initializing DMA connection...\n")
        if vmm:
            print("DMA connected!...\n")
            print("Collecting process id of ac_client.exe")

            if process_Main:

                print("Got process id: " + str(process_Main))
                for each in ACVars.modules:
                    print("Collecting modules: ")
            
                    trial  = process_Main.module(each)
                    base[each] = trial.base

                    print("\t" + each + ":" + str(base[each]))
        

    def local_Player():
        local_Player = process_Main.memory.read(base["ac_client.exe"] + unhex(ACVars.LocalP), 0x04)# +  unhex(ACVars.healthO), 0x04)
        #return local_Player

    def infHealth():
        feature = 'infHealth'
        on = check(feature2, feature)
        while on:
            try:
            ###LOCAL PLAYER HEALTH###
                ##READ##
                local_Player1 = process_Main.memory.read(int.from_bytes(local_Player, "little") + unhex(ACVars.healthP), 0x04)
                print(int.from_bytes(local_Player1, "little"))

                ##WRITE##
                
                process_Main.memory.write(int.from_bytes(local_Player, "little") + unhex(ACVars.healthP), bytes_val)#writing to memory
                on = check(feature2, feature)
            except KeyboardInterrupt:
                sys.exit("Bye")
            except UnicodeDecodeError:
                pass

    def infAmmo():
        feature = 'infAmmo'
        on = check(feature2, feature)
        while on:
            try:
                ###PRIMARY WEAPON AMMO###
                Ammo = process_Main.memory.read(int.from_bytes(local_Player, "little") + unhex(ACVars.PAmmo), 0x04)
                print(int.from_bytes(Ammo, "little"))

                bytes_val1 = integer_val1.to_bytes(4, 'little') #int to proper bytes for memory
                process_Main.memory.write(int.from_bytes(local_Player, "little") + unhex(ACVars.PAmmo), bytes_val1)#writing to memory


                ###SECONDAY WEAPON AMMO###
                SAmmo = process_Main.memory.read(int.from_bytes(local_Player, "little") + unhex(ACVars.SAmmo), 0x04)
                print(int.from_bytes(SAmmo, "little"))

                process_Main.memory.write(int.from_bytes(local_Player, "little") + unhex(ACVars.SAmmo), bytes_val1)#writing to memory
                on = check(feature2, feature)
            except KeyboardInterrupt:
                sys.exit("Bye")
            except UnicodeDecodeError:
                pass

    def infArmor():
        feature = 'infArmor'
        on = check(feature2, feature)
        while on:
            try:
                ###ARMOR###
                Armor = process_Main.memory.read(int.from_bytes(local_Player, "little") + unhex(ACVars.Armor), 0x04)
                print(int.from_bytes(Armor, "little"))

                process_Main.memory.write(int.from_bytes(local_Player, "little") + unhex(ACVars.Armor), bytes_val1)#writing to memory
                on = check(feature2, feature)
            except KeyboardInterrupt:
                sys.exit("Bye")
            except UnicodeDecodeError:
                pass

    def infGrenades():
        feature = 'infGrenades'
        on = check(feature2, feature)
        while on:
            try:

                ###GRENADES###
                Grenades = process_Main.memory.read(int.from_bytes(local_Player, "little") + unhex(ACVars.Grenades), 0x04)
                print(int.from_bytes(Grenades, "little"))

                process_Main.memory.write(int.from_bytes(local_Player, "little") + unhex(ACVars.Grenades), bytes_val1)#writing to memory
                on = check(feature2, feature)
            except KeyboardInterrupt:
                sys.exit("Bye")
            except UnicodeDecodeError:
                pass


    def speedHack():
        feature = 'speedHack'
        on = check(feature2, feature)
        while True:
            try:
                ###SPEEDHACK###
                new_speed = 2.0
                Speed = process_Main.memory.read(int.from_bytes(local_Player, "little") + unhex(ACVars.direction), 0x04)
                print(int.from_bytes(Speed, "little"))

                if any(ACVars.movement) == Speed:
                    new_speed = Speed * new_speed
                    process_Main.memory.write(int.from_bytes(local_Player, "little") + unhex(ACVars.direction), new_speed)#writing to memory
     
                time.sleep(0.05)
                on = check(feature2, feature)
            except KeyboardInterrupt:
                sys.exit("Bye")
            except UnicodeDecodeError:
                pass

    featFuncs = {
    'infHealth' : infHealth(),
    'infAmmo' : infAmmo(),
    'infArmor' : infArmor(),
    'infGrenades' : infGrenades(),
    #'speedHack' : speedHack(),
    }

def timet():
    return time.perf_counter_ns()

def CSGO_Client():
    base = {}

    vmm = memprocfs.Vmm(['-device', 'fpga'])
    process_Main = vmm.process("csgo.exe")

    print("\n(-----------------------------------)\n")
    print("Initializing DMA connection...\n")
    if vmm:
        print("DMA connected!...\n")
        print("Collecting process id of csgo.exe")

        if process_Main:

            print("Got process id: " + str(process_Main))
            for each in CSVars.modules:
                print("Collecting modules: ")
            
                trial  = process_Main.module(each)
                base[each] = trial.base

                print("\t" + each + ":" + str(base[each]))

    
    

    integer_val = 6 #int
    bytes_val = integer_val.to_bytes(4, 'little') #int to proper bytes for memory
    integer_val1 = 4 #int
    bytes_val1 = integer_val1.to_bytes(4, 'little') #int to proper bytes for memory

    while True:
        try:
            #for  i in range(1,32):
            start = timet()
            #print(start) 
            local_Player = process_Main.memory.read(base["client.dll"] + CSVars.dwLocalPlayer, 0x4)

            playerTeam = process_Main.memory.read(int.from_bytes(local_Player, "little") + unhex(CSVars.m_iTeamNum), 0x4)

            entityId = process_Main.memory.read(int.from_bytes(local_Player, "little") + CSVars.m_iCrosshairId, 0x4)
            #print(int.from_bytes(entityId, "little") -1)

            test = (int.from_bytes(entityId, "little") -1)

            entity = process_Main.memory.read(base["client.dll"] + CSVars.dwEntityList + (test * 0x10), 0x4)
            #print(int.from_bytes(entity, "little"))

            entityTeam = process_Main.memory.read(int.from_bytes(entity, "little") + CSVars.m_iTeamNum, 0x4)
            ##print(vmm.hex(playerTeam))
            #print('\n')
            #print(int.from_bytes(entityTeam, "little"))
            entInt = int.from_bytes(entityTeam, "little")
            #print("deciding\n")
            #if entInt > 0 and entInt < 64 and playerTeam != entityTeam:
            
            if entInt > 0 and entInt < 64:
                    #process_Main.memory.write(base["client.dll"] + CSVars.dwEntityList + (i * 0x10) + unhex(CSVars.m_bSpotted), bytes_val)
                shooting = process_Main.memory.read(base["client.dll"] + unhex(CSVars.dwForceAttack), 0x4)
                #print(int.from_bytes(shooting, "little"))
                if shooting != bytes_val:
                    process_Main.memory.write(base["client.dll"] + unhex(CSVars.dwForceAttack), bytes_val)
                    #print("SHOT\n")
                    time.sleep(.5)
                    
                        #process_Main.memory.write(base["client.dll"] + unhex(CSVars.dwForceAttack), bytes_val1)
                    
            #else:
                #print("nope\n")
            #local_Player = process_Main.memory.read(base["ac_client.exe"] + unhex(ACVars.LocalP), 0x04)
            #glow_manager = process_Main.memory.read(base["client.dll"] + unhex(CSVars.dwGlowObJectManager), 0x04)
                #teamID = process_Main.memory.read(base["client.dll"] + CSVars.m_iTeamNum, 0x04)
                #print(int.from_bytes(teamID, "little"))
                #entity1 = process_Main.memory.read(int.from_bytes(entity, "little") + CSVars.m_bIsLocalPlayer, 0x04)
            #entity1 = process_Main.memory.read(base["client.dll"] + unhex(CSVars.dwLocalPlayer), 0x04)# + CSVars.m_iTeamNum, 0x04)
            #print(entity1)
     
            end = timet()
            print(end - start)

        except KeyboardInterrupt:
            sys.exit("Bye")
        except UnicodeDecodeError:
            pass
            time.sleep(0.075)

def SoTF_Client():   
    base = {}

    vmm = memprocfs.Vmm(['-device', 'fpga'])
    process_Main = vmm.process("SonsOfTheForest.exe")

    print("\n(-----------------------------------)\n")
    print("Initializing DMA connection...\n")
    if vmm:
        print("DMA connected!...\n")
        print("Collecting process id of SonsOfTheForest.exe")

        if process_Main:

            print("Got process id: " + str(process_Main))
            for each in TFVars.modules:
                print("Collecting modules: ")
            
                trial  = process_Main.module(each)
                base[each] = trial.base

                print("\t" + each + ":" + str(base[each]))


    while True:
        try:


            ###LOCAL PLAYER OBJECT###

            local = FindDMAAddy(process_Main, base["GameAssembly.dll"], TFVars.localP, arch = 64)
            print(local)

     
     
            time.sleep(2.05)
        except KeyboardInterrupt:
            sys.exit("Bye")
        except UnicodeDecodeError:
            pass

        time.sleep(.05)

games = {
'ac_client' : AC_Client(),
#'csgo' : CSGO_Client(),
}
     
window = tk.Tk()
window.title("Synapse Software")
"""MAIN//"""
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_AC = tk.Button(master=window, text="Assault Cube", command=lambda:my_open())
btn_AC.grid(row=0, column=0, sticky="nsew")

btn_decrease = tk.Button(master=window, text="CS:GO", command=CSGO_Client)
btn_decrease.grid(row=0, column=1, sticky="nsew")

btn_TF = tk.Button(master=window, text="SoTF", command=SoTF_Client)
btn_TF.grid(row=0, column=2, sticky="nsew")
"""//END"""

def my_open():
    w_child=Toplevel(window) # Child window 
    w_child.geometry("200x200")  # Size of the window 
    w_child.title("Synapse Software")

    AC_Client.Innit()
    AC_Client.local_Player()

    health = tk.Button(w_child, text='Infinite Health', command=runner('infHealth', "ac_client"))
    health.grid(row=1, column=2)

    b3 = tk.Button(w_child, text=' Close Child',
                   command=w_child.destroy)
    b3.grid(row=3,column=2)

    #h = threading.Thread(target=manager, args=[])
    #h.run()

window.mainloop()