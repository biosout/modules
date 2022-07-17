from .. import loader
from asyncio import sleep

@loader.tds
class ForeverOnlineMod(loader.Module):
    """Постоянный онлайн"""
    strings = {'name': 'Forever Online'}

    async def client_ready(self, client, db):
        self.db = db

    async def onlinecmd(self, message):
        """Запустить постоянный онлайн"""
        if not self.db.get("Forever Online", "status"):
            self.db.set("Forever Online", "status", True)
            await message.edit("Постоянный онлайн включенᕙ( ͡° ͜ʖ ͡°)ᕗ")
            while self.db.get("Forever Online", "status"):
                await message.client(__import__("telethon").functions.account.UpdateStatusRequest(offline=False))
                await sleep(60)

        else:
            self.db.set("Forever Online", "status", False)
            await message.edit("Постоянный онлайн выключен¯\_(ツ)_/¯")