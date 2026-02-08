from telethon import TelegramClient, events
import discord
import os
import asyncio

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
channel_telegram = os.getenv("TG_CHANNEL")

discord_token = os.getenv("DISCORD_TOKEN")
discord_channel_id = int(os.getenv("DISCORD_CHANNEL_ID"))

discord_client = discord.Client(intents=discord.Intents.default())

async def main():
    await discord_client.login(discord_token)
    channel = discord_client.get_channel(discord_channel_id)

    async with TelegramClient('session', api_id, api_hash) as tg:
        @tg.on(events.NewMessage(chats=channel_telegram))
        async def handler(event):
            if event.text:
                await channel.send(event.text)

        await tg.run_until_disconnected()

asyncio.run(main())

