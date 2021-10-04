traning_data = [
    ['Green',3,'Mango'],
['Yellow',3,'Mango'],
['Red',1,'Grape'],
['Red',1,'Grape'],
['Yellow',3,'Lemon'],
]
header = ["color","diameter","label"]
def unique_vals(rows,col):
    return set([row[col] for row in rows])
def class_counts(rows):
    counts ={ }
    for row in rows :
        label = row[-1]
        if label not in counts:
            counts[label]=0
        counts[label]+=1
    return counts
