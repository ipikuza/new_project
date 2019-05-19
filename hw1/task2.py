class seconTask:

    # #2.1
    def first_task_dict(self):
        a = {'a': 1, 'b': 4, 't': 67}
        b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
        intersect = []
        for key in a.keys():
            if key in b.keys():
                intersect.append(key)
        print(intersect)

    #2.2
    def second_task_dict(self):
        a = {'a': 1, 'b': 4, 't': 67}
        b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}

        intersect = []
        for key in b.keys():
            if key not in a.keys():
                intersect.append(key)
        print(intersect)
