import argparse
import csv

parser = argparse.ArgumentParser('Olympic Athletes', 'This program will help you to...')
#add in the description any other features which you and me will add :)
parser.add_argument('input_file', help='Enter the name of file which you want to use', required=True)
parser.add_argument('-medals', help="Enter a target of this program '-medals'", required=True)
parser.add_argument('team', help='Enter a countre which medals you want to see or the team acronym', required=True)
parser.add_argument('year', help='Enter which olympic games you want to see', required=True)
parser.add_argument('output', help="Enter 'output', if you want to output data")
parser.add_argument('output_file', help='Enter a file in which you want to save your data')

arg = parser.parse_args()

user_file = arg.input_file
user_team = arg.team
user_year = arg.year

file_lines = []
with open(f'{user_file}', 'r') as athlet_file:
    try:
        csv_file = csv.reader(athlet_file)
    except Exception:
        tsv_file = athlet_file.split('\t')
    header = next(athlet_file)
    for lines in athlet_file or tsv_file:
        file_lines.append(lines)
print(file_lines)

TEAM = header.index('Team')
NOC = header.index('NOC')

#Програма має обробити наданий файл та вивести в стовбчик
# перші десять медалістів з цієї країни на заданій олімпіаді
# (у форматі "ім'я - дисципліна - тип медалі"), а під цим - сумарну
# кількість медалей за типом (золоті, срібні та бронзові) у цієї країни.
# Програма має коректно обробляти крайні випадки (у заданої країни менше 10 медалей,
# введена країна не існує або у введений рік не проводилась олімпіада). Якщо користувач
# ввів параметр -output, то результат має бути виведений не тільки на екран, а і у вказаний файл

