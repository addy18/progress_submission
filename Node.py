class Node(object):
    data = -1
    next = None

    def __init__(self, data = 0, next = None): #initialize node object
        self.data = data    #assign data
        self.next = next    #initialize next as null

    def set_data(self, new_d):
        self.data = new_d

    def set_next(self, new_n):
        self.next = new_n

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

# see how big the list is
    def get_count(self):
        temp = self.head
        count = 0

        while temp is not None:
            count += 1
            temp = temp.next
        return count

# adds to end of the list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None: # if list empty, set new node as head
            self.head = new_node
            return
        last = self.head # traverse til you reach last node
        while last.next is not None:
            last = last.next

        last.next = new_node # change the next of the last node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
# PURE PSUEDO CODE
    def bubble_sort(self):
        # n is the length of the linked list
        for i in range(n):
            swapped = false
            for j in range start at 0 end at n-i-1:
                # swap if element is greater than the next
                if node > node+1:
                    temp = node
                    node = node+1
                    node+1 = temp
                    swapped = true
            #if elements weren't swapped by inner loop break it!
            if swap = false
                break

# PURE PSUEDO CODE SO IT DOES NOT WORK YET
    def merge_sort(self, h1, h2):
        # if head is null of length is equal to 1
        if head is null or length of linked list is <= 1
            return
        # divide list into half
        else length of linked list // 2
            (h1 and h2)
        # set next to h1 to null
        h1.next = None
        # apply merge sort to first half (h1)
        left_half = merge_Sort(h1)
        # apply merge sort to second half (h2)
        right_half = merge_sort(h2)
        # put the to halves back together using another method
        complete_list = sorted_list(left_half,right_half)
        return complete_list



linked_list = LinkedList() # empty list
f = open("test.txt", "r")
f1 = open("test2.txt", "r")

# combines the two text files
for nums in f.readlines():
    linked_list.append(nums)
for i in f1.readlines():
    linked_list.append(i)

linked_list.print_list()
linked_list.bubble_sort()
linked_list.merge_sort()
