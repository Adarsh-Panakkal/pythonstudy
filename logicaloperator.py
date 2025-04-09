"""if applicant has high income AND good credit Eligible for loan"""
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")



"""if applicant has high income OR good credit Eligible for loan"""
has_high_income = True
has_good_credit = True
if has_high_income or has_good_credit:
    print("Eligible for loan")



"""If applicant has good credit AND doesn't have criminal record"""
has_high_income = True
has_criminal_record = False
if has_high_income and not has_criminal_record:
    print("Eligible for loan")
