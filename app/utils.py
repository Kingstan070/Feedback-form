import csv

def get_question():
    '''
    Returns:
        (list) with questions in it

    '''
    rows = []
    with open('question.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    
    return rows