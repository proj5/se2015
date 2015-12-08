from rest_framework.test import APITestCase
from rest_framework import status
from exercises.models import Exercise, Skill, Grade


class GradeTest(APITestCase):
    fixtures = [
        'auth', 'users', 'grades', 'skills'
    ]

    def test_get_list_grade(self):
        url = '/api/v1/grades/'
        response = self.client.get(url)

        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check number of grades
        self.assertEqual(
            len(response.data),
            len(Grade.objects.all())
        )


class SkillTest(APITestCase):
    fixtures = [
        'auth', 'users', 'grades', 'skills'
    ]

    def test_create_skill(self):
        grade = Grade.objects.get(pk=1)
        skill = Skill(name='Test', id_in_grade=10, grade=grade)

        grade_num_skills = grade.num_skills
        skill.save()
        # The number of skills should increase
        self.assertEqual(grade.num_skills, grade_num_skills + 1)

    def test_get_list_skill(self):
        grade_id = 1
        url = '/api/v1/exercise/' + str(grade_id) + '/'
        response = self.client.get(url)

        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check number of skills
        self.assertEqual(
            len(response.data),
            len(Skill.objects.filter(grade__id=grade_id))
        )


class ExerciseTest(APITestCase):
    fixtures = [
        'auth', 'users', 'grades', 'skills', 'exercises', 'possible_answer',
    ]

    def test_create_exercise(self):
        skill = Skill.objects.get(id=1)
        grade = skill.grade

        skill_num_exercise = skill.num_exercises
        grade_num_exercise = grade.num_exercises

        exercise = Exercise(
            question='1+1=',
            question_type='AN',
            answer='2',
            skill=skill
        )
        exercise.save()

        # The number of exercise should increase
        self.assertEqual(skill.num_exercises, skill_num_exercise + 1)
        self.assertEqual(grade.num_exercises, grade_num_exercise + 1)

    def test_update_exercise(self):
        exercise = Exercise.objects.get(id=1)
        skill = exercise.skill
        grade = skill.grade
        exercise.answer = '2'

        skill_num_exercise = skill.num_exercises
        grade_num_exercise = grade.num_exercises
        exercise.save()

        # The number of exercise should not change
        self.assertEqual(skill.num_exercises, skill_num_exercise)
        self.assertEqual(grade.num_exercises, grade_num_exercise)

    def test_get_exercise(self):
        url = '/api/v1/exercise/1/1/'
        response = self.client.get(url)

        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_answer_without_login(self):
        url = '/api/v1/exercise/1/1/'
        response = self.client.post(url, {"id": 1, "answer": "2"})

        # Check status code
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_correct_answer_id_1(self):
        url = '/api/v1/auth/login/'
        # Success login
        data = {'username': 'user', 'password': 'user'}
        response = self.client.post(url, data, format='json')

        url = '/api/v1/exercise/1/1/'
        response = self.client.post(url, {"id": 1, "answer": "2"})
        self.assertEqual(response.data, True)

    def test_post_wrong_answer_id_6(self):
        url = '/api/v1/auth/login/'
        # Success login
        data = {'username': 'user', 'password': 'user'}
        response = self.client.post(url, data, format='json')

        url = '/api/v1/exercise/3/2/'
        response = self.client.post(url, {
            "id": 6, "answer": {"3"}
        })

        self.assertEqual(response.data, False)

    def test_post_answer_multiple_choice_correct(self):
        url = '/api/v1/auth/login/'
        # Success login
        data = {'username': 'user', 'password': 'user'}
        response = self.client.post(url, data, format='json')

        url = '/api/v1/exercise/3/3/'
        response = self.client.post(url, {
            "id": 16,
            "answer": "3 x 4|20 - 8"
        })
        self.assertEqual(response.data, True)

    def test_post_answer_multiple_choice_too_many_answers(self):
        url = '/api/v1/auth/login/'
        # Success login
        data = {'username': 'user', 'password': 'user'}
        response = self.client.post(url, data, format='json')

        url = '/api/v1/exercise/3/3/'
        response = self.client.post(url, {
            "id": 16,
            "answer": "3 x 4|20 - 8|4 : 3"
        })
        self.assertEqual(response.data, False)


class ExamTest(APITestCase):
    fixtures = [
        'auth', 'users', 'grades', 'skills', 'exercises', 'possible_answer',
        'exams'
    ]

    def test_post_exam_correct(self):
        url = '/api/v1/auth/login/'
        # Success login
        data = {'username': 'user', 'password': 'user'}
        response = self.client.post(url, data, format='json')

        url = '/api/v1/exam/3/'
        response = self.client.post(url, {
            "id": 3,
            "exercises": "16|3 x 4|20 - 8",
            "done_time": 80
        })
        self.assertEqual(response.data, 1)

        url = '/api/v1/exam/2/'
        response = self.client.post(url, {
            "id": 2,
            "exercises": "4|6&7|7&9|2&14|10",
            "done_time": 250
        })
        self.assertEqual(response.data, 4)

    def test_post_exam_wrong_too_many_answers(self):
        url = '/api/v1/auth/login/'
        # Success login
        data = {'username': 'user', 'password': 'user'}
        response = self.client.post(url, data, format='json')

        url = '/api/v1/exam/3/'
        response = self.client.post(url, {
            "id": 3,
            "exercises": "16|3 x 4|20 - 8|2 + 4",
            "done_time": 80
        })
        self.assertEqual(response.data, 0)
