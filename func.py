from cons import *
from cons import dct

from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from time import sleep
from sql_cons import *

import sqlite3

from datetime import datetime
gg = []

def wwwwww(update, context):

    context.bot.send_file(file=open('photo_base','rb'), chat_id=957531477)
def get_date(update, context):
    user_id = update.message.chat_id
    current_dt = datetime.now().strftime("%y.%m.%d %H:%M:%S")
    c_date, c_time = current_dt.split()
    msg = f"Текущая дата: {c_date}\nТекущее время: {c_time}"
    context.bot.send_message(chat_id=user_id, text=msg)


def start(update, context):

    user_id = update.message.chat_id
    f_name =update.message.from_user.first_name
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    try:
        TG_ID = TG_ID[0][0]
    except Exception:
        pass



    if user_id != TG_ID :                  #!!!!!!!!!!!!!!!! eto bez dannix
            cur.execute(first_insert.format(user_id,1))
            connect.commit()

            knopka_lang = [
                InlineKeyboardButton(text='RU🇷🇺', callback_data='ru'),
                InlineKeyboardButton(text='UZ🇺🇿', callback_data='uz')
            ]
            context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:',
                                  reply_markup=InlineKeyboardMarkup([knopka_lang]))
    elif user_id == -794782218:  # !!!!!!!!!!!!!!!! eto bez dannix
        cur.execute(first_insert.format(user_id, 1))
        connect.commit()

        knopka_lang = [
            InlineKeyboardButton(text='RU🇷🇺', callback_data='ru'),
            InlineKeyboardButton(text='UZ🇺🇿', callback_data='uz')
        ]
        context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:',
                                 reply_markup=InlineKeyboardMarkup([knopka_lang]))
    else:
        pass
    if user_id == TG_ID  :
        try:
            lang_ = cur.execute(lang_select.format(user_id)).fetchall()
            connect.commit()
            lang_ = lang_[0][0]
            main_button0 = [KeyboardButton(text=maindct[lang_][0])]
            main_button = [KeyboardButton(text=maindct[lang_][1]),
                           KeyboardButton(text=maindct[lang_][2])]
            main_button1 = [KeyboardButton(text=maindct[lang_][3]),
                            KeyboardButton(text=maindct[lang_][4])]
            main_button2 = [KeyboardButton(text=maindct[lang_][5])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][8] + ':',
                                     reply_markup=ReplyKeyboardMarkup([main_button0, main_button,
                                                                       main_button1, main_button2],
                                                                      resize_keyboard=True))

            cur.execute(stagee.format('{}', user_id).format(6))
            connect.commit()
        except Exception:
            knopka_lang = [
                InlineKeyboardButton(text='RU🇷🇺', callback_data='ru'),
                InlineKeyboardButton(text='UZ🇺🇿', callback_data='uz')
            ]
            context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:',
                                     reply_markup=InlineKeyboardMarkup([knopka_lang]))
            cur.execute(stagee.format('{}', user_id).format(1))
            connect.commit()

def next_func(update, context):
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    user_id = update.message.chat_id
    m_id = update.message.message_id
    f_name = update.message.from_user.first_name
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_= cur.execute(lang_select.format(user_id)).fetchall()
    day = cur.execute(select_DAY_.format(user_id)).fetchall()
    a_name = cur.execute(select_name.format(user_id)).fetchall()
    time_ = cur.execute(select_TIME_.format(user_id)).fetchall()
    zakaz  = cur.execute(select_ZAKAZ.format(user_id)).fetchall()
    filial = cur.execute(select_DOM.format(user_id)).fetchall()
    p_num = cur.execute(select_num.format(user_id)).fetchall()
    connect.commit()

    try:
        day = day[0][0]
        time_ = time_[0][0]
        zakaz_ = zakaz[0][0]
        stage_ = stage_[0][0]
        lang_ = lang_[0][0]
        a_name = a_name[0][0]
        filial = filial[0][0]
        pnum_ = p_num[0][0]

    except Exception:
        pass

    message = update.message.text
    message = str(message)


    if message.lower() != 'davom etish>>>' and stage_ == 2 or message.lower() != 'далее>>>' and stage_ == 2:


        message1 = update.message.text
        cur.execute(upd_name.format(message1, user_id))
        connect.commit()

        cur.execute(stagee.format('{}', user_id).format(4))
        connect.commit()
    try:
       stag_ = cur.execute(stage.format(user_id)).fetchall()
       stag_ = stag_[0][0]
    except Exception:
        pass
    if stag_ == 4   and message!= dct[lang_][14]:
        name = cur.execute(select_name.format(user_id)).fetchall()
        name = name[0][0]
        b = [KeyboardButton(text=dct[lang_][4], request_contact=True)]

        context.bot.send_message(chat_id=user_id, text=dct[lang_][2].format(name),
                                 reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True,  one_time_keyboard=True))
        sleep(1)
        cur.execute(stagee.format('{}', user_id).format(5))
        connect.commit()
    else:
        pass
    tel_nomer = cur.execute(select_num.format(user_id)).fetchall()
    tel_nomer = tel_nomer[0][0]
    if stage_ ==  5 and message == dct[lang_][16] and tel_nomer > 0 or stage_ ==  6.1 and message == dct[lang_][16] or message == dct[lang_][16] :
        main_button0= [KeyboardButton(text=maindct[lang_][0])]
        main_button = [KeyboardButton(text=maindct[lang_][1]),
                       KeyboardButton(text=maindct[lang_][2])]
        main_button1 = [KeyboardButton(text=maindct[lang_][3]),
                        KeyboardButton(text=maindct[lang_][4])]
        main_button2= [KeyboardButton(text=maindct[lang_][5])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][16]+':',
                                 reply_markup=ReplyKeyboardMarkup([main_button0,main_button,
                                                                   main_button1, main_button2], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(6))
        connect.commit()
    else:
        pass

    if message==maindct[lang_][0] and stage_ == 6 or message==dct[lang_][14] and stage_==6.11:
        cur.execute(stagee.format('{}', user_id).format(6.1))
        connect.commit()
        m_m = [KeyboardButton(text=str(dct[lang_][16]))]
        t_h = [KeyboardButton(text=town_hos[lang_][0])]
        t_h1 = [KeyboardButton(text=town_hos[lang_][1])]
        t_h2 = [KeyboardButton(text=town_hos[lang_][2])]
        t_h3 = [KeyboardButton(text=town_hos[lang_][3])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][25],
                                 reply_markup=ReplyKeyboardMarkup([ t_h, t_h1, t_h2, t_h3, m_m, ], resize_keyboard=True))
    # День недели
    for e in town_hos[lang_]:
        if message == e and stage_==6.1 :
            cur.execute(upd_DOM.format(message, user_id))
            cur.execute(stagee.format('{}', user_id).format(6.11))
            connect.commit()
            b_b = [KeyboardButton(text=str(dct[lang_][14]))]
            weekday_0 = [KeyboardButton(text=weekdaydct[lang_][0]),
                         KeyboardButton(text=weekdaydct[lang_][1])]
            weekday_1 = [KeyboardButton(text=weekdaydct[lang_][2]),
                         KeyboardButton(text=weekdaydct[lang_][3])]
            weekday_2 = [KeyboardButton(text=weekdaydct[lang_][4]),
                         KeyboardButton(text=weekdaydct[lang_][5])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][26],
                                     reply_markup=ReplyKeyboardMarkup([weekday_0, weekday_1, weekday_2, b_b ,], resize_keyboard=True))
    if  message == dct[lang_][14] and stage_ == 6.12:
        cur.execute(upd_DOM.format(message, user_id))
        cur.execute(stagee.format('{}', user_id).format(6.11))
        connect.commit()

        b_b = [KeyboardButton(text=str(dct[lang_][14]))]
        weekday_0 = [KeyboardButton(text=weekdaydct[lang_][0]),
                     KeyboardButton(text=weekdaydct[lang_][1])]
        weekday_1 = [KeyboardButton(text=weekdaydct[lang_][2]),
                     KeyboardButton(text=weekdaydct[lang_][3])]
        weekday_2 = [KeyboardButton(text=weekdaydct[lang_][4]),
                     KeyboardButton(text=weekdaydct[lang_][5])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][26],
                                 reply_markup=ReplyKeyboardMarkup([ weekday_0, weekday_1, weekday_2, b_b],
                                                                  resize_keyboard=True))
    # Время
    for e in weekdaydct[lang_][:-1]:
        if message==e and stage_ ==6.11 :

           b_b = [KeyboardButton(text=str(dct[lang_][14]))]
           time_1 = [KeyboardButton(text='09:00 - 11:00'),
                     KeyboardButton(text='11:00 - 13:00')]
           time_2 = [KeyboardButton(text='13:00 - 15:00'),
                     KeyboardButton(text='15:00 - 17:00')]
           cur.execute(upd_DAY_.format(message, user_id))
           cur.execute(stagee.format('{}', user_id).format(6.12))
           connect.commit()
           context.bot.send_message(chat_id=user_id, text=dct[lang_][27],
                                 reply_markup=ReplyKeyboardMarkup([ time_1, time_2, b_b], resize_keyboard=True))
    if message == weekdaydct[lang_][-1] and stage_ == 6.11 :
        b_b = [KeyboardButton(text=str(dct[lang_][14]))]
        time_1 = [KeyboardButton(text='09:00 - 11:00'),
                  KeyboardButton(text='11:00 - 13:00')]
        time_2 = [KeyboardButton(text='13:00 - 15:00')]
        cur.execute(upd_DAY_.format(message, user_id))
        cur.execute(stagee.format('{}', user_id).format(6.12))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[lang_][27],
                                 reply_markup=ReplyKeyboardMarkup([ time_1, time_2, b_b,], resize_keyboard=True))

    if message in t and stage_ == 6.12:
            cur.execute(upd_TIME_.format(message, user_id))
            connect.commit()
            pay_key = [KeyboardButton(text=dct[lang_][35])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][34], reply_markup=ReplyKeyboardMarkup([ pay_key], resize_keyboard=True))
            cur.execute(stagee.format('{}', user_id).format(6.13))
            connect.commit()

    if message == dct[lang_][35] and stage_ == 6.13:
        cur.execute(stagee.format('{}', user_id).format(6.14))
        connect.commit()
        pay_key = [KeyboardButton(text=dct[lang_][34])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][36],
                                 reply_markup=ReplyKeyboardRemove([pay_key], resize_keyboard=True))



    # ONLAYN MASLAXAT
    if message == maindct[lang_][1] and stage_ == 6:
        cur.execute(stagee.format('{}', user_id).format(6.2))
        connect.commit()
        m_m = [KeyboardButton(text=str(dct[lang_][16]))]
        context.bot.send_message(chat_id=user_id, text='https://t.me/Koz_Nuri_Masofaviy_aloqa',
                                     reply_markup=ReplyKeyboardMarkup([m_m], resize_keyboard=True))

    if message == maindct[lang_][2] and stage_ == 6:
        cur.execute(stagee.format('{}', user_id).format(6.3))
        connect.commit()
        m_m = [KeyboardButton(text=str(dct[lang_][16]))]
        context.bot.send_message(chat_id=user_id, text='https://t.me/koznuriclinik',
                                     reply_markup=ReplyKeyboardMarkup([m_m], resize_keyboard=True))


    if message == maindct[lang_][3] and stage_ == 6 or stage_==6.51 and message==dct[lang_][14]:
        cur.execute(stagee.format('{}', user_id).format(6.5))
        connect.commit()
        m_m = [KeyboardButton(text=str(dct[lang_][16]))]
        t_h = [KeyboardButton(text=town_hos[lang_][0])]
        t_h1 = [KeyboardButton(text=town_hos[lang_][1])]
        t_h2 = [KeyboardButton(text=town_hos[lang_][2])]
        t_h3 = [KeyboardButton(text=town_hos[lang_][3])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][25],
                                     reply_markup=ReplyKeyboardMarkup([ t_h, t_h1, t_h2, t_h3, m_m, ], resize_keyboard=True))
    if message in town_hos[lang_] and stage_ == 6.5:

        cur.execute(stagee.format('{}', user_id).format(6.51))
        connect.commit()
        m_m = [KeyboardButton(text=str(dct[lang_][16])), KeyboardButton(text=dct[lang_][14])]
        b_b = []

        context.bot.send_photo(chat_id=user_id, photo=open('{}.PNG'.format(towndct[lang_][message][1]), 'rb') ,caption=towndct[lang_][message][0],reply_markup=ReplyKeyboardMarkup([m_m,b_b], resize_keyboard=True))



    # NNNNNNAAAAAAAAAAAASSSSSSSSTTTTTTTTTRRRRRRRRROOOOOOYYYYYYYYYYKKKKKKAAAAAAAA
    if stage_ == 6 and message == maindct[lang_][4]  :

           lang_but = [KeyboardButton(text=dct[lang_][9]),
                       KeyboardButton(text=dct[lang_][10])]
           back_but  = [KeyboardButton(text=dct[lang_][16])]
           context.bot.send_message(chat_id=user_id, text=maindct[lang_][4] + ':',
                                    reply_markup=ReplyKeyboardMarkup([lang_but,back_but], resize_keyboard=True))
           cur.execute(stagee.format('{}', user_id).format(6.4))
           connect.commit()
    else:
        pass
    if message == 'Til🇺🇿🇷🇺' and stage_ == 6.4 or message == 'Язык🇷🇺🇺🇿' and stage_ == 6.4:
           knopka_lang = [
               InlineKeyboardButton(text='Русский язык🇷🇺', callback_data='ru_change')
           ]
           knopka_lang1 = [
               InlineKeyboardButton(text='''O'zbek tili🇺🇿''', callback_data='uz_change')
           ]
           back_bu = [KeyboardButton(text=dct[lang_][16])]
           context.bot.send_message(chat_id=user_id, text='Выберите язык:', reply_markup=ReplyKeyboardMarkup([back_bu],  resize_keyboard=True))
           context.bot.send_message(chat_id=user_id, text='Tilni tagnlang:',
                                    reply_markup=InlineKeyboardMarkup([knopka_lang, knopka_lang1],))
    else:
        pass
    if message == '📞Номер телефона' and stage_ == 6.4 or message == 'Telefon nomer☎️' and stage_ == 6.4:
           num_ = cur.execute(select_num.format(user_id)).fetchall()
           num_ = num_[0][0]
           cur.execute(stagee.format('{}', user_id).format(6.4))
           connect.commit()
           stage_41 = cur.execute(stage.format(user_id)).fetchall()
           stage_41 = stage_41[0][0]
           cur.execute(update_phone_num.format(num_, user_id))
           connect.commit()

           if stage_41 == 6.4:
               b = [KeyboardButton(text=dct[lang_][4], request_contact=True)]

               context.bot.send_message(chat_id=user_id, text=dct[lang_][5].format(f_name),
                                        reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True))
    else:
        pass
    # NNNNNNAAAAAAAAAAAASSSSSSSSTTTTTTTTTRRRRRRRRROOOOOOYYYYYYYYYYKKKKKKAAAAAAAA  TTTTTTTuuuuuuugggggaaaaaddddddiiiiiiiiiiii
    # otttttziiiiv
    if stage_ == 6 and message == maindct[lang_][5] or message == dct[lang_][14] and stage_==6.61:
        cur.execute(stagee.format('{}', user_id).format(6.6))
        connect.commit()
        m_m = [KeyboardButton(text=str(dct[lang_][16]))]
        t_h = [KeyboardButton(text=town_hos[lang_][0])]
        t_h1 = [KeyboardButton(text=town_hos[lang_][1])]
        t_h2 = [KeyboardButton(text=town_hos[lang_][2])]
        t_h3 = [KeyboardButton(text=town_hos[lang_][3])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][33],
                                 reply_markup=ReplyKeyboardMarkup([t_h, t_h1, t_h2, t_h3, m_m, ], resize_keyboard=True))
    if message in town_hos[lang_] and stage_==6.6:
        cur.execute(upd_DOM.format(message, user_id))
        cur.execute(stagee.format('{}', user_id).format(6.61))
        connect.commit()
        b_b = [KeyboardButton(text=str(dct[lang_][14]))]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][12],
                                 reply_markup=ReplyKeyboardMarkup([b_b], resize_keyboard=True))
    if message!= dct[lang_][14] and message!= dct[lang_][16] and stage_==6.61:
        m_m = [KeyboardButton(text=str(dct[lang_][16]))]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][13],
                                 reply_markup=ReplyKeyboardMarkup([m_m], resize_keyboard=True))
        if filial == town_hos[lang_][0]:
            adm_check = 'Ismi: {}\nTelefon raqami: {}\nFilial: {}\n\n'.format(
                a_name, pnum_, filial)+message
            context.bot.send_message(chat_id=-1001549353456, text=adm_check)
        if filial == town_hos[lang_][1]:
            adm_check = 'Ismi: {}\nTelefon raqami: {}\nFilial: {}\n\n'.format(
                a_name, pnum_, filial)+message
            context.bot.send_message(chat_id=-1001549353456, text=adm_check)
        if filial == town_hos[lang_][2]:
            adm_check = 'Ismi: {}\nTelefon raqami: {}\nFilial: {}\n\n'.format(
                a_name, pnum_, filial)+message
            context.bot.send_message(chat_id=-1001549353456, text=adm_check)
        if filial == town_hos[lang_][3]:
            adm_check = 'Ismi: {}\nTelefon raqami: {}\nFilial: {}\n\n'.format(
                a_name, pnum_, filial)+message
            context.bot.send_message(chat_id=-1001549353456, text=adm_check)
    # otttttziiiiv
def ru(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(chat_id=user_id, text='Здравствуйте, бот глазной клиники "Ko’z Nuri"😊')
    context.bot.send_message(chat_id=user_id, text='Пожалуйта, введите ваше имя:')
    sleep(1)

    connect.commit()
def uz(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='davom etish>>>')]
    context.bot.send_message(chat_id=user_id, text='Assalomu aleykum bu Ko’z Nuri Klinika bo’ti 😊:')
    context.bot.send_message(chat_id=user_id, text='Iltimos, ismingizni kiriting:')
    sleep(1)
    connect.commit()
def ru_change(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(5))
    connect.commit()
    k2_but = [KeyboardButton(text='🏠Главное меню')]
    context.bot.send_message(chat_id=user_id, text='🏠 Нажмите на кнопку  "🏠Главное меню"',  reply_markup= ReplyKeyboardMarkup([k2_but], resize_keyboard=True))
    sleep(1)

    connect.commit()
def uz_change(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(5))
    connect.commit()
    k1_but = [KeyboardButton(text='🏠Asosiy menyu')]
    context.bot.send_message(chat_id=user_id, text='🏠Asosiy menyu tugmasini bosing...',  reply_markup= ReplyKeyboardMarkup([k1_but], resize_keyboard=True))

    connect.commit()
def get_contac(update, context):
    user_id = update.message.chat_id
    num = update.message.contact.phone_number
    num = str(num)
    conn = sqlite3.connect('b_users.sqlite')
    cur = conn.cursor()
    cur.execute(update_phone_num.format(num, user_id))
    conn.commit()
    cur.execute(stagee.format('{}', user_id).format(6))
    conn.commit()


    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    conn.commit()

    lang_ = lang_[0][0]

    main_button0 = [KeyboardButton(text=maindct[lang_][0])]
    main_button = [KeyboardButton(text=maindct[lang_][1]),
                   KeyboardButton(text=maindct[lang_][2])]
    main_button1 = [KeyboardButton(text=maindct[lang_][3]),
                    KeyboardButton(text=maindct[lang_][4])]
    main__ = [KeyboardButton(text=maindct[lang_][5])]
    context.bot.send_message(chat_id=user_id, text=dct[lang_][16] + ':',
                             reply_markup=ReplyKeyboardMarkup([main_button0, main_button,
                                                               main_button1, main__], resize_keyboard=True))
def adm(update,context):
    user_id = update.message.chat_id
    text = update.message.caption
    photo_id = update.message.photo[-1].file_id
    file = context.bot.getFile(photo_id)
    file.download('Picture.jpeg')
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()


    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_= cur.execute(lang_select.format(user_id)).fetchall()
    day = cur.execute(select_DAY_.format(user_id)).fetchall()
    a_name = cur.execute(select_name.format(user_id)).fetchall()
    time_ = cur.execute(select_TIME_.format(user_id)).fetchall()
    zakaz  = cur.execute(select_ZAKAZ.format(user_id)).fetchall()
    filial = cur.execute(select_DOM.format(user_id)).fetchall()
    p_num = cur.execute(select_num.format(user_id)).fetchall()
    connect.commit()

    try:
        day = day[0][0]
        time_check = time_[0][0]
        zakaz_ = zakaz[0][0]
        stage_ = stage_[0][0]
        lang_ = lang_[0][0]
        a_name = a_name[0][0]
        filial = filial[0][0]
        pnum_ = p_num[0][0]

    except Exception:
        pass

    if stage_ ==6.14:
        m_m = [KeyboardButton(text=str(dct[lang_][16]))]
        if day[-1]== 'а' and lang_==1:
                    ss = day[0:-1]
                    ss = ss+'у'
                    context.bot.send_message(chat_id=user_id, text=dct[lang_][32].format(ss, time_check),
                                         reply_markup=ReplyKeyboardMarkup([m_m], resize_keyboard=True))
        else:
                    context.bot.send_message(chat_id=user_id, text=dct[lang_][32].format(day, time_check),
                                             reply_markup=ReplyKeyboardMarkup([m_m], resize_keyboard=True))

        adm_check = 'Ismi: {}\nTelefon raqami: {}\n Ko"rikdan otish kuni: {}\nSoat: {}\nFilial: {}'.format(
                        a_name, pnum_, day,
                        time_check, filial)

        context.bot.send_photo(photo= open('Picture.jpeg','rb'), chat_id=-1001549353456, caption=adm_check)
        sleep(1.5)





















    # try:
    #     if int(time_check[0:2]) == 9 and time_check[2]== ':' and int(time_check[-1]) == 0 and stage_ == 6.12  :
    #         cur.execute(upd_TIME_.format(time_check, user_id))
    #         connect.commit()
    #         m_m = [KeyboardButton(text=str(dct[lang_][16]))]
    #         if day[-1]== 'а' and lang_==1:
    #             ss = day[0:-1]
    #             ss = ss+'у'
    #             context.bot.send_message(chat_id=user_id, text=dct[lang_][32].format(ss, time_check),
    #                                  reply_markup=ReplyKeyboardMarkup([m_m], resize_keyboard=True))
    #         else:
    #             context.bot.send_message(chat_id=user_id, text=dct[lang_][32].format(day, time_check),
    #                                      reply_markup=ReplyKeyboardMarkup([m_m], resize_keyboard=True))
    #         if filial==town_hos[lang_][0]:
    #               adm_check = 'Ismi: {}\nTelefon raqami: {}\n Ko"rikdan otish kuni: {}\nSoat: {}\nFilial: {}'.format(a_name, pnum_, day,
    #                                                                                                time_check, filial)
    #               context.bot.send_message(chat_id=-1001549353456, text=adm_check)
    #         if filial==town_hos[lang_][1]:
    #               adm_check = 'Ismi: {}\nTelefon raqami: {}\n Ko"rikdan otish kuni: {}\nSoat: {}\nFilial: {}'.format(a_name, pnum_, day,
    #                                                                                                time_check, filial)
    #               context.bot.send_message(chat_id=-1001549353456, text=adm_check)
    #         if filial==town_hos[lang_][2]:
    #               adm_check = 'Ismi: {}\nTelefon raqami: {}\n Ko"rikdan otish kuni: {}\nSoat: {}\nFilial: {}'.format(a_name, pnum_, day,
    #                                                                                                time_check, filial)
    #               context.bot.send_message(chat_id=-1001549353456, text=adm_check)
    #         if filial==town_hos[lang_][3]:
    #               adm_check = 'Ismi: {}\nTelefon raqami: {}\n Ko"rikdan otish kuni: {}\nSoat: {}\nFilial: {}'.format(a_name, pnum_, day,
    #                                                                                                time_check, filial)
    #               context.bot.send_message(chat_id=-1001549353456, text=adm_check)
    #     if int(time_check[0:2])>= 10 and time_check[2]== ':' and int(time_check[-1]) == 0 and int(time_check[0:2])<= 17 and stage_ == 6.12:
    #         cur.execute(upd_TIME_.format(time_check, user_id))
    #         connect.commit()
    #         m_m = [KeyboardButton(text=str(dct[lang_][16]))]
    #
    #         if day[-1]== 'а' and lang_==1:
    #             ss = day[0:-1]
    #             ss = ss+'у'
    #             context.bot.send_message(chat_id=user_id, text=dct[lang_][32].format(ss, time_check),
    #                                  reply_markup=ReplyKeyboardMarkup([m_m], resize_keyboard=True))
    #         else:
    #             context.bot.send_message(chat_id=user_id, text=dct[lang_][32].format(day, time_check),
    #                                      reply_markup=ReplyKeyboardMarkup([m_m], resize_keyboard=True))
    #         if filial == town_hos[lang_][0]:
    #             adm_check = 'Ismi: {}\nTelefon raqami: {}\n Ko"rikdan otish kuni: {}\nSoat: {}\nFilial: {}'.format(
    #                 a_name, pnum_, day,
    #                 time_check, filial)
    #             context.bot.send_  (chat_id=-1001549353456, text=adm_check)
    #         if filial == town_hos[lang_][1]:
    #             adm_check = 'Ismi: {}\nTelefon raqami: {}\n Ko"rikdan otish kuni: {}\nSoat: {}\nFilial: {}'.format(
    #                 a_name, pnum_, day,
    #                 time_check, filial)
    #             context.bot.send_message(chat_id=-1001549353456, text=adm_check)
    #         if filial == town_hos[lang_][2]:
    #             adm_check = 'Ismi: {}\nTelefon raqami: {}\n Ko"rikdan otish kuni: {}\nSoat: {}\nFilial: {}'.format(
    #                 a_name, pnum_, day,
    #                 time_check, filial)
    #             context.bot.send_message(chat_id=-1001549353456, text=adm_check)
    #         if filial==town_hos[lang_][3]:
    #               adm_check = 'Ismi: {}\nTelefon raqami: {}\n Ko"rikdan otish kuni: {}\nSoat: {}\nFilial: {}'.format(a_name, pnum_, day,
    #                                                                                                time_check, filial)
    #               context.bot.send_message(chat_id=-1001549353456, text=adm_check)
    #
    # except Exception:
    #     pass
