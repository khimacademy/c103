'''
5-4. 외계인 색 #2
연습문제 5-3에서 했던 것처럼 외계인 색을 고르고 if-else 문을 만드세요.
- 외계인 색이 녹색이라면 플레이어가 외계인을 격추하고 5점을 얻었다는 문장을 출력하세요.
- 외계인 색이 녹색이 아니라면 플레이어가 10점을 얻었다는 문장을 출력하세요.
- 이 프로그램은 if 블록을 사용하는 버전과 else 블록을 사용하는 버전, 두 가지로 만드세요.

Output1:
You just earned 5 points!

Output2:
You just earned 10 points!
'''

alien_color = 'green'
# alien_color = 'yellow'

if alien_color == 'green':
    print('You just earned 5 points!')
else:
    print('You just earned 10 points!')

