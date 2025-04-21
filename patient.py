class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptom = []
       

    def full_name(self) :
        return f"{self.__first_name} {self.__surname}"


    def get_doctor(self) :
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor.full_name()

    def add_symptoms(self, symptoms):
        self.__symptoms.extend(symptoms)

    def print_symptoms(self):
        """prints all the symptoms"""
        if self.__symptoms == []:
            print(f"{self.full_name()} has no recorded symptoms")
        else:
            print(f"{self.full_name()}'s symptoms are as follows: ")
            for symptom in self.__symptoms:
                print(f"- {symptom}")

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
