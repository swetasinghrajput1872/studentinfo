import mysql.connector

def insert_record():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sweta@2007",  # enter your password
            database="imr1",
            use_pure=True
        )
        cur = con.cursor()

        rollno = int(input("Enter roll no: "))
        name = input("Enter name: ")
        branch = input("Enter branch name: ")

        C = int(input("Enter C marks (0-100): "))
        Cpp = int(input("Enter C++ marks (0-100): "))
        Python = int(input("Enter Python marks (0-100): "))

        # Marks Validation
        for marks in (C, Cpp, Python):
            if marks < 0 or marks > 100:
                raise ValueError("Marks should be between 0 and 100")

        total = C + Cpp + Python
        percentage = (total / 300) * 100

        sql = """
        INSERT INTO data_1
        (rollno, name, branch, C, Cpp, Python, total, percentage)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (rollno, name, branch, C, Cpp, Python, total, percentage)

        cur.execute(sql, values)
        con.commit()

        print("Data successfully inserted!")

    except ValueError as ve:
        print("Input Error:", ve)

    except mysql.connector.Error as err:
        print("Database Error:", err)

    except Exception as e:
        print("Unexpected Error:", e)

    finally:
        try:
            cur.close()
            con.close()
            print("Database connection closed.")
        except:
            pass

insert_record()
