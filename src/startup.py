from asyncio.windows_events import NULL
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="!")

# region Events

@bot.event
async def on_ready():
    print(f"{bot.user.name} is running...")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return()
    await bot.process_commands(message)

# endregion Events

# region Commands

@bot.command(name="hi")
async def say_hi(ctx):
    name = ctx.author.name
    response = f'Hello {name}'
    await ctx.send(response)


async def read_history(channel_to_read, server_member):
    counter = 0
    async for message in channel_to_read.history(limit=None):
        if message.author == server_member:
            counter += 1
    return counter


@bot.command(pass_context=True)
async def history(ctx, target_member: discord.Member, target_channel: discord.TextChannel = NULL):
    server = ctx.message.guild
    server_channels = server.text_channels

    if(target_channel == NULL):
        total_count = 0
        for server_channel in server_channels:
            total_count += await read_history(server_channel, target_member)
        await ctx.send(f'{target_member.display_name} has sent **{total_count}** messages in all channels.')
    else:
        await ctx.send(f'{target_member.display_name} has sent **{await read_history(target_channel, target_member)}** messages in the {target_channel.mention} channel.')

# endregion Commands

# readline() for first line only, allows to have multiple keys in one file
# strip() to remove the trailing newline "\n"
botKey = open("BotKey.txt").readline().strip()
bot.run(botKey)
