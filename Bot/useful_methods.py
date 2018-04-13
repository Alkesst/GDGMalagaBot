from telegram import InlineQueryResultArticle, InputTextMessageContent


def hello(bot, update):
    update.message.reply_text(f'Hello {update.message.from_user.first_name}')


def it_rocks(bot, update):
    update.message.reply_text(f'Yeeeah, Google I/O rocks!!!')


def start(bot, update):
    update.message.reply_text('Thanks for waking me up! I was bored with so much sleep :(')


def secret(bot, update, args):
    if ''.join(args) == "GoogleIO2018":
        bot.send_message(chat_id=update.message.chat_id, text='Now you can use super commands!')
    else:
        update.message.reply_text('Error! Wrong password!')


def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    results.append(
        InlineQueryResultArticle(
            id=query.lower(),
            title='lower',
            input_message_content=InputTextMessageContent(query.lower())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)

