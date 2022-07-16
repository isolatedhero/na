# 함수를 정의할 때 매개변수 대신 **kwargs를 지정합니다.
# [참고] kwargs는 딕셔너리로 전달받습니다.
def printValues3(**kwargs):
    for i in kwargs.items():
        print(f'{i[0]}은(는) {i[1]}입니다.')
