import random

from Jmthon.razan.resources.strings import *
from userbot import jmthon

from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event

plugin_category = "utils"


@jmthon.ar_cmd(
    pattern="نسبه الحب(?:\s|$)([\s\S]*)",
    command=("نسبه الحب", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rza = random.choice(roz)
    await edit_or_reply(
        mention, f"نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {rza} 😔🖤"
    )


@jmthon.ar_cmd(
    pattern="نسبه الانوثه(?:\s|$)([\s\S]*)",
    command=("نسبه الانوثه", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1917795624:
        return await edit_or_reply(mention, f"**لاتتجاوز حدودك مع المطور الاساسي😉😉**")
    if user.id == 1917795624:
        return await edit_or_reply(mention, f"**لاتتجاوز حدودك مع المطور الاساسي😉😉**")
    if user.id == 1917795624:
        return await edit_or_reply(mention, f"**لاتتجاوز حدودك مع المطور الاساسي😉😉**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"⌯︙نسبة الانوثة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@jmthon.ar_cmd(
    pattern="نسبه الغباء(?:\s|$)([\s\S]*)",
    command=("نسبه الغباء", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1917795624:
        return await edit_or_reply(mention, f"**0% ♥🙂**")
    if user.id == 1917795624:
        return await edit_or_reply(mention, f"**0% ♥🙂**")
    if user.id == 1917795624:
        return await edit_or_reply(mention, f"**0% ♥🙂**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الغباء لـ [{muh}](tg://user?id={user.id}) هـي {rzona} 😂💔"
    )
