import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.connections_mdb import add_connection, all_connections, if_active, delete_connection



@Client.on_message((filters.private | filters.group) & filters.command(Config.CONNECT_COMMAND))
async def addconnection(client,message):
    userid = message.from_user.id
    chat_type = message.chat.type

    if chat_type == "private":
        try:
            cmd, group_id = message.text.split(" ", 1)
        except:
            await message.reply_text(
                "<b>Doğru biçimde girin!</b>\n\n"
                "<code>/connect groupid</code>\n\n"
                "<i>Bu botu grubunuza ekleyerek Grup kimliğinizi alın ve  <code>/id</code></i>",
                quote=True
            )
            return

    elif (chat_type == "group") or (chat_type == "supergroup"):
        group_id = message.chat.id

    try:
        st = await client.get_chat_member(group_id, userid)
        if (st.status == "administrator") or (st.status == "creator") or (str(userid) in Config.AUTH_USERS):
            pass
        else:
            await message.reply_text("Verilen grupta yönetici olmalısınız!", quote=True)
            return
    except Exception as e:
        print(e)
        await message.reply_text(
            "Geçersiz Grup Kimliği!\n\nDoğruysa, grubunuzda bulunduğumdan emin olun!!",
            quote=True
        )
        return

    try:
        st = await client.get_chat_member(group_id, "me")
        if st.status == "administrator":
            ttl = await client.get_chat(group_id)
            title = ttl.title

            addcon = await add_connection(str(group_id), str(userid))
            if addcon:
                await message.reply_text(
                    f"Başarıyla bağlı **{title}**\nŞimdi grubunuzu benim pm'imden yönetin !",
                    quote=True,
                    parse_mode="md"
                )
                if (chat_type == "group") or (chat_type == "supergroup"):
                    await client.send_message(
                        userid,
                        f"Connected to **{title}** !",
                        parse_mode="md"
                    )
            else:
                await message.reply_text(
                    "Bu sohbete zaten bağlısınız!",
                    quote=True
                )
        else:
            await message.reply_text("Beni gruba yönetici olarak ekleyin.", quote=True)
    except Exception as e:
        print(e)
        await message.reply_text(
            "Some error occured! Try again later.",
            quote=True
        )
        return


@Client.on_message((filters.private | filters.group) & filters.command(Config.DISCONNECT_COMMAND))
async def deleteconnection(client,message):
    userid = message.from_user.id
    chat_type = message.chat.type

    if chat_type == "private":
        await message.reply_text("Grupları görüntülemek veya gruplarla bağlantıyı kesmek için /connections çalıştır!", quote=True)

    elif (chat_type == "group") or (chat_type == "supergroup"):
        group_id = message.chat.id

        st = await client.get_chat_member(group_id, userid)
        if not ((st.status == "administrator") or (st.status == "creator") or (str(userid) in Config.AUTH_USERS)):
            return

        delcon = await delete_connection(str(userid), str(group_id))
        if delcon:
            await message.reply_text("Bu sohbetle bağlantı başarıyla kesildi", quote=True)
        else:
            await message.reply_text("Bu sohbet benimle bağlantılı değil.!\nBağlanmak için yapın connect.", quote=True)


@Client.on_message(filters.private & filters.command(["connections"]))
async def connections(client,message):
    userid = message.from_user.id

    groupids = await all_connections(str(userid))
    if groupids is None:
        await message.reply_text(
            "Etkin bağlantı yok!! Önce bazı gruplara bağlanmalıdır.",
            quote=True
        )
        return
    buttons = []
    for groupid in groupids:
        try:
            ttl = await client.get_chat(int(groupid))
            title = ttl.title
            active = await if_active(str(userid), str(groupid))
            if active:
                act = " - ACTIVE"
            else:
                act = ""
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{title}:{act}"
                    )
                ]
            )
        except:
            pass
    if buttons:
        await message.reply_text(
            "Bağlı grup bilgileriniz ;\n\n",
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
