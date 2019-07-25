from question import Question
class QuestionService:
    question= []
    @classmethod
    def loadQuestion(cls):
       with open("question1.txt") as file:
           qdata = file.readlines()
           for line in qdata:
                  q = line.split(",")
                  cls.question.append(Question(*q))
    @classmethod
    def begin_quiz(cls):
        cls.loadQuestion()
        print(f"total question found :{len(cls.question)}")
        num_correct =0
        num_wrong =0
        for i,question in enumerate(cls.question):
            print(f"{i+1}.{question}")
            ch = input("enter ur choice {A,B,C,D} ONLY...")
            if ch==question.canswer.strip():
                num_correct+=1
            else:
                num_wrong+=1
        cls.show_result(num_correct,num_wrong)
      
    @classmethod
    def show_result(cls,num_correct,num_wrong):
           print("*"*50)
           total_q=len(cls.question)
           print(f"total question:{total_q}")
           print(f"number of question crrct:{num_correct}")
           print(f"question is wrong:{num_wrong}")
           perc= ((num_correct)/total_q)*100
           print(f" percentage:{perc}")
           if perc>=65:
               print("congo pass u can leave")
           else:
                print("fail :u can go home ")

    