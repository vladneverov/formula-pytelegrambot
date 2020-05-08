import config
import telebot
from math import pi

bot = telebot.TeleBot(config.token)

'''
1 Запросить у пользователя 2 числа, одной строкой, через запятую с пробелом
2 Разбить строку на 2 числа, по запятой с пробелом
3 Добавить проверку int(), что это действительно 2 числа, а не буквы или строки через запятую
4 Одна функция вычисляет по формуле, другая показывает результат пользователю
5 В примере есть две функции, compute() складывает 2 числа введенных пользователем,
  а sqSphere() вычисляет площадь сферы, по первому числу, второе не имеет значение, по формуле.
  Подставляя в вычисление либо ту функцию либо ту, можно посмотреть результат.

  По умолчанию используется функция sqSphere()!
'''

user_num1 = 0
user_num2 = 0
user_result = 0

# если /start, /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    msg = bot.send_message(message.chat.id, "Привет " 
          + message.from_user.first_name + ", я бот\nВведите два числа в формате:\n2, 3")
    bot.register_next_step_handler(msg, process_numbers_step)

# Два числа одной строкой
def process_numbers_step(message):
    try:
       global user_num1, user_num2, user_result

       # разбиваем строку на два числа
       # по разделителю запятая с пробелом
       numbers = message.text.split(', ')
       user_num1 = int(numbers[0])
       user_num2 = int(numbers[1])

       # вычислить
       sqSphere()
       # показать результат пользователю
       bot.send_message(message.chat.id, resultPrint())
    except Exception as e:
       bot.reply_to(message, 'Это не число или что то пошло не так /start')

def resultPrint():
    '''
      Вывод результата пользователю
    '''
    global user_result

    return "Результат: " + str(user_result) + "\nВычислить еще, нажмите /start"

def compute():
    '''
      Складывает два числа

      введенных пользователем.
    '''
    global user_num1, user_num2, user_result

    user_result = user_num1 + user_num2

def sqSphere():
    '''
      Вычисляет площадь сферы по формуле S = 4πr2
    '''
    global user_num1, user_result

    user_result = 4 * pi * (user_num1 ** 2)

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)