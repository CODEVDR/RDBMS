from mymodules import *

print("\t\t\t\t\t\t Welcome to Indian Railways Ticket Booking Service")

cs = connect_server()
cs = cs[1]
cd = connect_database(cs)
while True:
    print("1.Sign Up")
    print("2.Sign In")
    print("3.Delete Account.")
    print("4.Log Out")
    n = input("Select And Enter : ")
    if n.isdigit():
        if int(n[0]) > 0 and int(n[0]) < 5:
            n = n[0]
        else:
            print("Select and Enter From 1,2,3,4")
    else:
        print("Invalid Syntax Enterd By user!")
    if n == "1":
        # Sign In
        name = input("Enter Your Name : ").lower()
        age = float(input("Enter Your Age : "))
        user_nm = input("Enter a User Name : ")
        pw = input("Enter a Password : ")
        try:
            q1 = f"""use railways_db;"""
            q2 = f"""create table if not exists user_data (name varchar(150)  NOT NULL,age float(5) NOT NULL,user_nm varchar(50) primary key NOT NULL,password varchar(50) NOT NULL);"""
            q3 = f"""insert into user_data values("{name}",{age},"{user_nm}","{pw}");"""
            execute_query(cd, q1)
            execute_query(cd, q2)
            execute_query(cd, q3)
        except:
            print(f"User Name {user_nm} Already Exists !!!")
    elif n == "2":
        # LOG IN
        user_nm = input("Enter Your User Name : ").lower()
        q1 = f"""use railways_db;"""
        q2 = f"""select * from user_data where user_nm="{user_nm}";"""
        execute_query(cd, q1)
        rd = read_query(cd, q2)
        if rd == []:
            print("Invalid Username !! ")
        else:
            pw = input("Enter Your Password : ")
            if rd[0][3] == pw:
                print(
                    f"Hii {user_nm.capitalize()} Indian Railways Welcomes You")
                if input("Do You Want To Continue [Y/N] : ").upper() == "Y":
                    print("T&C Tickets are Non-Refundable.")
                    while True:  # Inner Loop:
                        s = input(
                            "1.Ticket Booking\n2.Ticket Cancelling\n3.Checking Ticket Availability\n4.Booking History\n5.Exit\nSelect And Enter : ")
                        if s[0].isdigit():
                            if s[0] == "1":  # tested OK
                                # ticket Booking
                                print("Trains: Intercity|Rajdhani|Shatabdi|Garib Rath|Duronto")
                                tr_nm = input("Enter Tain Name : ").capitalize()
                                q2 = f""" select total_seats from train where  train_name="{tr_nm}";"""
                                rd1 = read_query(cd, q2)
                                if rd1[0][0]>=0 and rd1[0][0] <= 2000:
                                    ctr = 0
                                    fare = 0
                                    print(f"Total No Of Seats available is {rd1[0][0]}")
                                    for i in range(int(input("Enter Number Of Passengers : "))):
                                        # sql code
                                        q1 = f"""select * from train where train_name="{tr_nm}";"""
                                        v = read_query(cd, q1)
                                        # info
                                        nm = input("Enter Your Name : ").upper()
                                        train_no = v[0][1]
                                        age = int(input("Enter Your Age : "))
                                        gd = input(
                                            "Enter Gender [M/F/Rather Not To Say[RNS]]: ").upper()
                                        pc = input(
                                            "Enter Pass Concession [Y/N] : ").upper()
                                    
                                        # --------------------------------
                                        cl = int(input("1.1st class\n2.second class\n3.third class\nSelect and Enter : "))
                                        d = {1: "1stclass_fare",
                                             2: "2ndclass_fare", 3: "3rdclass_fare"}
                                        # --------------------------------
                                        # Queries
                                        q1 = "use railways_db"
                                        q2 = f"""insert into bookings values("{nm}","{tr_nm}",{train_no},{age},"{gd}",  "{pc}","{d[cl]}");"""
                                        execute_query(cd, q1)
                                        execute_query(cd, q2)
                                        q1 = f""" select {d[cl]} from train where train_no={v[0][1]};"""  # fare
                                        rd = read_query(cd, q1)
                                        if pc[0]=="Y":
                                            fare=0
                                        else:
                                            fare += rd[0][0]
                                        q2 = f""" select total_seats from train where train_no={train_no};"""
                                        rd1 = read_query(cd, q2)
                                        ctr += 1
                                    q3 = f"""update train set total_seats={rd1[0][0]}-{ctr} where train_name="{tr_nm}" && train_no={train_no};"""
                                    rq2 = execute_query(cd, q3)
                                    print(f"Ticket booked By Paying INR {fare}")
                                elif tr_nm == "Shatabdi" and (rd1[0][0]>=0 and rd1[0][0] <= 800):
                                    print(f"Total No Of Seats available is {rd1[0][0]}")
                                    for i in range(int(input("Enter Number Of Passengers : "))):
                                        # sql code
                                        q1 = f"""select * from train where train_name="{tr_nm}";"""
                                        v = read_query(cd, q1)
                                        # info
                                        nm = input("Enter Your Name : ").upper()
                                        train_no = v[0][1]
                                        age = int(input("Enter Your Age : "))
                                        gd = input(
                                            "Enter Gender [M/F/Rather Not To Say[RNS]]: ").upper()
                                        pc = input(
                                            "Enter Pass Concession [Y/N] : ").upper()
                                        # --------------------------------
                                        cl = int(input("1.1st class\n2.second class\n3.third class\nSelect and Enter : "))
                                        d = {1: "1stclass_fare",
                                             2: "2ndclass_fare", 3: "3rdclass_fare"}
                                        # --------------------------------
                                        # Queries
                                        q1 = "use railways_db"
                                        q2 = f"""insert into bookings values("{nm}","{tr_nm}",{train_no},{age},"{gd}",  "{pc}","{d[cl]}");"""
                                        execute_query(cd, q1)
                                        execute_query(cd, q2)
                                        q1 = f""" select {d[cl]} from train where train_no={v[0][1]};"""  # fare
                                        rd = read_query(cd, q1)
                                        fare += rd[0][0]
                                        q2 = f""" select total_seats from train where train_no={train_no};"""
                                        rd1 = read_query(cd, q2)
                                        ctr += 1
                                    q3 = f"""update train set total_seats={rd1[0][0]}-{ctr} where train_name="{tr_nm}" && train_no={train_no};"""
                                    rq2 = execute_query(cd, q3)
                                    print(f"Ticket booked By Paying INR {fare}")
                                else:
                                    print(f"No vaccency Try In Other Date Please...")
                                # Code To be From here
                            elif s[0] == "2":  # tested OK
                                # ticket Cancelling
                                ctr = 0
                                print("Trains: Intercity|Rajdhani|Shatabdi|Garib Rath|Duronto")
                                tr_nm = input("Enter Tain Name : ").capitalize()
                                for i in range(int(input("Enter Number Of Tickets to be Cancelled : "))):
                                    q1 = f"""select * from train where train_name="{tr_nm}";"""
                                    v = read_query(cd, q1)
                                    nm = input("Enter Your Name : ").upper()
                                    train_no = v[0][1]
                                    q2 = f""" select total_seats from train where train_no={train_no};"""
                                    rd1 = read_query(cd, q2)
                                    try:
                                        if rd1[0][0] <= 2000:
                                            age = int(input("Enter Your Age : "))
                                            q1 = f"""delete from bookings where name="{nm}" && age={age} && train_name="{tr_nm}" train_no={train_no};"""
                                            q2 = f""" select total_seats from train where train_no={train_no};"""
                                            rd1 = read_query(cd, q2)
                                            ctr += 1
                                            print(
                                                "Tickets Sucessfully Cancelled!!\n'Apka Dinn Subh Ho'")
                                        elif rd1[0][0] <= 800 and tr_nm == "Shatabdi":
                                            age = int(input("Enter Your Age : "))
                                            q1 = f"""delete from bookings where name="{nm}" && age={age} && train_name="{tr_nm}" train_no={train_no};"""
                                            q2 = f""" select total_seats from train where train_no={train_no};"""
                                            rd1 = read_query(cd, q2)
                                            ctr += 1
                                            print(
                                                "Tickets Sucessfully Cancelled!!\n'Apka Dinn Subh Ho'")
                                        else:
                                            print("Please Book Ticket First..")
                                            break
                                    except:
                                        print("Please Book Ticket First..")
                                        break
                                q3 = f"""update train set total_seats={rd1[0][0]}+{ctr} where train_name="{tr_nm}" && train_no={train_no};"""
                                rq2 = execute_query(cd, q3)
                            elif s[0] == "3":  # tested OK
                                # Check Availablity
                                print(
                                    "Trains: Intercity|Rajdhani|Shatabdi|Garib Rath|Duronto")
                                tr_nm = input(
                                    "Enter Tain Name : ").capitalize()
                                q1 = f"""select * from train where train_name="{tr_nm}";"""
                                v = read_query(cd, q1)
                                train_no = v[0][1]
                                q2 = f""" select total_seats from train where train_no={train_no};"""
                                rd1 = read_query(cd, q2)
                                if rd1[0][0] > 0 and rd1[0][0] <= 2000:
                                    print(
                                        f"\n\nAvailability of Seats in {tr_nm} Express is {rd1[0][0]}\n\n")
                                else:
                                    print(
                                        f"\n\nNo vaccancy in {tr_nm} Express.Please Try In Tatkal\n\n")
                            elif s[0] == "4":  # tested OK
                                # Booking History
                                nm = input("Enter Your Name : ").upper()
                                age = int(input("Enter Your Age : "))
                                q1 = f""" select * from bookings where name="{nm}" && age={age};"""
                                rd = read_query(cd, q1)
                                if rd != []:
                                    print(
                                        "NAME  TRAIN_NAME  TRAIN_NO  AGE  GENDER  PASS_CONC.  CLASS")
                                    for i in rd:
                                        print(i)
                                else:
                                    print(f"{nm} is Not Present In Database..")
                            elif s[0] == "5":
                                print("Exiting....")
                                break
                        else:
                            print("Enter A Valid Syntax !!")
                else:
                    pass
            else:
                print("Incorrect Password !!")
    elif n == "3":  # tested OK
        # delete Account
        user_nm = input("Enter Your User Name : ")
        try:
            q1 = f"""use railways_db"""
            q2 = f"""delete from user_data where user_nm="{user_nm}";"""
            execute_query(cd, q1)
            execute_query(cd, q2)
            print("Sucessfully Deleted !!!")
        except:
            print("An Unexpected Error Occured Please Try Again")
    elif n == "4":
        print("Sucessfully Logged Out!!!")

    s = input("Do You Want To Continue [Y/N] : ").upper()
    if s[0] == "Y":
        pass
    elif s[0] == "N":
        break
    else:
        print("Select And Enter Y/N")
