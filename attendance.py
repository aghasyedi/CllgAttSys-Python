import sqlite3,datetime
# import FaceRecognizer.IdentifyFaces as idfa
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
from PIL import Image, ImageTk
# subnum = simpledialog.askinteger("Enter Subject ", "1.Sub1 \n 2.Sub2 \n 3.Sub3 \n 4.Sub4 \n 5.Sub5")
# subject = ['sub1','sub2','sub3','sub4','sub5']
# connecting to the sql server
def Initialize(subnum):
    global con,cur
    subject = ['sub1','sub2','sub3','sub4','sub5']
    con = sqlite3.connect(f"D:\\Project and Report\\College Attendace System\\Files\\subs\\{subject[subnum-1]}.db")
    cur = con.cursor()

tday = datetime.datetime.now()
date1 = int(tday.day)
month1 = tday.strftime("%b").lower()


def updateAttendance(setAtt = 1):
    if setAtt == 2:
        a = simpledialog.askstring("Del Rol ", "Enter Roll to delete(sep by ',')")
        a = set(a.split(","))
    else:
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg;*.png")])
        if file_path:
            imgurl = file_path
        # Identify the image with the help of 'face_recognition' module and returns the roll numbers of student
        # a = idfa.main(imgurl)
        # print(a) #print roll number in sorted
        a = sorted(a)

    # print(date) #this help to identify the current date for ex, if today is 23rd Dec 2023, it will return only date i.e., "23"


    # updating attendance
    i = 2
    for i in a:
        i = int(i)
        cur.execute(f"update {month1} set Field{date1}=1 where roll = {i}")
        temp = f"SELECT roll from {month1} where roll = {i}"
        rett = cur.execute(temp)
        print(f"Attendace updated for ",rett.fetchone()[0])
    con.commit()
    del(i)
    # save the attendance


def deleteAttendace():
    
    delList = simpledialog.askstring("Del Rol ", "Enter Roll to delete(sep by ',')")
    delList = set(delList.split(","))
    try:
        for i in delList:
            cur.execute(f"update {month1} set Field{date1}=0 where roll = {i}")
        con.commit()
    finally:
        con.close()
    print("Attendance deleted")
    


def percentAttendance():
    subnum = simpledialog.askinteger("Enter month", "Enter month(1-12)")
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    ini_month = months[subnum-1][:3].lower()
    # ini_month = input("Enter first 3 char of month: ")[:3].lower()  # Replace with your desired initial month
    
    # Create Tkinter window
    window = tk.Tk()
    window.title("Attendance Display")

    canvas = tk.Canvas(window, width=400, height=300, scrollregion=(0, 0, 400, 1000))
    canvas.pack(expand=tk.YES, fill=tk.BOTH)

    # Create a scrollbar for the canvas
    scrollbar = tk.Scrollbar(window, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=scrollbar.set)

    #for month of ini_month it executed the percentage
    r = cur.execute(f"Select * from {ini_month}").fetchall()
    y_position = 10  # Initialize y_position
    
    
    result_label = tk.Label(canvas, text=f"Attendance for {ini_month}", anchor="w", justify="left")
    canvas.create_window(10, y_position, anchor="w", window=result_label)
    holidayPresent= simpledialog.askinteger("Enter number", "Enter holiday days:")
    y_position += 30  # Adjust the spacing between records if needed
    for i in range(len(r)):
        roll, name = r[i][0], str(r[i][1]).capitalize()
        j = sum(1 for k in range(2, len(r[i])) if r[i][k] == 1)
        percent = round((j / (date1-holidayPresent)) * 100, 2)

        result_text = f"Roll: {roll}, Name: {name}\tAttendance(%) = {percent}%"
        result_label = tk.Label(canvas, text=result_text, anchor="w", justify="left")
        canvas.create_window(10, y_position, anchor="w", window=result_label)
        y_position += 30  # Adjust the spacing between records if needed

''' #rejected due to non presence of presentation box
#percent of attendance of each month of specific result 
def percentAttendance():# Create a canvas to display the results
    
    tday = datetime.datetime.now()
    date1 = int(tday.day)
    # ini_month = str(input("Enter the starting month for it: ")).lower()[:3]
    ini_month = 'dec'
    print(ini_month)
    r = cur.execute(f"Select * from {ini_month}").fetchall()
    for i in  range(len(r)):
        print(f"Roll: {r[i][0]}, Name: {str(r[i][1]).capitalize()}", end="")
        j = 0
        l = 0
        for k in range(2, len(r[i])):
            if r[i][k] != 1:
                l = l+1
                pass
            else:
                l = l+1
                j = j+1
        percent = str(round((j/date1)*100,2)) + "%"
        print(f"\tAttendance(%) = {percent}")
'''


#add student to each months automatically
def addStudent():
    roll_st = simpledialog.askinteger("New Student", "Enter Roll:")
    name_st = "'"+simpledialog.askstring("New Student", "Enter Name:")+"'"
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    try:
        # roll_st = int(input("Enter Roll Number:"))
        # name_st = "'"+str(input("Enter Name: "))+"'"
        for month in months:
            table_name = month[:3]  # Take the first three characters as the table name
            truncate_query = f"insert into {table_name} (roll,name) values({roll_st},{name_st})" 
            cur.execute(truncate_query)
        con.commit()
    except sqlite3.IntegrityError as e:
        print(f"Unique Constraint Error Found: ",e)
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        con.close()


#del student to each months automatically
def delStudent():
    roll_st = simpledialog.askinteger("Delete Student", "Enter Roll to delete:")
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    try:
        # roll_st = int(input("Enter Roll Number:"))
        # name_st = "'"+str(input("Enter Name: "))+"'"
        for month in months:
            table_name = month[:3]  # Take the first three characters as the table name
            truncate_query = f"delete from {table_name} where roll = {roll_st}" 
            cur.execute(truncate_query)
        con.commit()
        print(f"Deleted Roll: {roll_st}")
    except sqlite3.IntegrityError as e:
        print(f"Unique Constraint Error Found: ",e)
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        con.close()



def main():
    
    root = tk.Tk()
    root.title("Attendance Management System")

    label = tk.Label(root, text="Select an option:")
    label.pack(pady=10)

    options = [
        "1. Calculate Percentage Attendance",
        "2. Update Attendance",
        "3. Add New Student",
        "4. Delete Student",
        "5. Manual Attendance",
        "6. Delete Attendance"
    ]

    for option in options:
        tk.Label(root, text=option).pack()

    tempo = simpledialog.askinteger("Select Option", "Enter a number from 1 to 6:")
    if tempo == 1:
        percentAttendance()
    elif tempo == 2:
        updateAttendance()
        
    elif tempo == 3:
        addStudent()
    elif tempo == 4:
        delStudent()
    elif tempo == 5:
        updateAttendance(setAtt=2)
    elif tempo == 6:
        deleteAttendace()
    
    print("--------------------------------------")
    print("'''''PLEASE CLOSE ALL TABS''''''")
    root.mainloop()
    print("'''''THANK YOU FOR USING COLLEGE ATTENDANCE SYSTEM''''''")
    


# try: 
#     Initialize(2)
#     main()
# except Exception as e:
#     print("Error found: ",e)