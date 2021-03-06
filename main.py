import discord
from discord.ext import commands
import json
import random
import sys
import traceback

intents = discord.Intents.all()
client = commands.Bot(command_prefix='l!', intents=intents)

@client.event
async def on_ready():
	print("hello world!")
	animezome = client.get_guild(816079042423947266)
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"Spotify"))

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()


# VVVVVV events VVVVVV


@client.event
async def on_member_join(member):
	welcome = discord.utils.get(member.guild.channels, id=816079044717969442)
	role = discord.utils.get(member.guild.roles, id=816079788333596692)

	await member.add_roles(role)
	await welcome.send(f"{member.mention} has joined the server\n\nwe now have {len(member.guild.members)} members")
	await member.send(f"welcome to **{member.guild.name}**")

@client.event
async def on_member_remove(member):
	welcome = discord.utils.get(member.guild.channels, id=816079044717969442)

	await welcome.send(f"{member.mention} has left the server\n\nwe now have {len(member.guild.members)} members")

@client.event
async def on_command_error(ctx:commands.Context, exception):
	embed = discord.Embed(color=discord.Color.red())
	if type(exception) is commands.errors.MissingRequiredArgument:
		embed.title = "You forgot an argument"
		embed.description = f"The syntax to `{client.command_prefix}{ctx.command.name}` is `{client.command_prefix}{ctx.command.name} {ctx.command.signature}`."
		await ctx.send(embed=embed)
	elif type(exception) is commands.CommandNotFound:
		embed.title = "Invalid command"
		embed.description = f"The command you just tried to use is invalid. Use `{client.command_prefix}help` to see all commands."
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(exception), exception, exception.__traceback__, file=sys.stderr)

client.run(token)
