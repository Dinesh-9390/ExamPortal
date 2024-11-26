import uuid
from app import db
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from app.models.audit_columns import AuditColumns
from sqlalchemy import ForeignKey

class QuestionsMst(db.Model, AuditColumns):
    __tablename__ = 'questions_mst'

    id = db.Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_type = db.Column(db.String(50), nullable=False)
    section_id = db.Column(ForeignKey('sections.id'))
    sub_section_id = db.Column(ForeignKey('sub_sections.id'))
    question = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    positive_weightage = db.Column(db.String(50), nullable=True)
    negative_weightage = db.Column(db.String(50), nullable=True)

    def to_dict(self):
        return {
            'id': str(self.id),
            'question_type': self.question_type,
            'section_id': self.section_id,
            'sub_section_id': str(self.sub_section_id),
            'question': self.question,
            'description': self.description,
            'positive_weightage': self.positive_weightage,
            'negative_weightage': self.negative_weightage,
            'is_active': self.is_active
        }