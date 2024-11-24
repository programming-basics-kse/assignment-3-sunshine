import argparse
import csv


def athletes_searcher (input_file, year_index, year_from_user, team_index, team_from_user, noc_index, medal_index, ):
    medal_list = ['Gold', 'Silver', 'Bronze']
    athletes_dictionary = {}
    for line in input_file:
        if line[year_index] == year_from_user:
            if (line[team_index] == team_from_user or lines[noc_index] == team_from_user) and line[medal_index] in medal_list:
                athletes_dictionary[line[NAME]] = {'discipline' : line[EVENT],
                                            'medal' : line[MEDAL],
                                             'place' : place_dict[line[MEDAL]]}
    return athletes_dictionary

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

def the_first_year_and_medals_dict(input_list,team, noc, u_country, file_year, medal):
    the_first_year = 2024
    years_medal_dict = {}
    for row in input_list:
        if row[team] == u_country or row[noc] == u_country:
            if int(year_validation(row[file_year])) < the_first_year:
                the_first_year = int(row[file_year])
            if row[file_year] in years_medal_dict and row[medal] in medals_dict:
                years_medal_dict[row[file_year]] += 1
            elif row[medal] in medals_dict:
                years_medal_dict[row[file_year]] = 1
    return the_first_year, years_medal_dict

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
    if len(year_place_summer) == 0:
        year_place_summer = f'this country does not participated in summer games in {year}'
    if len(year_place_winter) == 0:
        year_place_winter = f'this country does not participated in winter games in {year}'
    return year_place_summer, year_place_winter

def year_validation(year : str):
    if year.isdigit():
        return year
    else:
        return 0

def user_country_validation(user_county):
    if len(user_county) == 3:
        user_county = user_county.upper()
    else:
        user_county = user_county.capitalize()
    country_list = ['NAM', 'JPN', 'PAR', 'POR', 'TUN', 'YEM', 'MKD', 'HON', 'FRG', 'YMD', 'BER', 'BAH', 'SAA', 'MAD', 'UGA', 'BEN', 'DJI', 'ESA', 'SVK', 'TTO', 'FRA', 'HUN', 'ROU', 'ANT', 'SEN', 'LTU', 'KOS', 'GUM', 'JOR', 'ARM', 'CYP', 'BIH', 'BDI', 'IRI', 'BOT', 'MOZ', 'ANG', 'USA', 'TAN', 'EST', 'BLR', 'GRE', 'BRA', 'CIV', 'MTN', 'ERI', 'MYA', 'NRU', 'SWZ', 'COK', 'SEY', 'PRK', 'UAR', 'CPV', 'NIG', 'BEL', 'CRO', 'NCA', 'KOR', 'KGZ', 'ISV', 'MLI', 'CRC', 'SAM', 'LCA', 'FSM', 'CGO', 'GBS', 'GHA', 'TKM', 'GRN', 'EGY', 'BOH', 'NBO', 'MAR', 'PAN', 'QAT', 'BIZ', 'LBA', 'MNE', 'CAN', 'URU', 'NZL', 'DMA', 'DOM', 'SCG', 'GUY', 'BOL', 'ANZ', 'BAR', 'MHL', 'BRU', 'ISR', 'GAB', 'THA', 'MAS', 'CHI', 'GER', 'TPE', 'WIF', 'SRB', 'MAW', 'KUW', 'GUI', 'LBR', 'ARG', 'IRL', 'KEN', 'VIN', 'POL', 'CAY', 'RUS', 'NFL', 'COM', 'YAR', 'GEO', 'AND', 'BUR', 'SOL', 'CRT', 'ALG', 'MON', 'IRQ', 'LIB', 'NEP', 'IVB', 'HKG', 'TUV', 'ROT', 'PAK', 'FIJ', 'SLO', 'JAM', 'UAE', 'VAN', 'VEN', 'TJK', 'LAO', 'ETH', 'SYR', 'UZB', 'PLW', 'MDA', 'IOA', 'TUR', 'ECU', 'MEX', 'INA', 'SGP', 'COL', 'KAZ', 'NED', 'GAM', 'CZE', 'TLS', 'KSA', 'CHN', 'NOR', 'CUB', 'GUA', 'COD', 'SUI', 'ESP', 'CAF', 'ZIM', 'URS', 'FIN', 'MRI', 'SUR', 'PNG', 'BAN', 'ASA', 'SRI', 'OMA', 'MLT', 'KIR', 'MDV', 'BRN', 'EUN', 'UNK', 'STP', 'SMR', 'YUG', 'VIE', 'NGR', 'AZE', 'ZAM', 'ARU', 'CAM', 'ALB', 'BUL', 'CHA', 'RWA', 'MGL', 'SOM', 'IND', 'GDR', 'RSA', 'GBR', 'HAI', 'TCH', 'LAT', 'LUX', 'PER', 'DEN', 'TOG', 'CMR', 'TGA', 'BHU', 'LES', 'ISL', 'SWE', 'PHI', 'AHO', 'PUR', 'LIE', 'AFG', 'RHO', 'UKR', 'VNM', 'AUT', 'MAL', 'PLE', 'GEQ', 'SSD', 'ITA', 'SLE', 'SUD', 'SKN', 'AUS',
'France', 'Great Britain', 'Denmark', 'Cambodia', 'Lesotho', 'Oman', 'Israel', 'Cameroon', 'Morocco', 'Lebanon', 'Maldives', 'Dominican Republic', 'Zimbabwe', 'Mali', 'United Arab Emirates', 'Soviet Union', 'Turkey', 'Andorra', 'Costa Rica', 'Aruba', 'South Sudan', 'Bhutan', 'Russia', 'Greece', 'Kyrgyzstan', 'Chad', 'Japan', 'Italy', 'Venezuela', 'Moldova', 'Sri Lanka', 'Mauritius', 'Luxembourg', 'Seychelles', 'Belarus', 'China', 'Austria', 'Sierra Leone', 'Benin', 'Zambia', 'Estonia', 'Singapore', 'Brunei', 'Guatemala', 'Finland', 'Gambia', 'Liberia', 'Jamaica', 'Thailand', 'Monaco', 'Belize', 'Malawi', 'Bangladesh', 'Kiribati', 'Sao Tome and Principe', 'India', 'Uzbekistan', 'Czech Republic', 'Mongolia', 'Kosovo', 'Somalia', 'Albania', 'Sudan', 'United States', 'Turkmenistan', 'Madagascar', 'El Salvador', 'Egypt', 'Comoros', 'Palestine', 'Saudi Arabia', 'Malta', 'Angola', 'Spain', 'Saint Kitts and Nevis', 'Uruguay', 'Mauritania', 'Belgium', 'Germany', 'Czechoslovakia', 'Togo', 'Norway', 'Poland', 'Argentina', 'Saint Lucia', 'New Zealand', 'Grenada', 'Chile', 'Samoa', 'Trinidad and Tobago', 'Netherlands', 'Latvia', 'Peru', 'East Germany', 'Bosnia and Herzegovina', 'Namibia', 'Iceland', 'Cayman Islands', 'Laos', 'Syria', 'Tunisia', 'Switzerland', 'Mozambique', 'Armenia', 'Tajikistan', 'Suriname', 'Hungary', 'Botswana', 'Iraq', 'San Marino', 'Djibouti', 'Solomon Islands', 'Portugal', 'Senegal', 'Nigeria', 'Slovenia', 'Cyprus', 'Malaysia', 'Guinea', 'Brazil', 'Guam', 'Ghana', 'Vietnam', 'Paraguay', 'North Korea', 'Dominica', 'Vanuatu', 'Indonesia', 'Liechtenstein', 'Tuvalu', 'Algeria', 'Ecuador', 'South Korea', 'Bahamas', 'Kuwait', 'Slovakia', 'Tonga', 'Uganda', 'Kenya', 'Pakistan', 'Iran', 'Nicaragua', 'Nauru', 'Libya', 'Papua New Guinea', 'Georgia', 'Antigua and Barbuda', 'Yugoslavia', 'Bolivia', 'Guyana', 'Eritrea', 'Azerbaijan', 'Unified Team', 'Palau', 'Lithuania', 'Myanmar', 'Qatar', 'Bulgaria', 'Tanzania', 'Fiji', 'Burundi', 'Sweden', 'Barbados', 'Puerto Rico', 'Marshall Islands', 'Montenegro', 'Ethiopia', 'Cape Verde', 'Croatia', 'Ireland', 'Yemen', 'Central African Republic', 'Cuba', 'Burkina Faso', 'Ukraine', 'South Africa', 'Bahrain', 'Kazakhstan', 'Rwanda', 'Romania', 'Equatorial Guinea', 'Mexico', 'Canada', 'Colombia', 'Hong Kong', 'Afghanistan', 'Honduras', 'Australia', 'Panama', 'Serbia', 'Niger', 'Jordan', 'Philippines', 'Haiti', 'Saint Vincent and the Grenadines', 'Nepal', 'Gabon']
    while not user_county in country_list:
        user_county = input('Enter a country: ')
        if len(user_county) == 3:
            user_county = user_county.upper()
        else:
            user_county = user_county.capitalize()
    return user_county

def continue_validation(decision):
    while not decision == 'yes' and not decision == 'not':
        decision = input('Do you want to try again (Yes or Not) : ').lower()
    return decision

def datas_task_4(output_medals_list, user_country, year_1, summer_1, winter_1, avr):
    data = []
    data.append(f'The first year when {user_country} participated in Olympic year was {year_1}\nSummer location in {year_1}: {summer_1}\nWinter location in {year_1}: {winter_1}')
    data.append(f'The most successful was {output_medals_list[0][0]}: {output_medals_list[0][1]} medals\nThe worst year was {output_medals_list[-1][0]} : {output_medals_list[-1][1]} medals')
    data.append(f'The average amount of medals in {user_country}: {avr} medals')
    return data

def show_data (data):
    for char in data:
        print(char)

def file_data (file):
    import csv
    data = []
    with open(file, 'r') as data_file:
        csv_file = csv.reader(data_file)
        for row in csv_file:
            for char in row:
                data.append(char)
    return data

def output(data, output_file):
    with open(output_file, 'w') as file:
        for chars in data:
            file.write(chars)
            file.write('\n')
        file.write('\n')
    return output_file

def output_append (data, output_file):
    with open(output_file, 'a') as file:
        for chars in data:
            file.write(chars)
            file.write('\n')
        file.write("\n")
    return output_file

def delete_text(file):
    with open(file, 'w') as delete_text_file:
        delete_text_file.write('')
    return file

def additional_task(file_in_lines, argument_list : list):
    user_age =[]
    user_sex = []
    data = []
    sex_list = ['F', 'M']

    top_dict = {'1':{},
                '2':{},
                '3': {},
                '4':{}}
    for args in argument_list:
        if args in top_dict:
            user_age.append(args)
        elif args in sex_list:
            user_sex.append(args)
    for age, sex in zip(user_age, user_sex):
        for row in file_in_lines:
            if row[AGE].isdigit():
                if row[SEX] == sex and age_dict[int(age)] <= int(row[AGE]) < age_dict[int(age)+1] and row[MEDAL] in medals_dict:
                    if row[NAME] in top_dict[age]:
                        top_dict[age][row[NAME]] +=1
                    else:
                        top_dict[age][row[NAME]] = 1
        top_dict[age] = dict(sorted(top_dict[age].items(), key=lambda x: x[1], reverse=True))
        data.append(f'The top athlet in  {sex} sex and in {age_dict[int(age)]} - {age_dict[int(age) + 1]} age is {list(top_dict[age])[0]} - {top_dict[age][list(top_dict[age])[0]]} medals')
    return data



parser = argparse.ArgumentParser('Olympic Athletes', )
parser.add_argument('input_file', help='Enter the name of file which you want to use')
parser.add_argument('-medals', nargs= 2, choices= ['2014', '1988', '1948', '1904', '1928', '1980', '1896', '1920', '1932', '2002', '2006', '1964', '1936', '1952', '1996', '1992', '1984', '1906', '2010', '1968', '2012', '1912', '1972', '1908', '1994', '2004', '1976', '2000', '1900', '1998', '2008', '1960', '1924', '1956', '2016',
'NAM', 'JPN', 'PAR', 'POR', 'TUN', 'YEM', 'MKD', 'HON', 'FRG', 'YMD', 'BER', 'BAH', 'SAA', 'MAD', 'UGA', 'BEN', 'DJI', 'ESA', 'SVK', 'TTO', 'FRA', 'HUN', 'ROU', 'ANT', 'SEN', 'LTU', 'KOS', 'GUM', 'JOR', 'ARM', 'CYP', 'BIH', 'BDI', 'IRI', 'BOT', 'MOZ', 'ANG', 'USA', 'TAN', 'EST', 'BLR', 'GRE', 'BRA', 'CIV', 'MTN', 'ERI', 'MYA', 'NRU', 'SWZ', 'COK', 'SEY', 'PRK', 'UAR', 'CPV', 'NIG', 'BEL', 'CRO', 'NCA', 'KOR', 'KGZ', 'ISV', 'MLI', 'CRC', 'SAM', 'LCA', 'FSM', 'CGO', 'GBS', 'GHA', 'TKM', 'GRN', 'EGY', 'BOH', 'NBO', 'MAR', 'PAN', 'QAT', 'BIZ', 'LBA', 'MNE', 'CAN', 'URU', 'NZL', 'DMA', 'DOM', 'SCG', 'GUY', 'BOL', 'ANZ', 'BAR', 'MHL', 'BRU', 'ISR', 'GAB', 'THA', 'MAS', 'CHI', 'GER', 'TPE', 'WIF', 'SRB', 'MAW', 'KUW', 'GUI', 'LBR', 'ARG', 'IRL', 'KEN', 'VIN', 'POL', 'CAY', 'RUS', 'NFL', 'COM', 'YAR', 'GEO', 'AND', 'BUR', 'SOL', 'CRT', 'ALG', 'MON', 'IRQ', 'LIB', 'NEP', 'IVB', 'HKG', 'TUV', 'ROT', 'PAK', 'FIJ', 'SLO', 'JAM', 'UAE', 'VAN', 'VEN', 'TJK', 'LAO', 'ETH', 'SYR', 'UZB', 'PLW', 'MDA', 'IOA', 'TUR', 'ECU', 'MEX', 'INA', 'SGP', 'COL', 'KAZ', 'NED', 'GAM', 'CZE', 'TLS', 'KSA', 'CHN', 'NOR', 'CUB', 'GUA', 'COD', 'SUI', 'ESP', 'CAF', 'ZIM', 'URS', 'FIN', 'MRI', 'SUR', 'PNG', 'BAN', 'ASA', 'SRI', 'OMA', 'MLT', 'KIR', 'MDV', 'BRN', 'EUN', 'UNK', 'STP', 'SMR', 'YUG', 'VIE', 'NGR', 'AZE', 'ZAM', 'ARU', 'CAM', 'ALB', 'BUL', 'CHA', 'RWA', 'MGL', 'SOM', 'IND', 'GDR', 'RSA', 'GBR', 'HAI', 'TCH', 'LAT', 'LUX', 'PER', 'DEN', 'TOG', 'CMR', 'TGA', 'BHU', 'LES', 'ISL', 'SWE', 'PHI', 'AHO', 'PUR', 'LIE', 'AFG', 'RHO', 'UKR', 'VNM', 'AUT', 'MAL', 'PLE', 'GEQ', 'SSD', 'ITA', 'SLE', 'SUD', 'SKN', 'AUS',
'France', 'Great Britain', 'Denmark', 'Cambodia', 'Lesotho', 'Oman', 'Israel', 'Cameroon', 'Morocco', 'Lebanon', 'Maldives', 'Dominican Republic', 'Zimbabwe', 'Mali', 'United Arab Emirates', 'Soviet Union', 'Turkey', 'Andorra', 'Costa Rica', 'Aruba', 'South Sudan', 'Bhutan', 'Russia', 'Greece', 'Kyrgyzstan', 'Chad', 'Japan', 'Italy', 'Venezuela', 'Moldova', 'Sri Lanka', 'Mauritius', 'Luxembourg', 'Seychelles', 'Belarus', 'China', 'Austria', 'Sierra Leone', 'Benin', 'Zambia', 'Estonia', 'Singapore', 'Brunei', 'Guatemala', 'Finland', 'Gambia', 'Liberia', 'Jamaica', 'Thailand', 'Monaco', 'Belize', 'Malawi', 'Bangladesh', 'Kiribati', 'Sao Tome and Principe', 'India', 'Uzbekistan', 'Czech Republic', 'Mongolia', 'Kosovo', 'Somalia', 'Albania', 'Sudan', 'United States', 'Turkmenistan', 'Madagascar', 'El Salvador', 'Egypt', 'Comoros', 'Palestine', 'Saudi Arabia', 'Malta', 'Angola', 'Spain', 'Saint Kitts and Nevis', 'Uruguay', 'Mauritania', 'Belgium', 'Germany', 'Czechoslovakia', 'Togo', 'Norway', 'Poland', 'Argentina', 'Saint Lucia', 'New Zealand', 'Grenada', 'Chile', 'Samoa', 'Trinidad and Tobago', 'Netherlands', 'Latvia', 'Peru', 'East Germany', 'Bosnia and Herzegovina', 'Namibia', 'Iceland', 'Cayman Islands', 'Laos', 'Syria', 'Tunisia', 'Switzerland', 'Mozambique', 'Armenia', 'Tajikistan', 'Suriname', 'Hungary', 'Botswana', 'Iraq', 'San Marino', 'Djibouti', 'Solomon Islands', 'Portugal', 'Senegal', 'Nigeria', 'Slovenia', 'Cyprus', 'Malaysia', 'Guinea', 'Brazil', 'Guam', 'Ghana', 'Vietnam', 'Paraguay', 'North Korea', 'Dominica', 'Vanuatu', 'Indonesia', 'Liechtenstein', 'Tuvalu', 'Algeria', 'Ecuador', 'South Korea', 'Bahamas', 'Kuwait', 'Slovakia', 'Tonga', 'Uganda', 'Kenya', 'Pakistan', 'Iran', 'Nicaragua', 'Nauru', 'Libya', 'Papua New Guinea', 'Georgia', 'Antigua and Barbuda', 'Yugoslavia', 'Bolivia', 'Guyana', 'Eritrea', 'Azerbaijan', 'Unified Team', 'Palau', 'Lithuania', 'Myanmar', 'Qatar', 'Bulgaria', 'Tanzania', 'Fiji', 'Burundi', 'Sweden', 'Barbados', 'Puerto Rico', 'Marshall Islands', 'Montenegro', 'Ethiopia', 'Cape Verde', 'Croatia', 'Ireland', 'Yemen', 'Central African Republic', 'Cuba', 'Burkina Faso', 'Ukraine', 'South Africa', 'Bahrain', 'Kazakhstan', 'Rwanda', 'Romania', 'Equatorial Guinea', 'Mexico', 'Canada', 'Colombia', 'Hong Kong', 'Afghanistan', 'Honduras', 'Australia', 'Panama', 'Serbia', 'Niger', 'Jordan', 'Philippines', 'Haiti', 'Saint Vincent and the Grenadines', 'Nepal', 'Gabon'],
help="Enter a country or a team which medals you want to see and the year of this Olympic game")
parser.add_argument('-output', nargs= 1, help='Input the output file')
parser.add_argument('-interactive', help='If you want to work with input', action='store_true')
parser.add_argument('--top', nargs='*', choices=['F', 'M', '1', '2', '3', '4'], help='Show you the top in the sex you will choose and age category:\n1: 18-25\n2: 26-35\n3: 36-49\n4: 50+' )

arg = parser.parse_args()

user_file = arg.input_file#



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
SEX = header.index('Sex')
AGE = header.index('Age')

medals_dict = {'Gold' : 0,
              'Silver' : 0,
              'Bronze' : 0}

if arg.medals:
    user_team, user_year = arg.medals
    place_dict = {'Gold': 1,
                  'Silver': 2,
                  'Bronze': 3,
                  }
    athletes_dict = athletes_searcher(file_lines, YEAR, user_year, TEAM, user_team, NOC, MEDAL)
    athletes_dict = dict(sorted(athletes_dict.items(), key=lambda x: x[1]['place']))


    for athletes in athletes_dict:
        if athletes_dict[athletes]['medal'] in medals_dict:
            medals_dict[athletes_dict[athletes]['medal']] += 1
        else:
            medals_dict[athletes_dict[athletes]['medal']] = 1

    user_data = datas(athletes_dict, medals_dict, user_team, user_year)
    show_data(user_data)


elif arg.interactive:
    continue_or_not = 'yes'
    while not continue_or_not == 'not':
        user_country = user_country_validation(input('Enter a country: '))
        avr_amount_of_medals = 0
        the_first_year, years_medal_dict = the_first_year_and_medals_dict(file_lines, TEAM, NOC, user_country, YEAR, MEDAL)
        the_first_year_place_summer, the_first_year_place_winter = location_searcher(file_lines, str(the_first_year), SEASON, LOCATION, YEAR)
        years_medal_list = list(sorted(years_medal_dict.items(), key=lambda x: x[1], reverse=True))
        for year in years_medal_list:
           avr_amount_of_medals += year[1]
        avr_amount_of_medals = int(avr_amount_of_medals / len(years_medal_list))
        user_data = datas_task_4(years_medal_list, user_country, the_first_year, the_first_year_place_summer, the_first_year_place_winter, avr_amount_of_medals)
        output_append(user_data, 'task_4.txt')
        show_data(user_data)
        continue_or_not = continue_validation(input('Do you want to try again (Yes or Not): ').lower())
    user_data = file_data('task_4.txt')

elif arg.top:
    arguments = arg.top
    age_dict = {1: 18,
                2: 25,
                3: 35,
                4: 50,
                5: 1000}
    user_data = additional_task(file_lines, arguments)
    show_data(user_data)


if arg.output:
    user_output_file = arg.output[0]
    delete_text(user_output_file)
    try:
        output(user_data, user_output_file)
    except Exception:
        print('Something went wrong')
delete_text('task_4.txt')



#2 task
def total_medals(data, year):
    country_medals = {}
    for athlete in data:
        if athlete['Year'] == year and athlete['Medal']:
            team = athlete['Team']
            medal = athlete['Medal']
            if team not in country_medals:
                country_medals[team] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
            country_medals[team][medal] += 1

    results = []
    for team, medals in sorted(country_medals.items()):
        results.append(f"{team}: Gold: {medals['Gold']}, Silver: {medals['Silver']}, Bronze: {medals['Bronze']}")
    return results


#3 task
def overall_best_year(data, countries):
    country_yearly_medals = {country: {} for country in countries}

    for athlete in data:
        team = athlete['Team']
        year = athlete['Year']
        if team in countries and athlete['Medal']:
            if year not in country_yearly_medals[team]:
                country_yearly_medals[team][year] = 0
            country_yearly_medals[team][year] += 1

    results = []
    for country, yearly_medals in country_yearly_medals.items():
        if yearly_medals:
            best_year = max(yearly_medals, key=yearly_medals.get)
            results.append(f"{country}: Best Year: {best_year}, Medals: {yearly_medals[best_year]}")
        else:
            results.append(f"{country}: No medals won.")
    return results





