from csv import Error
import os
import sys
import types
import pygame
from termcolor import colored
import importlib
import screens
import core
import entities
import errors
import graphics
import models
import objects
import windows


class DevMode:
    __initialized:bool = False
    __instance = None
    __app = None

    def __init__(self):
        if DevMode.__instance != None:
            raise Error('Dev mode already has an instance running')

        DevMode.__initialized = True
        DevMode.__instance = self

    def init(app):
        print('Entering dev mode')

        DevMode.__app = app
        DevMode.help()
        
        DevMode()

    def help():
        print('Press', colored('R', 'white', attrs=['bold']), 'to restart')
        if DevMode.__app != None:
            print('Press', colored('r', 'white', attrs=['bold']), 'to reload')

    def restart():
        print('Restarting...')
        cmd = [sys.executable, sys.executable, *sys.argv]
        print('Command:', cmd)
        pygame.quit()
        os.execl(*cmd)
        
    def reload():
        dprint('Reloading...')
        modules = [
            screens,
            core,
            entities,
            errors,
            graphics,
            models,
            objects,
            windows
        ]

        visited = set()

        def _reload(mod):
            if mod in visited:
                return
            
            visited.add(mod)

            for name in dir(mod):
                attr = getattr(mod, name)
                if isinstance(attr, types.ModuleType):
                    if attr.__name__.startswith(mod.__name__):
                        _reload(attr)

            importlib.reload(mod)
                
        for mod in modules:
            _reload(mod)
            
        print(f'Reloaded {visited.__len__()} modules')
        
        DevMode.__app.refresh()
        

    def update(events:list[pygame.event.Event]):
        if not pygame.display.get_init():
            return

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.unicode == 'R':
                    DevMode.restart()
                elif event.unicode == 'r':
                    DevMode.reload()
    
    def isInitialized():
        return DevMode.__initialized

def dprint(*values: object, sep: str | None = " ", end: str | None = "\n"):
    if DevMode.isInitialized():
        print(*values, sep=sep, end=end)