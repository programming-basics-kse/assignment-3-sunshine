import argparse

parser = argparse.ArgumentParser('Olympic Athletes', 'This program will help you to...')
#add in the description and any other features which you and me will add :)
parser.add_argument('input_file', help='Enter the name of file which you want to use', required=True)
parser.add_argument('-medals', help="Enter a target of this program '-medals'", required=True)
parser.add_argument('team', help='Enter a countre which medals you want to see or the team acronym', required=True)
parser.add_argument('year', help='Enter which olympic games you want to see', required=True)
parser.add_argument('output', help="Enter 'output', if you want to output data")
parser.add_argument('output_file', help='Enter a file in which you want to save your data')

arg = parser.parse_args()

with open(arg.input_file, 'r') as athlet_file:



# Напишіть програму, що приймає наступні аргументи командного рядка:
#
# Адреса файлу з даними;
# Другим аргументом - завжди -medals
# Країна. Назва може вводитись як за повною назвою (колонка Team), так і за кодом
# Рік проведення Олімпіади
# (Опціонально) -output
# (Опціонально) файл для виведення результатів
