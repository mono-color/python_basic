# 텔레그램 봇관련 라이브러리
# pip install python-telegram-bot
Token = '5329723610:AAHdq5JB7PFg3CMtcCSJP8XxUzeG5aXdMD8'
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters

updater = Updater(token=Token, use_context=True)


def fn_echo(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    # 메세지 온거 그대로 리턴
    context.bot.send_message(chat_id=user_id, text=user_text)

def fn_command_diary(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    print('다이어리다:', user_text)

    echo_handler = MessageHandler(Filters.text & (Filters.command),fn_echo)
    updater.dispatcher.add_handler(echo_handler)

    diary_handler = CommandHandler('diary',fn_command_diary())
    updater.dispatcher.add_handler(diary_handler)
    updater.start_polling(timeout=5, clean=True)
    update.idle()