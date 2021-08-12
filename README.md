My Web Project - Homework Diary

This is my web project from SoftUni Python Web Framework course

The application is designed to facilitate  student's homework  submission and their assessment by teachers 

Server running at http://127.0.0.1:8001/


The is using django built-in User model for authentication

Each user has one of the following profiles:
    -Student profile, with First and Last Name and school class, is_staff=False
    -Teacher profile with First and Last Name and Subject they teach, is_staff=True

Students could add homework, see details,  edit, and comments only for their homeworks.
They could not delete homeworks and could not enter "Score" and change "Status" of the homework

Teachers could, Check homeworks(Edit), Delete, Add Comments only for homeworks where they are assigned by the student.  

Instruction for Students:
Register as Student
Complete your profile
Remeber you username and password for the next login

Add your homework
You could see a list of all homeworks in the system but you could see dtails and edit only your homeworks

Instruction for Teachers:

Register as teacher 
Comlete your profile
Remeber you username and password for the next login

How to check homework - download the attached homework to check it, enter a score  (2-6) and change the status to 'Checked' or 'Canceled'
If you make changes on the attached file, you could  attach your file and it will be visible by the student
 
