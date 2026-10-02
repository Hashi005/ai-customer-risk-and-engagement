# Agent / API Design

## Flow
User -> API -> Agent -> Tools -> Database / ML Model

## Endpoints (planned)
| Method | Path                          | Purpose             |
|--------|-------------------------------|---------------------|
| POST   | /api/chat                     | Chat -> agent       |
| GET    | /api/customer/{id}            | Profile             |
| GET    | /api/customer/{id}/invoices   | Invoices            |
| GET    | /api/customer/{id}/payments   | Payment history     |
| GET    | /api/customer/{id}/risk       | Risk score          |
| GET    | /api/collections/prioritized  | Ranked list         |
| POST   | /api/score/run                | Trigger scoring     |

## Agent Tool Mapping
| User says                        | Tools called                  |
|----------------------------------|-------------------------------|
| risk for SLT-011-45921           | get_customer, get_risk_score  |
| unpaid invoices for customer 3   | get_customer, get_invoices    |
| top 20 to call                   | get_prioritized_collections   |
