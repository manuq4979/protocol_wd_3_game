import asyncio
import time 
from aioconsole import ainput

class KEY:
    @staticmethod
    def get_instance():
        if "_instance" not in KEY.__dict__:
            KEY._instance = KEY()
            return KEY._instance
        else:
            return KEY._instance
    
    def __init__(self):
        self.key = ""
    def set_key(self, key):
        self.key = key
    def get_key(self):
        return self.key
    
async def wait_key():
    K = KEY.get_instance()
    key = await ainput()
    K.set_key(key)
    
    
async def main(def_animation_cycle):
    task1 = asyncio.create_task(wait_key())
    task2 = asyncio.create_task(def_animation_cycle())
    await task1
    await task2

def starting_anim(def_animation_cycle):
    # print(time.strftime ('%X'))
    asyncio.run(main(def_animation_cycle))
    # print(time.strftime ('%X'))