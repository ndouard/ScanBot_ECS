class auto_ai:
   'Common base class for all employees'
   ai_count = 0

   def __init__(self):
      auto_ai.ai_count += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary