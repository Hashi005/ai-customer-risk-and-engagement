# Architecture v1

## High-Level Flow
Customer → Chatbot/API → Agent → ML Model → Customer Data

## Components
- Chatbot/API: FastAPI endpoints that receive user requests
- Agent: Decides which tool to call based on user intent
- ML Model: Computes risk_score and priority_score
- Customer Data: PostgreSQL (customers, invoices, payments, teleops_usage)

## Ownership
| Component      | Owner              |
|----------------|--------------------|
| API + Agent    | Backend            |
| ML Model       | ML teammate        |
| Dataset        | Data teammate      |
| Chatbot UI     | Frontend teammate  |
