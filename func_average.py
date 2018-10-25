# simple funcion to return averages in CSV columns
# we need this to train baselines on CSV input from the EEG team

def average_column (csv):
    f = open(csv,"r")
    average = 0
    Sum = 0
    row_count = 0
    for row in f:
        for column in row.split(','):
            n=float(column)
            Sum += n
        row_count += 1
    average = Sum / len(column)
    f.close()
    return average
