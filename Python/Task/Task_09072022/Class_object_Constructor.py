import logging


class Logmessage:
    def __init__(self, filename, level, format):
        self.filename = filename
        self.level = level
        self.format = format
        logging.basicConfig(filename=self.filename, level=self.level, format=self.format)

    def log(self, message, method):
        if method == "INFO":
            logging.info(message)
        else:
            logging.error(message)


class ineuron:
    def __init__(self, student_name, course):
        self.student_name = student_name
        self.course = course
        self.logger = Logmessage("logfile.log", "INFO", "%(levelname)s:%(asctime)s:%(name)s:%(message)s")

    def registered_student(self):
        try:
            self.logger.log(f"{self.student_name} is registered in ineuron for course {self.course}", "INFO")
            return f"{self.student_name}  welcome in ineuron"
        except Exception as err:
            self.logger.log(err, "ERROR")


class Students:
    def __init__(self, fname, last, phone, email):
        self.fname = fname
        self.last = last
        self.phone = phone
        self.email = email
        self.logger = Logmessage("logfile.log", "INFO", "%(levelname)s %(asctime)s %(name)s %(message)s")

    def registration(self):
        """
        This function is for register the student in ineuron
        :return:
        """
        try:
            self.logger.log("Start Registration---------", "INFO")
            student_bool = False
            if student_bool:
                msg = "Student Already Registered"
            else:
                msg = "Student Registered Successfully"
            self.logger.log(msg, "INFO")
            return msg
        except Exception as err:
            self.logger.log(err, "ERROR")


class Courses:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.logger = Logmessage("logfile.log", "INFO", "%(levelname)s %(asctime)s %(name)s %(message)s")

    def new_Course_creation(self):
        """
        This function is for adding new course.
        :return:
        """
        try:
            self.logger.log("----------New Course Creation PProcess Start----------", "INFO")
            res = f"{self.course_name} is created."
            self.logger.log(res, "INFO")
            return res
        except Exception as err:
            self.logger.log(err, "ERROR")


class No_of_course:
    def __init__(self):
        self.course_count = 500
        self.logger = Logmessage("logfile.log", "INFO", "%(levelname)s %(asctime)s %(name)s %(message)s")

    def count_course(self):
        try:
            msg = f"Total courses in ineuron is : {self.course_count}"
            self.logger.log(msg, "INFO")
            return msg
        except Exception as err:
            self.logger.log(err, "ERROR")


class Blog:
    def __init__(self):
        self.logger = Logmessage("logfile.log", "INFO", "%(levelname)s:%(asctime)s:%(name)s:%(message)")

    def create_blog(self):
        """
        This method is for creating blog data
        :return:
        """
        try:
            self.logger.log("--------Start Blog Process----------", "INFO")
            msg = "Blog Created Successfully"
            self.logger.log(f"------{msg}---------", "INFO")
            return msg
        except Exception as err:
            self.logger.log(err, "ERROR")


class Affiliate:
    def __init__(self):
        self.logger = Logmessage("logfile.log", "INFO", "%(levelname)s:%(asctime)s:%(name)s:%(message)")

    def verify_afflication(self, name):
        try:
            self.logger.log("-------------Verification Affiliate Start-------", "INFO")
            if len(name) != 0:
                msg = "Affiliated"
            else:
                msg = "Not Affiliated"
            self.logger.log(f"-------------Verified Successfully-------: {msg}", "INFO")
            return msg
        except Exception as err:
            self.logger.log(err, "ERROR")


class Jobs:
    def __init__(self):
        self.logger = Logmessage("logfile.log", "INFO", "%(levelname)s:%(asctime)s:%(name)s:%(message)")

    def search_job(self, job_type):
        try:
            self.logger.log("-------------Search Job Process Start-------", "INFO")
            if job_type.lower() == "full time":
                job_list = ["Data Engineer", "Big Data", "ML"]
                msg = " ".join(job_list)
                self.logger.log(f"-------------{msg}: Permanent Position are available-------", "INFO")
            else:
                job_list = ["HR", "IT", "Pantry"]
            return job_list
        except Exception as err:
            self.logger.log(err, "ERROR")


class Internship:
    def __init__(self):
        self.logger = Logmessage("logfile.log", "INFO", "%(levelname)s:%(asctime)s:%(name)s:%(message)")

    def internship_availability_check(self, flag=False):
        try:
            if flag:
                self.logger.log("-------------Search Internships Process Start-------", "INFO")
                internship_availability_list = ["Data Engineer", "Big Data", "ML"]
                msg = " ".join(internship_availability_list)
                self.logger.log(f"-------------{msg} Internships Position are available-------", "INFO")
                return internship_availability_list
            else:
                self.logger.log(f"-------------Internships Position are not available-------", "INFO")
        except Exception as err:
            self.logger.log(err, "ERROR")


class ContactUs:
    def __init__(self):
        self.logger = Logmessage("logfile.log", "INFO", "%(levelname)s:%(asctime)s:%(name)s:%(message)")

    def contact_detail(self):
        try:
            msg = "For contact us send mail on this mail id support@ineuron.ai, Will get back to you in 48hrs."
            self.logger.log(msg, "INFO")
            return msg
        except Exception as err:
            self.logger.log(err, "ERROR")


# Object Creation of different classes
i = ineuron("Alex", "FSDS")
print(i.registered_student())

stud = Students("Rahul", "Gupta", "99909090", "abc@gmail.com")
print(stud.registration())

c = Courses(course_id='123', course_name="FSDS")
print(c.new_Course_creation())

no = No_of_course()
print(no.count_course())

bl = Blog()
print(bl.create_blog())

aff = Affiliate()
print(aff.verify_afflication("GOVT"))

j = Jobs()
print(j.search_job("FULL TIME"))

inter = Internship()
print(inter.internship_availability_check(True))

cont = ContactUs()
print(cont.contact_detail())