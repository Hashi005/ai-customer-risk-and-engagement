cat > README.md << 'EOF'
# SLT Customer Risk & Collection Prioritization — Backend

Week 1 deliverable: architecture + tool spec + DB schema + agent/API design.

## Stack
- Python 3.12, FastAPI, SQLAlchemy, PostgreSQL
- Agent skeleton with rule-based orchestrator (LLM-ready)

## Run
    source venv/bin/activate
    python -m app.db.ingest
    uvicorn app.main:app --reload

## Endpoints (planned)
- POST /api/chat
- GET  /api/customer/{id}
- GET  /api/collections/prioritized
- POST /api/score/run

## Week 1 Status
- [x] Architecture doc
- [x] Tool specs
- [x] DB schema + ingestion
- [x] Agent/API design
- [x] ML interface contract
EOF