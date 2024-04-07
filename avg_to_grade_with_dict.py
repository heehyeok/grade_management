# student = [{"name":"d","student_id":"2020","english_score":70,"c_score":80,"python_score": 60}
#            ,{"name":"c","student_id":"2020","english_score":50,"c_score":80,"python_score": 60}
#            ,{"name":"e","student_id":"2020","english_score":40,"c_score":80,"python_score": 60}
#            ,{"name":"f","student_id":"2020","english_score":30,"c_score":80,"python_score": 60}
#            ,{"name":"g","student_id":"2021","english_score":100,"c_score":80,"python_score": 60}]
rank = []
student = []

def get_info(student):
    name = input("학생의 이름 :")
    id = input("학생의 학번 :")
    english_score = int(input("학생의 영어 점수 :"))
    c_score = int(input("학생의 C언어 점수 :"))
    python_score = int(input("학생의 Python 점수 :"))

    student_dict = dict()
    student_dict["name"] = name
    student_dict["student_id"] = id
    student_dict["english_score"] = english_score
    student_dict["c_score"] = c_score
    student_dict["python_score"] = python_score
    
    student.append(student_dict)

    return student

def calculate(student):
    for i in range(len(student)):
        total = student[i]["english_score"] + student[i]["c_score"] + student[i]["python_score"] 
        student[i]["total"] = total

    for i in range(len(student)):
        student[i]['avg'] = student[i]["total"] / 3

    return student

def get_grade(student):
    for i in range(len(student)):
        if (student[i]['avg'] >= 90):
            student[i]['grade'] = 'A'

        elif (student[i]['avg'] >= 80):
            student[i]['grade'] = 'B'

        elif (student[i]['avg'] >= 70):
            student[i]['grade'] = 'C'

        elif (student[i]['avg'] >= 60):
            student[i]['grade'] = 'D'

        else:
            student[i]['grade'] = 'F'
    return student

def sorted_rank(student): #평균 점수를 통해서 
    total_score = []
    for i in range(len(student)):
        total_score.append(student[i]["total"])

    rank = [sorted(total_score, reverse = True).index(i) for i in total_score]
    return rank
        

def insert_student(student):
    student_dict = dict()
    name = input("학생의 이름 :")
    id = input("학생의 학번 :")
    english_score = int(input("학생의 영어 점수 :"))
    c_score = int(input("학생의 C언어 점수 :"))
    python_score = int(input("학생의 python 점수 :"))

    student_dict['name'] = name
    student_dict["student_id"] = id
    student_dict["english_score"]= english_score
    student_dict["c_score"]= c_score
    student_dict["python_score"] = python_score

    calculate(student)
    get_grade(student)

    index = int(input("몇 번째에 학생 정보를 입력할지 입력해주세요: "))

    student.insert(index,student_dict)
    return student

def remove_student(student,student_id):
    for i in range(len(student)):
        if student[i]["student_id"] == student_id:
            del student[i]
            print(f"{student_id}학번 학생의 정보를 삭제했습니다.")
        
    return student

def search_student(student,name,id):
    found = 0
    for i in range(len(student)):
        if (student[i]['name'] == name) and (student[i]["student_id"]==id):
            found = 1
    if(found == 1):
        print(f"이름이 {name}, 학번이 {id}인 학생은 존재합니다.")

    else:
        print(f"이름이 {name}, 학번이 {id}인 학생은 존재하지 않습니다.")

def count_over_80(student,subject):
    count = 0
    for i in range(len(student)):
        if student[i][subject] >= 80:
            count += 1

    print(f"{subject}에서 80점 이상 학생수는 {count}명입니다.")

def sort_total(student):
    print("총점을 기준으로 학생들을 정렬했습니다.")
    return sorted(student ,key= lambda student: (student['total']))

def print_info(student):
    print("성적 관리 프로그램")
    print("=" * 94)
    print("학번\t이름\t영어\tc-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("=" * 94)
    for i in range(len(student)):
        print(f"{student[i]["student_id"]}\t{student[i]["name"]}\t{student[i]["english_score"]}\t{student[i]["c_score"]}\t{student[i]["python_score"]}\t{student[i]["total"]}\t{student[i]["avg"]: 4.2f}\t{student[i]["grade"]}\t{rank[i]+1}\t")


#main

program_continue = 1
while(program_continue != 0):
    print("<성적 변환기 프로그램>")
    print("1.새로운 학생 입력")
    print("2.총점/평균 계산")
    print("3.학점 계산")
    print("4.등수 계산")
    print("5.학생 정보 출력")
    print("6.새로운 학생 삽입")
    print("7.학생 정보 삭제")
    print("8.탐색함수(학번,이름 입력)")
    print("9.총점을 기준으로 정렬")
    print("10. 80점 이상 학생 수 카운트")
    print("0.프로그램 종료")

    program_continue = int(input("어떤 기능을 사용할 지 입력해주세요. "))

    if (program_continue == 1):
        student = get_info(student)
        continue

    elif (program_continue == 2):
        student =calculate(student)
        continue

    elif (program_continue == 3):
        student =get_grade(student)
        continue

    elif(program_continue == 4):
        rank = sorted_rank
        continue

    elif (program_continue == 5):
        rank = sorted_rank
        print_info(student)
        continue
    
    elif (program_continue == 6):
        insert_student(student)
        continue

    elif(program_continue == 7):
        student_id = input("삭제하고 싶은 학생의 학번을 입력해주세요 :")
        remove_student(student,student_id)
        continue

    elif(program_continue == 8):
        student_id = input("찾고 싶은 학생의 학번을 입력해주세요 :")
        name = input("찾고 싶은 학생의 이름을 입력해주세요 :")
        search_student(student,name,student_id)
        continue

    elif(program_continue == 9):
        sort_total(student)
        continue

    elif(program_continue == 10):
        subject = input("확인하고 싶은 과목명을 입력해주세요 :")
        count_over_80(student,subject)
        continue

    else:
        program_continue == 0
        print("프로그램을 종료하겠습니다.")
