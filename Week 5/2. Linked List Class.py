# Code for Node and List classes (except for the remove() method) originally coded by James Shuttleworth. Acquired from CU Moodle.
class Node(object):
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class List(object):
    def __init__(self):
      self.head=None
      self.tail=None

    def insert(self,n,x):
      #Not actually perfect: how do we prepend to an existing list?
      if n!=None:
          x.next=n.next
          n.next=x
          x.prev=n
          if x.next!=None:
              x.next.prev=x
      if self.head==None:
          self.head=self.tail=x
          x.prev=x.next=None
      elif self.tail==n:
          self.tail=x

    def remove(self, n):
        if n.prev != None:
            n.prev.next = n.next
        else:
            self.head = n.next
        if n.next != None:
            n.next.prev = n.prev
        else:
            self.tail = n.prev

    def display(self):
      values=[]
      n=self.head
      while n!=None:
          values.append(str(n.value))
          n=n.next
      print("List: " + ",".join(values))

if __name__ == '__main__':
    l=List()
    n4 = Node(4)
    n6 = Node(6)
    n8 = Node(8)
    l.insert(None, n4)
    l.insert(l.head,n6)
    l.insert(l.head,n8)
    l.display()
    l.remove(n6)
    l.display()