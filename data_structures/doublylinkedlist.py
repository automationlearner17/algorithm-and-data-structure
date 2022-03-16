#!/usr/bin/python3

class Node:
  data = None
  previous_node = None
  next_node = None

  def __init__(self,data):
      self.data = data

  def __repr__(self):
      return "<NodeValue: %s>" % self.data


class Doublylinkedlist:
   def __init__(self):
      self.tail = None

   def is_empty(self):
      return self.tail == None
 
   def size(self):
       current = self.tail
       count = 0
       while current:
         current = current.previous_node
         count = count + 1
 
       return count

   def add(self,value):
       node = Node(value)
       if self.tail == None:
         self.tail = node
       else:
         node.previous_node = self.tail
         self.tail.next_node = node
         self.tail = node

   def insert(self,index,data):
       size = self.size()
       node = Node(data)
       count = 1
       current = self.tail
       if size < 1 or index > size:
         self.add(data)
       else:
        spot = size - index
        if spot == 0:
          current.next_node = node
          node.previous_node = current
          self.tail = node
        elif size == 1 and index == 0:
           current.previous_node = node
           node.next_node = current
        else:
            if count == spot:
              current.previous_node.next_node = node
              node.previous_node = current.previous_node
              node.next_node = current
              current.previous_node = node     
            else:
               while spot > count:
                  current = current.previous_node
                  count = count + 1
               if current.previous_node != None:
                current.previous_node.next_node = node
                node.previous_node = current.previous_node
                current.previous_node = node
                node.next_node = current
               else:
                current.previous_node = node
                node.next_node = current

   def remove(self,key):
      current = self.tail
      find = 0
      while current and find == 0:
           if current.data == key and current == self.tail:
             self.tail = current.previous_node
             find = 1
             return current.data
           elif current.data == key and current.previous_node != None:
             previous = current.previous_node
             next = current.next_node
             previous.next_node = next
             next.previous_node = previous
             find = 1
             return current.data
           elif current.data == key and current.previous_node == None:
             current.next_node.previous_node = None
             find = 1
             return current.data
           else:
             current = current.previous_node

   def delete(self,index):
          size = self.size()
          current = self.tail
          value = size
          while  value > 1:
            current = current.previous_node
            value = value - 1

          if index == 0:
            if size == 1:
              self.tail = current.previous_node
            else:
              previous = current.previous_node
              next = current.next_node
              next.previous_node = previous
          else:
             for i in range(0,index):
                 current = current.next_node
             if current.next_node == None:
                 self.tail = current.previous_node
             else:
                 previous = current.previous_node
                 next = current.next_node
                 previous.next_node = next
                 next.previous_node = previous

   def search(self,target):
           current = self.tail
           size = self.size()
           for i in range(0,size):
              if current.data == target:
                  return True
              else:
                current = current.previous_node

           return False 

   def find_node(self,index):
          size = self.size()
          current = self.tail
          spot = size - index
          for i in range(1,spot):
             current = current.previous_node
          return current
           
 


          
               
       
          
            
       



   def __repr__(self):
        nodes = []
        current = self.tail
        while current:
         if current is self.tail:
           nodes.append("[tail: %s]" % current.data)
         elif current.previous_node == None:
           nodes.append("[Head: %s]" % current.data)
         else:
           nodes.append("[%s]" % current.data)
         current = current.previous_node
        nodes.reverse()
        return '<=>'.join(nodes)
      
       

   
    




