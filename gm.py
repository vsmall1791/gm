import discord
import sys

class gm:
    def __init__(self, token, frens):
        self.token = token
        self.frens = frens
        self.client = discord.Client()

        @self.client.event
        async def on_ready():
            for fren, fren_name in self.frens.items():
                user = await self.client.fetch_user(fren)
                await user.send(sys.argv[1])
                print(f'\"{sys.argv[1]}\" sucessfully sent to {fren_name}')

    def run(self):
        self.client.run(self.token)

frens = {
        #Format: Friend_id : "friend_name"
        }

#Your token ID here
TOKEN = ""

gm = gm(TOKEN, frens)
gm.run()
