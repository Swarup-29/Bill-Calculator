


def main():

    fixed_charge = 138
    Wheeling_Changes_tax = 1.17
    Electricity_Duty = 0.16
    
    while True :
        try:
            user_input = input('Enter your units (if you want to exit than just enter "exit") : ')

            if user_input.lower() == 'exit':
                print("Thank your for using our program..😊")
                break
            
            try:
                unit = int(user_input)
                if unit <= 100:
                    energy_charge = 4.71
                elif unit <= 300:
                    energy_charge = 10.29
                elif unit <= 500:
                    energy_charge = 14.55
                elif unit <= 1000:
                    energy_charge = 16.64   
                
            except ValueError :
                print("Invalid input.")

            
            energy_charge_Tax = unit * energy_charge
            Wheeling_Changes = unit * Wheeling_Changes_tax
            Electricity_Duty_Tx = (fixed_charge + energy_charge_Tax + Wheeling_Changes) * Electricity_Duty
            Total_charge = fixed_charge + energy_charge_Tax + Wheeling_Changes + Electricity_Duty_Tx

            print('\n************Calculated bill************\n')
            print(f"Fixed Charge           : {fixed_charge}")
            print(f"Energy Charge          : {energy_charge_Tax}")
            print(f"Wheeling Charges       : {Wheeling_Changes}")
            print(f"Electricity Duty 16%   : {Electricity_Duty_Tx}")
            print("____________________________________________________")
            print(f"Total Electricity Bill : {Total_charge}")
        
        except ValueError as e:
            print(f"Please enter valid unit.{e}")



if __name__ == '__main__':
    main()







