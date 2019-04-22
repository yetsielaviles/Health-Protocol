
# Global variables
beds = ['121-A', '345-B', '234', '134', 'ICU-2']
protocols = ['gsw', 'broken bone', 'heart attack', 'head injury', 'flu']

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

    def get_protocols(self):
        global protocols
        return protocols

    def add_protocol(self, protocol):
        global protocols
        protocols.append(protocol)
        return protocols
