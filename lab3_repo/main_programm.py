import sub_class
import datetime
print("Пожалуйста, введите username или vk_id")
username = input()
client = sub_class.client_class()
client.get_params(1, username)
client.http_method = client.generate_url(client.method)
id = client._get_data(client.method,client.http_method)
client.get_params(2, id)
client.http_method = client.generate_url(client.method)
dates = client._get_data(client.method,client.http_method)
years = []
ages = []
for i in dates:
    try:
        dt = datetime.datetime.strptime(i,'%d.%m.%Y')
        date = dt.timetuple()
        years.append(date.tm_year)
    except:
        pass
for i in years:
   ages.append(2016-i)
f_age = min(ages)
l_age = max(ages)
for i in range(f_age, l_age + 1, 1):
    q = 0
    for el in ages:
        if el == i:
            q += 1
    print (str(i) + ' ' + '#' * q)


