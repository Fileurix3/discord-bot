import discord
from discord.ext import commands
from config import *
import sqlite3

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command("help")

#id of the first role (for 0 levl)
first_role = 1157396689934622725

#role id by level
role_lvl_10 = 1187625125495967774
role_lvl_50 = 1187625146962411532
role_lvl_100 = 1187625182597226526
role_lvl_200 = 1187625204181106719
role_lvl_500 = 1187625220853485589
role_lvl_1000 = 1187998108387389542

#level per message
level_message = 0.05

connection = sqlite3.connect("server.db")
cursor = connection.cursor()

@bot.event
async def on_ready():
    print(f'{bot.user} is ready to work!')
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            name TEXT,
            id INT,
            lvl INT
    )""")
    for guild in bot.guilds:
        for member in guild.members:
            if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
                cursor.execute(f"INSERT INTO users VALUES ('{member}','{member.id}', 0)")
            else:
                pass
    connection.commit()

#when a user logs into the server
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id=first_role)
    await member.add_roles(role)
    
    if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
        cursor.execute(f"INSERT INTO users VALUES ('{member}','{member.id}', 0)")
        connection.commit()
    else:
        pass

@bot.event
async def on_message(message):
        await bot.process_commands(message)
        cursor.execute(f"UPDATE users SET lvl = ROUND(lvl + {level_message}, 2) WHERE id = {message.author.id}")
        connection.commit()

        result = cursor.execute(f"SELECT name, lvl FROM users WHERE id = {message.author.id}").fetchone()
        
        if result and result[1] == 10:
            role = discord.utils.get(message.guild.roles, id=role_lvl_10)
            member = discord.utils.get(message.guild.members, name=result[0])
            await member.add_roles(role)

            await message.channel.send(embed = discord.Embed(
                title = f"{result[0]} reached level 10",
                description = f"gets the role {message.guild.get_role(role_lvl_10).mention}",
                color=discord.Color.blue()
            ))
        elif result and result[1] == 50:
            role = discord.utils.get(message.guild.roles, id=role_lvl_50)
            member = discord.utils.get(message.guild.members, name=result[0])
            await member.add_roles(role)

            await message.channel.send(embed = discord.Embed(
                title = f"{result[0]} reached level 50!",
                description = f"gets the role {message.guild.get_role(role_lvl_50).mention}",
                color=discord.Color.blue()
            ))
        elif result and result[1] == 100:
            role = discord.utils.get(message.guild.roles, id=role_lvl_100)
            member = discord.utils.get(message.guild.members, name=result[0])
            await member.add_roles(role)

            await message.channel.send(embed = discord.Embed(
                title = f"{result[0]} reached level 100!",
                description = f"gets the role {message.guild.get_role(role_lvl_100).mention}",
                color=discord.Color.blue()
            ))
        elif result and result[1] == 200:
            role = discord.utils.get(message.guild.roles, id=role_lvl_200)
            member = discord.utils.get(message.guild.members, name=result[0])
            await member.add_roles(role)

            await message.channel.send(embed = discord.Embed(
                title = f"{result[0]} reached level 200!",
                description = f"gets the role {message.guild.get_role(role_lvl_200).mention}",
                color=discord.Color.blue()
            ))
        elif result and result[1] == 500:
            role = discord.utils.get(message.guild.roles, id=role_lvl_500)
            member = discord.utils.get(message.guild.members, name=result[0])
            await member.add_roles(role)

            await message.channel.send(embed = discord.Embed(
                title = f"{result[0]} reached level 500!",
                description = f"gets the role {message.guild.get_role(role_lvl_500).mention}",
                color=discord.Color.blue()
            ))
        elif result and result[1] == 1000:
            role = discord.utils.get(message.guild.roles, id=role_lvl_1000)
            member = discord.utils.get(message.guild.members, name=result[0])
            await member.add_roles(role)

            await message.channel.send(embed = discord.Embed(
                title = f"{result[0]} reached level 1000!",
                description = f"gets the role {message.guild.get_role(role_lvl_1000).mention}",
                color=discord.Color.blue()
            ))

#add level
@bot.command()
@commands.has_permissions(administrator=True)
async def add(message, member: discord.Member = None, amout:float = None):
    if member is None:
        await message.send(f"specify the user")
    else:
        if amout is None:
            await message.send("indicate the number of levels")
        elif amout < 0:
            await message.send("cannot be specified less than 0")
        else:
            cursor.execute(f"UPDATE users SET lvl = ROUND(lvl + {amout}, 1) WHERE id = {member.id}")
            connection.commit()
            await message.send(embed = discord.Embed(
                description = f"user level **{member}** increased by {amout}",
                color=discord.Color.blue()
            ))

#reduce level
@bot.command()
@commands.has_permissions(administrator=True)
async def reduce(message, member: discord.Member = None, amout:float = None):
    if member is None:
        await message.send(f"specify the user")
    else:
        if amout is None:
            await message.send("indicate the number of levels")
        elif amout < 0:
            await message.send("cannot be specified less than 0")
        else:
            cursor.execute(f"UPDATE users SET lvl = ROUND(lvl - {amout}, 1) WHERE id = {member.id}")
            connection.commit()

            await message.send(embed = discord.Embed(
                description = f"user level **{member}** reduced by {amout}",
                color=discord.Color.blue()
            ))

#change level
@bot.command()
@commands.has_permissions(administrator=True)
async def change(message, member: discord.Member = None, amout:float = None):
    if member is None:
        await message.send(f"specify the user")
    else:
        if amout is None:
            await message.send("indicate the number of levels")
        elif amout < 0:
            await message.send("cannot be specified less than 0")
        else:
            cursor.execute(f"UPDATE users SET lvl = ROUND({amout}, 1) WHERE id = {member.id}")
            connection.commit()

            await message.send(embed = discord.Embed(
                description = f"user level **{member}** changed to {amout}",
                color=discord.Color.blue()
            ))

@bot.command()
async def leaderboard(message):
    count = 0
    embed = discord.Embed(
        title="top 10 by level",
        color=discord.Color.blue()
        )
    for i in cursor.execute(f"SELECT name, lvl FROM users ORDER BY lvl DESC LIMIT 10"):
        count += 1
        embed.add_field(
            name = f"{count}: {i[0]}",
            value = f"level: {i[1]}",
            inline = False
        )
    await message.channel.send(embed = embed)

#level
@bot.command()
async def level(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(embed = discord.Embed(
            description = f"user level **{ctx.author}**, **{cursor.execute(f"SELECT lvl FROM users WHERE id = {ctx.author.id}").fetchone()[0]} lvl**",
            color=discord.Color.blue()
        ))
    else:
        await ctx.send(embed = discord.Embed(
            description = f"user level **{member}**, **{cursor.execute(f"SELECT lvl FROM users WHERE id = {member.id}").fetchone()[0]} lvl**",
            color=discord.Color.blue()
        ))

#clearing chat
@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, a = 1000):
    await ctx.channel.purge(limit=a)

#bot token
bot.run("token")