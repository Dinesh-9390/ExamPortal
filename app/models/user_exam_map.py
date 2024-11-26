import uuid
from app import db
from sqlalchemy.dialects.postgresql import UUID
from app.models.audit_columns import AuditColumns
from sqlalchemy import ForeignKey


class UserExamMap(db.Model, AuditColumns):
    __tablename__ = 'user_exam_map'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(ForeignKey('user_mst.id'))
    exam_id = db.Column(ForeignKey('exams.id'))
    current_question_id = db.Column(ForeignKey('questions_mst.id'))
    start_time = db.Column(db.TIMESTAMP, nullable=False)
    end_time = db.Column(db.TIMESTAMP, nullable=False)
    status = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            'id': str(self.id),
            'user_id': self.user_id,
            'exam_id': self.exam_id,
            'is_active': self.is_active,
            'current_question_id': str(self.current_question_id),
            'start_time': self.start_time,
            'end_time': self.end_time,
            'status': self.status
        }