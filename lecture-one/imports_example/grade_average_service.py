def calculate_homework(assignment_args):
    sum_of_grades = 0
    for homework in assignment_args.values():
        sum_of_grades += homework
    final_grade = round(sum_of_grades/len(assignment_args),2)
    print(final_grade)