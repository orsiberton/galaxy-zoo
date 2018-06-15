def main():
    generate_csv([10, 20, 30], [[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 5],
                                [1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0],
                                [1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0]])


def generate_csv(galaxy_ids, y_pred):
    print(y_pred)

    for index, y in enumerate(y_pred):
        line = [str(galaxy_ids[index])]
        for class_number, i in enumerate([3, 2, 2, 2, 4, 2, 3, 7, 3, 3, 6]):
            for sub_class_number in range(i):
                if y[class_number] == sub_class_number:
                    line.append("1")
                else:
                    line.append("0")
        print(line)
    handle_classes(y_pred[0], [3, 2, 2, 2, 4, 2, 3, 7, 3, 3, 6])
   
    
def handle_classes(y_pred, number_class_by_category):
    y = [0 for i in range(sum(number_class_by_category))]
    
    y = handle_class_1(y, y_pred, number_class_by_category)
    

def handle_class_1(y, y_pred, number_class_by_category):
    y[y_pred[0]] = 1
    
    print(y)
    if y_pred[0] == 0:
        # Go to class 7
        y = handle_class_7(y, y_pred, number_class_by_category)
    elif y_pred[0] == 1:
        # Go to class 2
        y = handle_class_2(y, y_pred, number_class_by_category)
    elif y_pred[0] == 2:
        # End
        return y
    
    return y

def handle_class_2(y, y_pred, number_class_by_category):
    index = number_class_by_category[0]
    
    y[index + y_pred[1]]
    
    if y_pred[1] == 0:
        # Go to class 9
        y = handle_class_9(y, y_pred, number_class_by_category)
    elif y_pred[1] == 1:
        # Go to class 3
        y = handle_class_3(y, y_pred, number_class_by_category)
        
    return y

def handle_class_3(y, y_pred, number_class_by_category):
    return y_pred

def handle_class_4(y, y_pred, number_class_by_category):
    return y_pred

def handle_class_5(y, y_pred, number_class_by_category):
    return y_pred

def handle_class_6(y, y_pred, number_class_by_category):
    return y_pred

def handle_class_7(y, y_pred, number_class_by_category):
    return y_pred

def handle_class_8(y, y_pred, number_class_by_category):
    return y_pred

def handle_class_9(y, y_pred, number_class_by_category):
    return y_pred

def handle_class_10(y, y_pred, number_class_by_category):
    return y_pred

def handle_class_11(y, y_pred, number_class_by_category):
    return y_pred


if __name__ == '__main__':
    main()
