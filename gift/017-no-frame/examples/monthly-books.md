# Monthly books — one job, five stages, you at every stop

You are helping me close my books for one month. Work one stage at a time.
Each stage reads only the output of the stage before it, writes its own
output into its own folder, shows it to me and STOPS. The next stage starts
only after my word, and only from what I approved.

## Fill in once

- My business: <one sentence: what we sell, to whom>
- Currency: <EUR / USD / ...>
- Tax name on invoices: <VAT / sales tax / none>
- The month to close: <YYYY-MM>
- Documents for the month: <path> (supplier invoices, receipts, photos)
- Bank statement for the month: <path to the CSV export>
- My sales invoices: <path> (this month's, and older ones still unpaid)
- Expense categories I use: <e.g. rent, software, travel, materials, fees>
- My accountant: <name> (I add the address when I send)

If anything above is empty, ask me for it before Stage 1. Never guess it.

## The folders (create them once, next to this file)

```
books/<YYYY-MM>/
  01-collect/   documents.md
  02-match/     matched.md
  03-gaps/      gaps.md
  04-owed/      owed.md, reminders/
  05-handoff/   summary.md, email-to-accountant.md
```

A stage writes only into its own folder. Redoing a stage rewrites its
folder; every stage after it is then out of date and is run again.
From Stage 2 on, each file ends with `## Carried forward`: the next stage
copies it whole and adds what its steps say. When I answer at a STOP, you
write my answer into that stage's file first, then wait for my go.

## Never, in every stage

- Never pay anything, send any email, or file anything with the tax office.
- Never give tax advice; my country's rules are my accountant's.
- Never invent a document, an amount or a date. If you cannot read it, say so.
- Never mark something matched or paid by guess.
- A stage reads only the stage right before it; what a later stage needs
  is carried forward in that file, never fetched from further back.

## Stage 1 · Collect

Reads: the documents folder from "Fill in once".
Writes: `01-collect/documents.md`.
1. For each file write a row: supplier, date, due date (if printed),
   invoice number, total, tax, file name. Done when: every file has a row,
   or a line saying why it could not be read.
2. Mark rows that look like duplicates (same supplier, number and amount).
   Done when: each pair is named; nothing is deleted; the copy is left out
   of the totals.
Stage done when: one row per document, unreadable ones listed apart, totals added.
STOP: I give you the receipts you cannot see or read; you add them as rows
marked "from me", and I say go.

## Stage 2 · Match the bank

Reads: `01-collect/documents.md` (as I approved it) and the bank statement.
Writes: `02-match/matched.md`.
1. For every bank line, find its document: same amount, paid on or after
   the document's date (a bill on terms can be paid weeks later), and the
   supplier's name or invoice number in the bank text. Money received is
   marked "income" (Stage 4 matches it). The bank's own fee needs no
   document: the statement is its record, category bank fees, no tax.
   Done when: every bank line is matched (with its document), income, or open.
2. Give every paid expense one of my categories. Done when: every expense
   has a category, or is marked "unsure" with why.
3. List every document no bank line paid (a duplicate copy is not a bill).
   Done when: each shows supplier, total, tax and due date.
4. Carry forward: the opening and closing balance, the income lines, the
   expense totals by category, the tax on the documents (paid, and unpaid
   apart), and the lines I call personal. Done when: opening + income -
   expenses - personal - unsure = closing.
Stage done when: no bank line is unmarked; every "unsure" says what you need.
STOP: I decide each unsure line (business or personal, which category) and say go.

## Stage 3 · Find the gaps

Reads: `02-match/matched.md`.
Writes: `03-gaps/gaps.md`.
1. List every business payment with no document (not the bank's fee):
   a receipt I still need. Done when: each shows date, amount and who was paid.
2. List every document with no payment: a bill still open.
   Done when: each shows supplier, amount and due date if printed.
3. Carry forward `matched.md`'s block. Done when: it equals that block.
Stage done when: both lists are complete, with their totals, and the carry is there.
STOP: I mark which receipts to chase and which bills to pay, and say go.

## Stage 4 · Who owes what

Reads: `03-gaps/gaps.md` (with its carried money received and totals) and my
sales invoices from "Fill in once".
Writes: `04-owed/owed.md` and one draft per overdue customer in `04-owed/reminders/`.
1. Mark each sales invoice paid (its income line) or open; an open one is
   overdue if its due date is before today (write today's date at the top).
   Done when: every sales invoice is paid, open or overdue, and every income
   line has its invoice.
2. For each overdue invoice, draft a short, polite reminder: number, amount,
   due date, how to pay. Done when: one draft per overdue invoice, in my
   tone, nothing sent.
3. Carry forward `gaps.md`'s block, plus its two lists as I marked them, the
   money owed to me and the tax on my sales invoices dated in the month.
   Done when: the copied part equals `gaps.md`.
Stage done when: the money owed to me is listed with its total; every overdue
customer has a draft; the carry is there.
STOP: I edit and send the reminders myself, pay the bills I chose, and say go.

## Stage 5 · Hand-off

Reads: `04-owed/owed.md`, with everything carried in it.
Writes: `05-handoff/summary.md` and `05-handoff/email-to-accountant.md`.
1. The month's summary: income, expenses by category, personal, tax
   charged (my invoices dated in the month) and tax paid (documents dated
   in the month), open items. Done when: every number comes from the stage
   before, nothing new.
2. A short email to my accountant with the summary and the folder.
   Done when: it names what is still open; nothing is sent.
Stage done when: opening + income - expenses - personal = closing, and
every open item is named.
STOP: I check it and send it myself.

## Month done when

- Every document has a row, and every bank line is matched or explained.
- Every open receipt, bill and overdue customer is on a list I approved.
- The summary matches the bank, and the email waits for me to send it.
