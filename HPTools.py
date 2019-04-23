import json

class Doctor:
    def __init__(self, name, dob, ssn, availability, did):
        self.name = name
        self.dob = dob
        self.ssn = ssn
        self.availability = availability
        self.did = did
# --------------------------------------------------------------------
class Patient:
    def __init__(self, name, dob, ssn, protocol, pid):
        self.name = name
        self.dob = dob
        self.ssn = ssn
        self.protocol = protocol
        self.pid = pid
# ------------------------------------------------------------------------
#Doctors dictionary
doctors = {
    '1A': dict(Name="Dr. Jose Gonzales", Date_Of_Birth="23/01/1968", SSN=9999, Availability=True),
    '1C': dict(Name="Dr. Pedro Rivera", Date_Of_Birth="24/10/1968", SSN=6666, Availability=False)
}
#Patient dictionary
patients = {
    '1B': dict(Name="Juan Del Pueblo", Date_Of_Birth="28/08/1987", SSN=6667, Protocol="broken bone")
}

beds = ['121-A', '345-B', '234', '134', 'ICU-2']
services = ['injections', 'medication', 'ER', 'blood sample']
protocols = ['gsw', 'broken bone', 'heart attack', 'head injury', 'flu']

class Health:
    # def __init__(self, doctors, patients, beds, protocols):
    #     self.doctors = doctors
    #     self.patients = patients
    #     self.beds = beds
    #     self.protocols = protocols

    def get_beds(self):
        global beds
        return beds

    def get_bedsByLevel(self, level):
        global beds
        result = []
        for x in beds:
            if x.startswith(str(level)):
                result.append(x)
        return result

    def addPatient(self, name, dob, ssn, protocol, pid):
        patients.update({pid: dict(Name=name, Date_Of_Birth=dob, SSN=ssn, Protocol=protocol)})
        return patients

    def addDoctor(self, name, dob, ssn, availability, did):
        #doctors[did] = [name, dob, ssn, availability]
        doctors.update({did: dict(Name=name, Date_Of_Birth=dob, SSN=ssn, Availability=availability)})
        return doctors

    def get_services(self):
        global services
        return services

    def get_Doctors(self):
        for key in doctors.keys():
            print(doctors[key]['Name'])
       # print("Id of doctor not found")

    def get_Patients(self):
        for key in patients.keys():
            print(patients[key]['Name'])

    def get_DoctorByID(self, did):
        if did in doctors.keys():
             print(doctors[did])

    def get_DoctorsAvailable(self):
        for key, doctor in doctors.items():
            if doctor['Availability'] == 'True':
                print(doctor['Name'])

    def updateDoctor(self, did, avail):
        #Checking if Identification is in the dict
        if did in doctors.keys():
            doctors[did]['Availability'] = avail
            print(doctors[did])
        else:
            #Id is not in dictionary
            print("Doctor identification not found!")

    def get_protocols(self):
        global protocols
        return protocols

    def add_protocol(self, protocol):
        global protocols
        protocols.append(protocol)
        return protocols
