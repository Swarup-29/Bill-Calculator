from datetime import datetime

def generate_bill_text(units, fixed_charge, energy_charge, wheeling_charges, electricity_duty, total_bill):
    bill_text = (
        "************ Electricity Bill ************\n"
        f"Units Consumed          : {units}\n"
        f"Fixed Charge            : ₹{fixed_charge:.2f}\n"
        f"Energy Charge           : ₹{energy_charge:.2f}\n"
        f"Wheeling Charges        : ₹{wheeling_charges:.2f}\n"
        f"Electricity Duty @16%   : ₹{electricity_duty:.2f}\n"
        "------------------------------------------\n"
        f"Total Electricity Bill  : ₹{total_bill:.2f}\n"
        "******************************************\n"
    )
    return bill_text

def main():
    fixed_charge = 138
    wheeling_charge_rate = 1.17
    electricity_duty_rate = 0.16

    while True:
        user_input = input('Enter your units (or type "exit" to quit): ')

        if user_input.lower() == 'exit':
            print("Thank you for using our program 😊")
            break

        try:
            units = int(user_input)
            if units <= 0:
                print("Units must be a positive number!")
                continue

            if units <= 100:
                energy_charge_rate = 4.71
            elif units <= 300:
                energy_charge_rate = 10.29
            elif units <= 500:
                energy_charge_rate = 14.55
            elif units <= 1000:
                energy_charge_rate = 16.64
            else:
                print("This program currently supports up to 1000 units.")
                continue

            energy_charge = units * energy_charge_rate
            wheeling_charges = units * wheeling_charge_rate
            electricity_duty = (fixed_charge + energy_charge + wheeling_charges) * electricity_duty_rate
            total_bill = fixed_charge + energy_charge + wheeling_charges + electricity_duty

            # Display energy charge rate
            print(f"Energy Charge Rate: ₹{energy_charge_rate:.2f} per unit")

            # Generate text
            bill_text = generate_bill_text(units, fixed_charge, energy_charge, wheeling_charges, electricity_duty, total_bill)
            print("\n" + bill_text)

            # Save to file with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"Electricity_Bill_{timestamp}.txt"
            try:
                with open(filename, "w") as file:
                    file.write(bill_text)
                    print(f'📄 Bill has been saved as "{filename}"\n')
            except IOError:
                print("Error: Unable to save the bill to file.")

        except ValueError:
            print("Invalid input! Please enter a valid number or 'exit' to quit.")

if __name__ == '__main__':
    main()