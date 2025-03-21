class search:
    def __init__(self):
        pass

    def getTarget(self):
        Target = int(input("Enter target value: "))
        return Target

    def linear_search(self,lst,target):
        for i in range(len(lst)):
            if lst[i] == target:
                return f"Target found at index: {i}"

        return "Target not found"
    
    def binary_search(self,lst,target):
        lst.sort()
        low = 0
        high = len(lst)-1

        print(f"Sorted list is: {lst}")
        
        while(low<=high):
            mid = low+(high-low)//2

            if lst[mid] == target:
                return mid
            
            elif target > lst[mid]:
                low = mid+1

            elif target < lst[mid]:
                high = mid -1

        return "Target not found"


if __name__ == "__main__":
    trial1 = search()
    lst = [3, 7, 5, 9, 2, 4, 6, 1, 8]
    target = trial1.getTarget()
    #find_target = trial1.linear_search(lst,target)
    find_target = trial1.binary_search(lst,target)
    print(find_target)
