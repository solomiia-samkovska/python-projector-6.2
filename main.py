import csv
from convertor import temperature as t

def read_data(file_name):
    data_list = []
    with open (file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_list.append(row)
    return data_list


def convert_temperature(data_list, target_unit):

    converted_data_list = []

    for row in data_list:
        unit = row['Reading'][-1]
        temperature = int(row['Reading'].replace('°C', '').replace('°F', ''))

        if (target_unit == 'C') and (unit == 'F'):
            temperature = t.fahrenheit_to_celsius(temperature)
            
        if (target_unit == 'F') and (unit == 'C'):
            temperature = t.celsius_to_fahrenheit(temperature)  

        row['Reading'] = f'{round(temperature, 1)}°{target_unit}'
        converted_data_list.append(row)

    return converted_data_list

   
def write_data(converted_data, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Date', 'Reading']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(converted_data)


data = read_data('data.csv')
data_converted = convert_temperature(data,'C')
write_data(data_converted, 'temperature_converted.csv')