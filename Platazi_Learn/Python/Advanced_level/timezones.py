from datetime import datetime
import pytz

def bogotas_Date():
    time_zone = pytz.timezone('America/Bogota')
    date_time = datetime.now(time_zone)
    print('Bogota date: ', date_time.strftime('%d/%m/%Y, %H:%M:%S'))

def caracas_Date():
    time_zone = pytz.timezone('America/Caracas')
    date_time = datetime.now(time_zone)
    print('Caracas date: ', date_time.strftime('%d/%m/%Y, %H:%M:%S'))

def run():
    bogotas_Date()
    caracas_Date()


if __name__ == '__main__':
    run()