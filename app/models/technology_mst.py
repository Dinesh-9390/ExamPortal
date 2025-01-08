import uuid
from app import db
from app.models.audit_columns import AuditColumns
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

class TechnologyMst(db.Model, AuditColumns):
    __tablename__ = 'technology_mst'

    id = db.Column(UNIQUEIDENTIFIER, primary_key=True,  nullable=False, default=uuid.uuid4)
    technology_name = db.Column(db.String(225), nullable=False, unique=True)

    def to_dict(self):
        return{
            'id': str(self.id),
            'technology_name': self.technology_name
        }