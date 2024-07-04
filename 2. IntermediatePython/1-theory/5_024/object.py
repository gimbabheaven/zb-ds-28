# 중간고사 클래스와 기말고사 클래스를 상속관계로 만들고, 각각의 점수를 초기화
# 또한 총점 및 평균을 반환하는 기능

class MidExam:
    def __init__(self, s1, s2, s3):
        print('[MidExam] __init__()')

        self.mid_kor_exam = s1
        self.mid_eng_exam = s2
        self.mid_mat_exam = s3

    def printScores(self):
        print(f'mid_kor_score : {self.mid_kor_exam}')
        print(f'mid_eng_score : {self.mid_eng_exam}')
        print(f'mid_mat_score : {self.mid_mat_exam}')

class EndExam(MidExam):
    def __init__(self, s1, s2, s3, s4, s5, s6):
        print('[EndExam] __init__()')

        super().__init__(s1, s2, s3)

        self.end_kor_exam = s4
        self.end_eng_exam = s5
        self.end_mat_exam = s6

    def printScores(self):
        super().printScores()
        print(f'end_kor_score : {self.end_kor_exam}')
        print(f'end_eng_score : {self.end_eng_exam}')
        print(f'end_mat_score : {self.end_mat_exam}')

    def getTotalScore(self):
        total = self.mid_kor_exam + self.mid_eng_exam + self.mid_mat_exam
        total += self.end_kor_exam + self.end_eng_exam + self.end_mat_exam

        return total
    
    def getAvgScore(self):
        return self.getTotalScore() / 6
    
exam = EndExam(85, 90, 88, 75, 85, 95)
exam.printScores()
print(exam.getTotalScore())
print(exam.getAvgScore())