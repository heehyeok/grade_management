# student = [{"name":"d","student_id":"2020","english_score":70,"c_score":80,"python_score": 60}
#            ,{"name":"c","student_id":"2020","english_score":50,"c_score":80,"python_score": 60}
#            ,{"name":"e","student_id":"2020","english_score":40,"c_score":80,"python_score": 60}
#            ,{"name":"f","student_id":"2020","english_score":30,"c_score":80,"python_score": 60}
#            ,{"name":"g","student_id":"2021","english_score":100,"c_score":80,"python_score": 60}]

class Student:
    def __init__(self,name,id,english_score,c_score,python_score):
        self.name = name
        self.id = id
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score
        self.total = english_score + c_score + python_score
        self.avg = (english_score + c_score + python_score) / 3

    def get_grade(self):
            if (self.avg >= 90):
                self.grade = 'A'

            elif (self.avg >= 80):
                self.grade = 'B'

            elif (self.avg >= 70):
                self.grade = 'C'

            elif (self.avg >= 60):
                self.grade = 'D'

            else:
                self.grade = 'F'

    def get_rank(self,rank):
        self.rank = rank


        
class IO_program():
    def __init__(self):
        self.student_list = []
        self.rank = []

    def get_info(self):
        name = input("학생의 이름 :")
        id = input("학생의 학번 :")
        english_score = int(input("학생의 영어 점수 :"))
        c_score = int(input("학생의 C언어 점수 :"))
        python_score = int(input("학생의 Python 점수 :"))

        student = Student(name,id,english_score,c_score,python_score)
        self.student_list.append(student)


    def sorted_rank(self): #평균 점수를 통해서 
        total_score = []
        for student in (self.student_list):
            total_score.append(student.total)

        self.rank = [sorted(total_score, reverse = True).index(i) for i in total_score]
        
        i = 0
        for student in (self.student_list):
            student.get_rank(self.rank[i])
            i += 1

        return self.rank
    
    def print_rank(self):
        i = 0
        for student in self.student_list:
            print(f"{student.name}학생의 등수는 {self.rank[i]+1}")
            i += 1
    
    def remove_student(self,student_id):
        i = 0
        found = 0
        for student in (self.student_list):
            if (student.id == student_id):
                found = 1
                del self.student_list[i]
                print(f"{student_id}학번 학생을 리스트에서 제거했습니다.")
        if (found ==0 ):
            print(f"{student_id}학번 학생은 리스트에 존재하지 않습니다.")

        
    def search_student(self,name,id):
        found = 0
        for student in (self.student_list):
            if (student.name == name) and (student.id ==id):
                found = 1
        if(found == 1):
            print(f"이름이 {name}, 학번이 {id}인 학생은 존재합니다.")

        else:
            print(f"이름이 {name}, 학번이 {id}인 학생은 존재하지 않습니다.")

    def count_over_80(self):
        count = 0
        subject = input("과목을 입력해주세요.")
        if subject == "python":
            for student in (self.student_list):
                if student.python_score >= 80:
                    count += 1
        elif subject == "c":
            for student in (self.student_list):
                if student.c_score >= 80:
                    count += 1
        elif subject == "english":
            for student in (self.student_list):
                if student.english_score >= 80:
                    count += 1
        else:
            print(f"{subject}은 존재하지 않습니다.")
        print(f"{subject}에서 80점 이상 학생수는 {count}명입니다.")

    def insert_student(self):
        self.get_info()

        index = int(input("몇 번째에 학생 정보를 입력할지 입력해주세요: "))
        student = self.student_list.pop()
        self.student_list.insert(index,student)
        

    def print_info(self):
        print("성적 관리 프로그램")
        print("=" * 94)
        print("학번\t이름\t영어\tc-언어\t파이썬\t평균\t총점\t학점\t등수")
        print("=" * 94)
        i = 0
        self.sorted_rank()
        for student in (self.student_list):
            student.get_grade()
            print(f"{student.id}\t{student.name}\t{student.english_score}\t{student.c_score}\t{student.python_score}\t{student.total}\t{student.grade}\t{student.rank + 1}")


#main

program_continue = 1
program = IO_program()

while(program_continue != 0):
    print("=" * 94)
    print("<성적 변환기 프로그램>")
    print("1.새로운 학생 입력")
    print("2.등수 계산")
    print("3.학생 정보 출력")
    print("4.새로운 학생 삽입")
    print("5.학생 정보 삭제")
    print("6.탐색함수(학번,이름 입력)")
    print("7. 80점 이상 학생 수 카운트")
    print("0.프로그램 종료")
    print("=" * 94)

    program_continue = int(input("어떤 기능을 사용할 지 입력해주세요. "))

    if (program_continue == 1):
        program.get_info()
             
    elif(program_continue == 2):
        program.sorted_rank()
        program.print_rank()
        

    elif (program_continue == 3):
        program.print_info()
        
    elif (program_continue == 4):
        program.insert_student()
        
    elif(program_continue == 5):
        student_id = input("삭제하고 싶은 학생의 학번을 입력해주세요 :")
        program.remove_student(student_id)
        
    elif(program_continue == 6):
        student_id = input("찾고 싶은 학생의 학번을 입력해주세요 :")
        name = input("찾고 싶은 학생의 이름을 입력해주세요 :")
        program.search_student(name,student_id)

    elif(program_continue == 7):
        program.count_over_80()
        
    else:
        program_continue == 0
        print("프로그램을 종료하겠습니다.")

    print("=" * 94)
    print("\n\n\n\n")
