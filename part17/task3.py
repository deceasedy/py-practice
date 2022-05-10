"""
Напишите интерактивный учебник математики (контрольно-обучающая система). Он должен спрашивать у
пользователя в случайном порядке 5 вопросов. После опроса поставьте пользователю оценку.
"""

class Question:
    def __init__(self, text, answers, correct):
        self.text = text
        self.answers = answers
        self.correct = correct

    def show(self):
        print(f'Вопрос {questions.index(self) + 1}: "{self.text}"\nВарианты ответа:')
        for i in range(len(self.answers)):
            print(f'{i + 1}) {self.answers[i]}')

    def answer(self, attempt):
        if self.correct == attempt - 1:
            print(f'Верно! Правильный ответ: {self.answers[self.correct]}.')
            return 1
        print(f'Неправильно! Правильный ответ: {self.answers[self.correct]}.')
        return 0

questions = []
grade = 0

questions.append(Question("2 + 2", [4,5,3,2,6], 0))
questions.append(Question("2 ^ 3", [2,4,6,8,10], 3))
questions.append(Question("1 * 0", [0, 1], 0))
questions.append(Question("2 + 2 * 2", [8, 6], 1))
questions.append(Question("7 * 6", [36, 49, 42, 48], 2))

for i in questions:
    i.show()
    grade += i.answer(int(input('Ваш вариант: ')))
    print()

print(f'Ваша оценка: {grade}.')

