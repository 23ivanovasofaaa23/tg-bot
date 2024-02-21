from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime


TOKEN = '7172101292:AAGbROkdSkb2xGm3CzYWFrIskhxJjg_bNXE'
def start(update, context):
    update.message.reply_text('Привет! Я простой бот. Вот список команд, которые вы можете использовать:\n'
                              '/start - начать взаимодействие с ботом\n'
                              '/day - узнать текущий день недели на русском\n'
                              '/time - узнать текущее время\n'
                              '/year - узнать текущий год')

def day(update, context):
    days_in_russian = {
        'Monday': 'Понедельник',
        'Tuesday': 'Вторник',
        'Wednesday': 'Среда',
        'Thursday': 'Четверг',
        'Friday': 'Пятница',
        'Saturday': 'Суббота',
        'Sunday': 'Воскресенье'
    }

    today = datetime.datetime.now()
    day_of_week = today.strftime('%A')  # получаем день недели на английском
    day_in_russian = days_in_russian.get(day_of_week, 'Неизвестный день недели')
    update.message.reply_text(f'Сегодня {day_in_russian}.')

def time(update, context):
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    update.message.reply_text(f'Текущее время: {current_time}.')

def year(update, context):
    current_year = datetime.datetime.now().year
    update.message.reply_text(f'Текущий год: {current_year}.')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('day', day))
    dp.add_handler(CommandHandler('time', time))
    dp.add_handler(CommandHandler('year', year))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
