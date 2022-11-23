class Course:
    def __init__(self, code, cname, clevel):
        self.course_code=code
        self.course_name=cname
        self.course_level=clevel
        self.student_list=[]
    def get_course_info(self):
        return(f"course code: {self.course_code}, course name: {self.course_name}, course level: {self.course_level}")
    def add_student(self, student):
        self.student_list.append(student)
    def remove_student(self, student):
        self.student_list.remove(student)
    def get_list(self,course):
        return course.student_list
    def get_by_email (self, course, email):
        for stu in course.student_list:
            if(stu.student_email==email):
                return stu
