from pyrogram.types import InlineKeyboardButton

class Button(object):

    START_BUTTONS = [[InlineKeyboardButton('⚙ Channel ⚙', url='https://telegram.me/hackelitebotlist'), InlineKeyboardButton('⚙ Group ⚙', url='https://telegram.me/hackelite01'),],
                        [InlineKeyboardButton('⚜ Help and Informations ⚜', callback_data='help')]]

    HELP_BUTTONS = [[InlineKeyboardButton('⚙ Channel ⚙', url='https://telegram.me/hackelitebotlist'), InlineKeyboardButton('⚙ Group ⚙', url='https://telegram.me/hackelite01'),],
                        [InlineKeyboardButton('⚜ Back to Home ⚜', callback_data='home')]]
