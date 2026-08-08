from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='maths'), StudentFacts(likes='physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")
    @Rule(StudentFacts(likes='programming'), StudentFacts(likes='maths'))
    def computer(self):
        print("Suggested Career Path: maths")
    @Rule(StudentFacts(likes='biology'), StudentFacts(likes='chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")
    @Rule(StudentFacts(likes='electrical'), StudentFacts(likes='maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")
    @Rule(StudentFacts(likes='architecture'), StudentFacts(likes='design'))
    def architecture(self):
        print("Suggested Career Path: architecture")
    @Rule(StudentFacts(likes='graphics'), StudentFacts(likes='maths'))
    def civil(self):
        print("Suggested Career Path:civil engineering")
    @Rule(StudentFacts(likes='programing'), StudentFacts(likes='AI'))
    def aids(self):
        print("Suggested Career Path: AI Engineering")
def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    print("select the subject you are interset in\n")
    print("maths\n","physics\n","biology\n","graphics\n","architecture\n","mechanics\n","design\n","electrical\n","programing\n","AI\n")
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
if __name__ == "__main__":
    main()
