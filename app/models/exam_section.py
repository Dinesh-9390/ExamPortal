import uuid
from app import db
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from app.models.audit_columns import AuditColumns
from sqlalchemy import ForeignKey

class ExamSection(db.Model, AuditColumns):
    __tablename__ = 'exam_section'

    id = db.Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)
    exam_id = db.Column(ForeignKey('exams.id'))
    section_id = db.Column(ForeignKey('sections.id'))
    sub_section_id = db.Column(ForeignKey('sub_sections.id'))
    duration = db.Column(db.Integer, nullable=False)
    marks = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return({
            'id': str(self.id),
            'exam_id': str(self.exam_id),
            'section_id': str(self.section_id),
            'sub_section_id': str(self.sub_section_id),
            'duration': self.duration,
            'marks': self.marks
        })