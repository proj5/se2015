# API REQUIREMENTS FROM CLIENT
---
**API to get grade list**
* Server have to return a JSON file contains an array describing all the grades available. The URL should be static. 
* JSON file format
  * "id": "gradeID" 
  * "name": "gradeName" 
  * "imagePath": "path" 

---
**API to get single question**
* User have to specify gradeID and call the API to retrieve JSON file which contains a question data from server
* JSON file format
  * "id": "" 
  * "questionType": "" (questionType is number)   
  * "description": "" 
  * "imagePath": "" 
  * "answer": "" 

* More details about question type:
  * "1": single-choice question  
  * "2": multi-choice question
  * "3": short-answered question
    
---
**API to get contest questions**
* User have to specify gradeID and call the API to retrieve a JSON file contains a fixed number of questions
* JSON file format
  * "count": "" 
  * "questions": ({question}, {question}, {question}, ...) (format of each question is the same as format of question from API get single question)

---
**API to get skill list**
* User have to specify gradeID and call the API to retrieve a JSON file contains all skills in a grade
* JSON file format (an array of multiple skill object, each object is formatted as below)
  * "id": ""
  * "name": "" 

---
**On going APIs**
* API to retrieve user profile
* API to retrieve forum topics