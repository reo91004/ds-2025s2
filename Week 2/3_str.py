msg = "game over"
hi = "hello world"
sum = "예전엔" + hi + " 이제는" + msg
print(sum)

print(msg, "의 첫 글자는 ", msg[0])
print(msg, "의 끝 글자는 ", msg[-1])

hobby = "테니스"
age = 21
score = 4.5
msg1 = "당신의 학점은 %4.1f입니다" % score
msg2 = "취미=%s, 나이=%d, 학점=%f" % (hobby, age, score)
