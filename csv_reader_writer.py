import csv

print('-------1-------')

with open('WashingtonDC.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print('-------2-------')

with open('WashingtonDC.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)
    print(rows[0])
    for i in rows:
        print(i)

print('-------3-------')
# Пробуємо завантадити файл вказавши роздільник
with open('WashingtonDC.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)

# Пробуємо завантадити інший файл вказавши вірний роздільник
with open('data_exmpl_2.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)

print('-------4-------')
# Завантажуємо файл і шукаємо інфу

with open('data_exmpl_2.csv', 'r') as f:
    search = input("Enter the data you are searching for: ")
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        if search in str(row):
            print(row)


print('-------5-------')

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]

with open('my_data1.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

with open('my_data1.csv', 'r') as f:
    print(f.read())

print('-------6-------')
# запис за доп quoting
with open('my_data2.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        writer.writerow(row)

with open('my_data2.csv', 'r') as f:
    print(f.read())

print('-------7-------')
# запис за доп writerows
with open('my_data3.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(data)

with open('my_data3.csv') as f:
    print(f.read())

print('-------8-------')
# запис словарів
data_dic = [{
    'hostname': 'sw1',
    'location': 'London',
    'model': '3750',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw2',
    'location': 'Liverpool',
    'model': '3850',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw3',
    'location': 'Liverpool',
    'model': '3650',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw4',
    'location': 'London',
    'model': '3650',
    'vendor': 'Cisco'
}]

with open('my_data_dictwriter.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=list(data_dic[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in data_dic:
        writer.writerow(d)

with open('my_data_dictwriter.csv') as f:
    print(f.read())


ipnut()


# Для запису однієї строки словника
# writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})


# Завдання 1: Створити таблицю "Книга, автор, рік випуску", запитати користувача і заповнити кілька рядків.
# Завдання 2: Зробити програму-запрос, яка видає книги в файлі між певними роками випуску. Тобто, якщо введемо
# 1980 та 1990 то видасть всі книги в проміжку цих років



# pyinstaller --onefile D:\Python\pythonProject\pythonProject\maria2\csv_reader_writer.py
# Задача: створити програмку, яка інформацію з всіх файлів в папці копіює в такі ж файли, але змінюючи назву.

