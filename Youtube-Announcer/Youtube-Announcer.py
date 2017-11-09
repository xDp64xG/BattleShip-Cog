import discord
from discord.ext import commands

try: # check if BeautifulSoup4 is installed
	from bs4 import BeautifulSoup
	soupAvailable = True
except:
	soupAvailable = False
import aiohttp

class YTAnnouncer:
	"""My custom cog that does stuff!"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def update(self):
		List = []
		Link = ""
		#await self.bot.say("Get ready")
		i = 0
		print('Act')
		"""This does stuff!"""
		url = 'https://www.youtube.com/channel/UCJqiR6dpN3PqoNetKt-RB5w/videos'
		async with aiohttp.get(url) as response:
			soup = BeautifulSoup(await response.text(), "html.parser")
		#try:
		print('Try')
		print("Links")
		#32
		def Make_List(Lists):
			Link = ""
			Video = ""
			Dict = []
			Dict2 = []
			for var in Lists.find_all("a"):
				Video = str(var.get("title"))
				if Video == None or Video == "None" or Video == "":
					Video = ""
					#22
					#32
				Dict.append(Video)
				Link = str(var.get("href"))
				if Link == None or Link == "None" or Link == "":
					Video = ""

				Dict2.append(Link)
				#Link = str(var)
				#print(Link)
				"""if var != None or var != "":
					for var2 in Lists.find(id="video_title"):
						var2.get("video")
						print(Link)"""
			LatestLink = Dict2[32]
			LatestVideo = Dict[32]
			Main = 'https://www.youtube.com'
			LatestLink = Main + LatestLink
			#print(LatestVideo)
			#print("Videos \n",Dict[32:33])
			#print("Links \n", Dict2[32:33])
			Vid = ("Video: " + LatestVideo)
			Lin = ("Link: " + LatestLink)
			print("Video: ", LatestVideo)
			print("Link: ", LatestLink)
			Final = Vid, Lin
			#await self.bot.say(Vid, Lin)
			
		

			embed=discord.Embed(
				title="Latest Upload!", 
				description="Here it is:", 
				color=0x207cee)
			embed.set_author(
				name="Dp Bot", 
				icon_url='https://cdn.discordapp.com/attachments/365496580490395649/378066120420098048/dp_bot.png')
			embed.set_thumbnail(
				url='https://cdn.discordapp.com/attachments/365496580490395649/378066486620585997/youtube-icon.png')
			embed.add_field(
				name=Vid, 
				value=Lin, 
				inline=True)
			return embed

		Print = Make_List(soup)
		#print(Print[0])
		#print(Print[1])
		#await self.bot.say(Print[0])
		#await self.bot.say(Print[1])
		await self.bot.say(embed=Print)

def setup(bot):
	bot.add_cog(YTAnnouncer(bot))


