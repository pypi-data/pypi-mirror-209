# library mod by @xtsea

class SendPhoto:
    def __init__(self, chat_id, ph, replywithme, caption=None):
        self.chat_id = chat_id
        self.ph = ph
        self.caption = caption
        self.replywithme = replywithme

    async def __call__(self, client):
        if self.caption is None:
            await client.send_photo(self.chat_id, photo=self.ph, reply_to_message_id=self.replywithme)
        else:
            await client.send_photo(self.chat_id, photo=self.ph, caption=self.caption, reply_to_message_id=self.replywithme)


class SendVideo:
    def __init__(self, chat_id, vd, replywithme, caption=None):
        self.chat_id = chat_id 
        self.vd = vd
        self.replywithme = replywithme
        self.caption = caption

    async def __call__(self, client):
        if self.caption is None:
            await client.send_video(self.chat_id, video=self.vd, reply_to_message_id=self.replywithme)
        else:
            await client.send_video(self.chat_id, video=self.vd, caption=self.caption, reply_to_message_id=self.replywithme)


class SendMessage:
    def __init__(self, chat_id, txt, replywithme):
        self.chat_id = chat_id
        self.txt = txt
        self.replywithme = replywithme

    async def __call__(self, client):
        await client.send_message(self.chat_id, text=self.txt, reply_to_message_id=self.replywithme)


class SendSticker:
    def __init__(self, chat_id, stkr, replywithme):
        self.chat_id = chat_id
        self.stkr = stkr
        self.replywithme = replywithme

    async def __call__(self, client):
        await client.send_sticker(self.chat_id, sticker=self.stkr, reply_to_message_id=self.replywithme)


class SendDocument:
    def __init__(self, chat_id, dmt, replywithme, caption=None):
        self.chat_id = chat_id
        self.dmt = dmt
        self.replywithme = replywithme
        self.caption = caption

    async def __call__(self, client):
        if self.caption is None:
            await client.send_document(self.chat_id, document=self.dmt, reply_to_message_id=self.replywithme)
        else:
            await client.send_document(self.chat_id, document=self.dmt, caption=self.caption, reply_to_message_id=self.replywithme)

class FromUserID:
    def __init__(self, from_user_id):
        self.from_user_id = from_user_id

    async def __call__(self, message):
        return message.from_user.id == self.from_user_id


class FromUserUsername:
    def __init__(self, from_user_username):
        self.from_user_username = from_user_username

    async def __call__(self, message):
        return message.from_user.username == self.from_user_username


class ReplyFromUserID:
    def __init__(self, reply_from_user_id):
        self.reply_from_user_id = reply_from_user_id

    async def __call__(self, message):
        return message.reply_to_message.from_user.id == self.reply_from_user_id


class ReplyFromUserUsername:
    def __init__(self, reply_from_user_username):
        self.reply_from_user_username = reply_from_user_username

    async def __call__(self, message):
        return message.reply_to_message.from_user.username == self.reply_from_user_username


class ReplyToProcessing:
    def __init__(self, message):
        self.message = message

    async def __call__(self, message, user=None):
        user_id = user.id if user else None
        username = user.username if user else 'unknown'
        reply = await message.reply_text(self.message.format(user_id=user_id, username=username))
        return reply


class LinkOrReason:
    def __init__(self, message):
        self.message = message

    def __call__(self):
        message_split = self.message.text.split(" ", 1)
        return message_split[1] if len(message_split) > 1 else None
