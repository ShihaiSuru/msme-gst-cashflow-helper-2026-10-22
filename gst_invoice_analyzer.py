#!/usr/bin/env python3
"""
MSME GST Cashflow Helper — Starter Script
=========================================

A practical demo for Indian MSMEs:
- Loads sample GST invoices
- Performs basic compliance checks
- Calculates totals and estimates short-term cash-flow impact

Run: python gst_invoice_analyzer.py
"""

from datetime import datetime, timedelta
from typing import List, Dict

# Sample GST invoices (replace with real data from Excel/CSV/OCR)
SAMPLE_INVOICES: List[Dict] = [
    {
        "invoice_no": "INV-2026-001",
        "date": "2026-10-15",
        "buyer": "Sharma Traders",
        "hsn": "9403",
        "taxable_value": 50000,
        "gst_rate": 18,
        "due_days": 30,
        "payment_status": "pending"
    },
    {
        "invoice_no": "INV-2026-002",
        "date": "2026-10-18",
        "buyer": "Patel Electronics",
        "hsn": "8517",
        "taxable_value": 120000,
        "gst_rate": 18,
        "due_days": 15,
        "payment_status": "pending"
    },
    {
        "invoice_no": "INV-2026-003",
        "date": "2026-10-10",
        "buyer": "Mehta Textiles",
        "hsn": "5208",
        "taxable_value": 75000,
        "gst_rate": 5,
        "due_days": 45,
        "payment_status": "partial"
    }
]

VALID_GST_RATES = {0, 5, 12, 18, 28}

def validate_invoice(inv: Dict) -> List[str]:
    """Basic GST compliance checks."""
    issues = []
    if inv["gst_rate"] not in VALID_GST_RATES:
        issues.append(f"Unusual GST rate: {inv['gst_rate']}%")
    if inv["taxable_value"] <= 0:
        issues.append("Taxable value must be positive")
    if not inv.get("hsn"):
        issues.append("Missing HSN code")
    return issues

def calculate_gst(inv: Dict) -> Dict:
    """Compute GST amount and invoice total."""
    gst_amount = round(inv["taxable_value"] * inv["gst_rate"] / 100, 2)
    total = inv["taxable_value"] + gst_amount
    return {
        "gst_amount": gst_amount,
        "total": total
    }

def estimate_cashflow_gap(invoices: List[Dict], look_ahead_days: int = 30) -> Dict:
    """Estimate short-term receivables and GST liability."""
    today = datetime.now()
    receivables = 0.0
    gst_liability = 0.0
    for inv in invoices:
        if inv["payment_status"] == "pending":
            due_date = datetime.strptime(inv["date"], "%Y-%m-%d") + timedelta(days=inv["due_days"])
            if (due_date - today).days <= look_ahead_days:
                calc = calculate_gst(inv)
                receivables += calc["total"]
                gst_liability += calc["gst_amount"]
    return {
        "expected_receivables_30d": round(receivables, 2),
        "gst_liability_on_those": round(gst_liability, 2),
        "net_cash_impact": round(receivables - gst_liability, 2)
    }

def main():
    print("=== MSME GST Cashflow Helper ===\n")
    print("Analyzing sample invoices...\n")

    for inv in SAMPLE_INVOICES:
        issues = validate_invoice(inv)
        calc = calculate_gst(inv)
        print(f"Invoice: {inv['invoice_no']} | Buyer: {inv['buyer']}")
        print(f"  Taxable: ₹{inv['taxable_value']:,} | GST @{inv['gst_rate']}%: ₹{calc['gst_amount']:,} | Total: ₹{calc['total']:,}")
        if issues:
            print(f"  ⚠️ Issues: {', '.join(issues)}")
        else:
            print("  ✓ Basic checks passed")
        print()

    gap = estimate_cashflow_gap(SAMPLE_INVOICES)
    print("--- 30-Day Cash-Flow Estimate ---")
    print(f"Expected receivables: ₹{gap['expected_receivables_30d']:,}")
    print(f"GST liability on those: ₹{gap['gst_liability_on_those']:,}")
    print(f"Net cash impact: ₹{gap['net_cash_impact']:,}")
    print("\nTip: Replace SAMPLE_INVOICES with real data and extend with UPI reconciliation.")

if __name__ == "__main__":
    main()
