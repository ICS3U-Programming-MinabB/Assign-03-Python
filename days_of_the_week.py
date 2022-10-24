#!/usr/bin/env python3
# Created By: Minab Berhane
# Date: Oct 19, 2022
##this program tells you the number that matches the day of the week


def main():
    # user input for month
    days = input("\033[1;35;40mEnter a number that represents a day (2 = Tuesday): ")
    print("")

    # Checks the case for the correct day
    match days:
        case "1":
            print("\033[1;35;34m1 = Monday!")
        case "2":
            print("\033[1;35;36m2 = Tuesday!")
        case "3":
            print("\033[1;35;34m3 = Wednesday")
        case "4":
            print("\033[1;35;36m4 = Thursday")
        case "5":
            print("\033[1;35;34m5 = Friday")
        case "6":
            print("\033[1;35;36m6 = Saturday!")
        case "7":
            print("\033[1;35;34m7 = Sunday!")
            # Checker to make sure the code marks if something incorrect is inputted
        case Default:
            print("\033[1;35;33mInvalid input, use numbers from 1-7")


if __name__ == "__main__":
    main()
