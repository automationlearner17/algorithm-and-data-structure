#!/usr/bin/python3

class Node:
   data=None
   next_node=None
   
   def __init__(self,data):
     self.data=data
   
   def __repr__(self):
     return "<NodeValue: %s>" % self.data


class Linkedlist:
   def __init__(self):
     self.head=None
   
   def is_empty(self):
     return self.head == None
   
   def size(self):
     current=self.head
     count=0
     while current:
       count=count+1
       current=current.next_node
     return count

   def add(self,data):
   
      new_node = Node(data)
      new_node.next_node = self.head
      self.head = new_node
   
   def search(self,key):
      current= self.head
      while current:
       if current.data == key:
         return current
       else:
         current= current.next_node
      return None

   def insert(self,data,index):
      if index == 0:
       self.add(data)
      
      if index > 0:
        new = Node(data)
        current = self.head
        count = 0
        while index > 1:
          current = current.next_node
          index = index - 1
        
        perv_node = current
        next_node = current.next_node
        perv_node.next_node = new
        new.next_node = next_node
   def remove(self,key):
      current = self.head
      previous = None
      found = False
      
      while current and  not found:
        if current.data == key and current is self.head:
          found = True 
          self.head = current.next_node
          return current.data
        elif current.data == key:
          found = True
          previous.next_node = current.next_node
          return current.data
        else:
          previous = current
          current = current.next_node
   def delete(self,index):
       current = self.head
       previous = None
       next = None
       if index == 0:
        self.head = current.next_node
       else:
         while index > 0:
           previous = current
           current = current.next_node
           next = current.next_node
           index = index - 1
         previous.next_node = next
   
   def find_node(self,index):
     """
      it will retrun node for given index
 
     """
     if index == 0:
      return self.head
     else:
       current = self.head
       while index > 0:
         current = current.next_node
         index = index - 1
       return current
      
         
          
            
            
           
   
   def __repr__(self):
      nodes=[]
      current= self.head
      while current:
        if current is self.head:
          nodes.append("[head: %s]" % current.data)
        elif current.next_node is None:
          nodes.append("[tail: %s]" % current.data)
        else:
          nodes.append("[%s]" % current.data)
        current = current.next_node
      return '-> '.join(nodes)
         


