from firebase_admin import firestore

db = firestore.client()

def get_student(student_id):
    return db.collection("students").document(student_id).get()