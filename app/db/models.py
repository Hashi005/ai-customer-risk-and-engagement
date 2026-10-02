from sqlalchemy import (
    Column, Integer, String, Date, DateTime, Numeric, Text,
    ForeignKey, func,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    slt_account_no = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    phone = Column(String(15))
    email = Column(String(100))
    connection_type = Column(String(20))
    tenure_months = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now())

    invoices = relationship("Invoice", back_populates="customer")
    payments = relationship("Payment", back_populates="customer")
    usage = relationship("TeleopsUsage", back_populates="customer")
    scores = relationship("RiskScore", back_populates="customer")


class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    due_date = Column(Date, nullable=False)
    paid_date = Column(Date)
    status = Column(String(20), default="unpaid")
    customer = relationship("Customer", back_populates="invoices")


class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    paid_date = Column(Date, nullable=False)
    days_late = Column(Integer, default=0)
    customer = relationship("Customer", back_populates="payments")


class TeleopsUsage(Base):
    __tablename__ = "teleops_usage"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    month = Column(Date, nullable=False)
    data_usage_gb = Column(Numeric(10, 2))
    complaints = Column(Integer, default=0)
    downtime_hours = Column(Numeric(10, 2), default=0)
    customer = relationship("Customer", back_populates="usage")


class RiskScore(Base):
    __tablename__ = "risk_scores"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    risk_score = Column(Numeric(4, 3), nullable=False)
    priority_score = Column(Numeric(4, 3), nullable=False)
    recommended_action = Column(String(50))
    reasons = Column(Text)
    scored_at = Column(DateTime, server_default=func.now())
    customer = relationship("Customer", back_populates="scores")