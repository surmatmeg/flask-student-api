import unittest
from app import create_app, db
from app.models import Student

class StudentAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(database_uri="sqlite:///:memory:")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_student(self):
        payload = {"name": "Alex Smith", "course": "Software Engineering", "email": "alex@example.com"}
        response = self.client.post('/api/students', json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Alex Smith", response.get_data(as_text=True))

    def test_get_students(self):
        response = self.client.get('/api/students')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()