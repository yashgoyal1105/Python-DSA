class sort:
    def __init__(self):
        pass 

    def bubble_sort(self, lst): #n^2 
        for i in range(len(lst)-1):
            for j in range(i+1,len(lst)):
                if(lst[i] > lst[j]):
                    lst[i],lst[j] = lst[j],lst[i]
        return lst
    
    def selection_sort(self,lst): #n^2 - select the next lowest and then swap with ith ele
        for i in range(len(lst)-1):
            min_index = i
            for j in range(i+1,len(lst)):
                if lst[j]<lst[min_index]:
                    lst[j],lst[min_index] = lst[min_index],lst[j]
        return lst

    def insertion_sort(self,lst): #n^2 - sub sorting array
        for i in range(1,len(lst)):
            current = lst[i]
            previous = i-1

            while(previous>=0 and lst[previous]>current):
                lst[previous+1] = lst[previous]
                previous -= 1

            lst[previous+1] = current

        return lst
    

if __name__ == "__main__":
    arr1 = sort()
    lst = [3, 7, 5, 9, 2, 4, 6, 1, 8]
    #sorted_lst = arr1.bubble_sort(lst)
    #sorted_lst = arr1.selection_sort(lst)
    sorted_lst = arr1.insertion_sort(lst)
    print(sorted_lst)


