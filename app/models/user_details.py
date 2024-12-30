from app import db
import uuid
from app.models.audit_columns import AuditColumns
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import DECIMAL, ForeignKey

class UserDetails(db.Model, AuditColumns):
    __tablename__ = 'user_details'

    id = db.Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(ForeignKey('user_mst.id'), nullable=False)
    aadhaar_number = db.Column(db.String, nullable=False)
    college_name = db.Column(db.String(225), nullable=False)
    roll_number = db.Column(db.String(50), nullable=False)
    qualification = db.Column(db.String(255), nullable=True)
    experience_type = db.Column(db.String(50), nullable=False)
    experience = db.Column(DECIMAL, nullable=True)

    def to_dict(self):
        return {
            'id': str(self.id),
            'user_id': str(self.user_id), 
            'aadhaar_number': self.aadhaar_number,
            'college_name': self.college_name,
            'roll_number': self.roll_number,
            'qualification': self.qualification,
            'experience': str(self.experience),
            'created_tstmp': self.created_tstmp,
            'updated_tstmp': self.updated_tstmp,
            'created_by': str(self.created_by),
            'updated_by': str(self.updated_by)
        }