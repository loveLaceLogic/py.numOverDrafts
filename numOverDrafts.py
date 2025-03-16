# This program calculates the account fee for a checking account.

try:
    # Get user inputs for balance and number of overdrafts
    balance = int(input("Enter the balance: "))
    numOverDrafts = int(input("Enter the number of overdrafts: "))

    # Calculate the fee
    fee = (0.01 * balance) - (5 * numOverDrafts)

    # Display the fee, ensuring it's formatted properly
    print(f"Your fee is: ${fee:.2f}")
    print("Thanks for using this program.")
    
except ValueError:
    print("Invalid input! Please enter valid numbers for balance and overdrafts.")
