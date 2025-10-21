import express from "express";
import cors from "cors";
import { nanoid } from "nanoid";
import { CreateInvoiceInput } from "./schemas.js";
import { getBillingClient } from "./mcpClient.js";
import { CallToolResultSchema } from "@modelcontextprotocol/sdk/types.js";

const app = express();
app.use(cors());
app.use(express.json());

// In-memory operation progress store (demo)
const progress = new Map<string, { done: boolean; events: string[]; result?: any }>();

app.post("/api/invoices", async (req, res) => {
  const parsed = CreateInvoiceInput.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.flatten() });
  }
  
  const opId = nanoid();
  progress.set(opId, { done: false, events: ["received"] });
  
  // Kick off async tool call (no queue here for brevity)
  (async () => {
    try {
      const client = await getBillingClient();
      progress.get(opId)!.events.push("connecting-mcp");
      
      const idempotency_key = opId; // demo only
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
      
      progress.get(opId)!.events.push("invoice-created");
      
      if (!createResp.content || createResp.content.length === 0) {
        throw new Error("MCP error creating invoice");
      }
      
      const createResult = JSON.parse((createResp.content[0] as any).text);
      const invId = createResult.invoice_id;
      
      const getResp = await client.request({
        method: "tools/call",
        params: {
          name: "billing.get_invoice",
          arguments: {
            invoice_id: invId
          }
        }
      }, CallToolResultSchema);
      
      progress.get(opId)!.events.push("invoice-fetched");
      
      progress.set(opId, {
        done: true,
        events: Array.from(progress.get(opId)!.events),
        result: getResp.content ? JSON.parse((getResp.content[0] as any).text) : null
      });
    } catch (e: any) {
      progress.set(opId, {
        done: true,
        events: Array.from(progress.get(opId)!.events),
        result: { error: e?.message || "unknown" }
      });
    }
  })();
  
  res.status(202).json({ opId });
});

// Simple SSE stream of progress
app.get("/api/stream/:opId", (req, res) => {
  res.setHeader("Content-Type", "text/event-stream");
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Connection", "keep-alive");
  
  const { opId } = req.params;
  
  res.write(`event: ping\ndata: ${JSON.stringify({ t: Date.now() })}\n\n`);
  
  const interval = setInterval(() => {
    const p = progress.get(opId);
    if (!p) return;
    
    res.write(`event: progress\ndata: ${JSON.stringify({ events: p.events, done: p.done })}\n\n`);
    
    if (p.done) {
      res.write(`event: result\ndata: ${JSON.stringify(p.result)}\n\n`);
      clearInterval(interval);
      res.end();
    }
  }, 400);
  
  req.on("close", () => clearInterval(interval));
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`backend listening on :${PORT}`));
