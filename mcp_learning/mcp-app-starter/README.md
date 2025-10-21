# MCP App Starter

A minimal, end-to-end scaffold that demonstrates Model Context Protocol (MCP) integration:

- **MCP Server**: Billing domain server (TypeScript, in-memory store) exposing tools via JSON Schema
- **Backend Orchestrator**: Express + TypeScript that connects to MCP server, exposes HTTP API, and streams progress via SSE
- **React Frontend**: Submits requests, shows tool-call progress, and renders results

⚠️ This is intentionally tiny and unopinionated. Replace the toy billing logic with real APIs (Stripe/Xero/etc.) behind the MCP tool.

## Project Structure

```
mcp-app-starter/
├─ servers/
│ └─ billing/
│   ├─ package.json
│   ├─ tsconfig.json
│   └─ src/
│     └─ index.ts
├─ backend/
│ ├─ package.json
│ ├─ tsconfig.json
│ ├─ src/
│ │ ├─ index.ts
│ │ ├─ mcpClient.ts
│ │ └─ schemas.ts
│ └─ .env.example
├─ frontend/
│ ├─ package.json
│ ├─ tsconfig.json
│ └─ src/
│   └─ App.tsx
└─ README.md
```

## Run Locally

### Prerequisites
- Node.js 20+

### 1) Install Dependencies

```bash
# Install dependencies for each workspace
cd servers/billing && npm i && npm run build
cd ../../backend && npm i && npm run build
cd ../frontend && npm i
```

### 2) Start Backend

```bash
cd backend && npm run dev
```

### 3) Start Frontend

```bash
cd frontend && npm run dev
```

Open http://localhost:5173 (or Vite's shown port). Backend listens at http://localhost:3001

## How It Works

- The backend launches the Billing MCP server as a child process and talks over stdio
- Frontend submits invoice creation requests to the backend
- Backend orchestrates MCP tool calls and streams progress via Server-Sent Events
- Replace the toy billing logic with real provider calls **inside the MCP tools**

## Hardening Checklist

- **AuthN/Z**: JWT or session; route-level RBAC; per-tool allow/deny
- **Secrets**: .env → key vault; never pass raw keys to frontend
- **Observability**: OpenTelemetry spans around each client.callTool; redact PII
- **Resilience**: retries w/ backoff, circuit breaker, timeout per tool; idempotency keys
- **Queues**: move long jobs to a worker; progress via events persisted to Redis
- **Schema governance**: version tools (billing.create_invoice@v1); deprecate windows
- **Tests**: contract tests on MCP inputs/outputs; mocked MCP in E2E; golden snapshots
- **Compliance**: audit log of tool invocations (user, time, inputs hash, outcome)

## Extending to Multiple Domains

Spin up additional MCP servers (e.g., crm, docs, payments) and mount routes in the backend that proxy tool calls. Keep each domain's auth isolated in its server, not the frontend.
