import emails, tests, random

gen_suffix = ["ex", "xr", "ax", "ox", "ie", "io", "ui", "ux", "op", "go", "on", "Og"]

# ++++++++++++++++++++++++++++++emails++++++++++++++++++++++++++++
email = random.choice(emails.mail)
premail = random.choice(gen_suffix)
email_ex = premail + email
# with open("usernames.txt") as names:
#     names.read()
#     for 
names = random.choice(tests.name)

# +++++++++++++++++++++++phone number+++++++++++++++++++++++++++++++
suffix = ["090", "091", "070", "080", "081"]
pick = random.choice(suffix)

for i in range(8):
    phone = random.randint(0, 9)

phone_number = pick + str(phone)*2

phone_number = tests.phone_number

# +++++++++++++++++++++++++NAMES+++++++++++++++++++++++++++
name_suffix = random.choice(gen_suffix)



print(email_ex)