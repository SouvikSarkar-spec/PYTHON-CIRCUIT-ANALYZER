x = int(input('''===== CIRCUIT ANALYZER =====
1. Ohm's Law
2. Series Resistance
3. Parallel Resistance
4. KCL
5. KVL
6. Exit
Enter your choice: '''))

if x == 1:
    y = int(input('''===== OHM'S LAW =====
1. Find Voltage
2. Find Current
3. Find Resistance
Enter your choice: '''))

    if y == 1:
        I = float(input("Enter Current (I) in Amperes: "))
        R = float(input("Enter Resistance (R) in Ohms: "))
        V = I * R
        print("Voltage (V) =", V, "Volts")

    elif y == 2:
        V = float(input("Enter Voltage (V) in Volts: "))
        R = float(input("Enter Resistance (R) in Ohms: "))
        I = V / R
        print("Current (I) =", I, "Amperes")

    elif y == 3:
        V = float(input("Enter Voltage (V) in Volts: "))
        I = float(input("Enter Current (I) in Amperes: "))
        R = V / I
        print("Resistance (R) =", R, "Ohms")