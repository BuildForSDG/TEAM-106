import re, requests
from bs4 import BeautifulSoup
import csv

file = open('stack.csv', 'w', newline='')
data = csv.writer(file, delimiter = '|')
data.writerow(['FullName','Reputation','Answers','Questions','PeopleReached','Location','Github','Membership','Tags'])


def scrape(link):
    user = requests.get(link)
    soup = BeautifulSoup(user.text, "html.parser")

    # Full Name
    name = soup.find_all('div', {'class': 'grid--cell fw-bold'})
    name = str(re.findall('>.+<', str(name)))
    x , y = name.index('>'), name.index('<')
    name = name[x+1:y]

    # Reputation
    rep = soup.find_all('div', {'class': 'grid--cell fs-title fc-dark'})
    rep = str(re.findall('[0-9]*,*[0-9]*,[0-9]+', str(rep)))
    rep = rep[1:-1]
    reputation = re.sub(',', '', rep)

    # Answers, Questions, People Reached.
    try:
      answ = soup.find_all('div', {'class': 'grid--cell fs-body3 fc-dark fw-bold'})
      ans = re.findall('[0-9]+,*[0-9]+', str(answ))
      reached = re.findall(r'[.][0-9]+[a-z]+', str(answ))
      answers = ans[0]
      if len(ans) == 3:
        questions = ans[1]
      else:
        questions = ''
      peoplereached = ans[-1] + reached[0]
    except:
      answers, questions, peoplereached = '', '', ''
    
    # Location, Github and Membership
    loc = soup.find_all('div', {'class': 'grid--cell fl1'})
    loc = soup.find_all('div', {'class': 'grid--cell fl1'})
    member = re.findall('Member for .+ months', str(loc))
    membership = re.findall('[0-9]*\syears*,\s[0-9]+\smonths', str(member))
    loc = re.findall(r'fl1">.+</div>', str(loc))
    #location = re.findall('[a-zA-Z]*,\s*[a-zA-Z]*\s*[a-zA-Z]+', str(loc))
    loc_str = str(loc)
    m, n = loc_str.index('f'), loc_str.index(r'/')
    location = str(loc)[m+5:n-1]
    if 'profile' in location or 'href' in location:
      location = ''
    github = re.findall(r'https://github.com/[a-z]+', str(loc))
    #location = location[0]
    if github == []:
      github = ''
    else:
      github = github[0][20:]
    if membership == []:
      membership = ''
    else:
      membership = membership[0]

    # Tags
    tag = soup.find_all('div', {'class': 'grid--cell ws-nowrap'})
    tags = re.findall('>.+</a>', str(tag))
    tags = [i[1:-4] for i in tags if len(i)<15]
    d = ', '
    tags = d.join(tags)

    data.writerow([name, reputation, answers, questions, peoplereached, location, github, membership, tags])


profile_links = open('finalsource.txt', 'r')

# i = 1
# for profile_link in profile_links.readlines():
#   profile_link = profile_link[:-1]
#   try:
#     scrape(profile_link)
#   except:
#     continue
#   if i == 100:
#     break
#   i+=1

profile_links = [i[:-1] for i in profile_links]
lenght = len(profile_links)
x = 50000
while x<lenght:
  try:
    scrape(profile_links[x])
  except:
    continue
  print("Profile {} done".format(x))
  x+=1 
    
