from flask import Blueprint, request, jsonify
from app import db
from app.models import Student

api_bp = Blueprint('api', __name__)

@api_bp.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'course', 'email')):
        return jsonify({"error": "Missing required fields"}), 400

    new_student = Student(name=data['name'], course=data['course'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.to_dict()), 201

@api_bp.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students]), 200

@api_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    return jsonify(student.to_dict()), 200

@api_bp.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"}), 200