import requests
import telebot
import datetime
import mysql.connector
from datetime import date
import conf
from oruzhie import keyboard, keyboard_sht, keyboard_snip, keyboard_pp, \
    keyboard_drob, keyboard_pist, keyboard_gran, keyboard_bomb

bot = telebot.TeleBot(conf.token)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='standoff2_ars'
)

# Получаем текущую дату
current_date = date.today()

# Получаем текущее время
current_date_time = datetime.datetime.now()
current_time = current_date_time.time()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'✋ <b>Привет, {message.from_user.first_name} {message.from_user.last_name}</b> 🤚 \n\n '
                     f'🔥 Здесь ты найдёшь <b>всё оружие из Standoff 2</b> с подробным описанием и точными характеристиками, '
                     f'а также <b>информацию про наносимый урон</b>.\n\n'
                     f'⚡️ Для того, что бы получить подробное <b>описание и точные характеристики оружия</b>, '
                     f'жми соответствующие кнопки ниже.',
                     reply_markup=keyboard, parse_mode='html')

    print(current_date, current_time, '|',
          '\033[1m' + 'Пользователь:' + '\033[0m', message.from_user.username, '|',
          '\033[1m' + 'Имя пользователя:' + '\033[0m', message.from_user.first_name, message.from_user.last_name, '|',
          'нажал команду /start.')

    with open('1.txt', 'a', encoding='UTF8') as file:
        file.write(f'\n {current_date} {current_time} Пользователь {message.from_user.username}, '
                   f'{message.from_user.first_name} {message.from_user.last_name}: использование команды /start')
        file.close()


# Обрабатываем callback_data
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'shturmovye-vintovki-v-standoff-2':
        bot.send_message(callback.message.chat.id,
                         '<b>Штурмовые винтовки</b> — это основное оружие в игре. '
                         'Их можно использовать на ближних, средних и дальних дистанциях. '
                         'Поэтому штурмовые винтовки можно назвать <b>самым универсальным оружием</b>. \n\n'
                         '<b>Выбери интересующее оружие, что бы узнать о нём подробнее.</b> \n\n'
                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_sht)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: выбрал штурмовые винтовки')
            file.close()

    elif callback.data == 'snayperskie-vintovki-v-standoff-2':
        bot.send_message(callback.message.chat.id,
                         '<b>Снайперские винтовки</b> — это оружие для опытных стрелков, что умеют играть на позиции '
                         'снайпера. В обязанности снайпера в команде спецназа входит защита своей точки. '
                         'А в команде террористов снайпер должен первым устранить противника, чтобы отрыть вход '
                         'на защищаемую точку. \n\n'
                         '<b>Выбери интересующее оружие, что бы узнать о нём подробнее.</b> \n\n'
                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_snip)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: выбрал снайперские винтовки')
            file.close()

    elif callback.data == 'pistolety-pulemyoty-v-standoff-2':
        bot.send_message(callback.message.chat.id,
                         '<b>Пистолеты-пулемёты</b> — это отличное оружие для штурма или игры на ближних дистанциях. '
                         'Они хорошо подходят для стрельбы во время движения.\n\n'
                         '<b>Выбери интересующее оружие, что бы узнать о нём подробнее.</b> \n\n'
                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_pp)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: выбрал пистолеты-пулемёты')
            file.close()

    elif callback.data == 'droboviki-v-standoff-2':
        bot.send_message(callback.message.chat.id,
                         '<b>Дробовики</b> — это оружие для стрельбы на ближних дистанциях или внутри помещений. '
                         'Их лучше всего использовать на определённых позициях, где можно полноценно раскрыть их потенциал.\n\n'
                         '<b>Выбери интересующее оружие, что бы узнать о нём подробнее.</b> \n\n'
                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_drob)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: выбрал дробовики')
            file.close()

    elif callback.data == 'pistolety-v-standoff-2':
        bot.send_message(callback.message.chat.id,
                         '<b>Пистолеты</b> — это оружие для начала матча или раундов, когда у команды нет денег. '
                         'Некоторые пистолеты можно использовать для штурма во время экономических раундов. \n\n'
                         '<b>Выбери интересующее оружие, что бы узнать о нём подробнее.</b> \n\n'
                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_pist)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: выбрал пистолеты')
            file.close()

    elif callback.data == 'granaty-v-standoff-2':
        bot.send_message(callback.message.chat.id,
                         '<b>Гранаты</b> — это тактическое оружие, обращение с которым должен освоить каждый игрок. '
                         'Несколько удачно брошенных гранат могут помочь вам выиграть раунд. '
                         'И наоборот, неудачно брошенные гранаты могут стать причиной проигрыша. \n\n'
                         '<b>Выбери гранату, что бы узнать о ней подробнее.</b> \n\n'
                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_gran)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: выбрал гранаты')
            file.close()

    elif callback.data == 'bomby-v-standoff-2':
        bot.send_message(callback.message.chat.id,
                         'В игре используется всего одна бомба. Жми ниже, что бы узнать о ней.\n\n'
                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_bomb)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: выбрал бомбы')
            file.close()

    # Обработка нажатий кнопок штурмовых винтовок ---------------------------------------------------------------------
    elif callback.data == 'akr':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 1")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект:: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_sht)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: АКР')
            file.close()

    elif callback.data == 'famas':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 2")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_sht)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: FAMAS')
            file.close()

    elif callback.data == 'akr-12':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 11")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_sht)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: AKR-12')
            file.close()

    elif callback.data == 'm4':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 12")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_sht)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: M4')
            file.close()

    elif callback.data == 'm16':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 13")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_sht)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: M16')
            file.close()

    elif callback.data == 'fnfal':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 14")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_sht)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: FnFal')
            file.close()

    # Обработка нажатий кнопок снайперских винтовок -------------------------------------------------------------------
    elif callback.data == 'm40':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 17")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект:: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_snip)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: М40')
            file.close()

    elif callback.data == 'awm':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 18")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект:: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_snip)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: AWM')
            file.close()

    elif callback.data == 'm110':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 19")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_snip)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: M110')
            file.close()

    # Обработка нажатий кнопок пистолеты-пулемёты -------------------------------------------------------------------
    elif callback.data == 'ump45':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 28")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект:: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_pp)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: UMP45')
            file.close()

    elif callback.data == 'mp7':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 29")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект:: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_pp)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: MP7')
            file.close()

    elif callback.data == 'p90':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 30")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'{item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект:: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_pp)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: P90')
            file.close()

    elif callback.data == 'mp5':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 31")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_pp)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: MP5')
            file.close()

    # Обработка нажатий кнопок дробовиков -----------------------------------------------------------------------------
    elif callback.data == 'sm1014':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 32")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект:: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_drob)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: SM1014')
            file.close()

    elif callback.data == 'fabm':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 33")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_drob)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: FABM')
            file.close()

    # Обработка нажатий кнопок пистолетов -----------------------------------------------------------------------------
    elif callback.data == 'desert-eagle':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 20")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> - {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект:: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_pist)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: Desert Eagle')
            file.close()

    elif callback.data == 'g22':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 21")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект:: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_pist)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: G22')
            file.close()

    elif callback.data == 'usp':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 22")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект:: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_pist)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: USP')
            file.close()

    elif callback.data == 'p350':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 23")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Патроны: <b>{item[5]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n'
                         f'⚡️ Темп стрельбы: <b>{item[7]}</b> \n'
                         f'⚡️ Отдача: <b>{item[8]}</b> \n'
                         f'⚡️ Скорость движения: <b>{item[9]}</b> \n'
                         f'⚡️ Пробиваемость брони: <b>{item[10]}</b> \n'
                         f'⚡️ Проникновение в объект:: <b>{item[11]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_pist)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: P350')
            file.close()

    elif callback.data == 'fs':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 24")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n\n'

                         '<b>Урон:</b> \n'
                         f'⚡️ Урон в голову без шлема: <b>{item[12]}</b> \n'
                         f'⚡️ Урон в голову со шлемом: <b>{item[13]}</b> \n'
                         f'⚡️ Урон в руки без защиты: <b>{item[14]}</b> \n'
                         f'⚡️ Урон в руки с защитой: <b>{item[15]}</b> \n'
                         f'⚡️ Урон в живот без защиты: <b>{item[16]}</b> \n'
                         f'⚡️ Урон в живот с защитой: <b>{item[17]}</b> \n'
                         f'⚡️ Урон в ноги без защиты: <b>{item[18]}</b> \n'
                         f'⚡️ Урон в ноги с защитой: <b>{item[19]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_pist)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: F/S')
            file.close()

    elif callback.data == 'tec-9':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 25")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_pist)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: TEC-9')
            file.close()

    # Обработка нажатий кнопок гранаты --------------------------------------------------------------------------------
    elif callback.data == 'oskolochnaya-granata':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 34")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n'
                         f'⚡️ Награда: <b>{item[4]}</b> \n'
                         f'⚡️ Урон: <b>{item[6]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_gran)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: осколочная граната')
            file.close()

    elif callback.data == 'osleplyayuschaya-granata':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 35")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_gran)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: ослепляющая граната')
            file.close()

    elif callback.data == 'dymovaya-granata':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 36")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         '<b>Характеристики:</b> \n'
                         f'⚡️ Стоимость: <b>{item[3]}</b> \n\n'

                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_gran)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: Дымовая граната')
            file.close()

    # Обработка нажатий кнопок бомбы --------------------------------------------------------------------------------------
    elif callback.data == 'c4':
        cursor = db.cursor()
        cursor.execute("SELECT * FROM oruzhie WHERE id = 37")
        result = cursor.fetchall()

        for item in result:
            print(item)

        bot.send_message(callback.message.chat.id,
                         f'<b>{item[1]}</b> — {item[2]} \n\n'
                         'Чтобы вернуться в начало, нажми /start',
                         parse_mode='html', reply_markup=keyboard_bomb)

        with open('1.txt', 'a', encoding='UTF8') as file:
            file.write(f'\n {current_date} {current_time} Пользователь {callback.from_user.username}, '
                       f'{callback.from_user.first_name} {callback.from_user.last_name}: C4')
            file.close()

    else:
        bot.send_message(callback.message.chat.id, 'Извините, этот функционал ещё не готов.')


# print(callback)

bot.polling(non_stop=True)