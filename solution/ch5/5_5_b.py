'''
5-5. 외계인 색 #3
연습문제 5-4의 if-else 문을 if-elif-else 문으로 바꾸세요.
- 외계인이 녹색이면 플레이어가 5점을 얻었다는 메시지를 출력하세요.
- 외계인이 노란색이면 플레이어가 10점을 얻었다는 메시지를 출력하세요.
- 외계인이 빨간색이면 플레이어가 15점을 얻었다는 메시지를 출력하세요.
- 이 프로그램을 세 가지 버전으로 만들고 외계인 색에 맞는 메시지가 출력되는지 확인하세요.

Output for 'red' alien:
You just earned 15 points!
'''

alien_color = 'red'

if alien_color == 'green':
    print('You just earned 5 points!')
elif alien_color == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')

