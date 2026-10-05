def compute_forecast(month, sales):
    if month == "Jan" or month == "Feb" or month == "Mar":
        percent = 0.10
    elif month == "Apr" or month == "May" or month == "Jun":
        percent = 0.15
    elif month == "Jul" or month == "Aug" or month == "Sep":
        percent = 0.20
    else:
        percent = 0.25

    nextsales = sales * (1 + percent)

    return nextsales

response = input("Do you want to enter sales? Yes or No: ")

while response == "Yes":
    lastname = input("Enter last name: ")
    month = input("Enter month: ")
    sales = float(input("Enter sales: "))

    nextsales = compute_forecast(month, sales)

    print(f"Last name: {lastname}")
    print(f"Next month's sales: ${nextsales:.2f}")

    response = input("Do you want to enter another sale? Yes or No: ")