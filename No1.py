from datetime import datetime, timedelta

def print_date_after_days(num_days):
    today = datetime.today()
    future_date = today + timedelta(days=num_days)
    formatted_date = future_date.strftime("%A, %B %d, %Y")
    print(formatted_date)

num_days = int(input("Enter number of days: "))
print_date_after_days(num_days)