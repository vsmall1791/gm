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
        #Format
        #Friend_id : "friend_name"
        }

"""
Your discord authentication token
Can be found with the following steps:
    1. Open discord on a web browser
    2. Open Developer console
    3. Open Network tab
    4. Reload the page
    5. In the filter bar type "/api"
    6. Click on different entries until you find one that has an 'authentication attribute', copy that token and use that below

                                ***WARNING***
    DO NOT share your token it can be used by someone to access your account
"""
TOKEN = "Your token ID here"

gm = gm(TOKEN, frens)
gm.run()
