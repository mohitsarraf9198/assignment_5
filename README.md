# assignment_5
# My Python Practice Problems

Hey! These are my solutions to some Python exercises I've been working on. Still learning but getting the hang of it!

## Exercise 1: Student Grade Checker

So basically I had to make a program that stores student names and their marks, then lets you search for a student.

### What it needs to do:
- Make a dictionary with student names and marks
- Ask user for a student name  
- Show their marks if found
- Show "not found" message if student doesn't exist

### My Solution:
```python
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
```

I used `.get()` because it doesn't crash if the name isn't in the dictionary - it just returns `None`. Much safer than using `dictionary[key]` directly!

## Exercise 2: List Slicing Practice

This one was about working with lists - making one, taking part of it, and reversing it.

### What it needs to do:
- Create list from 1 to 10
- Get first 5 numbers 
- Reverse those 5 numbers
- Print everything

### My Solution:
```python
list = [1,2,3,4,5,6,7,8,9,10]
list_slice = list[:5]
print("Original List: ",list)
print("extracted first five element: ",list_slice)

list_slice.reverse()
print("reversed extracted elements: ",list_slice)
```

Had to be careful with the `.reverse()` method - it changes the list but doesn't return anything. That's why I had to call it on a separate line before printing.

## What I Learned

### Dictionaries:
- `.get()` is safer than direct key access
- Returns `None` if key doesn't exist instead of throwing an error
- Good for user input scenarios where you're not sure what they'll type

### Lists:
- Slicing with `[:5]` gets first 5 elements (index 0 to 4)
- `.reverse()` modifies the original list and returns `None` 
- Don't try to print the result of `.reverse()` directly!

### General stuff:
- Always handle cases where user input might not match your data
- Think about what happens when things go wrong

## Things I Could Improve

- Maybe use better variable names (apparently using `list` as a variable name isn't great?)
- Could make the student name search case-insensitive 
- Maybe use f-strings instead of `.format()` - heard they're more modern

## Notes to Self

The hardest part was remembering that some methods like `.reverse()` don't return what you expect. Took me a while to figure out why I was getting `None` printed out!

Also learned that slicing creates a new list, so when I reverse `list_slice`, it doesn't affect the original list. Pretty cool how that works.

Still getting used to Python syntax but these exercises helped a lot with understanding dictionaries and lists better.
