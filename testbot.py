import telebot
from config import TOKEN, CURRENCIES
from extensions import CurrenciesConverter, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def helper(message: telebot.types.Message):
    text = 'Для начала работы введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for currency in CURRENCIES.keys():
        text = '\n'.join((text, currency, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Слишком много параметров')

        quote, base, amount = values
        data = CurrenciesConverter.convert(quote, base, amount)
        base_ticker = CURRENCIES[base]
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {data["conversion_rates"][base_ticker] * float(amount)}'
        bot.send_message(message.chat.id, text)

bot.polling()