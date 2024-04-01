""" This is my holiday package program, It will give the user a choice of five destinations with different prices for
different lengths of stays as well as an option to hire a vehicle for the duration of the stay"""
# This function uses an if statement to return a price for each destination
def plane_cost(city_flight):
    if city_flight == "Amsterdam":
        return 250
    elif city_flight == "Ibiza":
        return 300
    elif city_flight == "Ayia Napa":
        return 400
    elif city_flight == "Zante":
        return 525
    elif city_flight == "Thailand":
        return 600
    else:
        return 0
# This function uses an if statement to get various prices for different lengths of stay
# which changes depending on the length of stay
def hotel_cost(num_nights):
    if num_nights >= 15:
        return num_nights * 55
    elif 13 <= num_nights <= 14:
        return num_nights * 65
    elif 9 <= num_nights <= 12:
        return num_nights * 80
    elif 5 <= num_nights <= 8:
        return num_nights * 90
    elif 1 <= num_nights <= 4:
        return num_nights * 100
    else:
        num_nights == 0
        return num_nights
# This function uses an if statement to get the price of a rental for a set amount of days
# which changes depending on the length of rental
def car_rental(rental_days):
    if rental_days >= 15:
        return rental_days * 25
    elif 13 <= rental_days <= 14:
        return rental_days * 35
    elif 9 <= rental_days <= 12:
        return rental_days * 40
    elif 5 <= rental_days <= 8:
        return rental_days * 50
    elif 1 <= rental_days <= 4:
        return rental_days * 60
    else:
        rental_days == 0
        return rental_days
# This function calculates the flight, hotel & car rental costs
# Converting the flight variable to an int so it prins the correct outcome
def holiday_cost(flights, hotel, rental):
    flights = int(plane_cost(city_flight))
    hotel = (hotel_cost(num_nights))
    rental = (car_rental(rental_days))
    return flights + hotel + rental


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
        print(f"\nOur day rate will apply for any 'day only' boookings under 24 hours, should you need a room.")
        break  # Advisses the user we only charge per night
    elif num_nights > 0 and num_nights <= 28:
        print(f"\nThe length of your stay will be {num_nights} nights.")
        break
    else:  # Advises the user we only do bookings for up to 28 days
        print(f"\nUnfortunately we do not offer a stay for {num_nights} nights. Please enter between 1 and 28 days.")


while True:
    rental_days = (int(input("\nPlease enter the amount of days you would like to rent a car for: ")))
    if rental_days == 0:
        print(f"\nYou have entered 0 nights, a fee of £60 will be charged for any bookings shorter than 24 hours.")
        break  # Advises the user they will be charged by the day if 0 is entered
    elif rental_days > 0 and rental_days <= 28:
        print(f"\nYou have chosen to hire a vehicle for {rental_days} days.")
        break
    else:  # Advises the user that we only do bookings for up to 28 days
        print(f"\nUnfortunately we do not offer a rental for {num_nights} nights. Please enter between 1 and 28 days.")


while True:
    print(f"\nIs this information correct?")
    answer = input(f"\nPlease type: 'Y/Yes' for Yes or 'N/No' for No: ").capitalize()
    if answer == "Y" or answer == "Yes":  # If yes then the totals are printed in the terminal
        total_cost = plane_cost(city_flight) + hotel_cost(num_nights) + car_rental(rental_days)
        print(F"\nThe total cost of the flight to {city_flight} will be £{plane_cost(city_flight)}.")
        print(F"\nThe total cost of the hotel in {city_flight} will be £{hotel_cost(num_nights)}.")
        print(F"\nThe total cost of the hired car while in {city_flight} will be £{car_rental(rental_days)}.")
        print(F"\nThe grand total of your holiday package to {city_flight} is £{total_cost}.")
        break
    elif answer == "N" or answer == "No":  # If no the user is asked to start again
        print(f"\nPlease start again.")
        break
    else:
        print(f"\nInvalid option please type either 'Y/Yes' for Yes or 'N/No' for No: ")
        continue  # If Y/N/Yes/No isn't entered it will ask the user to try again
