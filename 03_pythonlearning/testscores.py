def get_test_score(answer_sheet, student_answers):
    correct_answers = 0
    
    for i in range(0, len(answer_sheet)):
        if answer_sheet[i] == student_answers[i]:
            correct_answers += 1

    return (correct_answers / len(answer_sheet)) * 100
            

