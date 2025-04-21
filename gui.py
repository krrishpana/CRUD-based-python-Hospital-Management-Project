import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Admin import Admin  # Import Admin class from Admin.py
from Doctor import Doctor
import datetime
import collections
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import collections


# Initialize Admin and Doctor data
admin = Admin('admin', '123', 'B1 1AB')
doctors = [
    Doctor('John', 'Smith', 'Internal Med.'),
    Doctor('Jone', 'Smith', 'Pediatrics'),
    Doctor('Jone', 'Carlos', 'Cardiology')
]

# Tkinter App
class HospitalManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("500x550")

        self.login_screen()

    def login_screen(self):
        """Admin login screen"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Hospital Management System", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.check_login).pack(pady=10)

    def check_login(self):
        """Verify login credentials"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == admin._Admin__username and password == admin._Admin__password:
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def main_menu(self):
        """Main dashboard"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Main Menu", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.root, text="Doctor Management", command=self.doctor_management).pack(pady=5)
        tk.Button(self.root, text="Patient Management", command=self.patient_management).pack(pady=5)
        tk.Button(self.root, text="Admin Interface", command=self.admin_interface).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.login_screen).pack(pady=20)

    def doctor_management(self):
        """Doctor Management Panel"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Doctor Management", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.root, text="Register Doctor", command=self.register_doctor).pack(pady=5)
        tk.Button(self.root, text="View Doctors", command=self.view_doctors).pack(pady=5)
        tk.Button(self.root, text="Update Doctors", command=self.update_doctor).pack(pady=5)
        tk.Button(self.root, text="Delete Doctors", command=self.delete_doctor).pack(pady=5)
        tk.Button(self.root, text="Assign Doctor to Patient", command=self.assign_doctor).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=20)

    def register_doctor(self):
        """Register a new doctor"""
        def save_doctor():
            first = first_name_entry.get()
            last = surname_entry.get()
            spec = specialty_entry.get()
            if first and last and spec:
                doctors.append(Doctor(first, last, spec))
                messagebox.showinfo("Success", "Doctor registered successfully!")
                self.doctor_management()
            else:
                messagebox.showerror("Error", "All fields are required!")

        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Register Doctor", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="First Name").pack()
        first_name_entry = tk.Entry(self.root)
        first_name_entry.pack()

        tk.Label(self.root, text="Surname").pack()
        surname_entry = tk.Entry(self.root)
        surname_entry.pack()

        tk.Label(self.root, text="Specialty").pack()
        specialty_entry = tk.Entry(self.root)
        specialty_entry.pack()

        tk.Button(self.root, text="Register", command=save_doctor).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.doctor_management).pack(pady=10)

    def view_doctors(self):
        """Display list of doctors"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Doctor List", font=("Arial", 14)).pack(pady=10)
        for doc in doctors:
            tk.Label(self.root, text=f"{doc.full_name()} - {doc.get_speciality()}").pack()

        tk.Button(self.root, text="Back", command=self.doctor_management).pack(pady=10)


    def update_doctor(self):
        """Update doctor details"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Update Doctor", font=("Arial", 14)).pack(pady=10)

        # Dropdown for doctor selection
        doctor_names = [doc.full_name() for doc in doctors]
        if not doctor_names:
            messagebox.showerror("Error", "No doctors available!")
            self.doctor_management()
            return

        tk.Label(self.root, text="Select Doctor:").pack()
        self.selected_doctor_var = tk.StringVar(self.root)
        self.selected_doctor_var.set(doctor_names[0])  # Default selection
        doctor_dropdown = tk.OptionMenu(self.root, self.selected_doctor_var, *doctor_names)
        doctor_dropdown.pack()

        tk.Label(self.root, text="New First Name").pack()
        first_name_entry = tk.Entry(self.root)
        first_name_entry.pack()

        tk.Label(self.root, text="New Surname").pack()
        surname_entry = tk.Entry(self.root)
        surname_entry.pack()

        tk.Label(self.root, text="New Specialty").pack()
        specialty_entry = tk.Entry(self.root)
        specialty_entry.pack()

        def save_updated_doctor():
            selected_name = self.selected_doctor_var.get()
            for doctor in doctors:
                if doctor.full_name() == selected_name:
                    if first_name_entry.get():
                        doctor.set_first_name(first_name_entry.get())
                    if surname_entry.get():
                        doctor.set_surname(surname_entry.get())
                    if specialty_entry.get():
                        doctor.set_speciality(specialty_entry.get())

                    messagebox.showinfo("Success", "Doctor updated successfully!")
                    self.doctor_management()
                    return

        tk.Button(self.root, text="Update", command=save_updated_doctor).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.doctor_management).pack(pady=5)

    def delete_doctor(self):
        """Delete a doctor from the system"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Delete Doctor", font=("Arial", 14)).pack(pady=10)

        doctor_names = [doc.full_name() for doc in doctors]
        if not doctor_names:
            messagebox.showerror("Error", "No doctors available!")
            self.doctor_management()
            return

        tk.Label(self.root, text="Select Doctor to Delete:").pack()
        self.selected_doctor_var = tk.StringVar(self.root)
        self.selected_doctor_var.set(doctor_names[0])  # Default selection
        doctor_dropdown = tk.OptionMenu(self.root, self.selected_doctor_var, *doctor_names)
        doctor_dropdown.pack()

        def confirm_delete():
            selected_name = self.selected_doctor_var.get()
            for doctor in doctors:
                if doctor.full_name() == selected_name:
                    doctors.remove(doctor)
                    messagebox.showinfo("Success", "Doctor deleted successfully!")
                    self.doctor_management()
                    return

        tk.Button(self.root, text="Delete", command=confirm_delete).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.doctor_management).pack(pady=5)

    def assign_doctor(self):
        """Assign a doctor to a patient"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Assign Doctor to Patient", font=("Arial", 14)).pack(pady=10)

        # Load patients from file
        try:
            with open("patient.txt", "r") as f:
                patients = f.readlines()
        except FileNotFoundError:
            messagebox.showerror("Error", "No patients found!")
            self.doctor_management()
            return

        if not patients:
            messagebox.showinfo("Info", "No patients registered yet!")
            self.doctor_management()
            return

        tk.Label(self.root, text="Select Patient:").pack()
        self.patient_var = tk.StringVar(self.root)
        self.patient_var.set(patients[0].strip())  # Default selection
        patient_dropdown = tk.OptionMenu(self.root, self.patient_var, *[p.strip() for p in patients])
        patient_dropdown.pack()

        # Load doctor list
        tk.Label(self.root, text="Select Doctor:").pack()
        self.doctor_var = tk.StringVar(self.root)
        doctor_names = [doc.full_name() for doc in doctors]
        if doctor_names:
            self.doctor_var.set(doctor_names[0])  # Default selection
            doctor_dropdown = tk.OptionMenu(self.root, self.doctor_var, *doctor_names)
            doctor_dropdown.pack()
        else:
            messagebox.showerror("Error", "No doctors available!")
            self.doctor_management()
            return

        # Assign button
        tk.Button(self.root, text="Assign", command=self.assign_doctor_to_patient).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.doctor_management).pack(pady=5)

    def assign_doctor_to_patient(self):
        """Save assigned doctor to patient file and record registration date"""
        selected_patient = self.patient_var.get()
        selected_doctor = self.doctor_var.get()

        # Read patient data
        with open("patient.txt", "r") as f:
            patients = f.readlines()

        # Update patient data
        updated_patients = []
        for patient in patients:
            data = patient.strip().split(",")
            if data[0] == selected_patient.split(",")[0]:  # Matching patient name
                data[5] = selected_doctor  # Assign doctor (doctor's name is at index 5)
                registration_date = datetime.datetime.now().strftime("%Y-%m-%d") # Get current date
                data.append(registration_date) # Append registration date as the 7th field
            updated_patients.append(",".join(data) + "\n")

        # Write updated data back
        with open("patient.txt", "w") as f:
            f.writelines(updated_patients)

        messagebox.showinfo("Success", "Doctor assigned successfully and registration date recorded!") # Updated message
        self.doctor_management()

    def patient_management(self):
        """Patient Management Panel"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Patient Management", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.root, text="Register Patient", command=self.register_patient).pack(pady=5)
        tk.Button(self.root, text="View Patients", command=self.view_patients).pack(pady=5)
        tk.Button(self.root, text="View Family", command=self.group_patients_by_surname).pack(pady=5)
        tk.Button(self.root, text="Discharge Patient", command=self.discharge_patient).pack(pady=5)
        tk.Button(self.root, text="View Discharge Patient", command=self.view_discharged_patients).pack(pady=5)
        tk.Button(self.root, text="Relocate Patient", command=self.relocate_patient).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=20)

    def register_patient(self):
        """Register a new patient and store the date of registration"""
        def save_patient():
            full_name = name_entry.get()
            age = age_entry.get()
            mobile = mobile_entry.get()
            postcode = postcode_entry.get()
            symptoms = symptom_entry.get()
            reg_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Capture date

            if full_name and age and mobile and postcode and symptoms:
                with open("patient.txt", "a") as f:
                    f.write(f"{full_name},{age},{mobile},{postcode},{symptoms},not assigned,{reg_date}\n")
                messagebox.showinfo("Success", "Patient registered successfully!")
                self.patient_management()
            else:
                messagebox.showerror("Error", "All fields are required!")

        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Register Patient", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Full Name").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()

        tk.Label(self.root, text="Age").pack()
        age_entry = tk.Entry(self.root)
        age_entry.pack()

        tk.Label(self.root, text="Mobile").pack()
        mobile_entry = tk.Entry(self.root)
        mobile_entry.pack()

        tk.Label(self.root, text="Postcode").pack()
        postcode_entry = tk.Entry(self.root)
        postcode_entry.pack()

        tk.Label(self.root, text="Symptoms").pack()
        symptom_entry = tk.Entry(self.root)
        symptom_entry.pack()

        tk.Button(self.root, text="Register", command=save_patient).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.patient_management).pack(pady=5)


    def view_patients(self):
        """Display patients in a tabular format"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Patient List", font=("Arial", 14)).pack(pady=10)

        # Create Treeview Table
        columns = ("Full Name", "Age", "Mobile", "Postcode", "Symptoms", "Doctor")
        tree = ttk.Treeview(self.root, columns=columns, show="headings")

        # Define column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=100)

        # Load data from file
        try:
            with open("patient.txt", "r") as f:
                patients = f.readlines()
        except FileNotFoundError:
            messagebox.showerror("Error", "No patients found!")
            self.patient_management()
            return

        if not patients:
            messagebox.showinfo("Info", "No patients registered yet!")
            self.patient_management()
            return

        # Insert patient data into table
        for patient in patients:
            data = patient.strip().split(",")
            tree.insert("", "end", values=data)

        tree.pack(expand=True, fill="both")

        # Back Button
        tk.Button(self.root, text="Back", command=self.patient_management).pack(pady=10)


    """Group patients by surname and display in a tabular format"""
    def group_patients_by_surname(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Patients Grouped by Surname", font=("Arial", 14)).pack(pady=10)

        try:
            with open("patient.txt", "r") as f:
                patients = f.readlines()
        except FileNotFoundError:
            messagebox.showerror("Error", "No patients found!")
            self.patient_management()
            return

        surname_groups = {}
        for patient in patients:
            details = patient.strip().split(",")
            if len(details) < 6:
                continue
            full_name = details[0]
            surname = full_name.split()[-1]  # Get last name
            if surname not in surname_groups:
                surname_groups[surname] = []
            surname_groups[surname].append(details)

        # Create Treeview Table
        columns = ("Full Name", "Age", "Mobile", "Postcode", "Symptoms", "Doctor")
        tree = ttk.Treeview(self.root, columns=columns, show="headings")

        # Define column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=100)

        # Insert grouped data into table
        for surname, group in surname_groups.items():
            tree.insert("", "end", values=("", "", "", "", f"--- {surname} ---", ""))
            for details in group:
                tree.insert("", "end", values=details[:6])

        tree.pack(expand=True, fill="both")

        tk.Button(self.root, text="Back", command=self.patient_management).pack(pady=10)


    def discharge_patient(self):
        """Discharge a patient and move them to discharged.txt"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Discharge a Patient", font=("Arial", 14)).pack(pady=10)

        try:
            with open("patient.txt", "r") as f:
                patients = f.readlines()
        except FileNotFoundError:
            messagebox.showerror("Error", "No patients found!")
            self.patient_management()
            return

        if not patients:
            messagebox.showinfo("Info", "No patients registered yet!")
            self.patient_management()
            return

        tk.Label(self.root, text="Select Patient to Discharge:").pack()
        self.discharge_var = tk.StringVar(self.root)
        self.discharge_var.set(patients[0].strip())  # Default selection
        patient_dropdown = tk.OptionMenu(self.root, self.discharge_var, *[p.strip() for p in patients])
        patient_dropdown.pack()

        tk.Button(self.root, text="Discharge", command=self.confirm_discharge).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.patient_management).pack(pady=5)

    def confirm_discharge(self):
        """Move patient to discharged list"""
        selected_patient = self.discharge_var.get()

        with open("patient.txt", "r") as f:
            patients = f.readlines()

        updated_patients = []
        with open("discharged.txt", "a") as f:
            for patient in patients:
                if patient.strip() == selected_patient:
                    f.write(patient)  # Move to discharged list
                else:
                    updated_patients.append(patient)

        with open("patient.txt", "w") as f:
            f.writelines(updated_patients)  # Update active patient list

        messagebox.showinfo("Success", "Patient discharged successfully!")
        self.patient_management()

    def view_discharged_patients(self):
        """Display discharged patients in a tabular format"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Discharged Patients", font=("Arial", 14)).pack(pady=10)

        # Create Treeview Table
        columns = ("Full Name", "Age", "Mobile", "Postcode", "Symptoms", "Doctor")
        tree = ttk.Treeview(self.root, columns=columns, show="headings")

        # Define column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=100)

        # Load data from discharged.txt
        try:
            with open("discharged.txt", "r") as f:
                discharged_patients = f.readlines()
        except FileNotFoundError:
            messagebox.showerror("Error", "No discharged patients found!")
            self.patient_management()
            return

        if not discharged_patients:
            messagebox.showinfo("Info", "No discharged patients recorded yet!")
            self.patient_management()
            return

        # Insert patient data into table
        for patient in discharged_patients:
            data = patient.strip().split(",")
            tree.insert("", "end", values=data)

        tree.pack(expand=True, fill="both")

        # Back Button
        tk.Button(self.root, text="Back", command=self.patient_management).pack(pady=10)

    def relocate_patient(self):
        """Relocate a patient to a new doctor"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Relocate Patient", font=("Arial", 14)).pack(pady=10)

        try:
            with open("patient.txt", "r") as f:
                patients = f.readlines()
        except FileNotFoundError:
            messagebox.showerror("Error", "No patients found!")
            self.patient_management()
            return

        if not patients:
            messagebox.showinfo("Info", "No patients registered yet!")
            self.patient_management()
            return

        tk.Label(self.root, text="Select Patient to Relocate:").pack()
        self.relocate_patient_var = tk.StringVar(self.root)
        self.relocate_patient_var.set(patients[0].strip())  # Default selection
        patient_dropdown = tk.OptionMenu(self.root, self.relocate_patient_var, *[p.strip() for p in patients])
        patient_dropdown.pack()

        # Doctor List
        tk.Label(self.root, text="Select New Doctor:").pack()
        self.relocate_doctor_var = tk.StringVar(self.root)
        doctor_names = [doc.full_name() for doc in doctors]
        if doctor_names:
            self.relocate_doctor_var.set(doctor_names[0])  # Default selection
            doctor_dropdown = tk.OptionMenu(self.root, self.relocate_doctor_var, *doctor_names)
            doctor_dropdown.pack()
        else:
            messagebox.showerror("Error", "No doctors available!")
            self.patient_management()
            return

        tk.Button(self.root, text="Relocate", command=self.confirm_relocate_patient).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.patient_management).pack(pady=5)

    def confirm_relocate_patient(self):
        """Save the new doctor for the selected patient"""
        selected_patient = self.relocate_patient_var.get()
        selected_doctor = self.relocate_doctor_var.get()

        with open("patient.txt", "r") as f:
            patients = f.readlines()

        updated_patients = []
        for patient in patients:
            data = patient.strip().split(",")
            if data[0] == selected_patient.split(",")[0]:  # Matching patient name
                data[5] = selected_doctor  # Assign new doctor
            updated_patients.append(",".join(data) + "\n")

        with open("patient.txt", "w") as f:
            f.writelines(updated_patients)

        messagebox.showinfo("Success", "Patient relocated successfully!")
        self.patient_management()


    def admin_interface(self):
        """Admin Interface Panel"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Admin Interface", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.root, text="Update Admin Details", command=self.update_admin).pack(pady=5)
        tk.Button(self.root, text="View Management Report", command=self.view_report).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=20)

    def update_admin(self):
        """Allow the admin to update username, password, and address"""
        def save_admin_details():
            new_username = username_entry.get()
            new_password = password_entry.get()
            new_address = address_entry.get()

            if new_username:
                admin._Admin__username = new_username
            if new_password:
                admin._Admin__password = new_password
            if new_address:
                admin._Admin__address = new_address

            messagebox.showinfo("Success", "Admin details updated!")
            self.admin_interface()

        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Update Admin Details", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="New Username").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root, text="New Password").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        tk.Label(self.root, text="New Address").pack()
        address_entry = tk.Entry(self.root)
        address_entry.pack()

        tk.Button(self.root, text="Save", command=save_admin_details).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.admin_interface).pack(pady=5)

    def view_report(self):
        """Main report selection page with buttons for each report"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Management Reports", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="Total Doctors", command=self.show_total_doctors).pack(pady=5)
        tk.Button(self.root, text="Total Patients per Doctor", command=self.show_patients_per_doctor).pack(pady=5)
        tk.Button(self.root, text="Total Appointments per Month", command=self.show_appointments_per_month).pack(pady=5) # Calls chart version
        tk.Button(self.root, text="Patients Based on Illness Type", command=self.show_illness_report).pack(pady=5)

        tk.Button(self.root, text="Back", command=self.admin_interface).pack(pady=10)

    def show_total_doctors(self):
        """Display total number of doctors as a graph"""
        for widget in self.root.winfo_children():
            widget.destroy()

        total_doctors = len(doctors)

        fig, ax = plt.subplots(figsize=(10, 3))
        ax.bar(["Total Doctors"], [total_doctors], color="blue")
        ax.set_ylabel("Count")
        ax.set_title("Total Doctors in System")

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        tk.Button(self.root, text="Back", command=self.view_report).pack(pady=10)

    def show_patients_per_doctor(self):
        """Display total patients per doctor as a bar chart"""
        for widget in self.root.winfo_children():
            widget.destroy()

        try:
            with open("patient.txt", "r") as f:
                patients = f.readlines()
        except FileNotFoundError:
            patients = []

        doctor_patient_count = {}
        for patient in patients:
            details = patient.strip().split(",")
            if len(details) < 6:
                continue
            doctor_name = details[5].strip()
            doctor_patient_count[doctor_name] = doctor_patient_count.get(doctor_name, 0) + 1

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(doctor_patient_count.keys(), doctor_patient_count.values(), color="green")
        ax.set_ylabel("Number of Patients")
        ax.set_title("Total Patients per Doctor")
        ax.set_xticklabels(doctor_patient_count.keys(), rotation=45, ha="right")

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        tk.Button(self.root, text="Back", command=self.view_report).pack(pady=10)


    def show_appointments_per_month(self):
        """Display number of patient registrations per month per doctor as a bar chart in Tkinter"""
        for widget in self.root.winfo_children():
            widget.destroy()

        try:
            with open("patient.txt", "r") as f:
                patients = f.readlines()
        except FileNotFoundError:
            messagebox.showerror("Error", "No patient data file found!")
            self.view_report()
            return

        if not patients:
            messagebox.showinfo("Info", "No patient registrations found.")
            self.view_report()
            return

        # Dictionary to store appointments per doctor per month (same as before)
        doctor_monthly_appointments = collections.defaultdict(lambda: collections.defaultdict(int))

        for patient_line in patients:
            patient_data = patient_line.strip().split(",")
            if len(patient_data) < 7:
                print(f"Warning: Skipping invalid patient data line (not enough fields): {patient_line.strip()}")
                continue

            try:
                doctor_name = patient_data[5].strip()
                registration_date_str = patient_data[6].strip()
                registration_date = datetime.datetime.strptime(registration_date_str, "%Y-%m-%d").date()
                month_year = registration_date.strftime("%Y-%m")
                doctor_monthly_appointments[doctor_name][month_year] += 1
            except (ValueError, IndexError, Exception) as e:
                print(f"Warning: Skipping line due to data issues: {patient_line.strip()}. Error: {e}")

        if not doctor_monthly_appointments:
            messagebox.showinfo("Info", "No patient appointments data to display.")
            self.view_report()
            return

        # Prepare data for bar chart
        months = sorted(list(set(month for doctor_data in doctor_monthly_appointments.values() for month in doctor_data.keys()))) # Unique months in sorted order
        doctors = sorted(doctor_monthly_appointments.keys()) # Doctors in sorted order
        bar_width = 0.8 / len(doctors) # Adjust bar width for grouping, smaller if more doctors
        bar_positions = {} # Store starting position for each doctor's bars

        fig = Figure(figsize=(8, 6), dpi=100) # Adjust figure size as needed
        ax = fig.add_subplot(111)

        for index, doctor_name in enumerate(doctors):
            counts = [doctor_monthly_appointments[doctor_name].get(month, 0) for month in months] # Get counts for each month, 0 if no appointments
            positions = [i + index * bar_width for i in range(len(months))] # Positions for each doctor's bars for each month
            ax.bar(positions, counts, width=bar_width, label=doctor_name)
            bar_positions[doctor_name] = positions # Store positions for x-tick alignment

        # Set chart labels and title
        ax.set_xlabel("Month")
        ax.set_ylabel("Number of Registrations")
        ax.set_title("Patient Registrations Per Month Per Doctor")
        ax.set_xticks([pos + bar_width * (len(doctors) - 1) / 2 for pos in range(len(months))]) # Set x ticks in the middle of each month group
        ax.set_xticklabels(months, rotation=45, ha="right")
        ax.legend() # Show doctor names in legend
        fig.tight_layout() # Adjust layout to prevent labels from overlapping

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1, padx=10, pady=10)

        tk.Button(self.root, text="Back to Report Menu", command=self.view_report).pack(pady=10)


    def show_illness_report(self):
        """Display patients categorized by illness type as a pie chart"""
        for widget in self.root.winfo_children():
            widget.destroy()

        try:
            with open("patient.txt", "r") as f:
                patients = f.readlines()
        except FileNotFoundError:
            patients = []

        illness_counts = {}
        for patient in patients:
            details = patient.strip().split(",")
            if len(details) < 5:
                continue
            illness = details[4].strip()
            illness_counts[illness] = illness_counts.get(illness, 0) + 1

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.pie(illness_counts.values(), labels=illness_counts.keys(), autopct="%1.1f%%", colors=["red", "blue", "green", "orange"])
        ax.set_title("Patients Based on Illness Type")

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()
        tk.Button(self.root, text="Back", command=self.view_report).pack(pady=10)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementApp(root)
    root.mainloop()