# app/ -- Application Package Root

## Purpose

FastAPI application package for Alpine Notetaker. Contains the app factory, middleware stack,
lifespan manager, and all sub-packages organized in a layered architecture.

## Key Files

- **main.py** -- Application factory (`create_app()`), lifespan manager, middleware stack, route registration.
  This is the single entry point for the API server. The `app = create_app()` call at module level
  is what uvicorn picks up.
- **__init__.py** -- Empty package init.

## Architecture

The codebase follows a layered architecture with clear dependency direction:

```
core/          Infrastructure foundation (22 modules: config, DI, errors, middleware, streams, security, encryption)
  |
models/        SQLAlchemy ORM definitions (22 model files incl. base.py mixins)
  |
repositories/  Data access layer (generic CRUD base + domain queries)
  |
services/      Business logic (32 root modules + 9 sub-packages: clients, ingestion,
  |               llm, metrics, ml, pipeline, plugins, teams, zoom)
  |
dependencies/  FastAPI dependency injection wiring (Annotated type aliases)
  |
api/v1/        REST endpoints (24 route modules)
  |
schemas/       Pydantic request/response serialization (27 schema files)
  |
dto/           Internal Pydantic DTOs for service-to-service communication
  |               (8 files: 5 root + 3 external/ for zoom, teams, google_drive)
  |
tasks/         Async background workers (7 sub-packages: audio_preprocess, common,
                 embedding, ingestion, llm_processing, ml, plugins)
```

## Patterns

**Middleware ordering** in `create_app()` -- added bottom-to-top, executed outermost-first:

1. CORS (outermost -- must process preflight before anything else)
2. CorrelationID (assigns X-Request-ID to every request via ContextVar)
3. ErrorLogging (logs request/response with timing)
4. AuditMiddleware (captures POST/PUT/PATCH/DELETE mutations)
5. RateLimit (Redis sliding window, dual-scope: per-key + per-org)
6. AuthCookie (extracts api_key cookie into Authorization header)

**Lifespan startup sequence:**

1. `setup_logging()` -- structured JSON logging with Loki integration
2. `migrate()` -- Alembic migrations via `asyncio.to_thread`
3. `init_db()` -- async engine + session factory
4. `init_api_containers()` -- DI container (eagerly validates all services)
5. Seed default plans and plugins
6. Plugin registry validation (fail-fast if active plugin has no executor)
7. Redis connect + stream/consumer group setup
8. Broker start
9. `health_service.mark_startup_complete()` -- startup probe transitions to 200

**Graceful shutdown:** 30-second timeout, drains broker, Redis, DB in order.

## Gotchas

- Middleware order matters: CORS *must* be outermost. FastAPI adds middleware bottom-to-top,
  so the last `add_middleware()` call executes first.
- `ORJSONResponse` is the default response class (faster than stdlib json).
- The pydub SyntaxWarning filter at the top of main.py suppresses a known issue in Python 3.13+.
- All code is linted by ruff (`select = ["ALL"]`) and type-checked by mypy (`strict = true`).
  Configuration lives in `pyproject.toml`.  Pre-commit hooks enforce both on every commit.

## Related Packages

- `core/` -- Infrastructure (config, DI, errors, middleware, streams, security)
- `models/` -- ORM model definitions (22 files)
- `repositories/` -- Data access layer
- `services/` -- Business logic and ML processing (32 root + 9 sub-packages)
- `dependencies/` -- FastAPI DI wiring
- `api/` -- Route registration and health probes
- `api/v1/` -- Versioned REST endpoints (24 modules)
- `schemas/` -- Pydantic serialization schemas (27 files)
- `dto/` -- Internal Pydantic DTOs (8 files: 5 root + 3 external)
- `tasks/` -- Async background workers (7 sub-packages incl. common/ shared infra)


<claude-mem-context>
# Recent Activity

### Feb 6, 2026

| ID | Time | T | Title | Read |
|----|------|---|-------|------|
| #451 | 7:31 PM | 🔵 | Backend FastAPI Application Architecture and Lifecycle | ~463 |
</claude-mem-context>
