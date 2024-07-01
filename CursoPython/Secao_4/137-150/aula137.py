# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from dateutil.relativedelta import relativedelta

# data_str = '2022-04-20 07:49:23'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'
# data_str2 = '20/04/2022'
# data_str_fmt2 = '%d/%m/%Y'

# # data = datetime(2022, 4, 20, 7, 30, 59)
# data = datetime.strptime(data_str, data_str_fmt)
# data2 = datetime.strptime(data_str2, data_str_fmt2)

# data = datetime.now(timezone('America/Sao_Paulo'))
# data_segs = data.timestamp()
# print(data_segs)
# print(data.fromtimestamp(data_segs))
# print(data2)

format = '%d/%m/%Y %H:%M:%S'

data1 = datetime.strptime('18/10/2005 17:00:00', format)
data2 = datetime.strptime('15/04/2009 17:05:00', format)

# delta = timedelta(days=10, hours=2)
delta = relativedelta(data2, data1)
print(delta.days, delta.years, delta.months)
# print(data_fim - delta)
# print(data_fim)
# print(data_fim + relativedelta(seconds=60, minutes=10))

# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)
