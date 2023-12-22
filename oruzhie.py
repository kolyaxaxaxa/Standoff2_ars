from telebot import types

# Создаём Inline кнопки и выводим их на форму
keyboard = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Штурмовые винтовки', callback_data='shturmovye-vintovki-v-standoff-2')
btn2 = types.InlineKeyboardButton('Снайперские винтовки', callback_data='snayperskie-vintovki-v-standoff-2')
keyboard.row(btn1, btn2)
btn3 = types.InlineKeyboardButton('Пистолеты-пулемёты', callback_data='pistolety-pulemyoty-v-standoff-2')
keyboard.row(btn3)
btn4 = types.InlineKeyboardButton('Дробовики', callback_data='droboviki-v-standoff-2')
btn5 = types.InlineKeyboardButton('Пистолеты', callback_data='pistolety-v-standoff-2')
keyboard.row(btn4, btn5)
btn6 = types.InlineKeyboardButton('Гранаты', callback_data='granaty-v-standoff-2')
btn7 = types.InlineKeyboardButton('Бомбы', callback_data='bomby-v-standoff-2')
keyboard.row(btn6, btn7)

# Инлайн клавиатура для штурмовых винтовок
keyboard_sht = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('АКР', callback_data='akr')
btn2 = types.InlineKeyboardButton('FAMAS', callback_data='famas')
btn3 = types.InlineKeyboardButton('AKR-12', callback_data='akr-12')
keyboard_sht.row(btn1, btn2, btn3)
btn4 = types.InlineKeyboardButton('M4', callback_data='m4')
btn5 = types.InlineKeyboardButton('M16', callback_data='m16')
btn6 = types.InlineKeyboardButton('FnFal', callback_data='fnfal')
keyboard_sht.row(btn4, btn5, btn6)

# Инлайн клавиатура для снайперских винтовок
keyboard_snip = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('M40', callback_data='m40')
btn2 = types.InlineKeyboardButton('AWM', callback_data='awm')
btn3 = types.InlineKeyboardButton('M110', callback_data='m110')
keyboard_snip.row(btn1, btn2, btn3)

# Инлайн клавиатура для пистолетов-пулемётов
keyboard_pp = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('UMP45', callback_data='ump45')
btn2 = types.InlineKeyboardButton('MP7', callback_data='mp7')
keyboard_pp.row(btn1, btn2)
btn3 = types.InlineKeyboardButton('P90', callback_data='p90')
btn4 = types.InlineKeyboardButton('MP5', callback_data='mp5')
keyboard_pp.row(btn3, btn4)

# Инлайн клавиатура для дробовиков
keyboard_drob = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('SM1014', callback_data='sm1014')
btn2 = types.InlineKeyboardButton('FABM', callback_data='fabm')
keyboard_drob.row(btn1, btn2)

# Инлайн клавиатура для пистолетов
keyboard_pist = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Desert Eagle', callback_data='desert-eagle')
btn2 = types.InlineKeyboardButton('G22', callback_data='g22')
btn3 = types.InlineKeyboardButton('USP', callback_data='usp')
keyboard_pist.row(btn1, btn2, btn3)
btn4 = types.InlineKeyboardButton('P350', callback_data='p350')
btn5 = types.InlineKeyboardButton('F/S', callback_data='fs')
btn6 = types.InlineKeyboardButton('TEC-9', callback_data='tec-9')
keyboard_pist.row(btn4, btn5, btn6)

# Инлайн клавиатура для гранат
keyboard_gran = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Осколочная граната', callback_data='oskolochnaya-granata')
btn2 = types.InlineKeyboardButton('Ослепляющая граната', callback_data='osleplyayuschaya-granata')
keyboard_gran.row(btn1, btn2)
btn3 = types.InlineKeyboardButton('Дымовая граната', callback_data='dymovaya-granata')
keyboard_gran.row(btn3)

# Инлайн клавиатура для бомбы
keyboard_bomb = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('C4', callback_data='c4')
# keyboard_bomb.row(btn1)
keyboard_bomb.add(btn1)