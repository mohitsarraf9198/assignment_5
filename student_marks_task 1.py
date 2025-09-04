student_marks = {
'Ravi':10,
'John':70,
'Manoj':40,
'Supriya':87,
'Satyam':93
}
name = input("enter Student's name: ")
marks = student_marks.get(name)
if marks is not None:
    print("{}'s marks: {}".format(name,marks))
else:
    print("Student not found!")

