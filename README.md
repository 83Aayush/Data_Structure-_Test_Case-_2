# 🛒 Inventory Management System (Python)

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](#-contributing)  

A simple **command-line Inventory Management System** written in Python.  
This project helps manage stock items using **SKU (Stock Keeping Unit)** numbers, perform **sales operations**, and check **zero-stock items**.  

It’s designed to be **beginner-friendly** for Python learners, while also covering important programming practices like **functions, loops, lists, and condition handling**.  

---

## ✨ Features

- 📦 **Add Inventory** – Input items with unique SKUs and quantities  
- 💰 **Process Sales** – Deduct stock when items are sold  
- ⚠️ **Handle Errors** – Detect insufficient stock or non-existing SKUs  
- 🔎 **Zero Stock Identification** – Find SKUs with 0 quantity  
- 📉 **Sale to Zero** – Sell an item until stock becomes zero  
- 📋 **Show Current Inventory** – View all items in real time  
- 🖥 **Menu-Driven Interface** – Easy to use CLI navigation  

---

📊 Sample Workflows
✅ Normal Sale

Sell items that are in stock.

Inventory updates automatically.

⚠️ Insufficient Stock

If you try to sell more than available, program warns you.

❌ Non-Existing SKU

If SKU doesn’t exist, program notifies user.

🟢 Zero Stock

Easily check which SKUs are out of stock.

---

🎯 Future Enhancements

🔗 Database Integration (SQLite/MySQL) for persistent storage

🌐 Web-based UI (Flask/Django) or Desktop GUI (Tkinter/PyQt)

📈 Sales & Inventory Reports (CSV/PDF export)

👥 Multi-user role-based access

