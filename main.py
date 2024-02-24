import csv
from convertor import temperature as t, distance as d

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

        row['Reading'] = f"{round(temperature, 1)}°{target_unit}"
        converted_data_list.append(row)

    return converted_data_list


def convert_distance(data_list, target_unit):

    converted_data_list = []

    for row in data_list:
        if "m" in row['Distance']:
            unit = "m"
        elif "ft" in row['Distance']:
            unit = "ft"
        distance = int(row['Distance'].replace('m', '').replace('ft', ''))

        if (target_unit == 'm') and (unit == 'ft'):
            distance = d.feet_to_meters(distance)
        if (target_unit == 'ft') and (unit == 'm'):
            distance = d.meters_to_feet(distance)

        row['Distance'] = f"{round(distance, 1)}{target_unit}"
        converted_data_list.append(row)

    return converted_data_list


def write_data(converted_data, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Date', 'Distance', 'Reading']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(converted_data)


data = read_data('data.csv')
data_temp_converted = convert_temperature(data,'C')
write_data(data_temp_converted, 'temperature_converted.csv')
data_dist_converted = convert_distance(data, 'ft')
write_data(data_dist_converted, 'distance_converted.csv')