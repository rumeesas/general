#function to calculate LDL cholesterol
def calculate_ldl(total_chol, hdl_chol):
    ldl_chol = total_chol - hdl_chol
    return ldl_chol

#function to assess cholesterol level based off of healthy averages for adults
def classify_chol(ldl_chol):
    if ldl_chol < 100:
        return "Optimal"
    elif 100 <= ldl_chol < 130:
        return "Nearly Optimal"
    elif 130 <= ldl_chol < 160:
        return "Borderline High"
    elif 160 <= ldl_chol < 190:
        return "High"
    else:
        return "Very High"

#call for user input to assess cholesterol health
total_chol = float(input("Input total cholesterol level (mg/dL): "))
hdl_chol = float(input("Input HDL cholesterol level (mg/dL): "))

#calculate user's LDL cholesterol level.
ldl_chol = calculate_ldl(total_chol, hdl_chol)
print("Your LDL cholesterol level is", ldl_chol, "mg/dL")

#classify whether this is healthy or not for an average adult
classification = classify_chol(ldl_chol)
print("This is classified as", classification,"for an average adult.")
