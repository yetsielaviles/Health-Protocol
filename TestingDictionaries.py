# #Doctors dictionary
# #Lista Global que almacena doctores
# DictDoctors={}
# DictDoctors["doctos"] = []
# doctors = DictDoctors["doctors"]
# #Lista global que almacena pacientes
# DictPatients={}
# DictPatients["patients"] = []
# patients = DictDoctors["patients"]

doctors = \
    {
    '1A': {'Name': "Dr. Jose Gonzales",
           'Date_Of_Birth': "23/01/1968",
           'SSN': 9999,
           'Availability': 'True'},

    '1C': {
        'Name': "Dr. Pedro Rivera",
        'Date_Of_Birth': "24/10/1968",
        'SSN': 6666,
        'Availability': 'False'
    }
}

#Patient dictionary

patients = {
    '1B': dict(Name="Juan Del Pueblo", Date_Of_Birth="28/08/1987", SSN=6667, Protocol="broken bone")
}

#-------------- Searching if availability == 'true' (true is a string because of update)-----------------
# for key, doctor in doctors.items():
#     if doctor['Availability'] == 'True':
#         print(doctor['Name'])

#-------------- Searching if the key is in the dictionary -----------------------------------------------
# if '1A' in doctors.keys():
#         if doctors['1A']['Availability'] == 'True':
#             print(doctors['1A']['Name'])
# else:
#         print("boo")
#------------- Now trying update method -----------------------------------------------------------------
did = '1A'
avail = 'False'
# if id in doctors.keys():
#         if doctors[id]['Availability'] == 'True':
#             # doctors['1A'].update(doctors['1C'])
#             doctors[id]['Availability'] = availability
#             print(doctors['1A'])
# else:
#         print("boo")

#Checking if Identification is in the dict
# if did in doctors.keys():
#             doctors[did]['Availability'] = avail
#             print(doctors[did])
# else:
#             #Id is not in dictionary
#             print("Doctor identification not found!")

#Looking for info using id
id = '1A'
if id in doctors.keys():
    print(doctors[id])