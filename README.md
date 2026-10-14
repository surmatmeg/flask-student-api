🎓 Flask Student API & CI/CD Pipeline

A lightweight RESTful API built with Python, Flask, and SQLite for managing student records. This project demonstrates backend architecture using the application factory pattern, automated testing with `unittest`, and automated continuous integration via GitHub Actions.

---

## 🛠 Tech Stack

* **Language:** Python 3.13
* **Framework:** Flask & Flask-SQLAlchemy
* **Database:** SQLite
* **Testing:** Python `unittest` framework
* **CI/CD:** GitHub Actions

---

## 📁 Project Structure

* **`app/`** — Application package containing core business logic
  * **`__init__.py`** — Application factory pattern & database setup
  * **`models.py`** — Database models & schema definitions
  * **`routes.py`** — API endpoints & request handlers
* **`tests/`** — Automated test suite
  * **`test_api.py`** — Unit and integration tests
* **`.github/workflows/`** — Continuous Integration setup
  * **`ci.yml`** — GitHub Actions workflow configuration
* **`requirements.txt`** — Project dependencies
* **`run.py`** — Application entry point

---

## 🧪 Running Tests Locally

To run the test suite locally, execute:

```bash
python -m unittest discover -s tests
