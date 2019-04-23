from testing.tests import doctors, patients, beds, services, protocols

class Health:

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
        # Checking if Identification is in the dict
        if did in doctors.keys():
            doctors[did]['Availability'] = avail
            print(doctors[did])
        else:
            # Id is not in dictionary
            print("Doctor identification not found!")

    def get_protocols(self):
        global protocols
        return protocols

    def add_protocol(self, protocol):
        global protocols
        protocols.append(protocol)
        return protocols
