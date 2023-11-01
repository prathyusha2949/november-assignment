class School:
    def __init__( self, name, location, num_students, num_teachers, facilities ) :
        self.name = name 
        self.location = location
        self.num_students = num_students
        self.num_teachers = num_teachers
        self.facilities = facilities
school1 = School("ABC School","Kamepalli", 500, 30, ["library","playground"])
school2 = School("XYZ School","Kamepalli", 700, 40, ["science lab","sports field"])
school3 = School("123 School","Kamepalli", 400, 25, ["computer lab","music room"])
school4 = School("PQR School","Kamepalli", 600, 35, ["art studio","gymnasium"])
school5 = School("EFG School","Kamepalli", 650, 29, ["cafetoria","auditorium"])
#Accessing the attributes of the objects
print(school1.name)
print(school2.num_students)
print(school3.facilities)
print(school4.location)
print(school5.num_teachers)