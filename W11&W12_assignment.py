overall_max_life = 0
overall_min_life = 1000

max_life_country = ""
max_life_country_code = ""
max_life_year = ""

min_life_country = ""
min_life_country_code = ""
min_life_year = ""

interest_max_life = 0
interest_min_life = 1000
interest_max_life_country = ""
interest_min_life_country = ""

life_exp_list = []


year_of_interest = input("Enter the year of interest: ")

with open("life-expectancy.csv") as life_data:
    for i, line in enumerate(life_data):

        if i != 0:

            cleaned = line.strip()
            life_expectancy_data = line.split(",")
            country = life_expectancy_data[0]

            country_code = life_expectancy_data[1]
        
            year = int(life_expectancy_data[2])
        
            life_exp = float(life_expectancy_data[3])
            
            if life_exp < overall_min_life:
                overall_min_life = life_exp
                min_life_country = country
                min_life_country_code = country_code
                min_life_year = year

            if life_exp > overall_max_life:
                overall_max_life = life_exp
                max_life_country = country
                max_life_country_code = country_code
                max_life_year = year

        


            if year == year_of_interest:

                life_exp_list.append(life_exp)
                
                if life_exp < interest_min_life:
                    interest_min_life = life_exp
                    interest_min_life_country = country

                if life_exp > interest_max_life:
                    interest_max_life = life_exp
                    interest_max_life_country = country


    avg_life_exp = sum(life_exp_list)/len(life_exp_list)       


                
                          




    print(f"The overall max life expectancy is: {overall_max_life} from {max_life_country} in {max_life_year}")
    print(f"The overall min life expectancy is: {overall_min_life} from {min_life_country} in {min_life_year}")
    print("")
    print(f"For the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {avg_life_exp}")
    print(f"The max life expectancy was in {interest_max_life_country} with {interest_max_life}")
    print(f"The min life expectancy was in {interest_min_life_country} with {interest_min_life}")
