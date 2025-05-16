def send_image(bot, img_path, tg_chat_id):
    with open(img_path, 'rb') as document:
        bot.send_document(chat_id=tg_chat_id, document=document)
