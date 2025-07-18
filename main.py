


def main():
    while True:
        user_input = input("Enter the number of units consumed (or type 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Thank you for using the Electricity Bill Calculator!")
            break

        try:
            units = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a number or type 'exit' to quit.\n")
            continue

        
        fixed_charge = 138
        fac_rate = 1.17
        wheeling_rate = 1.2133

        
        if units <= 100:
            energy_rate = 4.71
        elif units <= 300:
            energy_rate = 10.29
        elif units <= 500:
            energy_rate = 14.55
        else:
            energy_rate = 16.64

        
        energy_charge = units * energy_rate
        fac_charge = units * fac_rate
        wheeling_charge = units * wheeling_rate
        total = fixed_charge + energy_charge + fac_charge + wheeling_charge

        
        print("\n--- Electricity Bill ---")
        print(f"Units Consumed        : {units} units")
        print(f"Fixed Charge          : ₹{fixed_charge:.2f}")
        print(f"Energy Charge         : ₹{energy_charge:.2f}")
        print(f"Electricity Duty      : ₹{fac_charge:.2f}")
        print(f"Wheeling Charge       : ₹{wheeling_charge:.2f}")
        print(f"-----------------------------")
        print(f"Total Bill            : ₹{total:.2f}\n")

if __name__ == '__main__':
    main()
