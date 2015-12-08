# API REFERENCES
Note: The format using to send data from server to client and backwards is JSON and HTTP protocol is used

## User
---
#### * POST api/v1/accounts/ *
Create new user account

Parameters: username, email, password, confirm_password, first_name

---
#### * POST api/v1/auth/login/ *
User login

Parameters: username, password

---
#### * POST api/v1/auth/logout/ *
User logout

---
#### * GET api/v1/accounts/ *
Get all user info from server

JSON format:
```
{
  "id": 1,
  "user": {
    "email": "admin@email.com",
    "username": "admin",
    "first_name": "Admin"
  },
  "school": "Đại học Công nghệ",
  "class_in_school": null,
  "created_at": "2015-10-06T13:25:09.749000Z",
  "updated_at": "2015-12-08T08:41:37.486000Z"
  ...
}
```

---
#### * GET api/v1/auth/accounts/:username/ *
Get specific user info from server

JSON format:
```
{
  "id": 1,
  "user": {
    "email": "admin@email.com",
    "username": "admin",
    "first_name": "Admin"
  },
  "school": "Đại học Công nghệ",
  "class_in_school": null,
  "created_at": "2015-10-06T13:25:09.749000Z",
  "updated_at": "2015-12-08T08:41:37.486000Z"
}
```

---
#### * PUT api/v1/auth/accounts/:username/ *
Update user profile

Parameters: user, password, school, class_in_school

---
#### * GET api/v1/avatar/:username/ *
Get the avatar of a user

JSON format:
```
{
  "avatar": "static/img/default.jpg"
}
```

---
## Grade
#### * GET api/v1/grades/ *
Get list of grades

JSON format:
```
{
  {
    "id": 1,
    "name": "1"
  },
  {
    "id": 2,
    "name": "2"
  }
  ...
}
```

---
## Skill
---
#### * GET api/v1/exercise/:gradeId/ *
Get list skills for a specific grade

JSON format:
```
{
  {
    "name": "Phép cộng hai số có một chữ số",
    "id_in_grade": 1,
    "grade": {
      "id": 1,
      "name": "1"
    }
  },
  {
    "name": "Số lớn nhất, nhỏ nhất",
    "id_in_grade": 2,
    "grade": {
      "id": 1,
      "name": "1"
    }
  }
}
```

---
## Exercise
---
#### * GET api/v1/exercise/:gradeId/:skillId/ *
Get an exercise in a specific grade and skill

JSON format:
```
{
  "id": 95,
  "question": "Đố bạn biết 1 + 2 bằng bao nhiêu?",
  "question_type": "AN",
  "possible": [],
  "image": null,
  "pub_date": "2015-12-04T15:42:40.153000Z",
  "skill": {
    "name": "Phép cộng hai số có một chữ số",
    "id_in_grade": 1,
    "grade": {
      "id": 1,
      "name": "1"
    }
  }
}
```

---
#### * POST api/v1/exercise/:gradeId/:skillId/ *
Post user answer for a specific exercise

Parameters: id, answer

---
## Exam
---
#### * GET api/v1/exam-list/:gradeId/ *
Get a list of exam in a specific grade

JSON format:
```
{
  {
    "id": 4,
    "grade": 2,
    "name": "Kiểm tra tháng 9/2015"
  },
  {
    "id": 10,
    "grade": 2,
    "name": "Kiểm tra tháng 10/2015"
  }
}
```

---
#### * GET api/v1/exam/:examId/ *
Get an exam with id is examId

JSON format:
```
{
  "id": 3,
  "grade": 3,
  "name": "Testing 3",
  "time_limit": 90,
  "num_exercises": 1,
  "exercises": (list of exercise),
  "taken": false
}
```

---
#### * POST api/v1/exam/:examId/ *
Post user answer for exam to server

Parameters: id, exercises, done_time

---
## ExamRecord
---
#### * GET api/v1/exam-record-user/:examId/ *
Get exam record for a specific user 

JSON format:
```
{
  "user": (user info),
  "exercise_records": (list of exercises),
  "score": 4,
  "done_time": 7
}
```

---
#### * GET api/v1/exam-record/:examId *
Get exam record for all user

JSON format:
```
{
  {
    "user": {
      "id": 1,
      "user": {
        "email": "admin@email.com",
        "username": "admin",
        "first_name": "Admin"
      },
      "school": "Đại học Công nghệ",
      "class_in_school": null,
      "created_at": "2015-10-06T13:25:09.749000Z",
      "updated_at": "2015-10-06T13:25:09.749000Z"
    },
    "score": 3,
    "done_time": 7
  },
  {
    "user": {
      "id": 2,
      "user": {
        "email": "user@email.com",
        "username": "user",
        "first_name": "Nguyen User"
      },
      "school": "ĐHSPHN",
      "class_in_school": null,
      "created_at": "2015-10-06T13:26:42.918000Z",
      "updated_at": "2015-10-06T13:26:42.918000Z"
    },
    "score": 2,
    "done_time": 6
  }
}
```

---
## ExerciseRecord
---
#### * GET api/v1/accounts/records/:username/ *
Get exercise record for a user

JSON format:
```
{
  "total_score": 47,
  "count_correct_answer": 11,
  "count_wrong_answer": 0,
  "total_record": 11
}
```