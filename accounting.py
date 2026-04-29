from collections import defaultdict
from dataclasses import dataclass
from typing import List


# Fixed chart of accounts
ACCOUNTS = {
    "1000": "Cash",
    "1100": "Accounts Receivable",
    "2000": "Accounts Payable",
    "4000": "Revenue",
    "5000": "Expense",
}


@dataclass
class Posting:
    account: str
    amount: float
    partner: str = ""


def create_sale(amount: float, partner: str) -> List[Posting]:
    return [
        Posting("1100", amount, partner),   # AR
        Posting("4000", amount, partner),  # Revenue
    ]


def receive_payment(amount: float, partner: str):
    return [
        Posting("1000", amount, partner),   # Cash ↑
        Posting("1100", -amount, partner),  # AR ↓
    ]


def create_expense(amount: float, partner: str):
    return [
        Posting("5000", amount, partner),   # Expense
        Posting("2000", amount, partner),  # AP
    ]


def pay_vendor(amount: float, partner: str):
    return [
        Posting("2000", -amount, partner),   # AP ↓
        Posting("1000", -amount, partner),  # Cash ↓
    ]


def calculate_stats(postings: List[Posting]):
    stats = defaultdict()
    stats["revenue"] =sum(p.amount for p in postings if p.account == "4000")
    stats['expenses'] = sum(p.amount for p in postings if p.account == "5000")
    stats['profit'] = stats['revenue'] - stats['expenses']
    stats['cash'] = [p.amount for p in postings if p.account == '1000']
    stats['pay'] = sum(p.amount for p in postings if p.account == '2000')
    stats['receive'] = sum(p.amount for p in postings if p.account == '1100')
    return stats


def partner_ledger(postings: List[Posting]):
    ledger = defaultdict(int)

    for p in postings:
        if not p.partner:
            continue

        if p.account == "1100":  # AR
            ledger[p.partner] += p.amount

        elif p.account == "2000":  # AP
            ledger[p.partner] -= p.amount

    return ledger