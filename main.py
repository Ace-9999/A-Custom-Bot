import discord, time, random, asyncio, json, os
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.members = True
tdu = discord.Client(intents = intents)


@tdu.event
async def on_ready():
	print('Logged in')
	print("I'm online and working")
	for i in range(10000):
	    await tdu.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Peeps Flex on Normies"))
	    await asyncio.sleep(2000)
	    await tdu.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Freeloaders Freeload"))
	    await asyncio.sleep(900)
	    await tdu.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Members' Problems"))
	    await asyncio.sleep(900)
	    await tdu.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Modmail"))
	    await asyncio.sleep(900)

@tdu.event
async def on_member_join(member):
    guild = tdu.get_guild(799907027832537088)
    channel = guild.get_channel(811087796055965736)
    if member in guild.members:
        wlcm = discord.Embed(colour = discord.Colour.green(), title = f"{str(member)} Just Joined Us!", description = f"Give a warm welcome to to {member.mention}!")
        wlcm.set_thumbnail(url = f"{member.avatar_url}")
        wlcm.add_field(name = "Member Count", value = f"{len(guild.members)}", inline = False)
        await channel.send(embed = wlcm)
        await member.send("If you ever get banned appeal!\ndiscord.gg/DQVKQRHKQe\nAlso, make sure to verify in <#811087754653859841> and then take your roles in <#811087789248217130>.\nAnd please don't leave us <a:CatCri:817353340085731358>")
    else:
        return None

@tdu.event
async def on_member_remove(member):
    guild = tdu.get_guild(799907027832537088)
    channel = guild.get_channel(811087852540395551)
    if member not in guild.members:
        wl = discord.Embed(colour = discord.Colour.red())
        wl.set_author(name = "Peaky Dankers" , icon_url = "https://cdn.discordapp.com/attachments/773795863327408158/811112465332174888/pixil-gif-drawing_1.gif")
        wl.add_field(name = "An Idiot Just Dropped Out" , value = f"{member.mention} Just left\nWe are now **{len(guild.members)}** people\nTheir ID - {member.id}")
        wl.set_footer(text = "Did they just freeload? BAN THEM")
        await channel.send(embed = wl)
    else:
        return None

@tdu.event
async def on_message(message):
	message.content = message.content.lower()
	if message.author == tdu.user:
		return

	def get_afk_data():
		with open("afk.json", "r") as f:
			users = json.load(f)
		return users

	def open_afk(user):
		users = get_afk_data()
		with open("afk.json", "r") as f:
			users = json.load(f)
		if str(user.id) in users:
			return False
		else:
			users[str(user.id)] = {}
			users[str(user.id)]["afk_status"] = False
			users[str(user.id)]["afk_msg"] = None
			users[str(user.id)]["toggle"] = False
		with open("afk.json", "w") as f:
			json.dump(users, f)
		return True
		message.content = message.content.lower()



#AFK check
	user = message.author
	users = get_afk_data()
	open_afk(user)
	if users[str(user.id)]["afk_status"] == True and users[str(user.id)]["toggle"] == True:
		users[str(user.id)]["afk_status"] = False
		users[str(user.id)]["afk_msg"] = None
		users[str(user.id)]["toggle"] = False
		with open("afk.json", "w") as f:
			json.dump(users, f)
		afkembed = discord.Embed(title = f"{message.author.name} is no longer AFK", color = discord.Color.magenta())
		afkembed.set_thumbnail(url = message.author.avatar_url)
		afkembed.set_footer(text = "Your AFK has been removed")
		await message.channel.send(embed=afkembed)
	if len(message.mentions) != 0:
		user = message.mentions[0]
		users = get_afk_data()
		open_afk(user)
		x = users[str(user.id)]["afk_status"]
		if x == False:
			pass
		else:
			if message.author.id != 784617399907123250:
				reason = users[str(user.id)]["afk_msg"]
				afkembed = discord.Embed(title = f"{user.name} is AFK", description = f"{reason}", color = discord.Color.magenta())
				afkembed.set_thumbnail(url = user.avatar_url)
				afkembed.set_footer(text = "To set an AFK, use //afk [afk]")
				xx = await message.channel.send(embed=afkembed)
				await asyncio.sleep(10)
				await xx.delete()

#help menu
	if message.content.startswith("//help"):
		e = discord.Embed(title = 'Peaky Dankers Bot', colour=discord.Colour.teal())
		e.set_thumbnail(url = "https://cdn.discordapp.com/icons/799907027832537088/a_95a472a09f87d29ace0e482aa4c49c0d.gif?size=1024")
		e.add_field(name = "Lock & Unlock", value = '`//lock [reason]`, `//unlock`', inline = False)
		e.add_field(name = "Automated Heists", value = '`//heist [amount]`', inline = False)
		e.add_field(name = "Events", value = '`//event [details]`, `//evdone`', inline = False)
		e.add_field(name = "Slowmode", value = '`//sm [time e.g. 1m]`', inline = False)
		e.add_field(name = "8ball", value = '`//8ball [question]`', inline = False)
		e.add_field(name = "Complex AutoMath", value = '`Type some math like 100+200 *5-2000`', inline = False)
		e.add_field(name = "Purge", value = '`//purge [number of msgs]`', inline = False)
		e.add_field(name = "AFK", value = '`//afk [afk message]`', inline = False)
		e.set_footer(text = "NOTE: All [] are not supposed to be used.\nE.g. //heist 1 mil not //heist [1 mil]")
		await message.channel.send(embed=e)


#Giveaways [will be updated further soon]
	if message.content.startswith("//gstart"):
		if discord.utils.get(message.author.roles, name = "Giveaway Manager") is None:
			await message.channel.send('You need the Giveaway Manager Role to do this!')
			return
		cur = datetime.now()
		info = []
		info = message.content.split()
		if len(info) >= 4:
			dur = info[1]
			win = info[2]
		else:
			await message.channel.send("**Incorrect Syntax!** \n`//gstart <time> <winners> <prize>`")
		if len(info) >= 4:
			success = True
			if 'm' in dur:
				timing = (dur.strip('m'))
				endtime = cur + timedelta(minutes = int(timing))
				timing = timing + ' minutes'
			elif 'h' in dur:
				timing = (dur.strip('h'))
				endtime = cur + timedelta(hours = int(timing))
				timing = timing + ' hours'
			elif 'd' in dur:
				timing = (dur.strip('d'))
				endtime = cur + timedelta(days = int(timing))
				timing = timing + ' days'
			elif 's' in dur:
				timing = dur.strip('s')
				endtime = cur + timedelta(seconds = int(timing))
				timing = timing + ' seconds'
			else:
				await message.channel.send(f"Couldn't extract time from `{dur}` \nMake sure you put a `d` or `m` or `h` at the end!")
				success = False
			if 'w' in win:
				winners = int(win.strip('w'))
			else:
				await message.channel.send(f"Couldn't extract winners from `{win}` \nMake sure you put a `w` at the end!")
				success = False
			prize = info[3:]
			prize = str(prize)
			prize = str(prize.replace('[', ''))
			prize = str(prize.replace(']', ''))
			prize = str(prize.replace('\'', ''))
			prize = str(prize.replace(',', ''))
			print(prize)
		if success == True:
			await message.author.send(f"A giveaway will be created, \nDuration: `{timing}` \nWinners: `{winners}` \nPrize: `{prize}`")
			success = False
		format = "%d/%m/%Y %H:%M"
		a = cur.strftime(format)
		gem = discord.Embed(colour = discord.Colour.orange(), title = f"{prize}", description = f"React with :tada: to enter!\n\n**Winners**: {winners}\n**Duration**: {timing}\n**Host:** {message.author.mention}\n**Ends at:** {endtime}")
		await message.channel.send(":tada: **GIVEAWAY!** :tada:")
		gemm = await message.channel.send(embed = gem)
		await gemm.add_reaction('🎉')
		while True:
			if datetime.now() >= endtime:
				break
			await asyncio.sleep(30)

		new_msg = await message.channel.fetch_message(gemm.id)
		users = await new_msg.reactions[0].users().flatten()
		users.pop(users.index(tdu.user))
		if int(len(users)) < int(winners):
			await message.channel.send("A winner **could not be determined** due to inadequate amount of reactions!")
		else:
			g = gemm.guild.id
			c = gemm.channel.id
			m = gemm.id

			win_dm = discord.Embed(colour = discord.Colour.green(), title = f"You Won in {message.guild.name}!", description = f"[Message Link](https://discord.com/channels/{g}/{c}/{m})")
			win_dm.add_field(name = "Prize", value = f"{prize}")
			win_dm.set_footer(text = "Claim your prize ASAP!")
			ez = []
			for i in range(winners):
				winner = (random.choice(users))
				await winner.send(embed = win_dm)
				winner = str(winner)
				ez.append(winner)
			def convertor(list, separator):
				ezay = []
				ezay = separator.join(list)
				return ezay
			separator = ' '
			ezay = convertor(ez, separator)
			await message.channel.send(f"Congratulations to **{ezay}** for winning **{prize}**\nhttps://discord.com/channels/{g}/{c}/{m}")
			sep = "\n"
			ezay_2 = convertor(ez, sep)

			end_e = discord.Embed(colour = discord.Colour.dark_green(), description = f"[Message Link](https://discord.com/channels/{g}/{c}/{m})")
			end_e.set_author(name = "Your Giveaway Has Ended!")
			end_e.add_field(name = "Winners", value = f"{ezay_2}")
			await message.author.send(embed = end_e)

			gem2 = discord.Embed(colour = discord.Colour.dark_orange(), title = "This giveaway has ended!")
			gem2.add_field(name = "Winners", value = f"{ezay_2}")
			gem2.set_footer(text = f"Contact {message.author.display_name} for prize!")

			await gemm.edit(embed = gem2)

#End
	if message.content.startswith("//gend"):
		if discord.utils.get(message.author.roles, name = "Giveaway Manager") is None:
			await message.channel.send('You need the Giveaway Manager Role to do this!')
			return
		a = []
		a = message.content.split()
		mid = a[1]
		rm = await message.channel.fetch_message(mid)
		if rm.author.id != 807488775663124480:
			await message.channel.send("Sorry, this message isn't of a giveaway!")
			print(rm.author.id)
		else:
			new_msg = await message.channel.fetch_message(mid)
			users = await new_msg.reactions[0].users().flatten()
			users.pop(users.index(tdu.user))
			if int(len(users)) < 1:
				await message.channel.send("A winner **could not be determined** due to inadequate amount of reactions!")
			else:
				g = rm.guild.id
				c = rm.channel.id
				m = mid

				win_dm = discord.Embed(colour = discord.Colour.green(), title = f"You Won in {message.guild.name}!", description = f"[Message Link](https://discord.com/channels/{g}/{c}/{mid})")
				win_dm.set_footer(text = "Claim your prize ASAP!")
				winner = (random.choice(users))
				await winner.send(embed = win_dm)
				winner = str(winner)
				await message.channel.send(f"Congratulations to **{winner}** for winning the ending of\nhttps://discord.com/channels/{g}/{c}/{m}")
#Reroll
	if message.content.startswith("//greroll"):
		if discord.utils.get(message.author.roles, name = "Giveaway Manager") is None:
			await message.channel.send('You need the Giveaway Manager Role to do this!')
			return
		a = []
		a = message.content.split()
		mid = a[1]
		rm = await message.channel.fetch_message(mid)
		if rm.author.id != 807488775663124480:
			await message.channel.send("Sorry, this message isn't of a giveaway!")
			print(rm.author.id)
		else:
			new_msg = await message.channel.fetch_message(mid)
			users = await new_msg.reactions[0].users().flatten()
			users.pop(users.index(tdu.user))
			if int(len(users)) < 1:
				await message.channel.send("A winner **could not be determined** due to inadequate amount of reactions!")
			else:
				g = rm.guild.id
				c = rm.channel.id
				m = mid

				win_dm = discord.Embed(colour = discord.Colour.green(), title = f"You Won in {message.guild.name}!", description = f"[Message Link](https://discord.com/channels/{g}/{c}/{mid})")
				win_dm.set_footer(text = "Claim your prize ASAP!!")
				winner = (random.choice(users))
				await winner.send(embed = win_dm)
				winner = str(winner)
				await message.channel.send(f"Congratulations to **{winner}** for winning the reroll \nhttps://discord.com/channels/{g}/{c}/{m}")
				

#returing bot latency
	if message.content.startswith('//ping'):
		em = discord.Embed(title = 'Pong!', description = f'{round(tdu.latency*1000)} ms', colour = discord.Colour.blue())
		await message.channel.send(embed=em)

#AutoMath
	if message.content.startswith('1') or message.content.startswith('2') or message.content.startswith('3') or message.content.startswith('4') or message.content.startswith('5') or message.content.startswith('6') or message.content.startswith('7') or message.content.startswith('8') or message.content.startswith('9'):
		if '+' in message.content or '-' in message.content or '*' in message.content or '/' in message.content:
			x = eval(message.content)
			x2 = "{:,}".format(x)
			embed = discord.Embed(title = f"`{x2}`", description = f"Raw - `{x}`\nFinal - `{x2}`", colour = discord.Color.orange())
			await message.channel.send(embed=embed)

#8ball
	if message.content.startswith('//8ball'):
		q = message.content.replace('//8ball', '')
		choices = ['it is decidedly so', 'reply hazy, try again', 'my sources say no', 'that would be a yes', '100%', 'no doubt about it', 'I tried. But i couldn\'t get a reply. Try again']
		ans = random.choice(choices)
		em = discord.Embed(description = ans,colour = discord.Color.blue())
		em.set_author(name = q, icon_url = message.author.avatar_url)
		await message.channel.send(embed=em)

#verification
	if message.channel.id == 811087754653859841:
		if message.content.startswith('//verify'):
			await message.delete()
			memrole = discord.utils.get(message.guild.roles, name = "Member")
			await message.author.add_roles(memrole)
			await message.author.send('You were successfully verified in Peaky Dankers.')
		else:
			await message.delete()
			await message.author.send('Uh oh!\nPlease type only `//verify` in <#811087754653859841>!')

#Heisting
	if message.content.startswith('//heist'):
		if discord.utils.get(message.author.roles, name="Heist Manager") is None:
			await message.channel.send(
			    'You need the Heist Manager Role for this!')
			return
		else:
			amount = message.content.replace('//heist ', '')
			pingrole = discord.utils.get(message.guild.roles, name='💰| Heist Pong')
			person = message.mentions[0]
			if '!' in str(amount):
				amount = amount.replace(f"<@!{person.id}>", '')
			else:
				amount = amount.replace(f"<@{person.id}>", '')
			await message.channel.send(f'{pingrole.mention}')
			em = discord.Embed(
			    title='Heist Time! <a:Pepe_Heist:800807282014552082>',
			    description=
			    f"**Amount** - {amount}\n**Sponsor** - {person.mention}\n**Slowmode** - 5 minutes\n__**Things to do -**__\n:point_right: Keep 1000 coins in your wallet\n:point_right: Keep a life saver in your inventory\n:point_right: Thank the sponsor in chat!",
			    colour=discord.Colour.green())
			em.set_footer(text='Ready? React!')
			x = await message.channel.send(embed=em)
			await x.add_reaction('<a:Pepe_Heist:800807282014552082>')

#Giveaway and event pinging without giving permissions
	if message.content.startswith('//gw'):
		if discord.utils.get(message.author.roles,
		                     name="Giveaway Manager") is None:
			await message.channel.send('You need the Giveaway manager Role for this!')
			return
		else:
			prize = message.content.replace('//gw ', '')
			pingrole = discord.utils.get(message.guild.roles, name='🎉 | Giveaway Pong')
			await message.channel.send(f'{pingrole.mention}')
			em = discord.Embed(title='Giveaway Time!',
			                   description=f"{prize}\nHost - {message.author.mention}",
			                   colour=discord.Colour.green())
			em.set_footer(text='Peaky Dankers')
			await message.channel.send(embed=em)

	if message.content.startswith('//event'):
		if discord.utils.get(message.author.roles,
		                     name="Event Manager") is None:
			await message.channel.send('You need the Event manager Role for this!')
			return
		else:
			prize = message.content.replace('//event ', '')
			pingrole = discord.utils.get(message.guild.roles,
			                             name='💵 | Event Pong')
			await message.delete()
			await message.channel.send(f'{pingrole.mention}')
			em = discord.Embed(title='Event Time!', description=f"Details - {prize}\nHost - {message.author.mention}", colour=discord.Colour.green())
			em.set_footer(text='Peaky Dankers')
			await message.channel.send(embed=em)

#Lock and Unlock
	if message.content.startswith('//lock'):
		if message.author.guild_permissions.manage_channels == True or message.author.guild_permissions.administrator == True:
			overwrite = message.channel.overwrites_for(
				message.guild.default_role)
			overwrite.send_messages = False
			await message.channel.set_permissions(
				message.guild.default_role, overwrite=overwrite)
			if ' ' in message.content:
				x = message.content.replace('//lock ','')
			else:
				x = message.content.replace('//lock','')
			if x == '':
				embed = discord.Embed(title = 'Channel Locked :lock:', description = f'By - {message.author.mention} \nReason - None Given', colour = discord.Colour.magenta())
			else:
				embed = discord.Embed(title = 'Channel Locked :lock:', description = f'By - {message.author.mention} \nReason - {x}', colour = discord.Colour.magenta())
			await message.channel.send(embed=embed)
		else:
			await message.delete()

	if message.content.startswith('//unlock'):
		if message.author.guild_permissions.manage_channels == True or message.author.guild_permissions.administrator == True:
			overwrite = message.channel.overwrites_for(
				message.guild.default_role)
			overwrite.send_messages = True
			await message.channel.set_permissions(
				message.guild.default_role, overwrite=overwrite)
			embed = discord.Embed(title = 'Channel Unlocked :unlock:', description = f'By - {message.author.mention}', colour = discord.Colour.magenta())
			await message.channel.send(embed=embed)
		else:
			await message.delete()

#Purge
	if message.content.startswith('//purge'):
		if message.author.guild_permissions.manage_messages == True:
			lim = int(message.content.replace('//purge', ''))
			if lim < 1:
				await message.delete()
				await message.channel.send(f'Mhmm. Pretty sure i can\'t purge less than 1 messages {message.author.mention}.')
			else:
				await message.channel.purge(limit=lim+1)
				x = await message.channel.send(f'**Purged {lim} messages**')
				await asyncio.sleep(5)
				await x.delete()
		else:
			await message.delete()
			return

#Heist Donations [possible to edit code for applications]
	if message.content.startswith('//hdonate'):
		await message.channel.send(f'Ok {message.author.mention}. Check DMs')
		await message.author.send('How much are you donating?')
		po = await tdu.wait_for('message', check = lambda msg: msg.author.id == message.author.id and str(msg.channel.type) == 'private')
		await message.author.send('Do you have enough bank space?\nIf you dont type `need a bank` or else type `yes i have a bank`')
		a2 = await tdu.wait_for('message', check = lambda msg: msg.author.id == message.author.id and str(msg.channel.type) == 'private')
		await message.author.send('If you do have a bank, when should we heist you?\nIf you dont just type `N/A`')
		a7 = await tdu.wait_for('message', check = lambda msg: msg.author.id == message.author.id and str(msg.channel.type) == 'private')
		await message.author.send('Any requirements? If not, type `none`')
		a4 = await tdu.wait_for('message', check = lambda msg: msg.author.id == message.author.id and str(msg.channel.type) == 'private')
		await message.author.send('Any message to go along with the event? If not, type `none`')
		a5 = await tdu.wait_for('message', check = lambda msg: msg.author.id == message.author.id and str(msg.channel.type) == 'private')
		pongrole = discord.utils.get(message.guild.roles, name = 'Heist Manager')
		embed = discord.Embed(title = f"{message.author.name} is donating to us!", colour = discord.Colour.magenta())
		appch = discord.utils.get(message.guild.channels, name = '🎁│donations-channel')
		await appch.send(pongrole.mention)
		embed = discord.Embed(title = f"{message.author.name} is donating to us!", colour = discord.Colour.magenta())
		embed.add_field(name = 'Heist Amount:', value = po.content)
		embed.add_field(name = 'Status of bank:', value = a2.content, inline = False)
		embed.add_field(name = 'Requirements:', value = a4.content, inline = False)
		embed.add_field(name = 'Preffered heist time:', value = a2.content, inline = False)
		embed.add_field(name = 'Message:', value = a5.content, inline = False)
		await appch.send(embed=embed)
		await message.author.send('Your dono application has been successfully sent!')

#Slowmode
	if message.content.startswith('//sm'):
		if message.author.guild_permissions.manage_channels == True:
			no_time = message.content.replace('//sm ', '')
			if 's' in no_time:
				t = no_time.strip('s')
				t = int(t)
				f_time = int(t)
				if t == 0:
					await message.channel.send(f'The Slowmode has been removed.')
				else:
					await message.channel.send(f'The Slowmode is now {t} seconds.')

			if 'h' in no_time:
				t = no_time.strip('h')
				t = int(t)
				f_time = int(t * 3600)
				await message.channel.send(f'The Slowmode is now {t} hours.')

			if 'm' in no_time:
				t = no_time.strip('m')
				t = int(t)
				f_time = int(t * 60)
				await message.channel.send(f'The Slowmode is now {t} minutes.') 
			await message.channel.edit(slowmode_delay=f_time)
		else:
			await message.delete()
			return


#AFK
	if message.content.startswith("//afk"):
		user = message.author
		users = get_afk_data()
		open_afk(user)
		reason = message.content.replace('//afk', '')
		if "@" in reason:
			await message.channel.send("Sorry, don't you try pinging people in your afk!")
		if reason == 'remove' or reason == 'r':
			users[str(user.id)]["afk_status"] = False
			users[str(user.id)]["afk_msg"] = None
			users[str(user.id)]["toggle"] = False
			with open("afk.json", "w") as f:
				json.dump(users, f)
			afkembed = discord.Embed(title = f"{message.author.name} is no longer AFK", color = discord.Color.magenta())
			afkembed.set_thumbnail(url = message.author.avatar_url)
			afkembed.set_footer(text = "Your AFK has been removed")
			await message.channel.send(embed=afkembed)
		else:
			if users[str(user.id)]["afk_status"] == True:
				if 'edit' in reason:
					new_msg = reason.replace('edit', '')
					users[str(user.id)]["afk_status"] = True
					users[str(user.id)]["afk_msg"] = new_msg
					with open("afk.json", "w") as f:
						json.dump(users, f)
					afkembed = discord.Embed(title = f"{message.author.name}'s AFK has been edited.", description = f"{new_msg}", color = discord.Color.magenta())
					afkembed.set_thumbnail(url = message.author.avatar_url)
					afkembed.set_footer(text = "When you are pinged this embed shall pop-up")
					await message.channel.send(embed=afkembed)
					return
				else:
					msg = users[str(user.id)]["afk_msg"]
					await message.channel.send(f'Hey!\nI see that you already have and AFK set: **{msg}**\nTo edit this use `//afk edit [new afk]`.')
					return

			if reason == '' or reason == ' ':
				reason = 'Just AFK, no reason'
			users[str(user.id)]["afk_status"] = True
			users[str(user.id)]["afk_msg"] = reason
			with open("afk.json", "w") as f:
				json.dump(users, f)
			afkembed = discord.Embed(title = f"{message.author.name} is now AFK", description = f"{reason}", color = discord.Color.magenta())
			afkembed.set_thumbnail(url = message.author.avatar_url)
			afkembed.set_footer(text = "When you are pinged an embed shall pop-up")
			await message.channel.send(embed=afkembed)
			await asyncio.sleep(300)
			users[str(user.id)]["toggle"] = True
			with open("afk.json", "w") as f:
				json.dump(users, f)

#Logging dank memer stuff [made custom]
	if message.content.startswith('pls enable') or message.content.startswith('pls disable') and message.author.guild_permissions.manage_guild == True:
		x = tdu.get_guild(799907027832537088)
		ch = x.get_channel(816277203800817686)
		if message.content.startswith('pls enable'):
			await ch.send(f'{message.author.name} successfully enabled something in {message.channel.mention} by running `{message.content}`')
		elif message.content.startswith('pls disable'):
			await ch.send(f'{message.author.name} successfully disabled something in {message.channel.mention} by running `{message.content}`')

	if message.content.startswith('pls rob') or message.content.startswith('pls steal'):
		em = discord.Embed(title = 'Rob and Heist are strictly disabled here!', description = '- Rob, steal, and heist is strictly forbidden in this server. Rest assured, your coins will be safe as the rob and heist commands are disabled server wide!\n\n**Note:** joining to rob and then quickly leaving may result in a ban!', colour = discord.Color.blue())
		em.set_footer(text = 'Enjoy your stay in Peaky Dankers!', icon_url = message.author.avatar_url)
		await message.channel.send(embed = em)


tdu.run('TOKEN')

