import os
from dotenv import load_dotenv
from telethon import TelegramClient, events, Button


load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('API_TOKEN')
channel_username = 'QuoteUniverse'


bot = TelegramClient('bot_session', api_id,
                     api_hash).start(bot_token=bot_token)


@bot.on(events.NewMessage(pattern=r"/customers"))
async def handler(event):
    channel = await bot.get_entity(channel_username)
    response = ""
    async for member in bot.iter_participants(channel):
        name = member.first_name
        response += f"{name} \n @{member.username} \n\n"
    await bot.send_message(event.chat_id, response)


@bot.on(events.NewMessage(pattern=r'/start'))
async def handler(event):
    # Get sender details
    sender = await event.get_sender()
    sender_name = f"{sender.first_name} {sender.last_name or ''}".strip()

    # keyboard = [
    #     [Button.text("Option A"), Button.text("Option B")],
    #     [Button.text("Option C")]
    # ]

    print(event.chat_id, event)
    await bot.send_file(event.chat_id, file='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmIyMGptaTU1cG1ldmF0NXpoeHJhYXhqaGllMzBuOWUzdGsydmkycyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VxbP9tLeKzazm/giphy.gif', caption=f"Hello {sender_name}, Welcome to the Xeno Universe! The bot is now live and ready to serve.")

print("bot running...")
bot.run_until_disconnected()
