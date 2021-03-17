import discord, time, datetime, random, asyncio, json, os

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
        await channel.send(member.mention)
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
        wl.add_field(name = "A Bitch Just Dropped Out" , value = f"{member.mention} Just left\nWe are now **{len(guild.members)}** people\nTheir ID - {member.id}")
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
				afkembed.set_footer(text = "To set an AFK, use p!afk [afk]")
				xx = await message.channel.send(embed=afkembed)
				await asyncio.sleep(10)
				await xx.delete()

	if message.content.startswith('p!8ball'):
		q = message.content.replace('p!8ball', '')
		choices = ['it is decidedly so', 'reply hazy, try again', 'my sources say no', 'that would be a yes', '100%', 'no doubt about it', 'nah, i wouldnt keep my hopes high on that', 'imma say no on that']
		ans = random.choice(choices)
		em = discord.Embed(description = ans,colour = discord.Color.blue())
		em.set_author(name = q, icon_url = message.author.avatar_url)
		await message.channel.send(embed=em)

	if message.content.startswith('p!ping'):
		em = discord.Embed(title = 'Pong!', description = f'{round(tdu.latency*1000)} ms', colour = discord.Colour.blue())
		await message.channel.send(embed=em)
	if message.content.startswith('1') or message.content.startswith('2') or message.content.startswith('3') or message.content.startswith('4') or message.content.startswith('5') or message.content.startswith('6') or message.content.startswith('7') or message.content.startswith('8') or message.content.startswith('9'):
		if '+' in message.content or '-' in message.content or '*' in message.content or '/' in message.content:
			x = eval(message.content)
			x2 = "{:,}".format(x)
			embed = discord.Embed(title = f"`{x2}`", description = f"Raw - `{x}`\nFinal - `{x2}`", colour = discord.Color.orange())
			await message.channel.send(embed=embed)

	if message.content.startswith("p!help"):
		e = discord.Embed(title = 'Peaky Dankers Bot', colour=discord.Colour.teal())
		e.set_thumbnail(url = "https://cdn.discordapp.com/icons/799907027832537088/a_95a472a09f87d29ace0e482aa4c49c0d.gif?size=1024")
		e.add_field(name = "Lock & Unlock", value = '`p!lock [reason]`, `p!unlock`', inline = False)
		e.add_field(name = "Automated Heists", value = '`p!heist [amount]`', inline = False)
		e.add_field(name = "Events", value = '`p!event [details]`, `p!evdone`', inline = False)
		e.add_field(name = "Slowmode", value = '`p!sm [time e.g. 1m]`', inline = False)
		e.add_field(name = "8ball", value = '`p!8ball [question]`', inline = False)
		e.add_field(name = "Complex AutoMath", value = '`Type some math like 100+200 *5-2000`', inline = False)
		e.add_field(name = "Purge", value = '`p!purge [number of msgs]`', inline = False)
		e.add_field(name = "AFK", value = '`p!afk [afk message]`', inline = False)
		e.set_footer(text = "NOTE: All [] are not supposed to be used.\nE.g. p!heist 1 mil not p!heist [1 mil]")
		await message.channel.send(embed=e)

	if message.content.startswith('p!heist'):
		if discord.utils.get(message.author.roles, name="Heist Manager") is None:
			await message.delete()
			await message.channel.send(
			    'You need the Heist Manager Role for this!')
			return
		else:
			amount = message.content.replace('p!heist ', '')
			await message.delete()
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

	if message.content.startswith('pls rob') or message.content.startswith('pls steal'):
		em = discord.Embed(title = 'Rob and Heist are strictly disabled here!', description = '- Rob, steal, and heist is strictly forbidden in this server. Rest assured, your coins will be safe as the rob and heist commands are disabled server wide!\n\n**Note:** joining to rob and then quickly leaving may result in a ban!', colour = discord.Color.blue())
		em.set_footer(text = 'Enjoy your stay in Peaky Dankers!', icon_url = message.author.avatar_url)
		await message.channel.send(embed = em)
	
	if message.content.startswith('p!gw'):
		if discord.utils.get(message.author.roles,
		                     name="Giveaway Manager") is None:
			await message.channel.send('You need the Giveaway manager Role for this!')
			return
		else:
			prize = message.content.replace('p!gw ', '')
			pingrole = discord.utils.get(message.guild.roles, name='🎉 | Giveaway Pong')
			await message.delete()
			await message.channel.send(f'{pingrole.mention}')
			em = discord.Embed(title='Giveaway Time!',
			                   description=f"{prize}\nHost - {message.author.mention}",
			                   colour=discord.Colour.green())
			em.set_footer(text='Peaky Dankers')
			await message.channel.send(embed=em)


	if message.content.startswith('p!event'):
		if discord.utils.get(message.author.roles,
		                     name="Event Manager") is None:
			await message.channel.send('You need the Event manager Role for this!')
			return
		else:
			prize = message.content.replace('p!event ', '')
			pingrole = discord.utils.get(message.guild.roles,
			                             name='💵 | Event Pong')
			await message.delete()
			await message.channel.send(f'{pingrole.mention}')
			em = discord.Embed(title='Event Time!', description=f"Details - {prize}\nHost - {message.author.mention}", colour=discord.Colour.green())
			em.set_footer(text='Peaky Dankers')
			await message.channel.send(embed=em)

	if message.content.startswith('p!unlock'):
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

	if message.content.startswith('p!purge'):
		if message.author.guild_permissions.manage_messages == True:
			lim = int(message.content.replace('p!purge', ''))
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

	if message.content.startswith('p!lock'):
		if message.author.guild_permissions.manage_channels == True or message.author.guild_permissions.administrator == True:
			overwrite = message.channel.overwrites_for(
				message.guild.default_role)
			overwrite.send_messages = False
			await message.channel.set_permissions(
				message.guild.default_role, overwrite=overwrite)
			if ' ' in message.content:
				x = message.content.replace('p!lock ','')
			else:
				x = message.content.replace('p!lock','')
			if x == '':
				embed = discord.Embed(title = 'Channel Locked :lock:', description = f'By - {message.author.mention} \nReason - None Given', colour = discord.Colour.magenta())
			else:
				embed = discord.Embed(title = 'Channel Locked :lock:', description = f'By - {message.author.mention} \nReason - {x}', colour = discord.Colour.magenta())
			await message.channel.send(embed=embed)
		else:
			await message.delete()

	if message.content.startswith('p!hdonate'):
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

	if message.content.startswith('p!sm'):
		if message.author.guild_permissions.manage_channels == True:
			no_time = message.content.replace('p!sm ', '')
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
    #Setting Up AFK
	if message.content.startswith("p!afk"):
		user = message.author
		users = get_afk_data()
		open_afk(user)
		reason = message.content.replace('p!afk', '')
		if "@" in reason:
			await message.channel.send("Sorry, don't you try pinging people in your afk!")
		else:
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
			await asyncio.sleep(100)
			users[str(user.id)]["toggle"] = True
			with open("afk.json", "w") as f:
				json.dump(users, f)
                
	if message.content.startswith('pls enable') or message.content.startswith('pls disable') and message.author.guild_permissions.manage_guild == True:
		x = tdu.get_guild(799907027832537088)
		ch = x.get_channel(816277203800817686)
		if message.content.startswith('pls enable'):
			await ch.send(f'{message.author.name} successfully enabled something in {message.channel.mention} by running `{message.content}`')
		elif message.content.startswith('pls disable'):
			await ch.send(f'{message.author.name} successfully disabled something in {message.channel.mention} by running `{message.content}`')
tdu.run('ODA3NDg4Nzc1NjYzMTI0NDgw.YB4uhg.ZRdXCTg6Z2woQVEtvSVD2gzd99I')

