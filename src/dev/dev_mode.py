from csv import Error
import os
import sys
from threading import Thread
from time import sleep
import pygame
from termcolor import colored


class DevMode(Thread):
    __initialized:bool = False
    __instance = None

    def __init__(self, group = None, target = None, name = None, args = ..., kwargs = None, *, daemon = None):
        if DevMode.__instance != None:
            raise Error('Dev mode already has an instance running')
        
        super().__init__(group, target, name, args, kwargs, daemon=daemon)

        DevMode.__initialized = True
        DevMode.__instance = self

    def init():
        print('Entering dev mode')

        DevMode.help()
        
        DevMode()
        DevMode.__instance.start()

    def stop():
        if DevMode.__instance == None:
            return

        print('Exiting dev mode')
        try:
            DevMode.__instance.join()
        except:
            pass

    def help():
        print('Press', colored('R', 'white', attrs=['bold']), 'to restart')

    def restart():
        print('Restarting...')
        cmd = [sys.executable, sys.executable, *sys.argv]
        print('Command:', cmd)
        DevMode.stop()
        pygame.quit()
        os.execl(*cmd)

    def run(self):
        while DevMode.__initialized:
            if not pygame.display.get_init():
                continue

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.unicode == 'R':
                        DevMode.restart()
            sleep(0.3)

    def join(self, timeout = None):
        DevMode.__initialized = False
        return super().join(timeout)
    
    def isInitialized():
        return DevMode.__initialized

def dprint(*values: object, sep: str | None = " ", end: str | None = "\n"):
    if DevMode.isInitialized():
        print(values, sep=sep, end=end)