class MyStack:
    #상태
    #상태:값을 저장하는 리스트와 사이즈, 마지막 요소 위치
    #행동
    #push, pop
    def __init__(self,size):
        self.size = size
        self.stack = [None]*size
        self.top = -1
    #stack의 마지막에 value를 추가한다.
    def push(self,value):
        self.top += 1
        self.stack[self.top] = value
    #stack의 마지막 value를 반환한다.
    def pop(self):
        self.top -= 1
        p = self.stack[self.top+1]
        self.stack[self.top + 1] = None
        return p

T = int(input())

for tc in range(1,T+1):
    string = input()

    stack = MyStack(len(string))
    for i in range(len(string)):
        if string[i] != stack.stack[stack.top]:
            stack.push(string[i])
        else:
            stack.pop()

    cnt = 0
    for a in stack.stack:
        if a != None:
            cnt += 1

    print(f'#{tc} {cnt}')
