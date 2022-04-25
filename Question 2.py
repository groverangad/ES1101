print("Question 2 : Tax calculation","\n")

Gross_Income=int(input("Enter the Gross income of the tax payer ="))

Num_Dependents=int(input("Enter the number of dependents of the taxpayer ="))

Standard_Deduction=10000

Dependent_Deduction=3000

Taxable_income=(Gross_Income)-Standard_Deduction-(Dependent_Deduction*Num_Dependents)

Tax = (Taxable_income *20)/100

print("The Tax to be paid is " , Tax)

