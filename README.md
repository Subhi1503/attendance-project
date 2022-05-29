# My Attendance Sheet (Facial Recognition Project)

My Attendance Sheet is an application which maintains and arranges the data, Tkinter based GUI-application. It records the details of the students in a database and with the help of face recognition feature the collection of data becomes easy and quick.
The web cam records the real time video of a student and recognises them and thus feeds their data. The desired details of the attendee is then sent to the attendance records folder.

## Tech Stacks and Algorithms Used:
1. Python
2. OpenCV
3. MySQL
4. Haarcascade Opencv (Object Detection)
5. LBPH Opencv (Face Recognition)
6. Tkinter


### The homepage of the application provides six features namely:
1. Student's Particulars - It contains the basic and academic details of the student through MySQL as a database.
2. Face Detection - An option which Captures the face of a person through webcam and recognizes it. Helps to maintain the attendance.
3. Images - Storage where the photos of the students are present whose data has already been saved in the system.
4. Train Data - This option helps to train the images stored in Photos folder so that it can be recognized.
5. Attendance - This option maintains precise attendance records of the students in the form of csv files. These CSV files can also be exported in the Excel Sheet if needed .
6. Exit Portal - Way to exit out of the application.


To execute this repository, kindly follow these steps:
1. Clone this repository to your local system.
2. Install all the required packages if not present.
3. Run the command- python main.py
