from userbot import jmthon

from . import *


@jmthon.on(admin_cmd(pattern="جلب الصورة"))
async def oho(event):
    if not event.is_reply:
        return await event.edit("يجـب عـليك الـرد عـلى صـورة ذاتيـة الـتدمير")
    rr9r7 = await event.get_reply_message()
    pic = await rr9r7.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
-تـم جـلب الصـورة بنجـاح ✅
- CH: @Zvvvn
- Dev: @YDDDE
  """,
    )
    await event.delete()


# 𝐊𝐡𝐚𝐥𝐢𝐉𝐓𝐇𝐎𝐍 𝐔𝐬𝐞𝐫𝐁𝐎𝐓
# 𝐊𝐡𝐚𝐥𝐢𝐉𝐓𝐇𝐎𝐍 𝐔𝐬𝐞𝐫𝐁𝐎𝐓
# @YDDDE
