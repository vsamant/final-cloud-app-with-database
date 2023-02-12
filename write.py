# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.contrib.auth.models import User, Permission
from onlinecourse.models import *
from datetime import date


# Your code starts from here:
def write_instructors():
    # Add instructors
    # Create a user
    #user_john = User(first_name='John', last_name='Doe', dob=date(1962, 7, 16))
    user_john = User.objects.create_user(username='john',password='john')
    user_john.is_staff = True
    user_john.save()
    instructor_john = Instructor(full_time=True, total_learners=30050)
    # Update the user reference of instructor_john to be user_john
    instructor_john.user = user_john
    instructor_john.save()
    
    instructor_yan = Instructor(full_time=True, total_learners=30050)
    instructor_yan.user = User(username='yan', password='yan',is_staff=True)
    instructor_yan.user.save()
    instructor_yan.is_staff = True
    instructor_yan.user_permissions = Permission.objects.all
    instructor_yan.save()

    #instructor_joy = Instructor(username='joy', full_time=False, total_learners=10040)
    #instructor_joy.save()
    
    #instructor_peter = Instructor(username='peter', full_time=True, total_learners=2002)
    #instructor_peter.save()
    print("Instructor objects all saved... ")

def write_courses():
    # Add Courses
    course_cloud_app = Course(name="Cloud Computing Fundamentals",
                              description="Develop and deploy application on cloud")
    course_cloud_app.save()
    course_python = Course(name="Python Developement",
                           description="Learn core concepts of Python and obtain hands-on "
                                       "experience via a capstone project")
    course_python.save()

    print("Course objects all saved... ")

def write_lessons():
    # Find course
    course_cloud_app = Course.objects.get(name="Python Developement")
    # Add lessons
    lession1 = Lesson(title='Lesson 1', content="Object-relational model")
    lession1.course = course_cloud_app
    lession1.save()
    lession2 = Lesson(title='Lesson 2', content="Django full stack project")
    lession2.course = course_cloud_app
    lession2.save()
    print("Lesson objects all saved... ")

def write_questions_choices():
    # Find course
    course_cloud_app = Course.objects.get(name="Python Developement")
    print("wqc found {}".format(course_cloud_app))

    # Add questions and choices
    question1 = Question(question_text="Is integer", grade="30")
    question1.course = course_cloud_app
    question1.save()

    choice11 = Choice(question=question1, 
                choice_text="100",
                is_correct=True)
    choice11.save()

    choice12 = Choice(question=question1, 
                choice_text="0",
                is_correct=True)
    choice12.save()

    choice13 = Choice(question=question1, 
                choice_text="integer",
                is_correct=False)
    choice13.save()

    question2 = Question(question_text="Control statements", grade="40")
    question2.course = course_cloud_app
    question2.save()

    choice21 = Choice(question=question2, 
                choice_text="loop",
                is_correct=False)
    choice21.save()

    choice22 = Choice(question=question2, 
                choice_text="if",
                is_correct=True)
    choice22.save()

    choice23 = Choice(question=question2, 
                choice_text="elif",
                is_correct=True)
    choice23.save()

    question3 = Question(question_text="A or B", grade="30")
    question3.course = course_cloud_app
    question3.save()

    choice31 = Choice(question=question3, 
                choice_text="A",
                is_correct=True)
    choice31.save()

    choice32 = Choice(question=question3, 
                choice_text="Z",
                is_correct=False)
    choice32.save()
    print("Question/Choice objects all saved... ")




def write_learners():
    # Add Learners
    user_james = User.ob
    learner_james = Learner(user_james, occupation='data_scientist',
                            social_link='https://www.linkedin.com/james/')
    learner_james.save()
    learner_mary = Learner(username='mary', password='mary', occupation='dba',
                           social_link='https://www.facebook.com/mary/')
    learner_mary.save()
    learner_robert = Learner(username='robert', password='roberrt', occupation='student',
                             social_link='https://www.facebook.com/robert/')
    learner_robert.save()
    learner_david = Learner(username='david', password='david',occupation='developer',
                            social_link='https://www.linkedin.com/david/')
    learner_david.save()
    learner_john = Learner(username='jsmith', password='jsmith', occupation='developer',
                           social_link='https://www.linkedin.com/john/')
    learner_john.save()
    print("Learner objects all saved... ")

def clean_data():
    # Delete all data to start from fresh
    Enrollment.objects.all().delete()
    User.objects.all().delete()
    Learner.objects.all().delete()
    Instructor.objects.all().delete()
    Course.objects.all().delete()
    Lesson.objects.all().delete()
    Question.objects.all().delete()
    Choice.objects.all().delete()


# Clean any existing data first
clean_data()
write_courses()
#write_instructors()
write_lessons()
#write_learners()
write_questions_choices()