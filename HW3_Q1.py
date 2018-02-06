class Patient:
    """ base class """
    def __init__(self, name):
        self.name = name

    def discharge(self):
        """ abstract method to be overridden in derived classes
        :returns the name and type of patient when called """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class EmergencyPatient(Patient):

    def __init__(self, name):
       Patient.__init__(self, name) #applying initialization back to the parent class
       self.expected_cost = 1000 #we want to store the cost and not attach it to each patient because they have the same cost

    def discharge(self):
       print(self.name,'EmergencyPatient')


class HospitalizedPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)
        self.expected_cost = 2000

    def discharge(self):
       print(self.name,'HospitalizedPatient')

class Hospital:

    def __init__(self): #open a brand new hospital
        self.patients = []
        self.cost = 0

    def admit(self, patients):
        self.patients.append(patients) #add multiple patient one at a time

    def discharge_all(self):
        for patients in self.patients:
         patients.discharge() #calls on the discharge function for the object patient
         self.cost += patients.expected_cost

    def get_total_cost(self):
        """ returns the total costs of the day """
        return self.cost


# create five patients
P1 = HospitalizedPatient('P1')
P2 = HospitalizedPatient('P2')
P3 = EmergencyPatient('P3')
P4 = EmergencyPatient('P4')
P5 = EmergencyPatient('P5')

# create the hospital object
H = Hospital()
H.admit(P1) #call the admit function for the hospital class
H.admit(P2)
H.admit(P3)
H.admit(P4)
H.admit(P5)
H.discharge_all()

# print the total cost of today
print(H.get_total_cost())
