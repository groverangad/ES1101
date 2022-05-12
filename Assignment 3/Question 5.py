num_h=int(input("Enter number of hydrogen atoms"))

num_c=int(input("Enter number of Carbon atoms"))

num_o=int(input("Enter number of Oxygen atoms"))

Mass_C=12.0107
Mass_H=1.00794
Mass_O=15.9994

Mass_Molecule=(num_h*Mass_H)+ (num_c*Mass_C)+(num_o*Mass_O)

print(Mass_Molecule)