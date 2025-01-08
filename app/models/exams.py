import uuid
from app import db
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from app.models.audit_columns import AuditColumns

class Exams(db.Model, AuditColumns):
    __tablename__ = 'exams'

    id = db.Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False, default=uuid.uuid4)
    title = db.Column(db.String(225), nullable=False)
    description = db.Column(db.String)
    access_code = db.Column(db.String(50), nullable=True)
    duration = db.Column(db.Integer, nullable=False)
    total_marks = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return({
            'id': str(self.id),
            'title': self.title,
            'description': self.description,
            'access_code': self.access_code,
            'duration': self.duration,
            'total_marks': self.total_marks
        })