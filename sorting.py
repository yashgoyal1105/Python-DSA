class Sort:
    def __init__(self):
        pass 

    def bubble_sort(self, lst):
        """
        desc : sorts an input list using buuble sort
        parameter: self and lst->(list) 
        return : returns sorted list
        """
        for i in range(len(lst)-1):
            for j in range(i+1, len(lst)):
                if lst[i] > lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
        return lst
    
    def selection_sort(self, lst):
        """
        desc: sorting with selection sort algorithm
        parameter: self and lst->(list)
        return: sorted list
        """
        for i in range(len(lst)-1):
            min_index = i
            for j in range(i+1, len(lst)):
                if lst[j] < lst[min_index]:
                    lst[j], lst[min_index] = lst[min_index], lst[j]
        return lst

    def insertion_sort(self, lst):
        """
        desc: sorting with insertion sort algorithm
        parameter: self and lst->(list)
        return: sorted list
        """
        for i in range(1, len(lst)):
            current = lst[i]
            previous = i - 1
            while previous >= 0 and lst[previous] > current:
                lst[previous + 1] = lst[previous]
                previous -= 1
            lst[previous + 1] = current
        return lst
    
    def merge_sort(self, lst):
        if len(lst) == 0:
            """
        desc: sorting with merge sort algorithm
        parameter: self and lst->(list)
        return: None
        """
            return "List is Empty"
        if len(lst) == 1:
            return lst
        mid = len(lst) // 2
        left_lst = self.merge_sort(lst[:mid])
        right_lst = self.merge_sort(lst[mid:])
        return self.merge(left_lst, right_lst)

    def merge(self, left_lst, right_lst):
        """
        desc: helper for merge sort algorithm
        parameter: self ,left_lst->(left part of the list till middle), right_lst->(right part of the list from middle)
        return: sorted list
        """
        sorted_lst = []
        i, j = 0, 0
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] <= right_lst[j]:
                sorted_lst.append(left_lst[i])
                i += 1
            else:
                sorted_lst.append(right_lst[j])
                j += 1
        sorted_lst += left_lst[i:]
        sorted_lst += right_lst[j:]
        return sorted_lst

    def quick_sort(self, lst):
        """
        desc: sorting a list via quick sort algorithm
        parameter: self ,lst->(list)
        return: sorted list
        """
        if len(lst) <= 1:
            return lst
        pivot = lst[len(lst) // 2]  
        left = [x for x in lst if x < pivot]  
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot] 
        return self.quick_sort(left) + middle + self.quick_sort(right)
                    
if __name__ == "__main__":
    list1 = Sort()
    lst = [3, 7, 5, 9, 2, 4, 6, 1, 8]
    
    print("Choose sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    
    choice = int(input("Enter your choice (1-5): "))
    
    if choice == 1:
        sorted_lst = list1.bubble_sort(lst)
    elif choice == 2:
        sorted_lst = list1.selection_sort(lst)
    elif choice == 3:
        sorted_lst = list1.insertion_sort(lst)
    elif choice == 4:
        sorted_lst = list1.merge_sort(lst)
    elif choice == 5:
        sorted_lst = list1.quick_sort(lst)
    else:
        print("Invalid choice!")
        exit()
    
    print("Sorted list:", sorted_lst)
