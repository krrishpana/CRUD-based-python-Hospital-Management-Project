from Doctor import Doctor
import datetime
import collections

class AuthenticationError(Exception):
    def __init__(self, message):
        print(message)

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
        print("-----Welcome to hospital system-----")
        print("Please login first.")
        print("-----Login-----")
        #Get the details of the admin

        try:

            username = input('Enter the username: ')
            password = input('Enter the password: ')
            # address = input('Enter the address: ')
            if self.__username != username:
                raise AuthenticationError('Incorrect username. Try again.')
            if self.__password != password:
                raise AuthenticationError('Incorrect password. Try again.')

        except AuthenticationError as e:
            return None # Return None to indicate login failure
        else:
            return username, password

    def find_index(self,index,doctors):

            # check that the doctor id exists
        if index in range(0,len(doctors)):

            return True

        # if the id is not in the list of doctors
        else:
            return False

    def view_patients(self):
        try:
            with open("patient.txt","r") as f:
                patients = f.readlines()
                if not patients:
                    print("No patients registered.")
                else:
                    print('ID |          Full Name           |  Age|    Mobile    | Postcode |     Doctor`s Full Name       | ')
                    for index, line in enumerate(patients):
                        all_data = line.strip().split(",")
                        if len(all_data)!=6 and len(all_data)!=7: # Modified to accept 6 or 7 fields (with or without date) so that there will be no errors
                            print(f"Skipping line {index + 1}: {line.strip()}")
                            continue
                        full_name, age, mobile, postcode, symptom, doctor, *_ = all_data 
                        print(f'{index+1 :>3}|{full_name:^30}|{age:>5}|{mobile:^14}|{postcode:^10}|{doctor:^30}|') # Reordered columns and adjusted widths
        except FileNotFoundError:
            print("Patients file not found.")


    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name = input('Enter the name of the doctor: ')
        surname = input('Enter the doctor\'s surname: ')
        speciality = input('Enter the doctor\'s speciality: ')

        return first_name, surname, speciality

    def get_patient_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the symptoms of the doctor in that order.
        """
        full_name = input('Enter the name of the patient: ')
        age = input('Enter the patient\'s age: ')
        mobile = input('Enter the patient\'s mobile: ')
        postcode = input('Enter the patient\'s postcode: ')
        input_symptom = input('Enter the patient\'s symptoms: ').strip()

        return full_name, age, mobile, postcode,input_symptom


    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input('Input: ')


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name , surname, speciality = self.get_doctor_details()

            doctor_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    doctor_exists = True
                    break

            if not doctor_exists:
                new_doctor = Doctor(first_name, surname, speciality)
                doctors.append(new_doctor)
                print("Doctor registered successfully.")

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: '))-1

                    doctor_index = self.find_index(index,doctors)

                    if doctor_index!=False:
                        doctor=doctors[index]
                        break

                    else:
                        print(f"Doctor with that ID was not found")

                        # doctor_index is the ID mines one (-1)

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect. Enter a numeric ID.')

            # menu

            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')

            while True:
                try:
                    op = int(input('Input: ')) # make the user input lowercase

                    if op==1:
                        updated_first_name = input("Enter new first name: ")
                        Doctor.set_first_name(doctor,updated_first_name)
                        break
                    elif op==2:
                        updated_surname = input("Enter new surname: ")
                        Doctor.set_surname(doctor,updated_surname)
                        break
                    elif op==3:
                        updated_speciality = input("Enter new speciality: ")
                        Doctor.set_speciality(doctor,updated_speciality)
                        break
                    else:
                        print("Invalid input, Try 1/2/3")
                except ValueError:
                    print("Enter a valid number")

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            try:
                doctor_index = int(input('Enter the ID of the doctor to be deleted: '))-1
                index = self.find_index(doctor_index, doctors)  # Use ID to find index

                 # use find index function to find the index of the doctor

                if index is not False:

                # if index in range(0,len(doctors)):
                    doctors.pop(doctor_index)
                    print("Doctor deleted.")
                else:
                    print(" The id entered was not found")
            except ValueError:
                print("Invalid ID entered.")
        else:
            print("Invalid Input. Try 1/2/3/4 ")


    def patient_management(self):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Patient Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')

        op = input('Input: ')


        # register
        if op == '1':
            print("-----Register-----")

            # get the patient details
            print('Enter the patient\'s details:')
            full_name, age, mobile, postcode,input_symptom = self.get_patient_details()
            try:
                with open("patient.txt","r") as f:
                    patients = f.readlines()
                for patient in patients:
                        full_name_from_file = patient.strip().split(",")[0]
                        if full_name_from_file == full_name:
                            print('Name already exists.')
                            break

                with open("patient.txt", "a") as f:
                    f.write(f"{full_name},{age},{mobile},{postcode},{input_symptom},not assigned\n")
                print('Patient registered.')
            except FileNotFoundError:
                print("Patients file not found.")

        # View
        elif op == '2':
            print("-----List of Patients-----")
            self.view_patients()


    def assign_doctor_to_patient(self,doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        import datetime  # Import datetime at the top of Admin.py or inside the function

        print("-----Assign Doctor to Patient-----") 
        print("-----Patients-----")
        self.view_patients()

        patient_index_input = input('Please enter the patient ID: ')
        try:
            patient_index = int(patient_index_input) - 1

            with open("patient.txt","r") as f:
                patients = f.readlines()

            if not 0 <= patient_index < len(patients): 
                print('Invalid patient ID.')
                return

        except ValueError:
            print('Invalid patient ID format. Please enter a number.')
            return

        patient_details = patients[patient_index].strip().split(",")

        print("\n-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patient_symptoms = patient_details[4] # Symptom is at index 4
        print(f"Patient symptoms: {patient_symptoms}") 

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)

        doctor_index_input = input('Please enter the doctor ID: ')
        try:
            doctor_index = int(doctor_index_input) - 1

            if self.find_index(doctor_index,doctors):
                    doctor = doctors[doctor_index]
                    doctor_details = f'{doctor.get_first_name()} {doctor.get_surname()}'

                    patient_details[5] = doctor_details  # Assign doctor's name at index 5 
                    if len(patient_details) == 6: # If no date exists yet, append it
                        patient_details.append(datetime.date.today().strftime("%Y-%m-%d"))
                    elif len(patient_details) == 7: # If date exists, update it
                        patient_details[6] = datetime.date.today().strftime("%Y-%m-%d")

                    patients[patient_index] = ",".join(patient_details) + "\n"
                    with open("patient.txt","w") as f:
                        f.writelines(patients)
                    print(f'Patient assigned to Dr. {doctor_details} and registration date recorded.') 

            else:
                print('Invalid doctor ID.')

        except ValueError:
            print('Invalid doctor ID format. Please enter a number.')


    def relocating_patients(self,doctors):
        print("-----Relocating Patients-----")

        print("-----Patients-----")
        self.view_patients()

        patient_index = input('Please enter the patient ID you want to relocate: ')
        with open("patient.txt","r") as f:
                patients = f.readlines()
        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients

            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        patient_details = patients[patient_index].strip().split(",")

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patient_symptoms = patient_details[4]
        print(patient_symptoms)

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    doctor = doctors[doctor_index]
                    doctor_details = f'{doctor.get_first_name()} {doctor.get_surname()}'

                    patient_details[5] = doctor_details # Correctly update doctor at index 5
                    patients[patient_index] = ",".join(patient_details) + "\n"
                    with open("patient.txt","w") as f:
                        f.writelines(patients)
                    print(f'Patient relocated to Dr. {doctor_details}.') # Informative message

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')

    def discharge(self):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """


        while True:
            print("-----View Patients-----")
            self.view_patients()
            discharge = input("Do want to discharge a patient(Y/N): ").upper()
            if discharge == 'Y':
                print("-----Discharge Patient-----")
                try:
                    with open("patient.txt","r") as f:
                        patients = f.readlines()

                    patient_index_input = input('Please enter the patient ID: ')
                    confirm_discharge = input(f"Confirm discharge for patient ID {patient_index_input} (Y/N): ").upper() # Confirmation message

                    if confirm_discharge == 'Y':
                            try: # try-except block for patient_index conversion
                                patient_index = int(patient_index_input) - 1 # Correct index calculation for list

                                if not 0 <= patient_index < len(patients): # Robust index check
                                    print('Invalid patient ID.')
                                else:
                                    discharged_patient_list=patients.pop(patient_index) # pop using correct index
                                    with open("discharged.txt","a") as f:
                                        f.writelines(discharged_patient_list)
                                        print(f"Patient ID {patient_index_input} has been discharged.") # Informative message

                                    with open("patient.txt","w") as f:
                                        f.writelines(patients)
                                break # Break out of the while loop after successful discharge
                            except ValueError:
                                print('Invalid patient ID format. Please enter a number.')
                                continue # Go back to ask for patient ID again
                    elif confirm_discharge == "N":
                        print("Discharge cancelled.") # Informative message
                        break # Exit loop if discharge cancelled
                except FileNotFoundError:
                    print("Error accessing patient data.") # More general error message
                    break # Exit loop if file not found
                except Exception as e: # Catch any other potential errors
                    print(f"An error occurred during discharge: {e}")
                    break # Exit loop on error
            elif discharge == "N":
                print("Discharge process cancelled.") # Informative message
                break
            else:
                print("Invalid input. Please enter Y or N.")


    def view_discharge(self):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharged Patients-----")
        try:
            with open("discharged.txt", "r") as f:
                discharged_patients = f.readlines()
                if not discharged_patients:
                    print("No patients discharged.")
                else:
                    print(' ID |           Full Name            |      Doctor`s Full Name        | Age   |     Mobile     | Postcode ')
                    for index, line in enumerate(discharged_patients):
                        # Split the line by commas and check if it has 6 values
                        fields = line.strip().split(",")
                        if len(fields) == 6 or len(fields) == 7: # Modified to accept 6 or 7 fields (with or without date)
                            full_name, age, mobile, postcode, symptom, doctor, *_ = fields # Use *_ to catch extra fields if present
                            print(f'{index+1:>3} | {full_name:^30} | {doctor:^30} | {age:>5} | {mobile:^14} | {postcode:^8}')
                        else:
                            print(f"Skipping invalid line {index+1}: {line.strip()}")
        except FileNotFoundError:
            print("Discharged file not found.")


    def view_same_surname(self):
        with open("patient.txt", "r") as file:
            lines = file.readlines()

        # Dictionary to store grouped patients
        patient_groups = {}

        # Process each line in the file
        for line in lines:
            details = line.strip().split(",")
            if len(details) < 4:
                continue  # Skip malformed lines

            full_name, age, mobile, postcode = details[:4]
            surname = full_name.split()[-1]

            if surname not in patient_groups:
                patient_groups[surname] = []
            patient_groups[surname].append((full_name, age, mobile, postcode))

             # Display the grouped patients
        for surname, group in patient_groups.items():
            print(f"\nPatients with surname '{surname}':")
            for patient in group:
                print(f"  {patient[0]} - Age: {patient[1]}, Mobile: {patient[2]}, Postcode: {patient[3]}")

    def view_management_report(self, doctors):
        print("-----Management Report-----")

        # menu
        print('Choose the report you want to view:')
        print(' 1 - Total number of doctors in the system')
        print(' 2 - Total number of patient per doctor')
        print(' 3 - Total number of appointments per month per doctor')
        print(' 4 - Total number of patients based on the illness type')

        op = input('Input: ')

        if op == '1':
            no_of_doctors = len(doctors)
            print(f"Total number of doctors in the system are {no_of_doctors}")

        elif op == '2':
            with open("patient.txt", "r") as file:
                lines = file.readlines()

            doctor_patient_count = {}

            for line in lines:
                details = line.strip().split(",")
                if len(details) < 6:
                    continue  # Skips empty values so that it doesnot give an error

                doctor_name = details[5].strip()

                # Count patients per doctor
                if doctor_name in doctor_patient_count:
                    doctor_patient_count[doctor_name] += 1  # Increment count
                elif doctor_name == 'not assigned':
                    continue
                else:
                    doctor_patient_count[doctor_name] = 1  # Initialize count

            print("-----Total number of patients per doctor-----")
            for doctor, count in doctor_patient_count.items():
                print(f"Dr.{doctor}: {count} patients")

        elif op == '3':
            """Display total number of patient registrations per month per doctor """
           
            try:
                with open("patient.txt", "r") as f:
                    patients = f.readlines()
            except FileNotFoundError:
                print("Error: patient.txt file not found.")
                return

            if not patients:
                print("No patient registrations found in patient.txt.")
                return

            # Use defaultdict for easier counting of appointments per doctor per month
            doctor_monthly_appointments = collections.defaultdict(lambda: collections.defaultdict(int))

            for patient_line in patients:
                patient_data = patient_line.strip().split(",")
                if len(patient_data) < 7:
                    print(f"Warning: Skipping invalid patient data line (not enough fields): {patient_line.strip()}")
                    continue  # Skip to the next patient

                try:
                    doctor_name = patient_data[5].strip()  # Doctor's name is at index 5
                    registration_date_str = patient_data[6].strip() # Registration date is at index 6

                    # Parse date string to datetime object (assuming YYYY-MM-DD format)
                    registration_date = datetime.datetime.strptime(registration_date_str, "%Y-%m-%d").date()
                    month_year = registration_date.strftime("%Y-%m")  # Format as YYYY-MM

                    doctor_monthly_appointments[doctor_name][month_year] += 1

                except ValueError as ve:
                    print(f"Warning: Skipping invalid date format or data in line: {patient_line.strip()}. Error: {e}")
                except IndexError: # In case of index out of range during data access.
                    print(f"Warning: Skipping line due to missing data fields: {patient_line.strip()}")
                except Exception as e: # Catch any other unexpected errors during processing
                    print(f"Warning: An unexpected error occurred processing line: {patient_line.strip()}. Error: {e}")


            if not doctor_monthly_appointments:
                print("No patient appointments data to display.")
                return

            print("\n----- Patient Registrations Per Month Per Doctor -----")
            for doctor, monthly_counts in doctor_monthly_appointments.items():
                print(f"\nDoctor: {doctor}")
                for month, count in sorted(monthly_counts.items()): # Sort months chronologically
                    print(f"  {month}: {count} registrations")
                    
        elif op == '4':
            with open("patient.txt", "r") as file:
                lines = file.readlines()

            symptom_counts = {}

            # Process each line in the file
            for line in lines:
                details = line.strip().split(",")
                if len(details) < 5:
                    continue  # Skips empty details

                symptoms = details[4].strip()

                # Count patients per symptom
                if symptoms in symptom_counts:
                    symptom_counts[symptoms] += 1
                else:
                    symptom_counts[symptoms] = 1

            print("-----Total number of patients based on their symptoms-----")
            for symptom, count in symptom_counts.items():
                print(f"{symptom}: {count} patients")

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')

        while True:
            try:
                op = int(input('Input: '))

                if op == 1:
                    username = input("Enter the new username: ")
                    self.__username = username
                    print(f"The new username is {username}")
                    break

                elif op == 2:
                    password = input('Enter the new password: ')
                    # validate the password
                    if password == input('Enter the new password again: '):
                        self.__password = password
                        break
                    else:
                        print("Passwords do not match. Please try again.")

                elif op == 3:
                    address = input("Enter the new address: ")
                    self.__address = address
                    print(f"The new address is {address}")
                    break
                else:
                    print("Invalid input. Please choose 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")


    