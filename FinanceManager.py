import csv


def finance_manager(file, month):
    transactions = []
    total_sum = 0
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            # Get the date, name, amount, and currency
            date = row[0]
            name = row[4]
            amount = float(row[5])

            # Extract the month from the date and compare with the specified month
            transaction_month = date.split('-')[1]
            if transaction_month == month:  # Compare with the specified month provided as input
                transaction = (date, name, amount)
                total_sum += amount
                transactions.append(transaction)

        print(f'Sum of transactions for {month.capitalize()} is {total_sum}')
        print('')
        return transactions


# Define the file path and handle user input with enhanced error handling
file_placeholder = 'C:\\Users\\Prince Sein\\Documents\\Python Dev\\automations\\csv manipulation\\test files\\transactions_{month}.csv'

while True:
    input_month = input("Enter the month (e.g., 01 for January): ")
    if input_month.isdigit() and 1 <= int(input_month) <= 12:  # Check if the input is a number between 1 and 12
        input_month = input_month.zfill(2)  # Add leading zero if necessary
        break
    else:
        print("Invalid input. Please enter a valid month (01 to 12).")

# Call the finance_manager() function with the file path and the user-input month
print(finance_manager(file_placeholder.format(month=input_month), input_month))
