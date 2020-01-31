import telebot
bot = telebot.TeleBot(token="")
@bot.message_handler(content_types=['new_chat_members'])
def function_name(message):
	bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAMyXjNfM9fcOznrXUt_tXqwDbiSAYsAApcAA5AAAVAg_eWGt5p_h7YYBA", message.message_id)

@bot.message_handler(commands=['ban'])
def send_something(message):
        reply = message.reply_to_message
        if (reply):
                user = reply.from_user
                extra = ", "
                my_parse_mod = ""
                if (user):
                        if (user.username):
                                extra = extra + "@" + user.username
                        else:
                                extra = extra + "[" + user.first_name + "](tg://user?id="+str(user.id)+")"
                                my_parse_mod = "Markdown"
                bot.send_message(message.chat.id, "Пошл вон из нашей деревни" + extra + "!!!", parse_mode=my_parse_mod)
                print(reply.text)
        else:
                bot.reply_to(message, "Сам себя забанить вздумал?")
bot.polling()
