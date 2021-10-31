#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (C) PR0FESSOR-99

import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

USERNAME=Config.BOT_USERNAME


# start_Msg, help_msg, about_msg
# Team Mo Tect
MT = "@universalmovieSS"


@Client.on_message(filters.private & filters.command("start"))
async def start_meg(client, update):
    text = f"""<b> 👋Hello {update.from_user.mention}\n\nI am an AutoCaption bot\n\nAll you have to do is add me to your channel and I will show you my power\n\nFor more info check help Button\n\n {MT}</b>"""
    reply_markup =  InlineKeyboardMarkup( [[
        InlineKeyboardButton("help↗️", callback_data="heroku"),
        InlineKeyboardButton("🗣️Group", url=https://t.me/joinchat/FYBCIcMfr0AyOTFl""),
        InlineKeyboardButton("Channel📢", url="https://t.me/joinchat/FYBCIcMfr0AyOTFl)
        ]]
    )
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

@Client.on_callback_query(filters.regex(r"^(heroku|about|motech)$"))
async def callback_data(client, update: CallbackQuery):

    query_data = update.data

    if query_data == "heroku":
        buttons = [[
            InlineKeyboardButton("🛑 JOIN MAIN CHANNEL 🛑", url="https://youtu.be/p4Z9ZN1lZUk")
            ],[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("❌️Close", callback_data="motech"),
            InlineKeyboardButton("About↗️", callback_data="about")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            f"""<b>🔻AutoCaption Bot🔻\n\nTake a look at the end of the video\nIt has to say\n\n🖥️Youtube Tutorial Video\n\nHeroku 👉 https://dashboard.heroku.com/\n\n {MT}</b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    if query_data == "about":https://t.me/joinchat/FYBCIcMfr0AyOTFl
        buttons = [[
            InlineKeyboardButton("🗣️Group", url="https://t.me/joinchat/FYBCIcMfr0AyOTFl"),
            InlineKeyboardButton("Channel📢", url="https://t.me/joinchat/FYBCIcMfr0AyOTFl"),
            InlineKeyboardButton("📃Bot List", url="https://t.me/joinchat/FYBCIcMfr0AyOTFl")
            ],[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("🔙Back", callback_data="heroku"),
            InlineKeyboardButton("❌️Close", callback_data="motech")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            """<b>➪ Bot Name</b> AutoCaptionBot\n\n➪ <b>Framework : Pyrogram</b>\n\n➪<b> Language : Python</b>\n\n➪<b> Server : Heroku</b> \n\n<b>➪ Version : 2.0.1</b>\n\n<b>➪ Source Code  : <a href="https://t.me/joinchat/FYBCIcMfr0AyOTFl/PrivateAutoCaption">Touch Me 🤗</a>\n\n➪ Developer :  @DARKWEBLOAD\n\n➪ Credits : <a href="https://t.me/joinchat/FYBCIcMfr0AyOTFl/PrivateAutoCaption/blob/main/mt_privateautocaption/Credits.md">Credits</a></b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "motech":
        await update.message.delete()
