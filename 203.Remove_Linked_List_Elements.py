# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def printList(head):
    while head != None:
        print(f"{head.val} ", end = '')

        head = head.next
    
    print("")

def removeElements(head, val):
    if head == None:
        return None

    r = head

    while head != None:
        while head.next != None and head.next.val == val:
            head.next = head.next.next

        head = head.next
        
    if r.val == val:
        if r.next == None:
            return None
        else:
            return r.next

    return r

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

printList(head)

head = removeElements(head, 6)

printList(head)

#---------------------------------------------------

head = None

printList(head)

head = removeElements(head, 1)

printList(head)

#---------------------------------------------------

head = ListNode(7)
head.next = ListNode(7)
head.next.next = ListNode(7)
head.next.next.next = ListNode(7)

printList(head)

head = removeElements(head, 7)

printList(head)
