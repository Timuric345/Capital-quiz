import json,random
class Game():
   def __init__(self,number_of_questions):
      self.number_of_questions = number_of_questions
      with open('countries.json') as file:
           self.data = json.load(file)
   def make_questions(self):
      question_list = []
      answers = []
      for a in range(self.number_of_questions):
         new_country = random.choice(self.data)
         q = f"What is the capital of {new_country['country']}?"
         question_list.append(q)
         answers.append(new_country['capital'])
      return (question_list,answers)
      


