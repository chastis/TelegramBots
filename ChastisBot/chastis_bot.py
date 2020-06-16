import telebot
import random

bot = telebot.TeleBot(token="TOKEN")
chastis_bot_id =  975253403
chastis_id = 377838268
chastis_bot_username = "@chastis_bot"
ifCodingWasAnAnimeList = ["если", "прог", "аниме", "было", "программирование", "кодинг", "джав", "плюсы" , "питон", "prog", "java", "c++", "python" ]
answerUltimateQuestionList = ["ответ", "вопрос", "42", "?"]
answer_answerList = {
        0 : "Ответ, кстати, 42",
        1 : "Возможно вопрос другой, но ответ однозначно 42",
        2 : "Дай подумать. .\n . \n ..\n . \n. .\n . \n. . . \n. семь с половиной миллион лет спустя .\n . \n. . .\n. . \n. .\n .Сорок Два",
        3 : "В вопросе уже содержится ответ!",
        4 : "Если бы автостопом по галактике было аниме...",
        5 : "42",
        6 : "Заходят как-то двое инопланетян в бар, заказывают ответ у задумчивого бармемна. Выйдете и зайдите нормально через 7.5 миллион лет, отвечает он им. Возвращаются они, а там армяне в нарды играют",
        7 : "Автору 42 лет",
        8 : "Почему каждый раз 42?",
        9 : "Скоро рассвет\n выхода нет\n 42, кстати\n ответ",
        10 : "Помогите меня держат в заложниках в офисе GSC",
        11 : "Отвэта не будет, отвэт принял ислам",
        12 : "Вот вы все задаете вопросы и задаете вопросы, а можно ведь просто задать один.... самый главный... 42, ой, простите",
        13 : "Помогите, Частис меня заставляет отвечать на подобные сообщения 42!",
        14 : "Не путайте пожалуйста 42 и 42!, запомните блин 42 == 42, а 42! == 1.4050061e+51",
        15 : "Вопрос не правильный, правильный вопрос: Сколько будет 6 * 9",
        16 : "Нашел мужик ответ (спойлер 42), а он ему как раз",
        17 : "Здесь могла быть ваша реклама! Оставьте вашу заявку, мы ее расмотрим в течении 7.5 миллионов лет!",
        18 : "42 день в году это 11 февраля, занимательно? правда ведь..?.....",
        19 : "- Отец, почему мою сестру зовут Роза? \n- Потому, что твоя мать любит розы. \n-Спасибо, отец! \n- Не за что, Сорок_Два",
        20 : "Однажды я буду стоять перед алтарем, в ожидании ответа на главной вопрос в моей жизни, Вселенной, и всем остальном. Ответ убил",
        21 : "Ответ убил",
        22 : "42 бутылки пива на стене,\n42 бутылки пива!\nВозьми одну, пусти по кругу,\n41 бутылка пива на стене!",
        23 : "Сколько у нас шпаг? В 10 с половиной раз больше, чем вы подумали!"
}
tastyPirozhkiList = ["пирожок", "пирог", "пирожоч"]
answer_tastyPirozhkiList = {
        0 : "А кто тут такой пирожулька?",
        1 : "Ах ты сладенький пирожочек!",
        2 : "Так бы и откусил кусочек пирожочка...",
        3 : "Какой сладенький пирожочек!"
}
shevaList = ["шева", "шеву", "кну", "шевченк"]
answer_shevaList = {
        0 : "Шева найкраща",
        1 : "Шева та еще щарага",
        2 : "Шева найкраща шарага"
}

chastisList = ["chastis", "частис", "шатох"]
answer_chastisList = {
        0 : "Только не кричи...",
        1 : "Опять работа?",
        2 : "О, это я, кстати!",
        3 : "Можно блин не так громко(",
        4 : "Что я блин уже натворил"
}

sunList = ["солн", "сонеч", "сонц"]
answer_sunList = {
        0 : "Ты тут настолящее солнышко!",
        1 : "А кто это тут такое солнышко",
        2 : "От солнышка слышу",
        3 : "Смотрю на тебя и надо прищюриваться"
}

stalkerList = ["сталкер", "stalker", "ждалкер", "чернобль", "припять"]
answer_stalkerList = {
        0 : "АААААААААААА НДА БЛЯТЬ НДА",
        1 : "Заблудился как-то долговец и кричит, подписывайтесь на @chastis_log",
        2 : "Жил значит один сталкер...",
        3 : "Здесь должен быть анекдот, но его с патчем добавят",
        4 : "Вот бы сталкер был бы аниме...",
        5 : "Помогите меня держат в заложниках в офисе GSC"
}

evaList = ["eva", "nge", "синди", "аска", "рэй", "ева"]
answer_evaList = {
        0 : "Только не заставляй снова лезть в робота",
        1 : "Как ты из робота вылез, уважаемый?",
        2 : "Время для комплиментации!",
        3 : "Как же хочется Асочку",
        4 : "Как же хочется Рэй",
        5 : "Вот бы Каору...",
        6 : "Щас бы к Мисаточке",
        7 : "У тебя чрезвычано мощное АТ поле!",
        8 : "Вызывайте Нерв, это же Ангел!!!",
        9 : "Если бы Евангелион был ... так стоп",
        10 : "Если бы аниме было программированием..."
}

sadList = ["(", "sad", "грустно", "обидно", "плохо"]
answer_sadList = {
        0 : "Все будет хорошо!",
        1 : "Не переживай, бывает и хуже",
        2 : "Могло быть и хуже",
        3 : "Скоро все наладится!",
        4 : "Не грусти, солнышко",
        5 : "Это не самое страшное, что могло произойти",
        6 : "Сочувствую(",
        7 : "Не так все плохо, как тебе могло показаться, честно",
        8 : "У меня конечно нет рук, так как я всего лишь бот, но я бы их не опускал!"
}

answer_loudList = {
        0 : "Блин, не кричи",
        1 : "Ой как громко(",
        2 : "Можно не так громко, пожалуйста...",
        3 : "Зачем ты кричишь, что-то случилось?",
        4 : "Не кричи, солнышко"
}

answer_stopList = {
        0 : "Ой, лучше перестать так делать",
        1 : "йой, хорошо, что второй раз не работает",
        2 : "Сколько это может продолжаться...",
        3 : "Так, так, так блин может лучше /chastis_bot",
        4 : "Ого, думал щас телеграм взломаю"
}

answer_chastisbotList = {
        0 : "Привет, солнышко",
        1 : "Чего ты хотел?",
        2 : "Спасибо, что называешь меня по имени",
        3 : "Как бы то ни было, но не путайте меня с @chastis`ом",
        4 : "Hello, world",
        5 : "Не знаю зачем, но подписывайтесь на шевацитатник. Блин, можно я не буду это говорить? Ладно!"
}


def botReplayAdvanced(message, exList) :
        if (message):
                listLen = len(exList)
                if (listLen>0):
                        a = random.randrange(listLen)
                        print(a)
                        bot.reply_to(message, exList[a])

def checkForMyCommand(message):
        if (message):
                if (message.entities):
                        if (len(message.entities) == 0):
                                return True
                        for entity in message.entities :
                                print(entity)
                                if (entity and entity.user) :
                                        if (entity.user.id == chastis_bot_id):
                                                return True
                                
        return False

def checForMyTag(message):
        if (message):
                if (message.text.find("@") == -1):
                        return True
                elif (message.text.find(chastis_bot_username) != -1):
                        return True
        return False

def checkInList(text, exList):
        for ex in exList:
                if text.lower().find(ex) != -1:
                        return True
        return False

@bot.message_handler(content_types=['new_chat_members'])
def function_name(message):
	bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAMyXjNfM9fcOznrXUt_tXqwDbiSAYsAApcAA5AAAVAg_eWGt5p_h7YYBA", message.message_id)

@bot.message_handler(commands=['ban'])
def send_ban(message):
        reply = message.reply_to_message
        if (reply):
                user = reply.from_user
                extra = ", "
                my_parse_mod = ""
                if (user):
                        print(user.id)
                        if (user.id==chastis_bot_id):
                                if (message.from_user and message.from_user.id == chastis_id):
                                        bot.reply_to(message, "Если я тебе чем то не угодил, хозяин, то это прежде всего твоя вина!")
                                else:
                                        bot.reply_to(message, "Не буду я себя банить, дуралей)")
                        elif (user.id==chastis_id):
                                bot.reply_to(message, "Не нужно хозяина из деревни прогонять, пожалуйста")
                        else:
                                if (user.username):
                                        extra = extra + "@" + user.username
                                else:
                                        extra = extra + "[" + user.first_name + "](tg://user?id="+str(user.id)+")"
                                        my_parse_mod = "Markdown"
                                bot.send_message(message.chat.id, "Пшел вон из нашей деревни" + extra + "!!!", parse_mode=my_parse_mod)
        else:
                bot.reply_to(message, "Сам себя забанить вздумал?")

@bot.message_handler(commands=['d20'])
def send_d20(message):
        if (checForMyTag(message)):
                bot.reply_to(message, str(random.randrange(20)+1))

@bot.message_handler(commands=['stop'])
def send_stop(message):
        if (checForMyTag(message)):
                if (message.from_user and message.from_user.id == chastis_id):
                        bot.reply_to(message,"Ты что забыл, что не добавлял такую команду, глупенький))))")
                else:
                        bot.reply_to(message,"Хорошая попытка) Остановить меня может только @chastis!")

@bot.message_handler(commands=['start', 'help'])
def send_start(message):
        if (checForMyTag(message)):
                bot.reply_to(message,"Добавь меня в свой чат и я буду приветствовать каждого новоприбывшего!")

@bot.message_handler(commands=['call_for_vika'])
def send_vika(message):
        bot.send_message(message.chat.id,"Вика вика вика вика вика")

@bot.message_handler(commands=['chastis'])
def send_chastis(message):
        bot.send_message(message.chat.id,"/chastis")
        botReplayAdvanced(message, answer_stopList)

@bot.message_handler(commands=['chastis_bot'])
def send_chastis_bot(message):
        botReplayAdvanced(message, answer_chastisbotList)

@bot.message_handler(commands=['get_some_help'])
def send_true_help(message):
        bot.send_message(message.chat.id,"Ха! Ничего не поможет)")

@bot.message_handler(commands=['get_beer'])
def send_beer(message):
        if (checForMyTag(message)):
                bot.reply_to(message, "Поздравляю, вы нашли пивную пасхалку!!! напишите @chastis что бы забрать ваш приз!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        if (message and message.text):
                if (message.text.find(chastis_bot_username) != -1):
                        botReplayAdvanced(message, answer_chastisbotList)
                elif checkInList(message.text, ifCodingWasAnAnimeList):
                        if random.randrange(42) == 37 :
                                bot.reply_to(message, "Если бы программирование было аниме...")
                elif checkInList(message.text, answerUltimateQuestionList):
                        if random.randrange(73+42) == 37 :
                                botReplayAdvanced(message, answer_answerList)
                elif checkInList(message.text, tastyPirozhkiList):
                        if random.randrange(42) == 37 :
                                botReplayAdvanced(message, answer_tastyPirozhkiList)
                elif checkInList(message.text, shevaList):
                        if random.randrange(42) == 37 :
                                botReplayAdvanced(message, answer_shevaList)
                elif checkInList(message.text, chastisList):
                        if random.randrange(42) == 37 :
                                botReplayAdvanced(message, answer_chastisList)
                elif checkInList(message.text, sunList):
                        if random.randrange(42) == 37 :
                                botReplayAdvanced(message, answer_sunList)
                elif checkInList(message.text, stalkerList):
                        if random.randrange(42) == 37 :
                                botReplayAdvanced(message, answer_stalkerList)
                elif checkInList(message.text, evaList):
                        if random.randrange(42) == 37 :
                                botReplayAdvanced(message, answer_evaList)
                elif checkInList(message.text, sadList):
                        if random.randrange(42) == 37 :
                                botReplayAdvanced(message, answer_sadList)
                elif (len(message.text) > 2 and message.text.upper() == message.text):
                        for c in message.text:
                                if c.isalpha():
                                        if random.randrange(42) == 37 :
                                                botReplayAdvanced(message, answer_loudList)
                                        return


bot.polling(none_stop=False, interval=1, timeout=1)


