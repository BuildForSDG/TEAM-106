import pandas as pd
import re

base =  pd.read_csv('stackGreat.csv', header=0, delimiter='|')
reputation = base['Reputation']
answers = base['Answers']
people_reached = base['PeopleReached']
location = base['Location']
github = base['Github']
membership = base['Membership']
tags = base['Tags']

def clean_reputation(data):
    '''A function to turn the value of reputation to integers'''
    new_data = []
    data = [str(i)[1:-1] for i in data]
    for i in data:
        a = re.sub(r'a', '', i) 
        if len(a)>1:
            new_data+=[int(a)]
        else:
            new_data+=[0]
    return new_data


def clean_answers(data):
    '''A function to turn the value of answers to integers'''

    new_data = []
    data = [str(i) for i in data]
    for i in data:
        a = re.sub(r',', '', i) 
        if len(a)>1 and a!='nan':
            new_data+=[int(a)]
        else:
            new_data+=[0]
    return new_data


def clean_people_reached(data):
    '''A function to turn the value of people reached to integers in their respective millions, thousands.'''

    new_data = []
    data = [str(i) for i in data]
    for i in data:
        a = re.sub(',', '', i)
        try:
            a = int(a)
            new_data+=[a]
        except:
            if a == 'nan':
                new_data+=[0]
            else:
                x = a[-1]
                b = a[:-1]
                z = re.sub('[.]', '', b)
                if x == 'k':
                    z = int(z)*1000
                elif x == 'm':
                    z = int(z)*1000000
                new_data+=[z]
    return new_data


def clean_location(data):
    '''A function to get just the country of users'''

    new_data = []
    data = [str(i) for i in data]
    for i in data:
        a = i.split(', ')
        a = [n.lower() for n in a]
        new_data+=[a[-1]]
    return new_data


def clean_membership(data):
    ''' A function to turn membership values from years and month to just months'''

    new_data = []
    data = [str(i) for i in data]
    
    for i in data:
        if i=='' or i=='nan':
            new_data+=[0]
            continue

        a = i.split(',')

        if len(a) >= 2:
            years = a[0]
            months = a[1]
            years, months = years.split(' '), months.split(' ')
            years, months = int(years[0]) * 12, int(months[1])
            mem = '{:.2f}'.format((years + months)/12)
            new_data += [mem]
        else:
            months = a[0]
            print(months)
            months = months.split(' ')
            mem = '{:.2f}'.format(int(months[0]) / 12)
            new_data+=[mem]
    return new_data
            

base['Reputation'] = clean_reputation(reputation)
base['Answers'] = clean_answers(answers)
base['PeopleReached'] = clean_people_reached(people_reached)
base['Location'] = clean_location(location)
base['Membership'] = clean_membership(membership)
base.to_csv('new.csv', sep='|', index=None)
