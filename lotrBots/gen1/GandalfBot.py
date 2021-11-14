import discord
from readToken import read_token


class GandalfBot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        pass


client = GandalfBot()
client.run(read_token('../../token.txt', 1))
