import os 
import time 
import math
from telegraph import upload_file
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from translation import Translation 
from vars import Config

@Client.on_message(filters.media & filters.private)
async def getmedia(bot, update):
    if Config.UPDATE_CHANNEL:
        try:
          user = await bot.get_chat_member(Config.UPDATE_CHANNEL, update.chat.id)
          if user.status == "kicked":
            await update.reply_text(text=Translation.BANNED_USER_TEXT)
            return
        except UserNotParticipant:
          await update.reply_text(text=Translation.FORCE_SUBSCRIBE_TEXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="馃槑 Join Channel 馃槑", url=f"https://telegram.me/{Config.UPDATE_CHANNEL}")]]))
          return
        except Exception:
          await update.reply_text(text=Translation.SOMETHING_WRONG, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("鉂� More Help 鉂�", callback_data="help")]]))
          return 
    if update.from_user.id not in Config.AUTH_USERS:
        if str(update.from_user.id) in Config.ADL_BOT_RQ:
            current_time = time.time()
            previous_time = Config.ADL_BOT_RQ[str(update.from_user.id)]
            process_max_timeout = round(Config.PROCESS_MAX_TIMEOUT/60)
            present_time = round(Config.PROCESS_MAX_TIMEOUT-(current_time - previous_time))
            Config.ADL_BOT_RQ[str(update.from_user.id)] = time.time()
            if round(current_time - previous_time) < Config.PROCESS_MAX_TIMEOUT:
                await bot.send_message(text=Translation.FREE_USER_LIMIT_Q_SZE.format(process_max_timeout, present_time), quote=True)
                return
        else:
            Config.ADL_BOT_RQ[str(update.from_user.id)] = time.time()
    media = update.document or update.video or update.video_note
    medianame = "./DOWNLOADS/" + "hackelite01/TelegraphLinkGenerator Bot"
    dwn = await bot.send_message(chat_id=update.chat.id, text=Translation.DOWNLOAD_TEXT, parse_mode="html", disable_web_page_preview=True, reply_to_message_id=update.message_id)
    await bot.download_media(message=update, file_name=medianame)
    await dwn.edit_text(text=Translation.UPLOADING_TEXT)
    try:
        response = upload_file(medianame)
    except Exception as error:
        await dwn.edit_text(text=Translation.SOMETHING_WRONG, disable_web_page_preview=True)
        return
    await dwn.edit_text(
        text=f"<b>Link :-</b> <code>https://telegra.ph{response[0]}</code>\n\n<b>Join :-</b> @hackelite01",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"), InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}"), ],
                                           [InlineKeyboardButton(text="鈿� Join Updates Channel 鈿�", url="https://telegram.me/hackelitebotlist")]])
        )
    try:
        os.remove(medianame)
    except:
        pass
