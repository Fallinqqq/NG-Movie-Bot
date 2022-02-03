import discord
from discord.ext import commands

botIntents = discord.Intents.default()
botIntents.members = True

bot = commands.Bot(command_prefix="!", intents=botIntents)


@bot.event
async def on_ready():
    print("Bot is running...")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return()
    await bot.process_commands(message)


@bot.command(name="hi")
async def say_hi(ctx):
    name = ctx.author.name
    response = f'Hello {name}'
    await ctx.send(response)


@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def members(ctx, *args):
    server = ctx.message.guild
    role_name = (' '.join(args))
    role_id = server.roles[0]
    for role in server.roles:
        if role_name == role.name:
            role_id = role
            break
    else:
        await ctx.send(f"Role '{role_name}' doesn't exist")
        return
    for member in server.members:
        for role in member.roles:
            if(role.name == role_id.name):
                await ctx.send(f"{member.display_name} - {member.id}")


#readline() for first line only, allows to have multiple keys in one file
#strip() to remove the trailing newline "\n"
botKey = open("BotKey.txt").readline().strip()
bot.run(botKey)
