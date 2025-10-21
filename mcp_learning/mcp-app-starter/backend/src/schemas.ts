import { z } from "zod";

export const CreateInvoiceInput = z.object({
  amount: z.number().nonnegative(),
  currency: z.string().length(3),
  customer_email: z.string().email(),
});

export type CreateInvoiceInput = z.infer<typeof CreateInvoiceInput>;
