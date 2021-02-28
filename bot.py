from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackContext

def welcome(update:Update,context:CallbackContext):
    
    for new_user in update.message.new_chat_members:
        user_name = ''
        chat_id = update.message.chat_id
        try:
            user_name = '@'+new_user['username']
        except Exception as e:
            user_name = new_user['firstname']
        context.bot.send_message(chat_id=chat_id, text=f'Welcome {user_name}. We are very glad to see u here.\n We hope u will give proper repect to other in this group.\nBest of Luck')

def main():
    updater = Updater('1407868038:AAEcSMKEB8Zli2pBMUxl0NFhne_BynE4FAQ')
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members,welcome))
    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()
