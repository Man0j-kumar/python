class Node:
    def __init__(self,d):
        self.data=d
        self.nxt=None
class SLL:
    def __init__(self):
        self.head=None
    def insert_beg(self,d):
        temp=Node(d)
        temp.nxt=self.head
        self.head=temp
        self.printval()
        print("\n")
    def insert_mid(self,d,position):
        newnode=Node(d)
        temp=self.head
        pos=0
        while((pos+1)<position):
            temp=temp.nxt
            if(temp==None):
                print("Invalid position")
                return
            pos=pos+1
        newnode.nxt=temp.nxt
        temp.nxt=newnode
        self.printval()
        print("\n")
    def insert_end(self,d):
        newnode=Node(d)
        temp=self.head
        while(temp.nxt!=None):
            temp=temp.nxt
        temp.nxt=newnode
        self.printval()
        print("\n")
    def delete_beg(self):
        temp=self.head
        self.head=self.head.nxt
        temp.nxt=None
        self.printval()
        print("\n")
    def delete_mid(self,position):
        pos=0
        temp=self.head
        while((pos+1)<position):
            temp=temp.nxt
            if(temp==None):
                print("Invalid position")
                return
            pos=pos+1
        temp1=temp.nxt
        temp.nxt=temp1.nxt
        self.printval()
    def delete_end(self):
        temp=self.head
        while(temp.nxt.nxt!=None):
            temp=temp.nxt
        temp.nxt=None
        self.printval()
    def printval(self):
        temp=self.head
        while(temp.nxt!=None):
            print(temp.data,"==>",end="")
            temp=temp.nxt
        print(temp.data)
ll=SLL()
ch=0
while ch!=8:
    print("1.Insert a node at begining \n2.Insert at the middle \n3.Insert at the end \n4.Delete the head node \n5.Delete at the middle \n6.Delete at the end \n7.Print the linked list \n8.Exit")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        data=input("Enter the data:")
        ll.insert_beg(data)
    elif(ch==2):
        data=input("Enter the data:")
        position=int(input("Enter the position:"))
        ll.insert_mid(data,position)
    elif(ch==3):
        data=input("Enter the data:")
        ll.insert_end(data)
    elif(ch==4):
        ll.delete_beg(data,position)
    elif(ch==5):
        position=int(input("Enter the position:"))
        ll.delete_mid(position)
    elif(ch==6):
        ll.delete_end()
    elif(ch==7):
        ll.printval()
