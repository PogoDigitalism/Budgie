import asyncio
from app import App

async def run():
    loop = asyncio.get_event_loop()

    a = App(loop)
    await a.show()

if __name__ == '__main__':
    # try:
    asyncio.run(run())
    # except:
    #     pass