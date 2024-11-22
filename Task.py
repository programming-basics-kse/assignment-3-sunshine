import argparse
import csv

def datas (athletes_dictionary, medals_dictionary, team, year):
    data = []
    if len(athletes_dictionary) < 10:
        for i, athlet in zip(range(len(athletes_dictionary) - 1), athletes_dictionary):
            data.append(f'{i + 1}. {athlet} - {athletes_dictionary[athlet]['discipline']} : {athletes_dictionary[athlet]['medal']}')
    else:
        for j, athlet in zip(range(10), athletes_dictionary):
            data.append(f'{j+1}. {athlet} - {athletes_dictionary[athlet]['discipline']} : {athletes_dictionary[athlet]['medal']}')
    data.append(f'\nThe total amount of the medals of the {team} team in {year}:\nGold: {medals_dictionary['Gold']}\nSilver: {medals_dictionary['Silver']}\nBronze: {medals_dictionary['Bronze']}')
    return data

def output(data, output_file):
    with open(output_file, 'w') as file:
        for chars in data:
            file.write(chars)
            file.write('\n')
    return output_file

def show_data (data):
    for char in data:
        print(char)

def year_validation(year : str):
    if year.isdigit():
        return year
    else:
        return 0

def location_searcher(input_file_list, year, SEASON, LOCATION, YEAR):
    year_place_winter = []
    year_place_summer = []
    for row in input_file_list:
        if row[YEAR] == year:
            if row[SEASON] == 'Summer':
                year_place_summer.append(row[LOCATION])
            elif row[SEASON] == 'Winter':
                year_place_winter.append(row[LOCATION])
    year_place_summer = set(year_place_summer)
    year_place_winter = set(year_place_winter)
    return year_place_summer, year_place_winter


parser = argparse.ArgumentParser('Olympic Athletes', 'This program will help you to...')
#add in the description any other features which you and me will add :)
parser.add_argument('input_file', help='Enter the name of file which you want to use')
parser.add_argument('-medals', nargs= 2, choices= ['2014', '1988', '1948', '1904', '1928', '1980', '1896', '1920', '1932', '2002', '2006', '1964', '1936', '1952', '1996', '1992', '1984', '1906', '2010', '1968', '2012', '1912', '1972', '1908', '1994', '2004', '1976', '2000', '1900', '1998', '2008', '1960', '1924', '1956', '2016',
'NAM', 'JPN', 'PAR', 'POR', 'TUN', 'YEM', 'MKD', 'HON', 'FRG', 'YMD', 'BER', 'BAH', 'SAA', 'MAD', 'UGA', 'BEN', 'DJI', 'ESA', 'SVK', 'TTO', 'FRA', 'HUN', 'ROU', 'ANT', 'SEN', 'LTU', 'KOS', 'GUM', 'JOR', 'ARM', 'CYP', 'BIH', 'BDI', 'IRI', 'BOT', 'MOZ', 'ANG', 'USA', 'TAN', 'EST', 'BLR', 'GRE', 'BRA', 'CIV', 'MTN', 'ERI', 'MYA', 'NRU', 'SWZ', 'COK', 'SEY', 'PRK', 'UAR', 'CPV', 'NIG', 'BEL', 'CRO', 'NCA', 'KOR', 'KGZ', 'ISV', 'MLI', 'CRC', 'SAM', 'LCA', 'FSM', 'CGO', 'GBS', 'GHA', 'TKM', 'GRN', 'EGY', 'BOH', 'NBO', 'MAR', 'PAN', 'QAT', 'BIZ', 'LBA', 'MNE', 'CAN', 'URU', 'NZL', 'DMA', 'DOM', 'SCG', 'GUY', 'BOL', 'ANZ', 'BAR', 'MHL', 'BRU', 'ISR', 'GAB', 'THA', 'MAS', 'CHI', 'GER', 'TPE', 'WIF', 'SRB', 'MAW', 'KUW', 'GUI', 'LBR', 'ARG', 'IRL', 'KEN', 'VIN', 'POL', 'CAY', 'RUS', 'NFL', 'COM', 'YAR', 'GEO', 'AND', 'BUR', 'SOL', 'CRT', 'ALG', 'MON', 'IRQ', 'LIB', 'NEP', 'IVB', 'HKG', 'TUV', 'ROT', 'PAK', 'FIJ', 'SLO', 'JAM', 'UAE', 'VAN', 'VEN', 'TJK', 'LAO', 'ETH', 'SYR', 'UZB', 'PLW', 'MDA', 'IOA', 'TUR', 'ECU', 'MEX', 'INA', 'SGP', 'COL', 'KAZ', 'NED', 'GAM', 'CZE', 'TLS', 'KSA', 'CHN', 'NOR', 'CUB', 'GUA', 'COD', 'SUI', 'ESP', 'CAF', 'ZIM', 'URS', 'FIN', 'MRI', 'SUR', 'PNG', 'BAN', 'ASA', 'SRI', 'OMA', 'MLT', 'KIR', 'MDV', 'BRN', 'EUN', 'UNK', 'STP', 'SMR', 'YUG', 'VIE', 'NGR', 'AZE', 'ZAM', 'ARU', 'CAM', 'ALB', 'BUL', 'CHA', 'RWA', 'MGL', 'SOM', 'IND', 'GDR', 'RSA', 'GBR', 'HAI', 'TCH', 'LAT', 'LUX', 'PER', 'DEN', 'TOG', 'CMR', 'TGA', 'BHU', 'LES', 'ISL', 'SWE', 'PHI', 'AHO', 'PUR', 'LIE', 'AFG', 'RHO', 'UKR', 'VNM', 'AUT', 'MAL', 'PLE', 'GEQ', 'SSD', 'ITA', 'SLE', 'SUD', 'SKN', 'AUS',
'France', 'Great Britain', 'Denmark', 'Cambodia', 'Lesotho', 'Oman', 'Israel', 'Cameroon', 'Morocco', 'Lebanon', 'Maldives', 'Dominican Republic', 'Zimbabwe', 'Mali', 'United Arab Emirates', 'Soviet Union', 'Turkey', 'Andorra', 'Costa Rica', 'Aruba', 'South Sudan', 'Bhutan', 'Russia', 'Greece', 'Kyrgyzstan', 'Chad', 'Japan', 'Italy', 'Venezuela', 'Moldova', 'Sri Lanka', 'Mauritius', 'Luxembourg', 'Seychelles', 'Belarus', 'China', 'Austria', 'Sierra Leone', 'Benin', 'Zambia', 'Estonia', 'Singapore', 'Brunei', 'Guatemala', 'Finland', 'Gambia', 'Liberia', 'Jamaica', 'Thailand', 'Monaco', 'Belize', 'Malawi', 'Bangladesh', 'Kiribati', 'Sao Tome and Principe', 'India', 'Uzbekistan', 'Czech Republic', 'Mongolia', 'Kosovo', 'Somalia', 'Albania', 'Sudan', 'United States', 'Turkmenistan', 'Madagascar', 'El Salvador', 'Egypt', 'Comoros', 'Palestine', 'Saudi Arabia', 'Malta', 'Angola', 'Spain', 'Saint Kitts and Nevis', 'Uruguay', 'Mauritania', 'Belgium', 'Germany', 'Czechoslovakia', 'Togo', 'Norway', 'Poland', 'Argentina', 'Saint Lucia', 'New Zealand', 'Grenada', 'Chile', 'Samoa', 'Trinidad and Tobago', 'Netherlands', 'Latvia', 'Peru', 'East Germany', 'Bosnia and Herzegovina', 'Namibia', 'Iceland', 'Cayman Islands', 'Laos', 'Syria', 'Tunisia', 'Switzerland', 'Mozambique', 'Armenia', 'Tajikistan', 'Suriname', 'Hungary', 'Botswana', 'Iraq', 'San Marino', 'Djibouti', 'Solomon Islands', 'Portugal', 'Senegal', 'Nigeria', 'Slovenia', 'Cyprus', 'Malaysia', 'Guinea', 'Brazil', 'Guam', 'Ghana', 'Vietnam', 'Paraguay', 'North Korea', 'Dominica', 'Vanuatu', 'Indonesia', 'Liechtenstein', 'Tuvalu', 'Algeria', 'Ecuador', 'South Korea', 'Bahamas', 'Kuwait', 'Slovakia', 'Tonga', 'Uganda', 'Kenya', 'Pakistan', 'Iran', 'Nicaragua', 'Nauru', 'Libya', 'Papua New Guinea', 'Georgia', 'Antigua and Barbuda', 'Yugoslavia', 'Bolivia', 'Guyana', 'Eritrea', 'Azerbaijan', 'Unified Team', 'Palau', 'Lithuania', 'Myanmar', 'Qatar', 'Bulgaria', 'Tanzania', 'Fiji', 'Burundi', 'Sweden', 'Barbados', 'Puerto Rico', 'Marshall Islands', 'Montenegro', 'Ethiopia', 'Cape Verde', 'Croatia', 'Ireland', 'Yemen', 'Central African Republic', 'Cuba', 'Burkina Faso', 'Ukraine', 'South Africa', 'Bahrain', 'Kazakhstan', 'Rwanda', 'Romania', 'Equatorial Guinea', 'Mexico', 'Canada', 'Colombia', 'Hong Kong', 'Afghanistan', 'Honduras', 'Australia', 'Panama', 'Serbia', 'Niger', 'Jordan', 'Philippines', 'Haiti', 'Saint Vincent and the Grenadines', 'Nepal', 'Gabon'],
help="Enter a country or a team which medals you want to see and the year of this Olympic game")
parser.add_argument('-output', nargs= 1, help='Input the output file')
parser.add_argument('-interactive', help='If you want to work with input', action='store_true')

arg = parser.parse_args()

user_file = arg.input_file

file_lines = []
with open(user_file, 'r') as athlet_file:
    try:
        csv_file = csv.reader(athlet_file, delimiter=',')
        header = next(csv_file)
        for lines in csv_file:
            file_lines.append(lines)
    except Exception:
        csv_file = csv.reader(athlet_file, delimiter='\t')
        header = next(csv_file)
        for lines in csv_file:
            file_lines.append(lines)

TEAM = header.index('Team')
NOC = header.index('NOC')
NAME = header.index('Name')
EVENT = header.index('Event')
YEAR = header.index('Year')
MEDAL = header.index('Medal')
LOCATION = header.index('City')
SEASON = header.index('Season')

place_dict = {'Gold' : 1,
              'Silver' : 2,
              'Bronze' : 3,
}
medals_dict = {'Gold' : 0,
              'Silver' : 0,
              'Bronze' : 0}

if arg.medals:
    user_team, user_year = arg.medals
    athletes_dict = {}
    for line in file_lines:
        if line[YEAR] == user_year:
            if (line[TEAM] == user_team or lines[NOC] == user_team) and line[MEDAL] in medals_dict:
                athletes_dict[line[NAME]] = {'discipline' : line[EVENT],
                                            'medal' : line[MEDAL],
                                             'place' : place_dict[line[MEDAL]]}

    athletes_dict = dict(sorted(athletes_dict.items(), key=lambda x: x[1]['place']))
    for athletes in athletes_dict:
        if athletes_dict[athletes]['medal'] in medals_dict:
            medals_dict[athletes_dict[athletes]['medal']] += 1
        else:
            medals_dict[athletes_dict[athletes]['medal']] = 1

    user_data = datas(athletes_dict, medals_dict, user_team, user_year)
    show_data(user_data)


elif arg.interactive:
    while True:
        user_country = input('Enter a country: ')
        the_first_year = 2024
        years_medal_dict = {}
        avr_amount_of_medals = 0
        for row in file_lines:
            if row[TEAM] == user_country or row[NOC] == user_country:
                if int(year_validation(row[YEAR])) < the_first_year:
                    the_first_year = int(row[YEAR])
                if row[YEAR] in years_medal_dict and row[MEDAL] in medals_dict:
                    years_medal_dict[row[YEAR]] += 1
                elif row[MEDAL] in medals_dict:
                    years_medal_dict[row[YEAR]] = 1
        the_first_year_place_summer, the_first_year_place_winter = location_searcher(file_lines, str(the_first_year), SEASON, LOCATION, YEAR)
        years_medal_list = list(sorted(years_medal_dict.items(), key=lambda x: x[1], reverse=True))
        for year in years_medal_list:
           avr_amount_of_medals += year[1]
        avr_amount_of_medals = int(avr_amount_of_medals / len(years_medal_list))
        print(f'The most successful was {years_medal_list[0][0]}: {years_medal_list[0][1]} medals')
        print(f'The worst year was {years_medal_list[-1][0]} : {years_medal_list[-1][1]} medals')
        print(f'The average amount of medals in {user_country}: {avr_amount_of_medals} medals')
        print(the_first_year_place_winter)
        print(the_first_year_place_summer)

if arg.output:
    user_output_file = arg.output[0]
    output(user_data, user_output_file)

# year and location winter & summer, medals
# програма має виводити статистику цієї країни - перша участь у олімпіаді (рік та місце проведення),
# найуспішніша олімпіада (за кількістю медалей, вивести це значення), найневдаліша, та середня кількість
# медалей кожного типу на кожній олімпіаді


