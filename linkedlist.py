class Node:
    def __init__(self,d):
        self.data=d
        self.nxt=None
class SLL:
    def __init__(self):
        self.head=None
    def insertatbeg(self,d):
        temp=Node(d)
        temp.nxt=self.head
        self.head=temp
        self.printval()
        print("\n")
    def deleteatbeg(self):
        temp=self.head
        self.head=self.head.nxt
        temp.nxt=None
        self.printval()
        print("\n")
    def printval(self):
        temp=self.head
        while(temp):
            print(temp.data,"==>",end="")
            temp=temp.nxt
ll=SLL()
ch=0
while ch!=4:
    print(" 1.Insert a node at begining \n 2.Delete the head node \n 3.Print the linked list \n 4.Exit \n")
    ch=int(input())
    if(ch==1):
        data=input("Enter the data: ")
        ll.insertatbeg(data)
    elif(ch==2):
        ll.deleteatbeg()
    elif(ch==3):
        ll.printval()
