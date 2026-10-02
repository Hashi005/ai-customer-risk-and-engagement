# ML Interface Contract

Backend expects: compute_risk(db, customer) -> dict

Returns:
{
  "risk_score": float,        # 0.0 - 1.0
  "priority_score": float,    # 0.0 - 1.0
  "recommended_action": str,  # IMMEDIATE_CALL | SMS_REMINDER | EMAIL | MONITOR
  "reasons": str
}

Until real model is ready, a mock lives in app/services/risk_service.py.
