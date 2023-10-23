import pandas as pd
import pyinputplus as pyip


def todaysday():
	d = pd.Timestamp(pd.Timestamp("today").strftime("%Y-%m-%d"))
	return d.day_name()


def dayofweek(day):
    days_list = ["Mon", "Tue", "Wed", 
                    "Thu", "Fri", "Sat", "Sun"]
    return days_list[(day - 1) % 7]

def main():
	day = pyip.inputNum("Enter a day num from 1 to 365: ")

	if (1 <= day <= 365):
		print(f"Number {day} is {dayofweek(day)}")
	else:
		print(ValueError, "Invalid day number")
	
	
if __name__ == "__main__":
    main()
    
