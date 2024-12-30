import uuid
from app import db
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from app.models.audit_columns import AuditColumns

class UserMst(db.Model, AuditColumns):
    __tablename__ = 'user_mst'

    id = db.Column(PG_UUID(as_uuid=True), primary_key=True,  nullable=False, default=uuid.uuid4)
    first_name = db.Column(db.String(225), unique=False, nullable=False)
    last_name = db.Column(db.String(225), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_number = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
        'id': str(self.id),
        'first_name': self.first_name,
        'last_name': self.last_name,
        'email': self.email,
        'mobile_number': self.mobile_number
        }