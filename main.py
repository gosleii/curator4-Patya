import telebot

bot = telebot.TeleBot('6865358970:AAFc_70hTDHtRCz6E6FhnsbvEvmYUVQP8CM')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет! Я просто бот :) Ты можешь нажать на кнопки ниже чтобы посмотреть что я умею ')


@bot.message_handler(commands=['chanel'])
def main(message):
    bot.send_message(message.chat.id, '[Канал Умскул](https://www.youtube.com/channel/UCggA5GaSPVyjsqomtwR5ufw',
                     parse_mode='Markdown')


@bot.message_handler(commands=['stishok'])
def main(message):
    bot.send_message(message.chat.id,
                     'На картине у зимы \nВсе бело от снега: \nПоле, дальние холмы,\nИзгородь, телега. \nНо порой блеснут на ней\n Средь поляны ватной \nКрасногрудых снегирей \nСолнечные пятна.',
                     parse_mode='Markdown')


bot.infinity_polling()