import uuid
from app import db
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from app.models.audit_columns import AuditColumns
from sqlalchemy import ForeignKey


class UserRoleMap(db.Model, AuditColumns):
    __tablename__ = 'user_role_map'

    id = db.Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)
    user_id = db.Column(ForeignKey('user_mst.id'))
    role_id = db.Column(ForeignKey('role_mst.id'))
    def to_dict(self):
        return {
            'id': str(self.id),
            'user_id': self.user_id,
            'role_id': self.role_id
        }