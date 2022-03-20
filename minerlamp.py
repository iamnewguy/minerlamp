# Light Attendance modify script

import profile
import sqlite3
import random
import datetime
from dateutil import parser
import json

#func read someone's attendance records
def read_record(db):
    id = input("Please input ID :")#aka WorkerNO
    conn = sqlite3.connect(db)
    cur  = conn.cursor()
    cmd = "select * from AttendanceTable where WorkerNO = \'"+id+"\'"
    cur.execute(cmd)
    print(cur.fetchall())
    cur.close()
    conn.close()
    comp()

#func incert a new record
def incert_record(db):
    id = input("Please input ID :")#aka WorkerNO
    ban = banci()
    if ban:
        b_time, e_time = random_time(ban)
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cmd = "insert into AttendanceTable (WorkerNO,LampChargingRackNO,Begin,End,Type) values (\'"+id+"\', 3,\'"+b_time+"\',\'"+e_time+"\',\'"+ban+"\')"
        cur.execute(cmd)
        conn.commit()
        cur.close()
        conn.close()
        comp()
    

#func delete a record
def delete_record(db):
    id = input("Please input ID :")#aka WorkerNO
    b_time = input("Please input the begin_time:")#aka Begin
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cmd = "delete from AttendanceTable where WorkerNO = \'"+id+"\' and Begin = \'"+b_time+"\'"
    cur.execute(cmd)
    conn.commit()
    cur.close()
    conn.close()
    comp()

#func banci 
def banci():
    ban = input("Please choose banci(1:morning;2:afternoon;3:evening):")
    if ban == "1":
        return "banci1"
    elif ban == "2":
        return "banci2"
    elif ban == "3":
        return "banci3"
    else:
        print("Error, quiting!")
        return False

#func date and time
def random_time(banci):
    date_in = input("Please enter the date(eg.03-15):")
    date = "2022-" + date_in
    b_date = date
    e_date = date
    if banci == "banci1":
        b_hour = " 07"
        e_hour = " 16"
        print(b_date)
    if banci == "banci2":
        b_hour = " 15"
        e_hour = " 00"
        date_tmp = parser.parse(date)
        date_tmp = date_tmp+datetime.timedelta(days=1)
        print(b_date)
        e_date = str(date_tmp.date())
    if banci == "banci3":
        b_hour = " 23"
        e_hour = " 08"
        date_tmp = parser.parse(date)
        date_tmp = date_tmp-datetime.timedelta(days=1)
        b_date = str(date_tmp.date())
        print(b_date)
    b_minute = ":"+str(random.randint(30,50))+":"
    e_minute = ":"+str(random.randint(11,30))+":"
    sec = []
    for i in range(2):
        second_tmp = random.randint(0,59)
        if second_tmp < 10:
            second = "0" + str(second_tmp)
        else:
            second = str(second_tmp)
        sec.append(second)
    b_time = b_date+b_hour+b_minute+sec[0]
    e_time = e_date+e_hour+e_minute+sec[1]
    return b_time, e_time


def comp():
    print("*"*50)
    print("\t\tMission Complete!")
    print("*"*50)


def load_json():
    with open("./profile.json") as f:
        xx = f.read()
        profile = json.loads(xx)
    return profile

if __name__=="__main__":
    profile = load_json()
    target_db = profile["db"]
    print(f"Trying to load database file at {target_db}")    
    while True:
        print("-"*50)
        print("Intro:")
        print("\tEnter 'i' to insert a new record.")
        print("\tEnter 'd' to delete a record.")
        print("\tEnter 'r' to show someone's record.")
        print("\tEnter else to quit this script.")
        print("-"*50)
        state = input("Please enter your property:")            
        if state == "i":
            incert_record(target_db)
        elif state == "d":
            delete_record(target_db)
        elif state == "r":
            read_record(target_db)
        else:
            break

