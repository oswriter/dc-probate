# dc-probate -- District of Columbia Probate Court Costs Calculator
# v. 2.1 (2016-11-19)
#
# Based on D.C. Superior Court Rules SCR-PD 425.
# For more information on D.C. probate see: 
# <http://www.dccourts.gov/internet/superior/org_probate/main.jsf>.
#
# (C) 2016 S.M. Oliva <oswriter@skipoliva.com>.
# Distributed under a BSD 3-Clause License.

import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

message = "Welcome to the D.C. Probate Court Costs Calculator"
message +="\nby S.M. Oliva <oswriter@skipoliva.com>."
message +="\nThis program is published under a BSD 3-Clause License."
message +="\n\nPlease enter dollar amounts without any currency symbols ($) or commas (,)."
print(message)

# Check to see if the estate has any real property.
# Estates carrying real property are subject to a $25 assessment.
# If real property is sold, sales proceeds are added to the estate.

real_estate = input("\nIs the estate carrying any real property in D.C.? (yes/no) ")
if real_estate == "yes":
	real_estate_sold = input("\nHas the personal representative sold the real property? (yes/no) ")
	if real_estate_sold == "yes":
		print("Please include the proceeds of the sale in the total value below.")
		assessment = 0 
	else:
		message = "A $25.00 assessment will be added to the total court costs."
		message += "\nDo not include the value of the real estate in the total value below."
		print(message)
		assessment = 25
else:
	assessment = 0
	
while True:
    personal_assets = input("\nWhat is the total value of all personal assets in the decedent's estate? ")

    try:
        personal_assets = int(personal_assets)
    except ValueError:
        print("Please enter a dollar amount without any currency symbols ($) or commas (,).")
    else:
        break

# Calculation of Court Costs pursuant to SCR-PD 425.

if personal_assets < 0:
    costs = 0
elif personal_assets < 500:
    costs = 0 + assessment
elif personal_assets < 2500:
    costs = 15 + assessment
elif personal_assets < 15000:
    costs = 50 + assessment
elif personal_assets < 25000:
    costs = 100 + assessment
elif personal_assets < 50000:
    costs = 150 + assessment
elif personal_assets < 75000:
    costs = 250 + assessment
elif personal_assets < 100000:
    costs = 350 + assessment
elif personal_assets < 500000:
    costs = 575 + assessment
elif personal_assets < 750000:
    costs = 825 + assessment
elif personal_assets < 1000000:
    costs = 1275 + assessment
elif personal_assets < 2500000:
    costs = 1800 + assessment
elif personal_assets < 5000000:
    costs = 2300 + assessment
else:
    costs = 2300 + (0.0002 * (personal_assets - 5000000)) + assessment
    
costs = locale.currency( costs, grouping=True ) 

print("\nThe D.C. court costs for this estate is " + costs + ".")
