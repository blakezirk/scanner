import os
import discord
import asyncio

TOKEN = os.getenv("DISCORD_TOKEN")
VOICE_CHANNEL_ID = int(os.getenv("VOICE_CHANNEL_ID"))
STREAM_URL = os.getenv("STREAM_URL")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

    voice_channel = client.get_channel(VOICE_CHANNEL_ID)
    if voice_channel is None:
        print("❌ Voice channel not found.")
        return

    vc = await voice_channel.connect()
    try:
        vc.play(discord.FFmpegPCMAudio(STREAM_URL, **FFMPEG_OPTIONS))
        print("🎙️ Now playing stream...")
    except Exception as e:
        print(f"❌ Failed to play stream: {e}")

client.run(TOKEN)
