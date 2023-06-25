import sys
from datetime import datetime
from datetime import timedelta  

# 3: Write a function that takes two arguments (feet and inches) with this time object
def do_something(feet, inches):
    print("Feet: ", feet)
    print("Inches: ", inches)

def main():
    dt = datetime.now()
   #utc = datetime.utcnow()
    time_string = dt.strftime("%X")

    # 2: Add the timedelta to the datetime and subtract 60 second and added 2 year . (Hit: timedelta(seconds=60))  For each condition, state the code and output.
    delta = timedelta(seconds=60)
    print(dt + delta)
    dt = dt + delta
    
    delta = timedelta(days=730)
    print(dt + delta)
    dt = dt + delta

    # Create a timedelta object representing 100 days, 10 hours, and 13 minutes
    delta = timedelta(days=100, hours=10, minutes=13)
    print(delta.days, delta.seconds, delta.microseconds)

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            _date, _time, store, item, cost, payment = data
            print(f"{dt}\t{time_string}\t{store}\t{item}\t{cost}\t{payment}")

    # 3: Run the do_something function with the following arguments: feet = 5, inches = 8
    do_something(5, 8)

main()
