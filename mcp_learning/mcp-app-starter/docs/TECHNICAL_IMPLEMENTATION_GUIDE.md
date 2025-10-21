# MCP App Starter - Technical Implementation Guide

## Table of Contents
1. [Architecture Overview](#architecture-overview)
2. [MCP Protocol Deep Dive](#mcp-protocol-deep-dive)
3. [Component-by-Component Breakdown](#component-by-component-breakdown)
4. [Data Flow Analysis](#data-flow-analysis)
5. [Code Implementation Details](#code-implementation-details)
6. [Development Workflow](#development-workflow)
7. [Troubleshooting Guide](#troubleshooting-guide)

## Architecture Overview

### System Architecture Diagram

```
┌─────────────────┐    HTTP/SSE     ┌─────────────────┐    stdio     ┌─────────────────┐
│                 │ ──────────────► │                 │ ──────────► │                 │
│   React         │                 │   Express        │             │   MCP Billing   │
│   Frontend      │ ◄────────────── │   Backend        │ ◄────────── │   Server        │
│   (Port 5173)   │                 │   (Port 3001)    │             │   (stdio)       │
└─────────────────┘                 └─────────────────┘             └─────────────────┘
```

### Component Responsibilities

1. **React Frontend**: User interface, form handling, real-time updates via SSE
2. **Express Backend**: API orchestration, MCP client management, SSE streaming
3. **MCP Billing Server**: Domain logic, tool implementation, data storage

## MCP Protocol Deep Dive

### What is MCP?

Model Context Protocol (MCP) is a standardized protocol for connecting AI applications to external data sources and tools. It provides a structured way for AI models to interact with external systems through a well-defined interface.

### MCP Architecture Components

#### 1. MCP Server
- **Purpose**: Exposes tools and resources to MCP clients
- **Transport**: Communicates via stdio, HTTP, or WebSocket
- **Tools**: Domain-specific functions that can be called by clients
- **Resources**: Data sources that can be read by clients

#### 2. MCP Client
- **Purpose**: Connects to MCP servers and calls their tools
- **Transport**: Uses same transport mechanism as server
- **Capabilities**: Can discover, call tools, and read resources

#### 3. Transport Layer
- **stdio**: Process-to-process communication via stdin/stdout
- **HTTP**: RESTful API communication
- **WebSocket**: Real-time bidirectional communication

### MCP Message Flow

```
Client                    Server
  │                         │
  │─── initialize ─────────►│
  │◄── initialized ──────────│
  │                         │
  │─── tools/list ─────────►│
  │◄── tools/list result ────│
  │                         │
  │─── tools/call ─────────►│
  │◄── tools/call result ────│
```

## Component-by-Component Breakdown

### 1. MCP Billing Server (`servers/billing/`)

#### File Structure
```
servers/billing/
├── package.json          # Dependencies and scripts
├── tsconfig.json         # TypeScript configuration
└── src/
    └── index.ts         # Main server implementation
```

#### Key Implementation Details

**Package Configuration (`package.json`)**
```json
{
  "name": "mcp-billing-server",
  "type": "module",
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.18.0",
    "zod": "^3.23.8"
  }
}
```

**Why These Dependencies?**
- `@modelcontextprotocol/sdk`: Official MCP SDK for TypeScript
- `zod`: Runtime validation library for input schemas
- `"type": "module"`: Enables ES modules for modern JavaScript

**Server Implementation (`src/index.ts`)**

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
```

**Key Concepts:**

1. **McpServer**: Main server class that handles MCP protocol
2. **StdioServerTransport**: Handles communication via stdin/stdout
3. **zod**: Provides runtime validation for tool inputs

**Tool Registration Pattern:**
```typescript
mcpServer.registerTool("tool_name", {
  description: "Tool description",
  inputSchema: {
    param1: z.string().describe("Parameter description"),
    param2: z.number().min(0).describe("Another parameter")
  }
}, async ({ param1, param2 }) => {
  // Tool implementation
  return {
    content: [
      {
        type: "text",
        text: JSON.stringify(result)
      }
    ]
  };
});
```

**Why This Pattern?**
- **Declarative**: Tools are defined with clear schemas
- **Type-safe**: Zod schemas provide runtime validation
- **Consistent**: All tools follow the same return format
- **Extensible**: Easy to add new tools

**Data Storage Strategy:**
```typescript
const invoices = new Map<string, InvoiceData>();
```

**Why In-Memory Storage?**
- **Simplicity**: No external database dependencies
- **Demo Purpose**: Focuses on MCP integration, not persistence
- **Performance**: Fast access for demonstration
- **Stateless**: Each server instance is independent

### 2. Express Backend (`backend/`)

#### File Structure
```
backend/
├── package.json          # Dependencies and scripts
├── tsconfig.json         # TypeScript configuration
├── env.example          # Environment variables template
└── src/
    ├── index.ts         # Main Express server
    ├── mcpClient.ts     # MCP client management
    └── schemas.ts       # Validation schemas
```

#### Key Implementation Details

**MCP Client Management (`src/mcpClient.ts`)**

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

**Client Connection Pattern:**
```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["dist/index.js"],
  cwd: new URL("../../servers/billing/", import.meta.url).pathname
});

const client = new Client({
  name: "billing-backend-client",
  version: "0.1.0"
});

await client.connect(transport);
```

**Why This Approach?**
- **Process Isolation**: MCP server runs in separate process
- **Transport Abstraction**: Easy to switch transport mechanisms
- **Connection Management**: Handles connection lifecycle
- **Error Handling**: Proper error propagation

**API Endpoint Implementation (`src/index.ts`)**

**Invoice Creation Endpoint:**
```typescript
app.post("/api/invoices", async (req, res) => {
  const parsed = CreateInvoiceInput.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.flatten() });
  }
  
  const opId = nanoid();
  progress.set(opId, { done: false, events: ["received"] });
  
  // Async operation...
});
```

**Key Design Decisions:**
- **Validation**: Zod schemas for input validation
- **Async Operations**: Non-blocking request handling
- **Progress Tracking**: Real-time operation status
- **Error Handling**: Structured error responses

**Server-Sent Events Implementation:**
```typescript
app.get("/api/stream/:opId", (req, res) => {
  res.setHeader("Content-Type", "text/event-stream");
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Connection", "keep-alive");
  
  const interval = setInterval(() => {
    const p = progress.get(opId);
    if (!p) return;
    
    res.write(`event: progress\ndata: ${JSON.stringify({ 
      events: p.events, 
      done: p.done 
    })}\n\n`);
    
    if (p.done) {
      res.write(`event: result\ndata: ${JSON.stringify(p.result)}\n\n`);
      clearInterval(interval);
      res.end();
    }
  }, 400);
});
```

**Why SSE Over WebSockets?**
- **Simplicity**: One-way communication is sufficient
- **HTTP Compatibility**: Works through firewalls and proxies
- **Automatic Reconnection**: Browser handles reconnection
- **Server Push**: Real-time updates without polling

### 3. React Frontend (`frontend/`)

#### File Structure
```
frontend/
├── package.json          # Dependencies and scripts
├── tsconfig.json         # TypeScript configuration
├── vite.config.ts        # Vite configuration
├── index.html           # HTML entry point
└── src/
    ├── main.tsx         # React entry point
    └── App.tsx          # Main application component
```

#### Key Implementation Details

**Vite Configuration (`vite.config.ts`)**
```typescript
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    host: true
  }
});
```

**Why Vite?**
- **Fast Development**: Hot Module Replacement (HMR)
- **Modern Build**: ES modules and tree shaking
- **TypeScript Support**: Built-in TypeScript support
- **Simple Configuration**: Minimal setup required

**React Component Structure (`src/App.tsx`)**

**State Management:**
```typescript
const [amount, setAmount] = useState(42);
const [currency, setCurrency] = useState("USD");
const [email, setEmail] = useState("demo@example.com");
const [opId, setOpId] = useState<string | null>(null);
const [events, setEvents] = useState<string[]>([]);
const [result, setResult] = useState<any>(null);
```

**Why This State Structure?**
- **Form Data**: Separate state for each form field
- **Operation Tracking**: Track current operation ID
- **Progress Display**: Store progress events
- **Result Display**: Store final operation result

**SSE Integration:**
```typescript
useEffect(() => {
  if (!opId) return;

  const es = new EventSource(`${backendURL}/api/stream/${opId}`);
  
  es.addEventListener("progress", (ev: MessageEvent) => {
    const payload = JSON.parse(ev.data);
    setEvents(payload.events || []);
  });

  es.addEventListener("result", (ev: MessageEvent) => {
    const payload = JSON.parse(ev.data);
    setResult(payload);
    es.close();
  });

  return () => es.close();
}, [opId, backendURL]);
```

**Why useEffect for SSE?**
- **Lifecycle Management**: Proper cleanup on unmount
- **Dependency Tracking**: Reconnects when opId changes
- **Event Handling**: Separate handlers for different event types
- **Memory Management**: Prevents memory leaks

## Data Flow Analysis

### Complete Request Flow

```
1. User submits form
   ↓
2. Frontend sends POST /api/invoices
   ↓
3. Backend validates input with Zod
   ↓
4. Backend generates operation ID
   ↓
5. Backend starts async MCP operation
   ↓
6. Backend returns operation ID immediately
   ↓
7. Frontend opens SSE connection
   ↓
8. Backend connects to MCP server via stdio
   ↓
9. Backend calls billing.create_invoice tool
   ↓
10. MCP server validates and stores invoice
    ↓
11. Backend calls billing.get_invoice tool
    ↓
12. MCP server returns invoice data
    ↓
13. Backend updates progress and sends SSE events
    ↓
14. Frontend receives progress updates
    ↓
15. Frontend displays final result
```

### Error Handling Flow

```
1. Error occurs at any step
   ↓
2. Error is caught and logged
   ↓
3. Progress is updated with error state
   ↓
4. SSE event sent with error information
   ↓
5. Frontend receives error event
   ↓
6. Frontend displays error message
   ↓
7. User can retry operation
```

## Code Implementation Details

### MCP Tool Implementation Pattern

**Input Schema Definition:**
```typescript
inputSchema: {
  amount: z.number().min(0).describe("Invoice amount"),
  currency: z.string().length(3).describe("Currency code (3 letters)"),
  customer_email: z.string().email().describe("Customer email address"),
  idempotency_key: z.string().describe("Unique key for idempotency")
}
```

**Tool Handler Implementation:**
```typescript
async ({ amount, currency, customer_email, idempotency_key }) => {
  // Idempotency check
  if (invoices.has(idempotency_key)) {
    return {
      content: [
        {
          type: "text",
          text: JSON.stringify({
            invoice_id: idempotency_key,
            reused: true
          })
        }
      ]
    };
  }
  
  // Create new invoice
  invoices.set(idempotency_key, {
    amount,
    currency,
    customer_email,
    status: "draft"
  });
  
  return {
    content: [
      {
        type: "text",
        text: JSON.stringify({
          invoice_id: idempotency_key,
          reused: false
        })
      }
    ]
  };
}
```

### Backend MCP Client Pattern

**Tool Call Implementation:**
```typescript
const createResp = await client.request({
  method: "tools/call",
  params: {
    name: "billing.create_invoice",
    arguments: {
      ...parsed.data,
      idempotency_key
    }
  }
}, CallToolResultSchema);
```

**Response Processing:**
```typescript
if (!createResp.content || createResp.content.length === 0) {
  throw new Error("MCP error creating invoice");
}

const createResult = JSON.parse((createResp.content[0] as any).text);
const invId = createResult.invoice_id;
```

### Frontend State Management Pattern

**Form Submission:**
```typescript
async function onSubmit(e: React.FormEvent) {
  e.preventDefault();
  setEvents([]);
  setResult(null);
  setOpId(null);

  const res = await fetch(`${backendURL}/api/invoices`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      amount: Number(amount),
      currency,
      customer_email: email
    })
  });

  const data = await res.json();
  if (data.opId) setOpId(data.opId);
}
```

## Development Workflow

### 1. Project Setup

**Install Dependencies:**
```bash
cd mcp-app-starter
npm install
```

**Build Components:**
```bash
npm run build:all
```

### 2. Development Process

**Start Backend:**
```bash
cd backend
npm run dev
```

**Start Frontend:**
```bash
cd frontend
npm run dev
```

**Or Use Startup Script:**
```bash
./start.sh  # Unix/Mac
start.bat   # Windows
```

### 3. Testing Workflow

**Test Backend API:**
```bash
curl -X POST http://localhost:3001/api/invoices \
  -H "Content-Type: application/json" \
  -d '{"amount": 100, "currency": "USD", "customer_email": "test@example.com"}'
```

**Test SSE Stream:**
```bash
curl -N http://localhost:3001/api/stream/{operation_id}
```

### 4. Debugging Tips

**MCP Server Debugging:**
- Check stdio transport connection
- Verify tool registration
- Monitor MCP protocol messages

**Backend Debugging:**
- Check MCP client connection
- Monitor progress updates
- Verify SSE event formatting

**Frontend Debugging:**
- Check SSE connection status
- Monitor state updates
- Verify API responses

## Troubleshooting Guide

### Common Issues

#### 1. MCP Server Connection Issues

**Problem**: Backend cannot connect to MCP server
**Symptoms**: "connecting-mcp" event never appears
**Solutions**:
- Verify MCP server builds successfully
- Check stdio transport configuration
- Ensure correct working directory path

#### 2. SSE Connection Issues

**Problem**: Frontend doesn't receive progress updates
**Symptoms**: Progress events don't appear
**Solutions**:
- Check CORS configuration
- Verify SSE endpoint URL
- Monitor browser network tab

#### 3. TypeScript Compilation Issues

**Problem**: Build fails with type errors
**Symptoms**: TypeScript compilation errors
**Solutions**:
- Update MCP SDK to latest version
- Check module resolution settings
- Verify import paths

#### 4. Port Conflicts

**Problem**: Services fail to start due to port conflicts
**Symptoms**: "EADDRINUSE" errors
**Solutions**:
- Kill existing processes on ports 3001/5173
- Use different ports in configuration
- Check for background processes

### Performance Optimization

#### 1. MCP Server Optimization
- Implement connection pooling
- Add request caching
- Optimize tool execution

#### 2. Backend Optimization
- Implement request queuing
- Add connection pooling
- Optimize SSE event frequency

#### 3. Frontend Optimization
- Implement request debouncing
- Add loading states
- Optimize re-renders

### Security Considerations

#### 1. Input Validation
- Validate all inputs on both frontend and backend
- Sanitize data before processing
- Implement rate limiting

#### 2. CORS Configuration
- Restrict origins in production
- Configure allowed headers and methods
- Implement proper authentication

#### 3. Error Handling
- Don't expose internal errors to clients
- Log errors for debugging
- Implement proper error boundaries

---

**Document Version:** 1.0  
**Last Updated:** September 18, 2025  
**Technical Lead:** Development Team
