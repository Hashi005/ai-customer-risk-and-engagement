# Agent Tool Specifications

1. get_customer(customer_id, slt_account_no) -> customer profile
2. get_invoices(customer_id, status) -> list of invoices
3. get_payment_history(customer_id, months) -> payment timeline
4. get_risk_score(customer_id) -> {risk_score, priority_score, action}
5. get_teleops_usage(customer_id, month) -> usage data
6. get_prioritized_collections(limit, min_priority) -> ranked list
