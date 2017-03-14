class AutoAI:
   'Common base class for all employees'
   ai_count = 0

   def __init__(self):
      auto_ai.ai_count += 1
   
   def display_count(self):
     print "Total Employee %d" % auto_ai.ai_count

   def display_employee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary