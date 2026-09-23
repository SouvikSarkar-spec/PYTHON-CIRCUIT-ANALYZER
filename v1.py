while True:
    Menu_choice = int(input('''===== CIRCUIT ANALYZER =====
1. Ohm's Law
2. Series Resistance
3. Parallel Resistance
4. KCL 
5. KVL 
6. Exit
Enter your choice: '''))

    if Menu_choice == 1:
        while True:
            Ohm_law = int(input('''===== OHM'S LAW =====
1. Find Voltage
2. Find Current
3. Find Resistance
4. Back to Main Menu
Enter your choice: '''))

            if Ohm_law == 1:
                I = float(input("Enter Current (I) in Amperes: "))
                R = float(input("Enter Resistance (R) in Ohms: "))

                if R == 0:
                    print("So there will be no current flow as the voltage is zero. Please enter a valid resistance value.")
                    continue

                V = I * R
                print(f"Voltage (V) = {V:.2f} Volts")

            elif Ohm_law == 2:
                V = float(input("Enter Voltage (V) in Volts: "))
                R = float(input("Enter Resistance (R) in Ohms: "))

                if R == 0:
                    print("Resistance cannot be zero. Please enter a valid resistance value.")
                    continue

                I = V / R
                print(f"Current (I) = {I:.2f} Amperes")

            elif Ohm_law == 3:
                V = float(input("Enter Voltage (V) in Volts: "))
                I = float(input("Enter Current (I) in Amperes: "))

                if I == 0:
                    print("Current cannot be zero. Please enter a valid current value.")
                    continue

                R = V / I
                print(f"Resistance (R) = {R:.2f} Ohms")

            elif Ohm_law == 4:
                print("Returning to Main Menu...")
                continue

            else:  # edge case for invalid input
                print("Invalid choice. Please select a valid option from the menu.")

    elif Menu_choice == 2:  # series resistance
        number_of_resistors = int(input("Enter the number of resistors in series: "))
        series_resistance = 0

        for i in range(number_of_resistors):
            resistor_value = float(
                input(f"Enter Resistance {i+1} (R{i+1}) in Ohms: ")
            )
            series_resistance += resistor_value

        print(f"Total Series Resistance (R) = {series_resistance:.2f} Ohms")

    elif Menu_choice == 3:  # Parallel Resistance
        number_of_resistors = int(input("Enter the number of resistors in parallel: "))
        parallel_resistance = 0

        for i in range(number_of_resistors):
            resistor_value = float(
                input(f"Enter Resistance {i+1} (R{i+1}) in Ohms: ")
            )
            parallel_resistance += 1 / resistor_value

        parallel_resistance = 1 / parallel_resistance

        print(f"Total Parallel Resistance (R) = {parallel_resistance:.2f} Ohms")

    elif Menu_choice == 4:
        while True:
            kcl_choice = int(input('''===== KIRCHHOFF'S CURRENT LAW (KCL) =====
1. Verify KCL
2. Find unknown Current
3. Back to Main Menu
Enter your choice: '''))

            if kcl_choice == 1:
                entering_current = int(
                    input("Enter the number of branches entering the circuit: ")
                )
                leaving_current = int(
                    input("Enter the number of branches leaving the circuit: ")
                )

                total_current = 0

                for i in range(entering_current):
                    enter_current = float(
                        input(f"Enter Current entering node I{i+1} in Amperes: ")
                    )
                    total_current += enter_current

                for j in range(leaving_current):
                    leave_current = float(
                        input(f"Enter Current leaving node I{j+1} in Amperes: ")
                    )
                    total_current -= leave_current

                print(f"Total Current (Itotal) = {total_current:.2f} Amperes")

                if total_current == 0:
                    print(
                        "KCL is verified. The sum of currents entering and leaving the node is zero."
                    )
                else:
                    print(
                        "KCL is not verified. The sum of currents entering and leaving the node is not zero."
                    )

            elif kcl_choice == 2:
                no_Entering_current = int(
                    input("Enter the number of branches entering the circuit: ")
                )
                no_Leaving_current = int(
                    input("Enter the number of branches leaving the circuit: ")
                )

                total_leaving_current = 0
                total_entering_current = 0

                choice = input(
                    "Do you want to find the unknown current entering or leaving the node? (enter/leave): "
                ).strip().lower()

                for i in range(no_Entering_current):
                    enter_current = float(
                        input(f"Enter Current entering node I{i+1} in Amperes: ")
                    )
                    total_entering_current += enter_current

                for j in range(no_Leaving_current):
                    leave_current = float(
                        input(f"Enter Current leaving node I{j+1} in Amperes: ")
                    )
                    total_leaving_current += leave_current

                if choice == "enter":
                    unknown_current = (
                        total_leaving_current - total_entering_current
                    )
                    print(
                        f"Unknown Current entering the node (Iunknown) = {unknown_current:.2f} Amperes"
                    )
                else:
                    unknown_current = (
                        total_entering_current - total_leaving_current
                    )
                    print(
                        f"Unknown Current leaving the node (Iunknown) = {unknown_current:.2f} Amperes"
                    )

            elif kcl_choice == 3:
                print("Returning to Main Menu...")
                continue

            else:
                print("Invalid choice. Please select a valid option from the menu.")

    elif Menu_choice == 5:
        while True:
            kvl_choice = int(input('''===== KIRCHHOFF'S VOLTAGE LAW (KVL) =====
1. Verify KVL
2. Find unknown Voltage
3. Back to Main Menu
Enter your choice: '''))

            if kvl_choice == 1:
                source_voltage = int(
                    input("Enter the number of voltage sources in the loop: ")
                )
                load_voltage = int(
                    input("Enter the number of loads in the loop: ")
                )

                total_voltage = 0

                for i in range(source_voltage):
                    voltage_source = float(
                        input(f"Enter Voltage of Source {i+1} in Volts: ")
                    )
                    total_voltage += voltage_source

                for j in range(load_voltage):
                    load_voltage_value = float(
                        input(f"Enter Voltage of Load {j+1} in Volts: ")
                    )
                    total_voltage -= load_voltage_value

                print(f"Total Voltage (Vtotal) = {total_voltage:.2f} Volts")

                if total_voltage == 0:
                    print(
                        "KVL is verified. The sum of voltages around the loop is zero."
                    )
                else:
                    print(
                        "KVL is not verified. The sum of voltages around the loop is not zero."
                    )

            elif kvl_choice == 2:
                no_Source_voltage = int(
                    input("Enter the number of voltage sources in the loop: ")
                )
                no_Load_voltage = int(
                    input("Enter the number of loads in the loop: ")
                )

                type_of_unknown = input(
                    "Is the unknown voltage a source or a load? (source/load): "
                ).strip().lower()

                total_voltage_source = 0
                total_load_voltage = 0
                voltage_source = 0
                load_voltage_value = 0
                unknown_voltage = 0

                for i in range(no_Source_voltage):
                    voltage_source = float(
                        input(f"Enter Voltage of Source {i+1} in Volts: ")
                    )
                    total_voltage_source += voltage_source

                for j in range(no_Load_voltage):
                    load_voltage_value = float(
                        input(f"Enter Voltage of Load {j+1} in Volts: ")
                    )
                    total_load_voltage += load_voltage_value

                if type_of_unknown == "source":
                    unknown_voltage = (
                        total_load_voltage - total_voltage_source
                    )
                    print(
                        f"Unknown Voltage (Vunknown) = {unknown_voltage:.2f} Volts"
                    )

                elif type_of_unknown == "load":
                    unknown_voltage = (
                        total_voltage_source - total_load_voltage
                    )
                    print(
                        f"Unknown Voltage (Vunknown) = {unknown_voltage:.2f} Volts"
                    )

            elif kvl_choice == 3:
                print("Returning to Main Menu...")
                continue

            else:
                print("Invalid choice. Please select a valid option from the menu.")

    elif Menu_choice == 6:
        print("Exiting the program. Goodbye!")
        exit()

    else:
        print("Invalid choice. Please select a valid option from the menu.")