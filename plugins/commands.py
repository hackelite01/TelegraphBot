from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from translation import Translation

from buttons import Button

@Client.on_callback_query()

async def button(bot, update):

    if update.data == "home":

        await update.message.delete()

        await start(bot, update.message)

    elif update.data == "help":

        await update.message.delete()

        await help(bot, update.message)

    elif update.data == "close":

        await update.message.delete()

@Client.on_message(filters.command(["start"]))

async def start(bot, update):

    await bot.send_message(chat_id=update.chat.id, text=Translation.START_TEXT.format(update.from_user.mention), parse_mode="html", disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(Button.START_BUTTONS), reply_to_message_id=update.message_id)

@Client.on_message(filters.command(["help"]))

async def help(bot, update):

    await bot.send_message(chat_id=update.chat.id, text=Translation.HELP_USER, parse_mode="html", disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(Button.HELP_BUTTONS), reply_to_message_id=update.message_id)

