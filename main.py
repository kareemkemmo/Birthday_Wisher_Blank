import pandas, random, smtplib
import datetime as dt
today = dt.datetime.now()
#TODO - put your send gmail here
my_email = "@gmail.com"
#TODO - create an app password (search google for tutorial) and put it here
my_password = ""
#TODO - edit birthdays.csv to have custom information (add as many rows as you want)
#TODO - run on the cloud

# ----------------------- Send Email Function ----------- #
def SendEmail(Person):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=Person["email"], msg=f"Subject:To {Person['name']}\n\n{MakeLetter(Person['name'])}")

# --------------------- Letter Maker Function ----------- #
def MakeLetter(name):
    letter_num = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_num}.txt") as f:
        letter = f.read()
        letter = letter.replace("[NAME]", f"{name}")
    return letter

# ----------------------- Load data --------------------- #
data = pandas.read_csv("birthdays.csv")
for (key, row) in data.iterrows():
    #check date
    if today.month == row["month"] and today.day == row["day"]:
        SendEmail(row)




