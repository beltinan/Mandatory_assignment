class Student:
    def __init__(self, sname, sage, semail):
        self.student_name = sname
        self.student_age = sage
        self.student_email = semail
    def get_student_info(self):
        return(f"name: {self.student_name}    , age: {self.student_age}    , email: {self.student_email}")