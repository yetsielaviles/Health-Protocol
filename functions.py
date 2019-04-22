
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


beds = ['121-A', '345-B', '234', '134', 'ICU-2']
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

