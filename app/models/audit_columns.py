from sqlalchemy import Column, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime

class AuditColumns:
    @declared_attr
    def created_tstmp(cls):
        return Column(DateTime, default=datetime.utcnow)

    @declared_attr
    def updated_tstmp(cls):
        return Column(DateTime, onupdate=datetime.utcnow)

    @declared_attr
    def created_by(cls):
        return Column(ForeignKey('user_mst.id'), nullable=True)

    @declared_attr
    def updated_by(cls):
        return Column(ForeignKey('user_mst.id'), nullable=True)

    @declared_attr
    def is_deleted(cls):
        return Column(Boolean, default=0)