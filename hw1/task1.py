from collections import Counter
from collections import OrderedDict


class firstTask:

    # 1.1
    def first_task_list(self):
        new_list = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
        print(max(new_list))
        print(min(new_list))

    #second option
        max_value = new_list[0]
        max(new_list)
        print(max_value)

        min_value = new_list[0]
        min(new_list)
        print(min_value)

    #1.2
    def second_task_list(self):
        new_list = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
        c = Counter(new_list)
        print(c)

    #1.3
    def third_task_list(self):
        new_list = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]

        # 1.3.1
        a = list(OrderedDict.fromkeys(new_list))
        print(a)

        #1.3.1
        b = list(dict.fromkeys(new_list))
        print(b)

        #1.3.2
        r = set(new_list)
        c = list(r)
        print(c)

        #values ​​that occur once
        print(list([k for k, v in Counter(new_list).items() if v == 1]))

