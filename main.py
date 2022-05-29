from tkinter import*
from tkinter import ttk
import tkinter
import tkinter
from PIL import Image,ImageTk
import os
from Student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition Arena")
        
#background image
        backimg = Image.open("college_images\download.jpg")
        backimg = backimg.resize((1920,880),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(backimg)

        label3 = Label(self.root,image=self.photoimg3)
        label3.place(x=0,y=0,width=1920,height=880)
#label
        title_lbl=Label(label3,text="",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1600,height=50)
        

#student button
        img4 = Image.open("college_images\StudentPortal.jpg")
        img4 = img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(label3,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=220)

        b2=Button(label3,text="Student's Particulars",command=self.student_details,cursor="hand2",font=("time new roman",15,"bold"),bg="black",fg="white")
        b2.place(x=100,y=300,width=220,height=40)


#Detect Face button
        img5 = Image.open("college_images\Detector.jpg")
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b3=Button(label3,image=self.photoimg5,cursor="hand2",command=self.face_recognition)
        b3.place(x=400,y=100,width=220,height=220)

        b4=Button(label3,text="Face Detection",command=self.face_recognition,cursor="hand2",font=("time new roman",15,"bold"),bg="black",fg="white")
        b4.place(x=400,y=300,width=220,height=40)

#Attendance button
        img6 = Image.open("college_images\Attend.jpg")
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b5=Button(label3,image=self.photoimg6,cursor="hand2",command=self.attendance_system)
        b5.place(x=700,y=100,width=220,height=220)

        b6=Button(label3,text="Attendance",command=self.attendance_system,cursor="hand2",font=("time new roman",15,"bold"),bg="black",fg="white")
        b6.place(x=700,y=300,width=220,height=40)


#Train button
        img8 = Image.open("college_images\TrainIcon.jpg")
        img8 = img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b9=Button(label3,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b9.place(x=100,y=400,width=220,height=220)

        b10=Button(label3,text="Train Data",cursor="hand2",command=self.train_data,font=("time new roman",15,"bold"),bg="black",fg="white")
        b10.place(x=100,y=600,width=220,height=40)

#Photos button
        img9 = Image.open("college_images\savedPhotos.jpg")
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b11=Button(label3,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b11.place(x=400,y=400,width=220,height=220)

        b12=Button(label3,text="Images",command=self.open_img,cursor="hand2",font=("time new roman",15,"bold"),bg="black",fg="white")
        b12.place(x=400,y=600,width=220,height=40)


#Exit button
        img11 = Image.open("college_images\Exit.jpg")
        img11 = img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b15=Button(label3,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b15.place(x=700,y=400,width=220,height=220)

        b16=Button(label3,text="Exit Portal",cursor="hand2",command=self.iExit,font=("time new roman",15,"bold"),bg="black",fg="white")
        b16.place(x=700,y=600,width=220,height=40)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
                self.root.destroy()
        else:
                return


#===============function buttons===============#

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def attendance_system(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_system(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_system(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()