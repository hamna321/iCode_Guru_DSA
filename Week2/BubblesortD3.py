class Hospital_Management_System:
    def __init__(self,info):
        info = str(input("Details for Patients or Staff info:"))
        print("Select 1 for Staff Details:") 
        print("Select 2 for Patients Details:")   
        
class Patient extends (Hospital_Management_System):
    def __init__(self,Details,Name,Patient_id,Test_name):
        self.Name = Name
        self.Test_name = Test_name
        self.Patient_id = Patient_id
        def Pateint_info(self):
         Details= int(input("Enter the number of your choice..."))
        if Details == 1:
            Name = str(input("Enter the name:"))
            Patient_id =int(input("Enter the patient id "))
            Test_name = str(input("Enter the report name your requiured of Patient"))
            print("Displaying the report of Patient")
            
            
class Staff extends (Hospital_Management_System):
    def __init__(self,Details,Name,Staff_id,Test_name):
        self.Name = Name
        self.Test_name = Test_name
        self.Staff_id = Staff_id
        Details= int(input("Enter the number of your choice..."))
        def Staff_info(self):
          if Details == 1:
            Name = str(input("Enter the name:"))
            Staff_id =int(input("Enter the patient id "))
            