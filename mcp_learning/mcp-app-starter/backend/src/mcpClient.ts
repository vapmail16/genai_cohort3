import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

let clientPromise: Promise<Client> | null = null;

export function getBillingClient(): Promise<Client> {
  if (clientPromise) return clientPromise;
  
  clientPromise = new Promise(async (resolve, reject) => {
    try {
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
      resolve(client);
    } catch (e) {
      reject(e);
    }
  });
  
  return clientPromise;
}
