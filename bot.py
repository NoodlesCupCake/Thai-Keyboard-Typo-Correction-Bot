import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import re

load_dotenv()

# Your bot token
TOKEN = os.getenv('DISCORD_TOKEN')

# A dictionary to map English typo to Thai text
eng2thai = {
    '1': 'ๅ',
    '!': '+',
    '@': '๑',
    '2': '/',
    '3': '-',
    '#': '๒',
    '4': 'ภ',
    '$': '๓',
    '5': 'ถ',
    '%': '๔',
    '6': 'ุ',
    '^': 'ู',
    '7': 'ึ',
    '&': '฿',
    '8': 'ค',
    '*': '๕',
    '9': 'ต',
    '': '๖',
    '0': 'จ',
    ')': '๗',
    '-': 'ข',
    '_': '๘',
    '=': 'ช',
    '+': '๙',
    'q': 'ๆ',
    'Q': '๐',
    'w': 'ไ',
    'W': '"',
    'e': 'ำ',
    'E': 'ฎ',
    'r': 'พ',
    'R': 'ฑ',
    't': 'ะ',
    'T': 'ธ',
    'y': 'ั',
    'Y': 'ํ',
    'u': 'ี',
    'U': '๊',
    'i': 'ร',
    'I': 'ณ',
    'o': 'น',
    'O': 'ฯ',
    'p': 'ย',
    'P': 'ญ',
    '[': 'บ',
    '{': 'ฐ',
    ']': 'ล',
    '}': ',',
    '\\': 'ฃ',
    '|': 'ฅ',
    'a': 'ฟ',
    'A': 'ฤ',
    's': 'ห',
    'S': 'ฆ',
    'd': 'ก',
    'D': 'ฏ',
    'f': 'ด',
    'F': 'โ',
    'g': 'เ',
    'G': 'ฌ',
    'h': '้',
    'H': '็',
    'j': '่',
    'J': '๋',
    'k': 'า',
    'K': 'ษ',
    'l': 'ส',
    'L': 'ศ',
    ';': 'ว',
    ':': 'ซ',
    '\'': 'ง',
    '"': '.',
    'z': 'ผ',
    'Z': '',
    'x': 'ป',
    'X': ')',
    'c': 'แ',
    'C': 'ฉ',
    'v': 'อ',
    'V': 'ฮ',
    'b': 'ิ',
    'B': 'ฺ',
    'n': 'ท',
    'N': '์',
    'm': 'ท',
    'M': '?',
    ',': 'ม',
    '<': 'ฒ',
    '.': 'ใ',
    '>': 'ฬ',
    '/': 'ฝ',
    '?': 'ฦ',
    ' ': ' ',
}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

user_toggles = {}

@bot.event
async def on_ready():
    print(f'{bot.user.name} ได้เชื่อมต่อเข้าสู่เซิร์ฟเวอร์ Discord!')

@bot.command(name='เปิดบอท')
async def enable_bot(ctx):
    user_id = ctx.author.id
    user_toggles[user_id] = True
    user_name = ctx.author.display_name
    await ctx.send(f"การใช้งานบอทแก้คำผิดอัตโนมัติได้ถูก `เปิด` แล้วสำหรับคุณ `{user_name}`")

@bot.command(name='ปิดบอท')
async def disable_bot(ctx):
    user_id = ctx.author.id
    user_toggles[user_id] = False
    user_name = ctx.author.display_name
    await ctx.send(f"การใช้งานบอทแก้คำผิดอัตโนมัติได้ถูก `ปิด` แล้วสำหรับคุณ `{user_name}`")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if (all(char in '5+' for char in message.content) and '5' in message.content) or re.search(r'=.+?=', message.content):
        return
    
    user_id = message.author.id
    if user_toggles.get(user_id, False):
        combined_message = message.content
        try:
            corrected_text = [eng2thai[eng_char] for eng_char in combined_message]
            if corrected_text:
                await message.channel.send(f'จริง ๆ ตั้งใจจะพิมพ์ว่า "{"".join(corrected_text)}"')
        except Exception:
            pass

    await bot.process_commands(message)

# # If you don't wanna use command (this will automatically convert every characters btw).
# @bot.event
# async def on_message(message: str):    
#     try:
#         corrected_text = [eng2thai[eng_char] for eng_char in message.content]
#         if corrected_text:
#             await message.channel.send(f'จริง ๆ ตั้งใจจะพิมพ์ว่า "{"".join(corrected_text)}"')
#     except Exception:
#         pass


bot.run(TOKEN)




