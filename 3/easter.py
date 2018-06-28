import sys

def easter_day(year):
	G = year % 19
	C = year // 100
	H = ((C-(C//4)-((8*C+13)//25)+19*G+15))%30
	I = H-(H//28)*(1-29//(H+1))*((21-G)//11)
	J = (year+(year//4)+I+2-C+(C//4))%7
	L = I-J
	month = 3+((L+40)//44)
	day = L+28-31*(month//4)

	if month == 3:
		month = "March"
	else:
		month = "April"
        
	if day == 1 or day == 21 or day == 31:
		n = "st"
	elif day == 2 or day == 22:
		n = "nd"
	elif day == 3 or day == 23:
		n = "rd"
	else:
		n = "th"

	s = "Easter day in "+ str(year) +": " + str(day) + n + " of " + month

	return s
   

def main(year): #pragma: no cover
	print ( "\n################################" )
	print (   "####       EASTER DAY       ####" )
	print (   "################################\n" )
    
	print ( easter_day(year) + "\n" )

if __name__== '__main__': #pragma: no cover
	if len(sys.argv) > 1:
		if int(sys.argv[1]) > 1582:
			main(int(sys.argv[1]))
		else:
			print("Year must be greather than 1582\n")
	else:
		print("Missing year\n")
