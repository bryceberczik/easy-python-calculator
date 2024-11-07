while True:

    operator = input("Select a operator: (+, -, *, /) ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
        print(round(result, 2))
    elif operator == "-":
        result = num1 - num2
        print(round(result, 2))
    elif operator == "*":
        result = num1 * num2
        print(round(result, 2))
    elif operator == "/":
        result = num1 / num2
        print(round(result, 2))
    else:
        print(f"{operator} is not a vaild choice")

    play_again = input("Would you like to play again? (Y/N) ")

    if play_again.lower() == "y":
        continue
    elif play_again.lower() == "n":
        print("Thank you for using my calculator!")
        break
    else:
        print(f"{play_again} is a invalid response, closing the application.")
        break
