# MCP App Starter - Teaching Presentation Guide

## Presentation Overview

**Title:** Building Modern AI Applications with Model Context Protocol (MCP)  
**Duration:** 60-90 minutes  
**Audience:** Developers, Technical Leads, AI Enthusiasts  
**Prerequisites:** Basic knowledge of JavaScript/TypeScript, React, Node.js  

## Learning Objectives

By the end of this presentation, participants will be able to:

1. **Understand MCP Architecture**: Explain what MCP is and how it works
2. **Implement MCP Servers**: Create their own MCP servers with tools
3. **Build MCP Clients**: Connect to MCP servers and call tools
4. **Design Full-Stack Applications**: Integrate MCP into web applications
5. **Apply Best Practices**: Follow MCP development patterns and conventions

## Presentation Structure

### Part 1: Introduction to MCP (15 minutes)
### Part 2: Architecture Deep Dive (20 minutes)
### Part 3: Live Coding Demonstration (30 minutes)
### Part 4: Hands-on Workshop (15 minutes)
### Part 5: Q&A and Discussion (10 minutes)

---

## Part 1: Introduction to MCP (15 minutes)

### Slide 1: What is Model Context Protocol?

**Speaker Notes:**
"Let's start with the fundamental question: What is MCP and why should we care about it?"

**Key Points:**
- MCP is a standardized protocol for connecting AI applications to external data sources and tools
- It provides a structured way for AI models to interact with external systems
- Think of it as a universal translator between AI and the real world

**Visual Aid:**
```
AI Model ←→ MCP Protocol ←→ External Systems
         (Standardized)    (Tools, Data, APIs)
```

### Slide 2: The Problem MCP Solves

**Speaker Notes:**
"Before MCP, integrating AI with external systems was messy and inconsistent."

**Problems Without MCP:**
- Each AI system had its own way of connecting to external tools
- No standardization across different platforms
- Difficult to maintain and extend integrations
- Security and reliability concerns

**Benefits With MCP:**
- Standardized protocol across all AI systems
- Easy to add new tools and capabilities
- Better security and error handling
- Reusable components and patterns

### Slide 3: MCP Architecture Overview

**Speaker Notes:**
"MCP follows a client-server architecture with clear separation of concerns."

**Components:**
1. **MCP Server**: Exposes tools and resources
2. **MCP Client**: Connects to servers and calls tools
3. **Transport Layer**: Handles communication (stdio, HTTP, WebSocket)

**Visual Aid:**
```
┌─────────────┐    Transport    ┌─────────────┐
│ MCP Client  │ ←─────────────→ │ MCP Server  │
│             │                 │             │
│ - Discovers │                 │ - Exposes   │
│ - Calls     │                 │   Tools     │
│ - Reads     │                 │ - Provides  │
│             │                 │   Resources │
└─────────────┘                 └─────────────┘
```

### Slide 4: MCP Standard Format

**Speaker Notes:**
"Let's understand the standard structure that all MCP servers and clients follow."

**MCP Server Standard Structure:**
1. **Server Setup**: Create server instance with name and version
2. **Tool Registration**: Define tools with names, descriptions, and input schemas
3. **Input Validation**: Use schemas to validate what data tools expect
4. **Tool Implementation**: Write business logic for each tool
5. **Response Format**: Return results in standard format with content and type
6. **Transport Connection**: Connect to transport method (stdio, HTTP, WebSocket)
7. **Error Handling**: Handle errors gracefully with meaningful messages
8. **Server Startup**: Start server and keep it running

**MCP Client Standard Structure:**
1. **Client Creation**: Create client instance with name and version
2. **Transport Setup**: Choose communication method (stdio, HTTP, WebSocket)
3. **Connection**: Establish connection to MCP server
4. **Tool Discovery**: Ask server what tools are available
5. **Tool Calls**: Call specific tools with required parameters
6. **Response Processing**: Handle results from tool calls
7. **Error Handling**: Deal with connection issues and failures
8. **Cleanup**: Properly close connections when done

**Standard Communication Flow:**
1. **Handshake**: Client and server introduce themselves
2. **Discovery**: Client asks server what tools are available
3. **Tool Calls**: Client requests specific tools to be executed
4. **Processing**: Server runs tool logic and processes request
5. **Response**: Server sends back results in standard format
6. **Error Handling**: Problems are communicated clearly

### Slide 5: Real-World Use Cases

**Speaker Notes:**
"MCP isn't just theoretical - it's being used in production applications today."

**Use Cases:**
- **File System Access**: AI can read/write files on your computer
- **Database Operations**: AI can query and update databases
- **API Integration**: AI can call external APIs (Stripe, GitHub, etc.)
- **Development Tools**: AI can run code, manage git repos, deploy applications
- **Business Applications**: AI can manage invoices, customers, orders

**Demo Preview:**
"We'll build a billing system where AI can create and manage invoices."

---

## Part 2: Architecture Deep Dive (20 minutes)

### Slide 5: Our Application Architecture

**Speaker Notes:**
"Let's look at the complete architecture of our MCP App Starter."

**Visual Aid:**
```
┌─────────────────┐    HTTP/SSE     ┌─────────────────┐    stdio     ┌─────────────────┐
│                 │ ──────────────► │                 │ ──────────► │                 │
│   React         │                 │   Express        │             │   MCP Billing   │
│   Frontend      │ ◄────────────── │   Backend        │ ◄────────── │   Server        │
│   (Port 5173)   │                 │   (Port 3001)    │             │   (stdio)       │
└─────────────────┘                 └─────────────────┘             └─────────────────┘
```

**Component Responsibilities:**

**React Frontend (Port 5173)**
- **Role**: User interface and user experience
- **Responsibilities**: 
  - Display forms for user input
  - Handle user interactions (clicks, form submissions)
  - Show real-time progress updates via Server-Sent Events
  - Display final results to users
- **Technology**: React 18, TypeScript, Vite
- **Communication**: HTTP requests to backend, SSE for real-time updates

**Express Backend (Port 3001)**
- **Role**: API orchestrator and MCP client
- **Responsibilities**:
  - Provide REST API endpoints for frontend
  - Act as MCP client to connect to MCP server
  - Validate input data using Zod schemas
  - Manage operation progress and status
  - Stream real-time updates via Server-Sent Events
- **Technology**: Express.js, TypeScript, MCP SDK
- **Communication**: HTTP with frontend, stdio with MCP server

**MCP Billing Server (stdio)**
- **Role**: Domain-specific business logic server
- **Responsibilities**:
  - Expose billing tools (create_invoice, get_invoice)
  - Implement business rules and validation
  - Store and manage invoice data
  - Handle MCP protocol communication
- **Technology**: Node.js, TypeScript, MCP SDK
- **Communication**: stdio transport with backend

### Slide 6: MCP Server Deep Dive

**Speaker Notes:**
"The MCP server is where the magic happens - it's where we define our domain tools."

**Key Concepts:**

**Tools**: Functions that can be called by MCP clients
- Think of tools as "capabilities" that the server offers
- Each tool has a name, description, and input requirements
- Tools perform specific business operations (create invoice, get invoice)
- Tools return structured results that clients can process
- Tools can have side effects (modify data) or be read-only

**Resources**: Data sources that can be read by clients
- Resources are like "read-only files" containing information
- Clients can request specific resources (e.g., "billing/invoices")
- Resources provide data without modifying anything
- Examples: invoice lists, user profiles, system configurations
- Resources are identified by URIs (like web addresses)

**Transport**: How the server communicates (we use stdio)
- Transport is the "communication method" between client and server
- stdio = direct process-to-process communication (like talking face-to-face)
- HTTP = web-based communication (like sending messages over internet)
- WebSocket = real-time bidirectional communication (like live video call)
- We use stdio because it's simple, fast, and perfect for local applications

**Code Example:**
```typescript
// Tool Registration
mcpServer.registerTool("billing.create_invoice", {
  description: "Create an invoice and return its id.",
  inputSchema: {
    amount: z.number().min(0).describe("Invoice amount"),
    currency: z.string().length(3).describe("Currency code"),
    customer_email: z.string().email().describe("Customer email"),
    idempotency_key: z.string().describe("Unique key for idempotency")
  }
}, async ({ amount, currency, customer_email, idempotency_key }) => {
  // Tool implementation
  return {
    content: [
      {
        type: "text",
        text: JSON.stringify({ invoice_id: idempotency_key })
      }
    ]
  };
});
```

### Slide 7: MCP Client Deep Dive

**Speaker Notes:**
"The MCP client connects to servers and calls their tools."

**Connection Process:**
1. **Create transport** (stdio, HTTP, WebSocket)
   - Choose how to communicate with the server
   - stdio: Direct process communication (what we use)
   - HTTP: Web-based communication for remote servers
   - WebSocket: Real-time communication for live updates

2. **Create client instance**
   - Give the client a name and version
   - Set up client capabilities and preferences
   - Prepare for connection to server

3. **Connect to server**
   - Establish communication channel
   - Perform handshake (introduce client to server)
   - Exchange capabilities and negotiate protocol version

4. **Discover available tools**
   - Ask server: "What tools do you have?"
   - Get list of available tools with descriptions
   - Understand what each tool does and what inputs it needs

5. **Call tools as needed**
   - Request specific tools to be executed
   - Send required parameters
   - Receive and process results

**Code Example:**
```typescript
// Client Connection
const transport = new StdioClientTransport({
  command: "node",
  args: ["dist/index.js"],
  cwd: "../../servers/billing/"
});

const client = new Client({
  name: "billing-backend-client",
  version: "0.1.0"
});

await client.connect(transport);

// Tool Call
const result = await client.request({
  method: "tools/call",
  params: {
    name: "billing.create_invoice",
    arguments: { amount: 100, currency: "USD", customer_email: "test@example.com" }
  }
}, CallToolResultSchema);
```

### Slide 8: Real-Time Communication with SSE

**Speaker Notes:**
"One of the coolest features is real-time progress streaming using Server-Sent Events."

**Why SSE?**
- One-way communication (server to client)
- Works through firewalls and proxies
- Automatic reconnection
- Simple to implement

**Implementation:**
```typescript
// Backend SSE Endpoint
app.get("/api/stream/:opId", (req, res) => {
  res.setHeader("Content-Type", "text/event-stream");
  
  const interval = setInterval(() => {
    const progress = progressStore.get(opId);
    res.write(`event: progress\ndata: ${JSON.stringify(progress)}\n\n`);
    
    if (progress.done) {
      res.write(`event: result\ndata: ${JSON.stringify(progress.result)}\n\n`);
      clearInterval(interval);
      res.end();
    }
  }, 400);
});

// Frontend SSE Connection
const es = new EventSource(`/api/stream/${opId}`);
es.addEventListener("progress", (event) => {
  const data = JSON.parse(event.data);
  setProgress(data.events);
});
```

### Slide 9: Data Flow Analysis

**Speaker Notes:**
"Let's trace through a complete request to understand how data flows through our system."

**Complete Flow (Detailed Step-by-Step):**

1. **User submits form → Frontend**
   - User fills out invoice form (amount, currency, email)
   - Clicks "Create Invoice" button
   - Frontend captures form data

2. **Frontend sends POST request → Backend**
   - Frontend makes HTTP POST to `/api/invoices`
   - Sends form data as JSON in request body
   - Waits for response from backend

3. **Backend validates input → Zod schemas**
   - Backend receives the request
   - Uses Zod to validate: amount (number), currency (3 chars), email (valid format)
   - If validation fails, returns error to frontend

4. **Backend generates operation ID → nanoid**
   - Creates unique operation ID (e.g., "abc123xyz")
   - This ID tracks the entire operation from start to finish
   - Stores operation in memory with initial status

5. **Backend starts async MCP operation → Background**
   - Starts background process (doesn't block the response)
   - This allows backend to respond immediately to frontend
   - MCP operations happen in parallel

6. **Backend returns operation ID → Frontend**
   - Sends operation ID back to frontend immediately
   - Frontend now knows how to track this specific operation
   - Backend continues processing in background

7. **Frontend opens SSE connection → Backend**
   - Frontend opens Server-Sent Events connection to `/api/stream/{operation_id}`
   - This creates a real-time communication channel
   - Backend can now send updates to frontend

8. **Backend connects to MCP server → stdio transport**
   - Backend (acting as MCP client) connects to MCP server
   - Uses stdio transport (direct process communication)
   - Establishes MCP protocol connection

9. **Backend calls MCP tools → MCP server**
   - Calls `billing.create_invoice` tool with form data
   - MCP server receives the tool call request
   - Server validates input and processes the request

10. **MCP server processes request → Domain logic**
    - Server creates invoice in memory storage
    - Generates invoice ID and stores invoice data
    - Calls `billing.get_invoice` to retrieve created invoice
    - Returns invoice data to backend

11. **Backend receives response → MCP client**
    - Backend receives invoice data from MCP server
    - Parses the JSON response
    - Updates operation status to "completed"

12. **Backend updates progress → SSE stream**
    - Backend sends progress update via SSE
    - Includes all events: "received", "connecting-mcp", "invoice-created", "invoice-fetched"
    - Marks operation as "done" and includes final result

13. **Frontend receives updates → Real-time UI**
    - Frontend receives SSE events
    - Updates progress list in real-time
    - Shows user what's happening step by step

14. **Frontend displays result → User**
    - Shows final invoice data to user
    - Closes SSE connection
    - User sees complete invoice information

**Visual Aid:**
```
User → Frontend → Backend → MCP Server
 ↑                              ↓
 ←── SSE Stream ←── Progress ←──┘
```

---

## Part 3: Live Coding Demonstration (30 minutes)

### Demo 1: Setting Up the Project (5 minutes)

**Speaker Notes:**
"Let's start by setting up our development environment."

**Commands:**
```bash
# Clone and setup
git clone <repository>
cd mcp-app-starter
npm install

# Build components
npm run build:all
```

**Key Points:**
- Workspace configuration for monorepo
- TypeScript setup for all components
- Dependency management

### Demo 2: MCP Server Implementation (10 minutes)

**Speaker Notes:**
"Now let's build our MCP server step by step."

**Step 1: Basic Server Setup**
```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const mcpServer = new McpServer({
  name: "billing-mcp",
  version: "0.1.0"
});
```

**Step 2: Tool Registration**
```typescript
mcpServer.registerTool("billing.create_invoice", {
  description: "Create an invoice and return its id.",
  inputSchema: {
    amount: z.number().min(0),
    currency: z.string().length(3),
    customer_email: z.string().email(),
    idempotency_key: z.string()
  }
}, async ({ amount, currency, customer_email, idempotency_key }) => {
  // Implementation
});
```

**Step 3: Server Startup**
```typescript
async function main() {
  const transport = new StdioServerTransport();
  await mcpServer.connect(transport);
  console.log("MCP billing server is running...");
}

main().catch(console.error);
```

**Live Demo:**
- Show server starting up
- Demonstrate tool registration
- Test with MCP inspector tool

### Demo 3: Backend Integration (10 minutes)

**Speaker Notes:**
"Now let's build the backend that connects to our MCP server."

**Step 1: MCP Client Setup**
```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

export function getBillingClient(): Promise<Client> {
  const transport = new StdioClientTransport({
    command: "node",
    args: ["dist/index.js"],
    cwd: "../../servers/billing/"
  });
  
  const client = new Client({
    name: "billing-backend-client",
    version: "0.1.0"
  });
  
  return client.connect(transport);
}
```

**Step 2: API Endpoint**
```typescript
app.post("/api/invoices", async (req, res) => {
  const parsed = CreateInvoiceInput.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.flatten() });
  }
  
  const opId = nanoid();
  progress.set(opId, { done: false, events: ["received"] });
  
  // Async MCP operation...
  
  res.status(202).json({ opId });
});
```

**Step 3: SSE Implementation**
```typescript
app.get("/api/stream/:opId", (req, res) => {
  res.setHeader("Content-Type", "text/event-stream");
  
  const interval = setInterval(() => {
    const progress = progressStore.get(opId);
    res.write(`event: progress\ndata: ${JSON.stringify(progress)}\n\n`);
    
    if (progress.done) {
      res.write(`event: result\ndata: ${JSON.stringify(progress.result)}\n\n`);
      clearInterval(interval);
      res.end();
    }
  }, 400);
});
```

**Live Demo:**
- Start backend server
- Test API endpoint with curl
- Show SSE stream in action

### Demo 4: Frontend Implementation (5 minutes)

**Speaker Notes:**
"Finally, let's build the React frontend that ties everything together."

**Key Components:**
```typescript
// Form submission
async function onSubmit(e: React.FormEvent) {
  e.preventDefault();
  
  const res = await fetch(`${backendURL}/api/invoices`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ amount, currency, customer_email })
  });
  
  const data = await res.json();
  if (data.opId) setOpId(data.opId);
}

// SSE connection
useEffect(() => {
  if (!opId) return;
  
  const es = new EventSource(`${backendURL}/api/stream/${opId}`);
  
  es.addEventListener("progress", (event) => {
    const data = JSON.parse(event.data);
    setEvents(data.events);
  });
  
  es.addEventListener("result", (event) => {
    const data = JSON.parse(event.data);
    setResult(data);
    es.close();
  });
  
  return () => es.close();
}, [opId]);
```

**Live Demo:**
- Start frontend server
- Show complete application in action
- Demonstrate real-time progress updates

---

## Part 4: Hands-on Workshop (15 minutes)

### Workshop Exercise: Add a New Tool

**Speaker Notes:**
"Now it's your turn! Let's add a new tool to our MCP server."

**Exercise: Add `billing.update_invoice_status` Tool**

**Requirements:**
1. Add a new tool that updates invoice status
2. Accept `invoice_id` and `status` parameters
3. Return updated invoice information
4. Handle error cases (invoice not found)

**Step-by-Step Instructions:**

**Step 1: Add Tool to MCP Server**
```typescript
mcpServer.registerTool("billing.update_invoice_status", {
  description: "Update the status of an existing invoice.",
  inputSchema: {
    invoice_id: z.string().describe("Invoice ID to update"),
    status: z.enum(["draft", "sent", "paid", "cancelled"]).describe("New status")
  }
}, async ({ invoice_id, status }) => {
  const invoice = invoices.get(invoice_id);
  if (!invoice) {
    return {
      content: [
        {
          type: "text",
          text: JSON.stringify({ error: "INVOICE_NOT_FOUND" })
        }
      ]
    };
  }
  
  invoice.status = status;
  invoices.set(invoice_id, invoice);
  
  return {
    content: [
      {
        type: "text",
        text: JSON.stringify({
          invoice: { id: invoice_id, ...invoice }
        })
      }
    ]
  };
});
```

**Step 2: Add Backend Endpoint**
```typescript
app.post("/api/invoices/:id/status", async (req, res) => {
  const { id } = req.params;
  const { status } = req.body;
  
  const opId = nanoid();
  progress.set(opId, { done: false, events: ["received"] });
  
  (async () => {
    try {
      const client = await getBillingClient();
      const result = await client.request({
        method: "tools/call",
        params: {
          name: "billing.update_invoice_status",
          arguments: { invoice_id: id, status }
        }
      }, CallToolResultSchema);
      
      progress.set(opId, {
        done: true,
        events: ["received", "status-updated"],
        result: JSON.parse(result.content[0].text)
      });
    } catch (error) {
      progress.set(opId, {
        done: true,
        events: ["received", "error"],
        result: { error: error.message }
      });
    }
  })();
  
  res.status(202).json({ opId });
});
```

**Step 3: Add Frontend Component**
```typescript
const [selectedInvoice, setSelectedInvoice] = useState(null);
const [newStatus, setNewStatus] = useState("");

async function updateInvoiceStatus() {
  const res = await fetch(`${backendURL}/api/invoices/${selectedInvoice.id}/status`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status: newStatus })
  });
  
  const data = await res.json();
  if (data.opId) setOpId(data.opId);
}
```

**Workshop Goals:**
- Understand MCP tool registration
- Learn backend integration patterns
- Practice frontend state management
- Experience complete development cycle

---

## Part 5: Q&A and Discussion (10 minutes)

### Common Questions and Answers

**Q: Why use MCP instead of direct API calls?**
**A:** MCP provides standardization, better error handling, tool discovery, and a consistent interface across different AI systems.

**Q: Can MCP servers be deployed independently?**
**A:** Yes! MCP servers can be deployed as separate services, making them highly scalable and maintainable.

**Q: What transport mechanisms are supported?**
**A:** MCP supports stdio (for local processes), HTTP (for web services), and WebSocket (for real-time communication).

**Q: How do you handle authentication in MCP?**
**A:** Authentication can be implemented at the transport layer or within individual tools, depending on your security requirements.

**Q: Can MCP servers call other MCP servers?**
**A:** Yes! MCP servers can act as clients to other MCP servers, creating powerful distributed systems.

### Discussion Topics

**Best Practices:**
- Tool design principles
- Error handling strategies
- Performance optimization
- Security considerations

**Real-World Applications:**
- Enterprise integrations
- Development tooling
- Business process automation
- AI-powered applications

**Future of MCP:**
- Protocol evolution
- Community adoption
- Tool ecosystem growth
- Integration patterns

---

## Presentation Materials

### Slides Template

**Slide 1: Title Slide**
- MCP App Starter
- Building Modern AI Applications with Model Context Protocol
- [Your Name] - [Date]

**Slide 2: Agenda**
- Introduction to MCP
- Architecture Deep Dive
- Live Coding Demonstration
- Hands-on Workshop
- Q&A and Discussion

**Slide 3: Learning Objectives**
- Understand MCP Architecture
- Implement MCP Servers
- Build MCP Clients
- Design Full-Stack Applications
- Apply Best Practices

### Demo Environment Setup

**Prerequisites:**
- Node.js 20+ installed
- Git installed
- Code editor (VS Code recommended)
- Terminal/Command Prompt

**Setup Commands:**
```bash
# Clone repository
git clone <repository-url>
cd mcp-app-starter

# Install dependencies
npm install

# Build all components
npm run build:all

# Start development servers
./start.sh  # or start.bat on Windows
```

### Workshop Materials

**Handout: Quick Reference Guide**
- MCP tool registration syntax
- Client connection patterns
- SSE implementation
- Common error patterns

**Code Templates:**
- Basic MCP server template
- Client connection template
- Tool implementation template
- Frontend integration template

---

## Assessment and Follow-up

### Knowledge Check Questions

1. **What are the three main components of MCP architecture?**
   **Answer**: The three main components are:
   - **MCP Server**: Exposes tools and resources to clients (like our billing server)
   - **MCP Client**: Connects to servers and calls their tools (like our Express backend)
   - **Transport Layer**: Handles communication between client and server (stdio, HTTP, WebSocket)

2. **How does stdio transport work in MCP?**
   **Answer**: stdio transport uses direct process-to-process communication:
   - Client spawns the server as a child process
   - Communication happens through stdin (input) and stdout (output) streams
   - No network setup required - it's like talking face-to-face
   - Fast and reliable for local applications
   - Perfect for our demo where backend and MCP server run on same machine

3. **What is the purpose of input schemas in MCP tools?**
   **Answer**: Input schemas serve multiple purposes:
   - **Validation**: Ensure data is in correct format before processing
   - **Documentation**: Describe what each tool expects as input
   - **Type Safety**: Provide clear data types (string, number, email, etc.)
   - **Error Prevention**: Catch invalid data before it causes crashes
   - **Client Guidance**: Help clients understand how to call tools correctly
   - **Example**: Our billing.create_invoice tool expects amount (number), currency (3 chars), email (valid format)

4. **How does Server-Sent Events enable real-time updates?**
   **Answer**: SSE creates a one-way communication channel from server to client:
   - Client opens persistent connection to server endpoint
   - Server can send updates anytime without client asking
   - Updates stream in real-time (every 400ms in our case)
   - Client receives events and updates UI immediately
   - Works through firewalls and proxies (unlike WebSockets)
   - Automatic reconnection if connection drops
   - **Example**: User sees "connecting-mcp" → "invoice-created" → "invoice-fetched" in real-time

5. **What are the benefits of using MCP over direct API calls?**
   **Answer**: MCP provides several key advantages:
   - **Standardization**: Same protocol works across different AI systems
   - **Tool Discovery**: Clients can automatically discover available tools
   - **Better Error Handling**: Structured error responses with clear messages
   - **Type Safety**: Input schemas ensure data integrity
   - **Extensibility**: Easy to add new tools without breaking existing clients
   - **Reusability**: Same MCP server can work with different AI applications
   - **Documentation**: Tools are self-documenting with descriptions and schemas
   - **Security**: Better authentication and authorization patterns
   - **Maintenance**: Easier to maintain and update compared to custom APIs

### Follow-up Resources

**Documentation:**
- MCP Official Documentation
- TypeScript SDK Reference
- Community Examples
- Best Practices Guide

**Next Steps:**
- Build your own MCP server
- Explore existing MCP tools
- Contribute to the MCP ecosystem
- Join the MCP community

**Contact Information:**
- GitHub Repository
- Community Discord
- Documentation Website
- Support Channels

---

**Presentation Version:** 1.0  
**Last Updated:** September 18, 2025  
**Presenter:** [Your Name]  
**Audience:** Developers, Technical Leads, AI Enthusiasts
