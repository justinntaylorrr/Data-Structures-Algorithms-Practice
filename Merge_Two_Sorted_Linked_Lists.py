class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        currentList = head

        while list1 and list2:
            if list1.val < list2.val:
                currentList.next = list1
                list1 = list1.next

            else:
                currentList.next = list2
                list2 = list2.next
            currentList = currentList.next

        currentList.next = list1 or list2

        return head.next
