
#Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        if head is None:
            return head
        #record = set([head.val])
        record = [head.val]
        cur, pre = head.next, head
        while cur:
            if cur.val in record:
                pre.next = cur.next
                cur = cur.next
            else:
                #record.add(cur.val)
                record.append(cur.val)
                pre = pre.next
                cur = cur.next
        return head
        # write your code here


if __name__ == '__main__':

    data = [-14,-14,-13,2,-13,-13,2,3,3]

    head = ListNode(data[0],next=None)
    temp = head
    for i in range(1,len(data)):
        temp.next = ListNode(data[i],next=None)
        temp = temp.next

    x = Solution()
    temp = x.deleteDuplicates(head)
    while temp is not None:
        print temp.val
        temp = temp.next

#this is in one-bench
