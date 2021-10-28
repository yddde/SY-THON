from telethon import Button, events

from Jmthon.razan.resources.mybot import *

from ..Config import Config

ROZ_PIC = "https://telegra.ph/file/d44048b69013e5e92d192.jpg"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("السورس") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.url("قنـاة السـورس ⚙️", "https://t.me/zVVVn"),
                    Button.url("المطـور 👨🏼‍💻", "https://t.me/YDDDE"),
                ]
            ]
            if ROZ_PIC and ROZ_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ROZ_PIC, text=ROZ, buttons=buttons, link_preview=False
                )
            elif ROZ_PIC:
                result = builder.document(
                    ROZ_PIC,
                    title="𝐊𝐡𝐚𝐥𝐢𝐉𝐓𝐇𝐎𝐍 𝐔𝐬𝐞𝐫𝐁𝐎𝐓",
                    text=ROZ,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="𝐊𝐡𝐚𝐥𝐢𝐉𝐓𝐇𝐎𝐍 𝐔𝐬𝐞𝐫𝐁𝐎𝐓",
                    text=ROZ,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@bot.on(admin_cmd(outgoing=True, pattern="السورس"))
async def repo(event):
    if event.fwd_from:
        return
    RR7PP = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(RR7PP, "السورس")
    await response[0].click(event.chat_id)
    await event.delete()


# edit by ~ @YDDDE
