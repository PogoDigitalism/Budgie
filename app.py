from utils.decorators import 
import customtkinter as ctk
import asyncio

class App(ctk.CTk):
    def __init__(self, loop) -> None:
        super().__init__()

        self.loop: asyncio.AbstractEventLoop = loop

        self.wm_protocol("WM_DELETE_WINDOW", self.on_close)

    # Async mainloop
    async def show(self):
        while True:
            self.update()
            await asyncio.sleep(.01)

    def on_close(self):
        self.destroy()
        self.loop.stop()