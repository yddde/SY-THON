from userbot import jmthon

from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event

plugin_category = "utils"


# كـتابة المـلف وتعديل.    :   زيد @YDDDE.      𝖪𝗁𝖺𝗅𝗂𝖩𝖳𝗁𝖮𝗇 𝖴𝗌𝖾𝖱 𝖡𝖮𝖳  || @zVVVn
# 𝖪𝗁𝖺𝗅𝗂𝖩𝖳𝗁𝖮𝗇 𝖴𝗌𝖾𝖱 𝖡𝖮𝖳  || @zVVVn
# 𝖪𝗁𝖺𝗅𝗂𝖩𝖳𝗁𝖮𝗇 𝖴𝗌𝖾𝖱 𝖡𝖮𝖳  || @zVVVn


@jmthon.ar_cmd(
    pattern="رفع زوجتي(?:\s|$)([\s\S]*)",
    command=("رفع زوجتي", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1518220300:
        return await edit_or_reply(mention, f"**- لا تجاوز حدودك مع المطور 😉😉**")
    if user.id == 1917795624:
        return await edit_or_reply(mention, f"**- لا تتجاوز حدودك مع 😉😉المطور**")
    if user.id == 1071774077:
        return await edit_or_reply(mention, f"**- لا تتجاوز حدودك مع المطور 😉😉**")
    if user.id == 1578777453:
        return await edit_or_reply(mention, f"**- لا تتجاوز حدودك مع المطور 😉😉**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"⌯︙المستخدم [{tag}](tg://user?id={user.id}) \n⌯︙ تـم رفعـه زوجتك عندكم خاص لاتزعجونا . 🙈💆‍♂️",
    )


@jmthon.ar_cmd(
    pattern="رفع كلب(?:\s|$)([\s\S]*)",
    command=("رفع كلب", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1917795624:
        return await edit_or_reply(mention, f"**لاتتجاوز حدودك مع المطور الاساسي 😉😉**")
    if user.id == 1071774077:
        return await edit_or_reply(mention, f"**لاتتجاوز حدودك مع المطور 😉😉**")
    if user.id == 1578777453:
        return await edit_or_reply(mention, f"**لاتتجاوز حدودك مع المطور 😉😉**")
    if user.id == 1518220300:
        return await edit_or_reply(mention, f"**لاتتجاوز حدودك مع المطور 😉😉**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"⌯︙المستخدم [{tag}](tg://user?id={user.id}) \n⌯︙ تـم رفعـه كلب خله ينبح 🐶",
    )


@jmthon.ar_cmd(
    pattern="رفع تاج(?:\s|$)([\s\S]*)",
    command=("رفع تاج", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"⌯︙المستخدم [{tag}](tg://user?id={user.id}) \n⌯︙ تـم رفعـه تاج 👑🔥"
    )


@jmthon.ar_cmd(
    pattern="رفع قرد(?:\s|$)([\s\S]*)",
    command=("رفع قرد", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1917795624:
        return await edit_or_reply(mention, f"**لاتتجاوز حدودك مع المطور الاساسي 😉😉**")
    if user.id == 1071774077:
        return await edit_or_reply(mention, f"**لاتتجاوز حدودك مع المطور 😉😉**")
    if user.id == 1578777453:
        return await edit_or_reply(mention, f"**لاتتجاوز حدودك مع المطور 😉😉**")
    if user.id == 1518220300:
        return await edit_or_reply(mention, f"**لاتتجاوز حدودك مع المطور 😉😉**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"⌯︙المستخدم [{tag}](tg://user?id={user.id}) \n⌯︙ تـم رفعـه قرد واعطائه موزه 🐒🍌",
    )


@jmthon.ar_cmd(
    pattern="رفع بقلبي(?:\s|$)([\s\S]*)",
    command=("رفع بقلبي", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"⌯︙المستخدم [{tag}](tg://user?id={user.id}) \n⌯︙ تـم رفعـه بقلبك بنجاح ❤🙈 "
    )


@jmthon.ar_cmd(
    pattern="رفع حمار(?:\s|$)([\s\S]*)",
    command=("رفع حمار", plugin_category),
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
    if user.id == 1917795624:
        return await edit_or_reply(mention, f"**لاتتجاوز حدودك مع المطور الاساسي😉😉**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"⌯︙المستخدم [{tag}](tg://user?id={user.id}) \n⌯︙ تـم رفـعه حمار هـنا "
    )


# كـتابة المـلف وتعديل.    :   زيد ~ @Y D D D E   𝖪𝗁𝖺𝗅𝗂𝖩𝖳𝗁𝖮𝗇 𝖴𝗌𝖾𝖱 𝖡𝖮𝖳  || @zVVVn
# 𝖪𝗁𝖺𝗅𝗂𝖩𝖳𝗁𝖮𝗇 𝖴𝗌𝖾𝖱 𝖡𝖮𝖳  || @zVVVn
# 𝖪𝗁𝖺𝗅𝗂𝖩𝖳𝗁𝖮𝗇 𝖴𝗌𝖾𝖱 𝖡𝖮𝖳  || @zVVVn


@jmthon.ar_cmd(
    pattern="رفع زوجي(?:\s|$)([\s\S]*)",
    command=("رفع زوجي", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"⌯︙المستخدم [{tag}](tg://user?id={user.id}) \n⌯︙تـم رفعه زوجك عندكم خاص لاتزعجونا 🙈😉 ",
    )


##YDDDE
