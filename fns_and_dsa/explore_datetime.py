from datetime import datetime ,timedelta

current_date  = datetime.now()

def display_current_datetime(): 

    format_time = current_date.strftime("%Y-%m-%d %H:%M:%S")

    return print(f"Current date and time: {format_time}")

def calculate_future_date(number_of_days):

    future_date = current_date + timedelta(days=number_of_days)

    future_date_formated = future_date.strftime("%Y-%m-%d")

    return print(f"Future date: {future_date_formated}")


display_current_datetime()
 
number_of_days = int(input("Enter the number of days to add to the current date:"))

calculate_future_date(number_of_days)
