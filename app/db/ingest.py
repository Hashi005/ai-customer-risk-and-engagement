import csv
from datetime import datetime
from pathlib import Path

from app.db.session import SessionLocal, engine
from app.db.models import Base, Customer, Invoice, Payment, TeleopsUsage

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _parse_date(value):
    if not value:
        return None
    return datetime.strptime(value.strip(), "%Y-%m-%d").date()


def _to_float(value):
    return float(value) if value not in (None, "", "NA") else None


def _to_int(value):
    return int(value) if value not in (None, "", "NA") else 0


def ingest_customers(db):
    path = DATA_DIR / "customers.csv"
    acct_to_id = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            c = Customer(
                slt_account_no=row["slt_account_no"].strip(),
                name=row["name"].strip(),
                phone=row.get("phone", "").strip() or None,
                email=row.get("email", "").strip() or None,
                connection_type=row.get("connection_type", "").strip() or None,
                tenure_months=_to_int(row.get("tenure_months")),
            )
            db.add(c)
            db.flush()
            acct_to_id[c.slt_account_no] = c.id
    db.commit()
    print(f"[ok] customers: {len(acct_to_id)}")
    return acct_to_id


def ingest_invoices(db, acct_to_id):
    path = DATA_DIR / "invoices.csv"
    n = 0
    with path.open() as f:
        for row in csv.DictReader(f):
            cid = acct_to_id.get(row["slt_account_no"].strip())
            if not cid:
                continue
            db.add(Invoice(
                customer_id=cid,
                amount=_to_float(row["amount"]),
                due_date=_parse_date(row["due_date"]),
                paid_date=_parse_date(row.get("paid_date")),
                status=row.get("status", "unpaid").strip(),
            ))
            n += 1
    db.commit()
    print(f"[ok] invoices: {n}")


def ingest_payments(db, acct_to_id):
    path = DATA_DIR / "payments.csv"
    n = 0
    with path.open() as f:
        for row in csv.DictReader(f):
            cid = acct_to_id.get(row["slt_account_no"].strip())
            if not cid:
                continue
            db.add(Payment(
                customer_id=cid,
                amount=_to_float(row["amount"]),
                paid_date=_parse_date(row["paid_date"]),
                days_late=_to_int(row.get("days_late")),
            ))
            n += 1
    db.commit()
    print(f"[ok] payments: {n}")


def ingest_teleops(db, acct_to_id):
    path = DATA_DIR / "teleops_usage.csv"
    n = 0
    with path.open() as f:
        for row in csv.DictReader(f):
            cid = acct_to_id.get(row["slt_account_no"].strip())
            if not cid:
                continue
            db.add(TeleopsUsage(
                customer_id=cid,
                month=_parse_date(row["month"]),
                data_usage_gb=_to_float(row.get("data_usage_gb")),
                complaints=_to_int(row.get("complaints")),
                downtime_hours=_to_float(row.get("downtime_hours")) or 0,
            ))
            n += 1
    db.commit()
    print(f"[ok] teleops_usage: {n}")


def main():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        acct_to_id = ingest_customers(db)
        ingest_invoices(db, acct_to_id)
        ingest_payments(db, acct_to_id)
        ingest_teleops(db, acct_to_id)
    finally:
        db.close()
    print("Done.")


if __name__ == "__main__":
    main()