import datetime 
import calendar
import sys
from random import randint

month_name = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
day_name = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

def FirstMondays(year):
	res = ""
	for month in range(1,13):
		d = datetime.date(year, month, 1)
		while d.weekday() != 0:
			d += datetime.timedelta(1)

		res += d.strftime('%d')[1]
		if (month%3==0):
			res += " "
	return res


def DateAsker(mode,gap):
	year = int(datetime.datetime.today().strftime('%Y'))
	year -= randint(0,gap)
	month = randint(1,12)
	month_range = calendar.monthrange(year,month)[1]
	day = randint(0,month_range)

	if(mode==0):
		print("Tips : {}".format(FirstMondays(year)))

	question = "{}/{}/{}".format(day,month,year)
	if(mode>1):
		question = "Le {} {} {}".format(day,month_name[month-1],year)
	print(question)

	rep = input().lower()
	while(rep not in day_name):
		print("Ce n'est pas un jour de la semaine")
		rep = input().lower()

	answer = calendar.weekday(year, month, day)
	answer = day_name[answer]
	if (rep == answer):
		print("Bonne réponse")
		return 1
	else:
		print("Faux, la réponse était : {}".format(answer))
		return 0

def Trainer(mode=0,gap=0,nb=1):
	print("\n"*30)
	succes = 0
	for i in range(nb):
		succes += DateAsker(mode,gap)
		print("\n"*3)
	ratio = succes/nb*100
	ratio = round(ratio,2)
	print("Ratio sur {} tentatives : {}%".format(nb,ratio))

########### 

iterations = 1
difficulte = 0
year_gap = 0

# ARG 1 = ITERATIONS 
if len(sys.argv) > 1 :
	iterations = int(sys.argv[1])
	if (iterations == 0):
		iterations = 1

# ARG 2 = DIFFICULTE
if len(sys.argv) > 2 : 
	difficulte = int(sys.argv[2])

# ARG 3 = YEAR GAP
if len(sys.argv) > 3 : 
	year_gap = 	 int(sys.argv[3])

##########

Trainer(difficulte,year_gap,iterations)