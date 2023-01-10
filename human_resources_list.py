with open("hr_system.txt") as hr_system:

    for line in hr_system:

        cleaned_list = line.strip
        splitted = line.split()
        name = splitted[0]
        id_number = splitted[1]
        job_tittle = splitted[2]
        salary = int(splitted[3])
        
        paycheck = salary/24
        
        if job_tittle == "Engineer":
            
            paycheck = paycheck + 1000
        
        print(f"{name} (ID: {id_number}), {job_tittle} - {paycheck:.2f}")
