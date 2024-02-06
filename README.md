# Learning management system M_N_S LMS using django web framework

Learning management system with lots of features. This project would be an excellent starting point for you if you wanted to design a learning management system (also known as university management system) for a university organisation or merely to understand the tech stack and develop your portfolio. 




Current features
----------------
* Dashboard: Analytics and demographics for the school. limited to administrators only
* News & Events: This page is accessible to all users.
* The administrator oversees the students.(Include, amend, remove)
* Lecturers are managed by the admin (Add, Update, Delete)
* Students are able to add and drop courses.
* Instructors turn in the following student scores: _attendance, midterm, final, assignment_
* Students' _Total, average, point, and grades_ are automatically calculated by the system.
* Each student should receive a **pass**, **fail**, or **pass with a warning** grade comment.
* Students' page with assessment results
* Students' grade result page
* Management of the semester and the year
* Grades and assessments will be categorised by semester.
* Provide documentation and a video for every course.
* Students' registration slips and grade results can be created in PDF format.
* Restrictions on page access
* quiz results being stored under each user
* Randomization of question order
* You may view previous quiz results on the category page.
* Correct responses may be displayed following each question or all at once at the conclusion.
* If a person is not signed in, they can still finish a quiz if their session lasts long enough. signed-in users can go back to an incomplete quiz to finish it.
* Users may only be allowed to attempt the quiz once.
* One can categorise questions.
* A progress page allows you to keep track of each category's success rate.
* You can provide an explanation for each question's outcome.
* It is possible to establish pass marks.
* type of multiple-choice question
* Type of question: True/False
* Types of essay questions
* A personalised message is shown to quiz takers who pass or fail.
* Users with the custom permission "view_sittings" can now see other users' quiz outcomes.
* An essay question marking page that displays finished quizzes and allows filtering by user or quiz



# Requirements:

> To run the project, the following programs are required:

- [Python3.8+](https://www.python.org/downloads/)
- [PostgreSQL database](https://www.postgresql.org/download/)

# Installation

- Clone the repo with

```bash
git clone https://github.com/Mosu1025/learning-Management-System.git
```

- Setup and activate a virtual Python environment.

```bash
python -m venv [name of the virtul enivroment]
```
- Active the the created virtual enviroment by run below command

```bash
[name of the virtul enivroment]\Scripts\activate
```

```bash
pip install -r requirements.txt
```

- Create `.env` file inside the root directory and include the following variables

```bash
DB_NAME=[YOUR_DB_NAME]
DB_USER=[DB_ADMIN_NAME]
DB_PASSWORD=[DB_ADMIN_PASSWORD]
DB_HOST=localhost
DB_PORT=[YOUR_POSTGRES_PORT default is 5432]
USER_EMAIL=[YOUR_EMAIL]
USER_PASSWORD=[EMAIL_PASSWORD]
EMAIL_FROM_ADDRESS=[EMAIL_FORM_ADDRESS]
DEBUG=True
SECRET_KEY=[YOUR_SECRET_KEY]
```

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

Last but not least, go to this address http://127.0.0.1:8000
