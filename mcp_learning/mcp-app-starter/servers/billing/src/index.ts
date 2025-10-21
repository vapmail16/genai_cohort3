import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// In-memory invoice store for demo purposes
const invoices = new Map<string, { 
  amount: number; 
  currency: string; 
  customer_email: string; 
  status: string 
}>();

const mcpServer = new McpServer({
  name: "billing-mcp",
  version: "0.1.0"
});

// Tool to create an invoice
mcpServer.registerTool("billing.create_invoice", {
  description: "Create an invoice and return its id.",
  inputSchema: {
    amount: z.number().min(0).describe("Invoice amount"),
    currency: z.string().length(3).describe("Currency code (3 letters)"),
    customer_email: z.string().email().describe("Customer email address"),
    idempotency_key: z.string().describe("Unique key for idempotency")
  }
}, async ({ amount, currency, customer_email, idempotency_key }) => {
  // Idempotency: reuse existing invoice if same key is seen
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
});

// Tool to get an invoice
mcpServer.registerTool("billing.get_invoice", {
  description: "Fetch an invoice by id (idempotency key).",
  inputSchema: {
    invoice_id: z.string().describe("Invoice ID to fetch")
  }
}, async ({ invoice_id }) => {
  const inv = invoices.get(invoice_id);
  
  if (!inv) {
    return {
      content: [
        {
          type: "text",
          text: JSON.stringify({ error: "NOT_FOUND" })
        }
      ]
    };
  }
  
  return {
    content: [
      {
        type: "text",
        text: JSON.stringify({
          invoice: {
            id: invoice_id,
            ...inv
          }
        })
      }
    ]
  };
});

async function main() {
  const transport = new StdioServerTransport();
  await mcpServer.connect(transport);
  console.log("MCP billing server is running...");
}

main().catch((error) => {
  console.error("Server error:", error);
  process.exit(1);
});
