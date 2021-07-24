# Note: This script doesn't work (yet)
# Experimental

import discord
import pandas as pd

client = discord.Client()
guild = discord.Guild


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('_'):

        cmd = message.content.split()[0].replace("_", "")
        if len(message.content.split()) > 1:
            parameters = message.content.split()[1:]

# on_message() runs every time a new message is sent
# check if message startswith '_'
# split content and save first element into cmd
# save the rest into list of parameters

        if cmd == 'scan':

            data = pd.DataFrame(columns=['content', 'time', 'author'])

            def is_command(msg):  # Checking if the message is a command call
                if len(msg.content) == 0:
                    return False
                elif msg.content.split()[0] == '_scan':
                    return True
                else:
                    return False

        # set to 10
        # 100 is default msg
        async for msg in message.channel.history(limit=10):
            if msg.author != client.user:
                if not is_command(msg):
                    data = data.append({'content': msg.content,
                                        'time': msg.created_at,
                                        'author': msg.author.name}, ignore_index=True)
                if len(data) == limit:
                    break

        file_location = "data.csv"
        data.to_csv(file_location)

client.run('token')
print("Done.")
