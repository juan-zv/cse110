def wind_chill(T, V):
    wind_chill_temp = 35.74 + 0.6215*T - 35.75*(V**0.16) + 0.4275*T*(V**0.16)
    return wind_chill_temp

def C_to_F(T):
    C = T*(9/5) +32
    return C



T= float(input("What is the temperature? "))

temp_type = input("Farenheit or Celsius (F/C)? ")

if temp_type.lower() == "f":

    for V in range(0, 60, 5):
        
        V += 5

        wind_chill_temp = wind_chill(T, V)

        print(f"At temperature {T}F, and wind speed {V} mph, the windchill is: {wind_chill_temp: .2f}F")


elif temp_type.lower() == "c":
    C = C_to_F(T)
    
    for V in range(0, 60, 5):
        
        V += 5

        wind_chill_temp = wind_chill(C, V)

        print(f"At temperature {C}F, and wind speed {V} mph, the windchill is: {wind_chill_temp: .2f}F")