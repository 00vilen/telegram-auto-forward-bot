import os
from telethon import TelegramClient, events

# Replace these with environment variables (safer for hosting services)
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")
DEST_CHANNEL = os.getenv("DEST_CHANNEL")

client = TelegramClient("userbot_session", API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def forward_message(event):
    try:
        await client.send_message(DEST_CHANNEL, event.message)
        print(f"Forwarded message: {event.message.text[:50]}")
    except Exception as e:
        print(f"Error: {e}")

print("✅ User bot is running...")
client.start()
client.run_until_disconnected()
