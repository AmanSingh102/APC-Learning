subject_marks_dict = {}

num_of_subject = int(input("Enter number of subjects ; "))

print()
for n in range(num_of_subject):
    subject = input("Enter subject : ").capitalize()
    marks = int(input(f"Enter marks for {subject} : "))
    subject_marks_dict.update({ subject : marks })

print("\n--- Subject and Marks of Student ---\n")
for i,j in subject_marks_dict.items():
    print(f"{i} : {j}")