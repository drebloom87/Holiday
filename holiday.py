""" This is my holiday package program, It will give the user a choice of five destinations with different prices for
different lengths of stays as well as an option to hire a vehicle for the duration of the stay"""


# This function uses an if statement to return a price for each destination
def plane_cost(city_flight):
    city_prices = {
        "Amsterdam": 250,
        "Ibiza": 300,
        "Ayia Napa": 400,
        "Zante": 525,
        "Thailand": 600
    }
    return city_prices.get(city_flight, 0)


# This function uses an if statement to get various prices for different lengths of stay
# which changes depending on the length of stay
def hotel_cost(num_nights):
    if num_nights >= 15:
        price_per_night = 55
    elif num_nights >= 13:
        price_per_night = 65
    elif num_nights >= 9:
        price_per_night = 80
    elif num_nights >= 5:
        price_per_night = 90
    elif num_nights >= 1:
        price_per_night = 100
    else:
        return 0
    return num_nights * price_per_night


# This function uses an if statement to get the price of a rental for a set amount of days
# which changes depending on the length of rental
def car_rental(rental_days):
    if rental_days >= 15:
        price_per_day = 25
    elif rental_days >= 13:
        price_per_day = 35
    elif rental_days >= 9:
        price_per_day = 40
    elif rental_days >= 5:
        price_per_day = 50
    elif rental_days >= 1:
        price_per_day = 60
    else:
        return 0
    return rental_days * price_per_day


# This function calculates the flight, hotel & car rental costs
# Converting the flight variable to an integer so that it prints the correct outcome
def holiday_cost(city_flight, num_nights, rental_days):
    flights = plane_cost(city_flight)
    hotel = hotel_cost(num_nights)
    rental = car_rental(rental_days)
    return flights + hotel + rental


def premium(city_flight, num_nights, rental_days):
    total_cost = holiday_cost(city_flight, num_nights, rental_days)
    premium_cost = total_cost * 1.35  # Adding 35%
    return premium_cost


city_choices = "Amsterdam", "Ayia Napa", "Ibiza", "Thailand", "Zante"
print("\n".join(city_choices))


while True:  # Use a while loop to ask the user to stop the program crashing when a wrong input is used
    city_flight = input("\nChoose which city you would like to fly to from the list above: ").capitalize()
    if city_flight in city_choices:  # .capitalize is used to avoid errors when a correct destination is input
        print(f"\nYou have chosen {city_flight} as your destination.")
        break
    else:  # Below is the error message for incorrect input
        print(f"\n{city_flight} is not a invalid destination choice. Please enter a valid destination")
        continue


while True:  # This while loop will ask the user to entre again if they enter anything not between 1 and 28
    num_nights = (int(input("\nPlease enter the number of nights you plan to stay: ")))
    if num_nights == 0:
        print(f"\nOur day rate will apply for any 'day only' bookings under 24 hours, should you need a room.")
        break  # Advises the user we only charge per night
    elif 0 < num_nights <= 28:
        print(f"\nThe length of your stay will be {num_nights} nights.")
        break
    else:  # Advises the user we only do bookings for up to 28 days
        print(f"\nUnfortunately we do not offer a stay for {num_nights} nights. Please enter between 1 and 28 days.")


while True:
    rental_days = (int(input("\nPlease enter the amount of days you would like to rent a car for: ")))
    if rental_days == 0:
        print(f"\nYou have entered 0 nights, a fee of £60 will be charged for any bookings shorter than 24 hours.")
        break  # Advises the user they will be charged by the day if 0 is entered
    elif 0 < rental_days <= 28:
        print(f"\nYou have chosen to hire a vehicle for {rental_days} days.")
        break
    else:  # Advises the user that we only do bookings for up to 28 days
        print(f"\nUnfortunately we do not offer a rental for {num_nights} nights. Please enter between 1 and 28 days.")


print(f"\nIs this information correct?")
answer = input(f"\nPlease type: 'Y/Yes' for Yes or 'N/No' for No: ").capitalize()
if answer in ["Y", "Yes"]:
    # Ask the user if they want to upgrade to premium
    upgrade = input("\nWould you like to upgrade to the premium package for an additional cost? (Y/N): ").capitalize()
    if upgrade in ["Y", "Yes"]:
        total_cost = premium(city_flight, num_nights, rental_days)
        print(f"\nYour premium holiday package to {city_flight} is £{total_cost}.")
    elif upgrade in ["N", "No"]:
        total_cost = plane_cost(city_flight) + hotel_cost(num_nights) + car_rental(rental_days)
        print(f"\nYou have chosen not to upgrade to premium.")
    else:
        print("\nInvalid option. Please type 'Y' for Yes or 'N' for No.")

    # Print out the cost details
    print(f"\nThe total cost of the flight to {city_flight} will be £{plane_cost(city_flight)}.")
    print(f"\nThe total cost of the hotel in {city_flight} will be £{hotel_cost(num_nights)}.")
    print(f"\nThe total cost of the hired car while in {city_flight} will be £{car_rental(rental_days)}.")
    print(f"\nThe grand total of your holiday package to {city_flight} is £{total_cost}.")

elif answer in ["N", "No"]:
    print(f"\nPlease start again.")
else:
    print(f"\nInvalid option please type either 'Y/Yes' for Yes or 'N/No' for No: ")
