
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""** Hey i am a group music Bot🥀 it's designed by...
 : [shyxd](https://t.me/I_follow_no_one)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀Creater🥀", url="https://t.me/I_follow_no_one")
                  ],[
                    InlineKeyboardButton(
                        "⚔️Fed⚔️", url="https://t.me/XdTeleban"
                    ),
                    InlineKeyboardButton(
                        "💜Group💜", url="https://t.me/XD_dead_killer"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🥀How to use🥀", url="https://telegra.ph/Shy-MusicX-Command-12-03"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Shyxd") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲..😎**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💜Support🤞", url="https://t.me/SiliconValleyBoy")
                ]
            ]
        )
   )
