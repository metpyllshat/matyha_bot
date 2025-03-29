from config import token

import discord
from ai import chat

intents = discord.Intents.default()
intents.message_content = True
history = ''
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Зашёл как {client.user}')

@client.event
async def on_message(message):
    global history
    if message.author == client.user:
        return

    if message.content.startswith('$matyha'):
        answer = chat(message.author.id,' '.join(message.content.split()[1:]),history)
        await message.channel.send(answer)
        history += f'{message.author.id} : {' '.join(message.content.split()[1:])} \n'
        history += f'Матвей Шаталов (Ты) : {answer} \n'
client.run(token)