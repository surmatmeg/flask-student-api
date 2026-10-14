# 🎓 Flask Student API & CI/CD Pipeline

A lightweight RESTful API built with Python, Flask, and SQLite for managing student records. This project demonstrates backend architecture using the application factory pattern, automated testing with `unittest`, and automated continuous integration via GitHub Actions.

---

## 🛠 Tech Stack

* **Language:** Python 3.13
* **Framework:** Flask & Flask-SQLAlchemy
* **Database:** SQLite
* **Testing:** Python `unittest` framework
* **CI/CD:** GitHub Actions

---

## 📁 Project Architecture
flask-student-api/
├── app/
│   ├── init.py      # App factory & DB initialization
│   ├── models.py        # Database models
│   └── routes.py        # API endpoints
├── tests/
│   └── test_api.py      # Automated test suite
├── .github/
│   └── workflows/
│       └── ci.yml       # GitHub Actions CI workflow
├── requirements.txt     # Dependency list
└── run.py               # Application entry point


---

## 🧪 Running Tests Locally

To run the test suite locally, execute:

```bash
python -m unittest discover -s tests

---

### Step 3: Save and Commit

1. Click the green **Commit changes...** button at the top right of the editor.
2. Click **Commit changes** in the pop-up modal.

*How to verify:* You will immediately see the formatted README rendered beautifully on your main repository homepage, and GitHub Actions will automatically trigger a quick run to ensure your repo stays green!

***

<Elicitations message="What would you like to do next?">
  <Elicitation label="Check GitHub Actions status" query="How do I check if my GitHub Actions workflow passed on GitHub?"/>
  <Elicitation label="Take a break" query="I want to pause here and take a break."/>
</Elicitations>
