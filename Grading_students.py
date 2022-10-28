def gradingStudents(grades):
    # Write your code here
    
    for i in range(0,len(grades)):
        
        if grades[i] < 38:
            continue
        else:
            ls= grades[i]
            item = ls % 5
            if item == 3:
                ls = ls + 2
                grades[i] = ls
            elif item == 4:
                ls = ls + 1
                grades[i] = ls
            else:
                continue
    return grades
