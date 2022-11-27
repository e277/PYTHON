# 2. Write a program to read the marks of 5 subjects through the keyboard. Find out the
#    aggregate and percentage of marks obtained by the student. Assume maximum marks
#    that can be obtained by a student in each subject as 100.
def cal_marks():
    marks = []
    no_of_marks = int(input("Enter the number of subjects: "))

    for i in range(0, no_of_marks):
        input_mark = int(input("Enter {} mark: ".format(i+1)))
        marks.append(input_mark)
    print("Array of student marks:", marks)

    print("Calculating Percentage of Marks:")
    sum = 0 
    for i in range(0, len(marks)):
        sum += marks[i]
    print("Aggregate:", sum)
    print("Percentage:", sum / no_of_marks)

if __name__ == "__main__":
    cal_marks()