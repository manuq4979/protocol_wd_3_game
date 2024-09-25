import asyncio
import time 
from aioconsole import ainput

key = ""
async def wait_key():
    global key
    key = await ainput()
    
    
async def main(def_animation_cycle):
    task1 = asyncio.create_task(wait_key())
    task2 = asyncio.create_task(def_animation_cycle())
    await task1
    await task2

def starting_anim(def_animation_cycle):
    # print(time.strftime ('%X'))
    asyncio.run(main(def_animation_cycle))
    # print(time.strftime ('%X'))