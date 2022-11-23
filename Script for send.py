import csv

# user information
Name = input("Enter your name :")
ProID = input("Enter Project ID :")

# Confirmation
ans1 = input("Does this change contains require deny rule or any removal ?")
ans2 = input("Does this change contains routing change ?")
ans3 = input("Does this change contains market change ?")

# ETE information
SCTASK = input("SCTASK number :")
RITM = input("RITM number :")
CHG = input("Change number :")
cmt = input("Comment :")

# creat an emplty dictionary
dicts = {}

# loop to assign the rows of the CSV to dictionary
with open("RITM.csv", "r") as f:
    reader = csv.reader(f)
    for i, line in enumerate(reader):
        dicts[i] = line

# get the first row of the dictionary
ip_ports = dicts[1]

source_ip = ip_ports[0]
source_SNM = ip_ports[1]
dst_ip = ip_ports[2]
dst_SNM = ip_ports[3]
ports = ip_ports[4]
prtcol = "TCP"

content = """ 
=================================================================================================
			Firwall Configuration/Script
--------------------------------------------------------------------------------------------------
*Script file Name - Use below example 
LSE - JH_ETE_9999_CHG_88888888_20201705
LCH - JH_CRQ_88888888_20201705
*Save the script in  Changes\Scripts For Changes - 2020\Change Scripts
*If you have multiple crq for one request, update the script into one file once the last crq is submitted.
*Attach approval if required
*Attach diagram if required
==================================================================================================
"""
user_information = [f"Assigned engineer{' ' * 1}: %s\n" % str(Name),
                    f"Project{' ' * 11}: %s \n" % str(ProID),
                    "\n"]
confirmation = [f"Does this change contains require deny rule or any removal ? %s\n" % str(ans1),
                f"Does this change contains routing change ? %s \n" % str(ans2),
                f"Does this change contains market change ? %s \n" % str(ans3),
                "\n"]
ETE = ["%s \n" % str(SCTASK),
       "%s \n" % str(RITM),
       "%s \n" % str(CHG),
       "%s \n" % str(cmt),
       "\n",
       "DEVICE CONFIGURATION \n"
       f"{'=' * 25}\n",
       "\n"
       ]


vdom = "London_CNF"
config = (f"{'.' * 20} %s {'.' * 20}\n" % vdom,
          f"RULE ID {' ' * 5}: \n"
          f"FROM ZONE {' ' * 3}: ANY \n"
          f"TO ZONE {' ' * 5}: ANY \n"
          f"SOURCE {' ' * 6}: %s %s \n" % (str(source_ip), str(source_SNM)),
          f"DESTINATION {' ' * 1}: %s %s \n" % (str(dst_ip), str(dst_SNM)),
          f"SERVICES {' ' * 4}: %s %s \n" % (str(ports), str(prtcol)),
          f"ACTION {' ' * 6}: PERMIT \n"
          f"{'.' * 24} END {'.' * 24}\n"
          "\n"
          )
back_config = (f"{'.' * 20} %s {'.' * 20}\n" % vdom,
               "Remove newly added policy \n"
               f"{'.' * 24} END {'.' * 24}\n")

# WRITE TO A FILE
f = open("sample.txt", "w")
f.write(content)
f.writelines(user_information)
f.writelines(confirmation)
f.writelines(ETE)
f.writelines(config)
f.writelines("BACK-OUT DEVICE CONFIGURATION \n")
f.writelines(f"{'=' * 30}\n")
f.writelines(back_config)
f.close()
