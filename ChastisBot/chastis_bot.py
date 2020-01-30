import telebot
bot = telebot.TeleBot(token="900026155:AAG8L7WvuWLEDBpedImtwOTHJXX2JqRcqp8")
@bot.message_handler(content_types=['new_chat_members'])
def function_name(message):
	bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAMyXjNfM9fcOznrXUt_tXqwDbiSAYsAApcAA5AAAVAg_eWGt5p_h7YYBA", message.message_id)
bot.polling()