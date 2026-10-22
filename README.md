# MSME GST Cashflow Helper

**AI-assisted GST invoice analyzer and short-term cash-flow estimator for Indian MSMEs.**

## Problem

Indian Micro, Small and Medium Enterprises (MSMEs) often struggle with:
- Manual extraction of data from GST invoices
- Basic compliance checks (HSN codes, GST rates, place of supply)
- Matching invoices against UPI / bank receipts
- Early visibility into working-capital gaps

These frictions lead to delayed GST filings, cash-flow surprises, and higher borrowing costs.

## Solution

This repository provides a lightweight, practical starting point:

1. Parse structured invoice data (JSON or CSV)
2. Run basic GST compliance checks
3. Estimate the near-term cash-flow impact (receivables vs. GST liability)
4. Flag potential mismatches for human review

Designed as a demo / starter kit that can later be connected to real OCR, UPI statement parsers, or accounting APIs.

## Features (Starter)

- Load sample GST invoices
- Validate common GST rate bands (0%, 5%, 12%, 18%, 28%)
- Calculate total taxable value, GST amount, and invoice total
- Simple cash-flow gap estimator (invoices due within N days vs. expected inflows)
- Clear console output for quick review

## Usage

```bash
python gst_invoice_analyzer.py
```

The script uses built-in sample data so you can run it immediately. Replace the sample data with your own invoice records (from Excel, accounting software export, or OCR output) to test real scenarios.

## Roadmap Ideas

- Add OCR integration (Tesseract / cloud vision) for scanned invoices
- UPI / bank statement reconciliation module
- Export to GST portal-friendly formats
- Simple Streamlit / Gradio UI for non-technical users
- Integration with open banking or accounting APIs

## License

MIT — free for personal and commercial use by MSMEs and developers.

---

Built to help Indian MSMEs manage cash flow with practical AI and data tools.
