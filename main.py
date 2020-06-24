import telebot
import random
import sqlite3
from bunker.list import crashLow, crashHigh, profList, ageList, rodList, polList, hobbyList, bagazhList, \
    characterList, healthList, fobiaList, dopInfList, catList, card1List, card2List, bunList, negBunList, negBunLow, \
    negBunHigh, pozBunList, pozBunLow, pozBunHigh, timeBun, bunSLow, bunSHight, populationLow, populationHigh, \
    headList, bodyList, legList, bootList, nbList, heightLow, heightHight, weightLow, weightHight, hairStyleList, \
    relationsList
from telebot import types

from sty import fg
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import sys
import requests
import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler

bot = telebot.TeleBot('1180948967:AAFDpzg8FdlikhzVwvRLvLd9716-ffHqvxw')  # Ключ этого бота




######################################### МОЙ КОД КОТОРЫЙ РАБОТАЕТ ################################################

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет! Чтобы начать играть, выбери нужный тебе пункт в клавиатуре данного бота.'
                     '\n\n version 0.3',
                     reply_markup=keyboard())


################################################################################################


############################## БЛОК КОДА С СИСТЕМОЙ ЦИФРА ОТВЕТ ################################
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Эй!   Привет так привет!   Не ожидал тебя тут увидеть.  '
                                          'Если хочешь сыграть в БУНКЕР, выбири нужный пункт во всплывающем меню',
                         reply_markup=keyboard())


    elif message.text == 'Катаклизм':  # Подбор Катаклизма
        crashA = '\nРазрушение инфраструктуры: ' + str(random.randint(crashLow, crashHigh)) + '%'
        populationA = '\nНаселения осталось: ' + str(random.randint(populationLow, populationHigh)) + '%'
        catA = '\nКатаклизм: \n' + str(random.choice(catList))
        bot.send_message(message.chat.id, catA + crashA + populationA,
                         reply_markup=keyboard())


    elif message.text == 'Бункер':  # Подбор БУНКЕРА
        bunA = '  \n\nБункер: ' + random.choice(bunList)
        timeBunA = '  \nВремя в бункере: ' + random.choice(timeBun)
        pozBunH = random.randint(pozBunLow, pozBunHigh)
        negBunH = random.randint(negBunLow, negBunHigh)
        bunSA = '  \nПлощадь бункера: ' + str(random.randint(bunSLow, bunSHight)) + '  кв. метров.'
        pozBunA = '\n➕Плюсы бункера: ' + str(random.sample(set(pozBunList), pozBunH))
        negBunA = '\n➖Минусы бункера: ' + str(random.sample(set(negBunList), negBunH))

        bot.send_message(message.chat.id, bunA + timeBunA + pozBunA + negBunA + bunSA,
                         reply_markup=keyboard())



    elif message.text == 'Карта игрока':  # Подбор БИО
        polA = '  \nПол: ' + random.choice(polList)
        ageA = '  \nВозвраст: ' + random.choice(ageList)
        rodA = '  \nОтношение к детям: ' + random.choice(rodList)
        hairStyleA = '  \n⁉️Прическа: ' + random.choice(hairStyleList)
        heightA = '  \n⁉️Рост: ' + str(random.randint(heightLow, heightHight)) + 'см.'
        weightA = '  \n⁉️Вес: ' + str(random.randint(weightLow, weightHight)) + 'кг.'
        bioA = polA + ageA + rodA + hairStyleA + heightA + weightA
        profA = '  \nПрофессия: ' + random.choice(profList)
        hobbyA = '  \n\nХобби: ' + random.choice(hobbyList)
        bagazhA = '  \n\nБагаж: ' + random.choice(bagazhList)
        characterA = '  \n\nЧеловеческие качества: ' + random.choice(characterList)
        healthA = '  \n\nСостояние здоровья: ' + random.choice(healthList)
        fobiaA = '  \n\nФобии: ' + random.choice(fobiaList)
        dopInfA = '  \n\nДополнительная информация: ' + random.choice(dopInfList)
        card1A = '  \nКарты действия 1: ' + random.choice(card1List)
        card2A = '  \nКарты действия 2: ' + random.choice(card2List)
        cardA = card1A + card2A
        headA = '  \n⁉️Головной убор: ' + random.choice(headList)
        bodyA = '  \n⁉️Торс: ' + random.choice(bodyList)
        legA = '  \n⁉️Ноги: ' + random.choice(legList)
        bootA = '  \n⁉️Обувь: ' + random.choice(bootList)
        nbA = '  \n⁉️Нижнее булье: ' + random.choice(nbList)
        relationsA = '  \n\nОтношения:  ' + random.choice(relationsList)

        bot.send_message(message.chat.id, profA + '\n\nБиологическая характеристика: ' + bioA + healthA + fobiaA
                         + hobbyA + characterA + dopInfA + bagazhA + cardA + relationsA +
                         '\n\n⁉️Одежда персонажа: ' + headA + bodyA + legA + bootA + nbA)

    # Вызов БИЛОГИЧЕСКОЙ ХАР-КИ
    elif message.text == 'Изм. БИО':
        polA = '  \nПол: ' + random.choice(polList)
        ageA = '  \nВозвраст: ' + random.choice(ageList)
        rodA = '  \nОтношение к детям: ' + random.choice(rodList)
        hairStyleA = '  \n⁉️Прическа: ' + random.choice(hairStyleList)
        heightA = '  \n⁉️Рост: ' + str(random.randint(heightLow, heightHight)) + 'см.'
        weightA = '  \n⁉️Вес: ' + str(random.randint(weightLow, weightHight)) + 'кг.'
        bioA = polA + ageA + rodA + hairStyleA + heightA + weightA
        bot.send_message(message.chat.id, '\n\nБиолгическая характеристика: ' + bioA)

    # Вызов СОСТ. ЗДОРОВЬЯ
    elif message.text == 'Изм. Здоровье':
        healthA = '  \n\nСостояние здоровья: ' + random.choice(healthList)
        bot.send_message(message.chat.id, healthA)

    # Вызов ФОБИИ
    elif message.text == 'Изм. Фобию':
        fobiaA = '  \n\nФобии: ' + random.choice(fobiaList)
        bot.send_message(message.chat.id, fobiaA)

    # Вызов ХОББИ
    elif message.text == 'Изм. Хобби':
        hobbyA = '  \n\nХобби: ' + random.choice(hobbyList)
        bot.send_message(message.chat.id, hobbyA)

    # Вызов ЧЕЛ. КАЧЕСТВ
    elif message.text == 'Изм. Качества':
        characterA = '  \n\nЧеловеческие качества: ' + random.choice(characterList)
        bot.send_message(message.chat.id, characterA)

    # Вызов ДОП. ИНФЫ
    elif message.text == 'Изм. Доп.Инфу.':
        dopInfA = '  \n\nДополнительная информация: ' + random.choice(dopInfList)
        bot.send_message(message.chat.id, dopInfA)

    # Вызов БАГАЖА
    elif message.text == 'Изм. Багаж':
        bagazhA = '  \n\nБагаж: ' + random.choice(bagazhList)
        bot.send_message(message.chat.id, bagazhA)

    elif message.text == 'Изм. Карту Д. 1':
        card1A = '  \n\nКарта действия: ' + random.choice(card1List)
        bot.send_message(message.chat.id, card1A)

    elif message.text == 'Изм. Карту Д. 2':
        card2A = '  \n\nКарта действия: ' + random.choice(card2List)
        bot.send_message(message.chat.id, card2A)

    # Вызов ОДЕЖДА
    elif message.text == 'Изм. Одежду':
        headA = '\n⁉️Головной убор: ' + random.choice(headList)
        bodyA = '\n⁉️Торс: ' + random.choice(bodyList)
        legA = '\n⁉️Ноги: ' + random.choice(legList)
        bootA = '\n⁉️Обувь: ' + random.choice(bootList)
        nbA = '\n⁉️Нижнее булье: ' + random.choice(nbList)

        bot.send_message(message.chat.id, '\nОдежда персонажа: ' + headA + bodyA + legA + bootA + nbA)

    # Вызов Правила
    elif message.text == 'Правила':
        bot.send_message(message.chat.id, '\nПравила:'
                                          '\n1. Минимальное количество игроков 8 человек.'
                                          '\n2. В начале игры ведущий генерирует катаклизм, убежище и '
                                          'персонажа для каждого играющего. Катастрофу и убежище ведущий оглашает в '
                                          'общий чат, проговаривая информацию, либо скидывая текстом. Роли ведущий '
                                          'скидывает в личные сообщения каждого игрока.'
                                          '\n3. Перед началом игры обговаривается приблизительное количество кругов, '
                                          'обычно это половина от общего числа играющих и количество характеристик, '
                                          'которые будут вскрываться в каждом ходу(Желательно вскрывать по 2 '
                                          'характеристики за ход, если количество игроков от 6 до 10, если игроков '
                                          'больше, то по 1 характеристике).'
                                          '\n4. Ведущий случайным образом выбирает, в какой последовательности игроки '
                                          'будут оглашать свои характеристики.'
                                          '\n5. Как только игра началась, каждый игрок должен вскрыть обязательно свою '
                                          'профессию и одну или две характеристики, в зависимости от того, как игроки '
                                          'решили до этого(Обговаривается заранее).'
                                          '\n6. После каждого круга начинается голосование, в ходе которого игроки имеют '
                                          'время высказаться и выбрать, кто по их мнению не заслуживает места в '
                                          'убежище. Кто набирает большее количество голосов – оправдывается и пытается '
                                          'переубедить других игроков в своей важности. Если он это делает успешно - '
                                          'игроки могут перенести свой голос на другого игрока, если у него не '
                                          'получается переубедить игроков за столом – он вылетает из игры. '
                                          'Выбивший игрок может остаться в чате игры, но должен замутиться, '
                                          'чтобы не мешать другим здраво закончить игру.'
                                          '\n7. Ваша цель попасть в бункер.'
                                          '\n8. Цель бункера, это:'
                                          '\n    8.1 Продолжить род.'
                                          '\n    8.2 Приспособиться к условиям жизни после бункера и жить дальше.'
                                          '\n9. Карта игрока - это Ваши характеристики, которые Вы вскрываете '
                                          'постепенно с другими игроками.'
                                          '\n10. Изм. ***** - это функция позволяющая заменить какие либо '
                                          'характеристики. Использовать ее можно только если:'
                                          '\n   10.1 - Если у Вас совпали характеристики с другим игроком (профессия, '
                                          'хобби, фобия, здоровье, доп.инфа, багаж, ч-кие качества), но есть исключения:'
                                          '\n       10.1.1 "Здоров" - может быть у нескольких игроков'
                                          '\n       10.1.2 "Нет фобии" - может быть у нескольких игроков'
                                          '\n   10.2 Если была использована карта действия'
                                          '\n   10.3 Если Вы спалили характеристику вне хода'
                                          '\n11. Карта действия, бывает 2х видов:'
                                          '\n   11.1 Карта Д. 1 - Влияет на характеристики игроков'
                                          '\n   11.2 Карта Д. 2 - Влияет на бункер'
                                          '\n12. Карты действия можно использовать в любое время'
                                          '\n13. Карты действия нельзя использовать после смерти/изгнания'
                                          '\n14. Сексолог изменяет характеристку "Против детей" у 1 человеку '
                                          'на "За детей"'
                                          '\n15. Психолог изменяет фобию у 1 человека на "Нет фобии"'
                                          '\n16. ')


def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Катаклизм')
    btn2 = types.KeyboardButton('Бункер')
    btn3 = types.KeyboardButton('Карта игрока')
    btn4 = types.KeyboardButton('Изм. БИО')
    btn5 = types.KeyboardButton('Изм. Здоровье')
    btn6 = types.KeyboardButton('Изм. Фобию')
    btn7 = types.KeyboardButton('Изм. Хобби')
    btn8 = types.KeyboardButton('Изм. Качества')
    btn9 = types.KeyboardButton('Изм. Доп.Инфу.')
    btn10 = types.KeyboardButton('Изм. Багаж')
    btn11 = types.KeyboardButton('Изм. Карту Д. 1')
    btn12 = types.KeyboardButton('Изм. Карту Д. 2')
    btn13 = types.KeyboardButton('Изм. Одежду')
    btn14 = types.KeyboardButton('Правила')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4, btn5)
    markup.add(btn6, btn7)
    markup.add(btn8, btn9)
    markup.add(btn10, btn13)
    markup.add(btn11, btn12)
    markup.add(btn14)
    return markup


bot.polling(none_stop=True, interval=0)
