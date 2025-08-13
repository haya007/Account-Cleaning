# Accounting Cleanup Wizard (Odoo)

## Overview
The **Accounting Cleanup Wizard** is a simple Odoo utility module that allows administrators to **bulk delete** accounting data such as:
- Customer invoices (`account.move` with `move_type = out_invoice`)
- Related journal entries
- Related payments

It is especially useful in **testing or development environments** where you need to quickly reset accounting data for a clean start.

⚠ **Important:**  
This tool is destructive — **once deleted, data cannot be recovered**. Use it only in development or testing databases, **never on production**.

---

## Features
- Deletes **all customer invoices**.
- Deletes related **journal entries**.
- Deletes related **customer payments**.
- Automatically moves records to **Draft** state before deletion to avoid restrictions.
- Accessible from **Accounting → Configuration → Accounting Cleanup**.

---

## Installation
1. Copy 'accounting_cleanup' module into your Odoo `addons` directory.
2. Update the app list and install.
