# -*- coding: utf-8 -*

import json, re
import matplotlib.pyplot as plt
import pandas as pd

continents = \
    {
        'Asia': ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus', 'East Timor', 'Georgia', 'Hong Kong', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Macao', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri', 'Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen'], 
        'Europe': ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'England', 'Estonia', 'Faroe Islands', 'Finland', 'France', 'Germany', 'Gibraltar', 'Greece', 'Holy See (Vatican City State)', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'North Macedonia', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'Northern Ireland', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russian Federation', 'San Marino', 'Scotland', 'Slovakia', 'Slovenia', 'Spain', 'Svalbard and Jan Mayen', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', 'Wales', 'Yugoslavia'], 
        'Africa': ['Algeria', 'Angola', 'Benin', 'Botswana', 'British Indian Ocean Territory', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Central African Republic', 'Chad', 'Comoros', 'Congo', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Lesotho', 'Liberia', 'Libyan Arab Jamahiriya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Mayotte', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Reunion', 'Rwanda', 'Saint Helena', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Swaziland', 'Tanzania', 'The Democratic Republic of Congo', 'Togo', 'Tunisia', 'Uganda', 'Western Sahara', 'Zambia', 'Zimbabwe'], 
        'Oceania': ['American Samoa', 'Australia', 'Christmas Island', 'Cocos (Keeling) Islands', 'Cook Islands', 'Fiji Islands', 'French Polynesia', 'Guam', 'Kiribati', 'Marshall Islands', 'Micronesia, Federated States of', 'Nauru', 'New Caledonia', 'New Zealand', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Palau', 'Papua New Guinea', 'Pitcairn', 'Samoa', 'Solomon Islands', 'Tokelau', 'Tonga', 'Tuvalu', 'United States Minor Outlying Islands', 'Vanuatu', 'Wallis and Futuna'], 
        'North America': ['Anguilla', 'Antigua and Barbuda', 'Aruba', 'Bahamas', 'Barbados', 'Belize', 'Bermuda', 'Canada', 'Cayman Islands', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'El Salvador', 'Greenland', 'Grenada', 'Guadeloupe', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica', 'Martinique', 'Mexico', 'Montserrat', 'Netherlands Antilles', 'Nicaragua', 'Panama', 'Puerto Rico', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Trinidad and Tobago', 'Turks and Caicos Islands', 'United States', 'Virgin Islands, British', 'Virgin Islands, U.S.'], 
        'Antarctica': ['Antarctica', 'Bouvet Island', 'French Southern territories', 'Heard Island and McDonald Islands', 'South Georgia and the South Sandwich Islands'], 
        'South America': ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Falkland Islands', 'French Guiana', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']
    }

linkedIn = {
    'python': 5400000,
    'java': 9940000,
    'c#': 3270000,
    'javascript': 6280000,
    'php': 3680000,
    'swift': 593000,
    'golang': 68000,
    'c++': 5900000,
    'scala': 254000,
    'kotlin': 114000,
    'ruby': 687000,
}

df = pd.read_csv('new.csv', header=0, delimiter='|')
top_languages = ['python', 'javaScript', 'php', 'java', 'swift', 'goLang', 'c#', 'c++', 'scala', 'kotlin', 'ruby']


def check_occurrence(sequence, row):
    '''A function to get the number of languages that a dev makes use of given his tags and top_langueges'''
    row = row.split(', ')
    occurrence = set(sequence).intersection(set(row))
    return occurrence


def get_frequencies(column):
    '''A function to get the number of times a language appears in all tags'''
    column = [str(item) for item in column]
    stats = {}
    for item in column:
        common_language = check_occurrence(top_languages, item)
        for i in common_language:
            if i in stats:
                stats[i] += 1
            else:
                stats[i] = 1
    return stats


def stack_language_stats():
    '''A function to display the graph of languages and their respective number of users'''
    frequency_list = get_frequencies(df['Tags'])
    plt.plot(list(frequency_list.keys()), list(frequency_list.values()))
    plt.title('Popular Languages stat on Stack Overflow')
    plt.xlabel('Languages')
    plt.ylabel('Developers')
    plt.show()


def linkedIn_stats(data):
    ''' A function to plot a graph of how top languages fare among LinkedIn users'''
    plt.plot(list(data.keys()), list(data.values()))
    plt.title('Popular Languages stat on LinkedIn')
    plt.xlabel('Languages')
    plt.ylabel('Developers')
    plt.show()


def experience_stats():
    ''' A function to show a graph of how developers fare with years of experience'''
    data = df['Membership']
    data_dict = {4:0, 6:0, 8:0, 10:0, 12:0} # The keys here represents years of exp and the values are their frequencies
    for i in data:
        if i<=4:
            data_dict[4] += 1
        elif i<=6:
            data_dict[6] += 1
        elif i<=8:
            data_dict[8] += 1
        elif i<=10:
            data_dict[10] += 1
        elif i<=12:
            data_dict[12] += 1
    plt.plot(list(data_dict.keys()), list(data_dict.values()), 'r-')
    plt.title('Developers by Experience')
    plt.xlabel('Years of Experience')
    plt.ylabel('Developers')
    plt.show()

stack_language_stats()
linkedIn_stats(linkedIn)
experience_stats()


def country_stats():
    ''' A function to get countries with their number of devs'''
    data = df['Location']
    data = dict(data.value_counts()) # Getting all unique countries/values in a dict with their frequencies
    country_csv = pd.read_csv('country.csv', delimiter='|')
    d, copy = {}, {}

    # Tried multiple algorithms but this is the best.
    for i in list(country_csv.columns)[1:-1]:
        ind = list(country_csv[i])
        for item in ind:
            a = ind.index(item)
            if item in data and a not in d:
                d.update({a:data[item]})
            elif item in data:
                d[a] += data[item]

    for key, value in d.items():
        copy[country_csv['name'][key]] = value
    return copy
        
countries = country_stats()


def check_continent(country):
    ''' A function to get the continent a country belongs to'''
    for key in continents:
        update = [i.lower() for i in continents[key]]
        if country in update:
            return key


def continents_stats(data):
    ''' A function that shows continents with their respective number of developers'''
    output = {}
    for key in data:
        m = check_continent(key)
        if m == None:
            continue
        try:
            output[m] += data[key]
        except:
            output.update({m:data[key]})
    plt.plot(list(output.keys()), list(output.values()))
    plt.title('Developers by continent')
    plt.xlabel('Continents')
    plt.ylabel('Developers')
    plt.show()

continents_stats(countries)


def continental(data, continent):
    ''' A function to show the graph of a particular continent's countries and it's no of devs
    Note that countries are in alphabetical order and 0 on the x axis means country[0] alphabetically'''

    output = {}     # cat_output means categorised output.
    for key in data:
        m = check_continent(key)
        if m == continent:
            output.update({key:data[key]})

    plt.plot(list(output.values()))
    plt.title('Developers by states in {}'.format(continent))
    plt.xlabel('Contries in {}'.format(continent))
    plt.ylabel('Developers')
    plt.show()


continental(countries, 'Asia')
continental(countries, 'Africa')
continental(countries, 'Antarctica')
continental(countries, 'Europe')
continental(countries, 'Oceania')
continental(countries, 'North America')
continental(countries, 'South America')
