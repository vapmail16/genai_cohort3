import { useEffect, useMemo, useState } from "react";

export default function App() {
  const [amount, setAmount] = useState(42);
  const [currency, setCurrency] = useState("USD");
  const [email, setEmail] = useState("demo@example.com");
  const [opId, setOpId] = useState<string | null>(null);
  const [events, setEvents] = useState<string[]>([]);
  const [result, setResult] = useState<any>(null);

  const backendURL = useMemo(() => 
    (import.meta.env.VITE_BACKEND_URL || "http://localhost:3001"), 
    []
  );

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

  return (
    <div style={{ maxWidth: 720, margin: "2rem auto", fontFamily: "ui-sans-serif, system-ui" }}>
      <h1>MCP Billing Demo</h1>
      <p>Creates an invoice via an MCP tool and streams progress.</p>

      <form onSubmit={onSubmit} style={{ display: "grid", gap: 12 }}>
        <label>
          Amount
          <input 
            type="number" 
            value={amount} 
            onChange={e => setAmount(Number(e.target.value))} 
          />
        </label>
        
        <label>
          Currency
          <input 
            value={currency} 
            onChange={e => setCurrency(e.target.value.toUpperCase())} 
            maxLength={3} 
          />
        </label>
        
        <label>
          Email
          <input 
            value={email} 
            onChange={e => setEmail(e.target.value)} 
          />
        </label>
        
        <button type="submit">Create invoice</button>
      </form>

      {events.length > 0 && (
        <div style={{ marginTop: 24 }}>
          <h3>Progress</h3>
          <ol>
            {events.map((ev, i) => <li key={i}>{ev}</li>)}
          </ol>
        </div>
      )}

      {result && (
        <div style={{ marginTop: 24 }}>
          <h3>Result</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
