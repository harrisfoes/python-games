from testscores import * 

def get_test_score(answer_sheet, student_answers):
    student_name = student_answers[0]
    actual_answers = student_answers[1:len(student_answers)]

    correct_answers = 0

    for i in range(0, len(answer_sheet)):
        if answer_sheet[i] == actual_answers[i]:
            correct_answers += 1

    return student_name, (correct_answers / len(answer_sheet)) * 100
    

