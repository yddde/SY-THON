""" جميع الحقوق محفوظة لسورس خليج ثون
𝖪𝗁𝖺𝗅𝗂𝖩𝖳𝗁𝖮𝗇 𝖴𝗌𝖾𝖱 𝖡𝖮𝖳  || @zVVVn """

import os
import re

import requests

from userbot import jmthon

try:
    from pyquery import PyQuery as pq
except ModuleNotFoundError:
    os.system("pip3 install pyquery")
    from pyquery import PyQuery as pq

plugin_category = "extra"


def get_download_url(link):
    post_request = requests.post(
        "https://www.expertsphp.com/download.php", data={"url": link}
    )

    request_content = post_request.content
    str_request_content = str(request_content, "utf-8")
    download_url = pq(str_request_content)("table.table-condensed")("tbody")("td")(
        "a"
    ).attr("href")
    return download_url


@jmthon.ar_cmd(
    pattern="بينت?(?:\s|$)([\s\S]*)",
    command=("بينت", plugin_category),
)
async def _(event):
    "لتحميل الصور من برنامج بينترست خاص بسورسنا فقط"
    R = event.pattern_match.group(1)
    links = re.findall(r"\bhttps?://.*\.\S+", R)
    await event.delete()
    if not links:
        Z = await event.respond("▾∮ يجب عليك وضع رابط لتحميله")
        await asyncio.sleep(2)
        await Z.delete()
    else:
        pass
    A = await event.respond("▾∮ يتم التحميل انتظر قليلا")
    RR7PP = get_download_url(R)
    await event.client.send_file(event.chat.id, RR7PP)
    await A.delete()
