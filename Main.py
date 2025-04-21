# Imports
from Admin import Admin
from Doctor import Doctor
# from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    # patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Register/view patient')
        print(' 3- Discharge patients')
        print(' 4- View discharged patient')
        print(' 5- Assign doctor to a new patient')
        print(' 6- Update admin details')
        print(' 7- Relocate patients to new doctor')
        print(' 8- Group patient of same surname')
        print(' 9- View management report')
        print(' 10- Quit')
        # get the option
        op = input('Option: ')

        if op == '1':
            Admin.doctor_management(admin, doctors)

        elif op == '2':
            Admin.patient_management(admin)  

        elif op == '3':
            Admin.discharge(admin)

        elif op == '4':
            Admin.view_discharge(admin)

        elif op == '5':
            # 4- Assign doctor to a patient
            Admin.assign_doctor_to_patient(admin,doctors)

        elif op == '6':
            # 5- Update admin detais
            admin.update_details()

        elif op == '7':
            admin.relocating_patients(doctors)

        elif op == '8':
            # 5- Update admin detais
            admin.view_same_surname()

        elif op == '9':
            admin.view_management_report(doctors)

        elif op == '10':
            print("Thank you for visiting..")
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
