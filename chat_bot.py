import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

# 加載 .env 檔案中的環境變數
load_dotenv(dotenv_path="confing.env") 

# 獲取環境變數的值
api_token = os.getenv('token')
api_channel = os.getenv('channel')

intents = discord.Intents.default()

chat_bot = commands.Bot(command_prefix='#', intents=intents)

@chat_bot.event
async def on_ready():
    print(">> bot is online <<")

@chat_bot.event
async def member_join(member):
    channel = chat_bot.get_channel(api_channel)
    await channel.send(f'{member} 歡迎加入!')

@chat_bot.event
async def member_remove(member):
    channel = chat_bot.get_channel(api_channel)
    await channel.send(f'{member} 離開了!')



chat_bot.run(api_token)
