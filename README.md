# 🧠 Cortex_CLI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange?style=for-the-badge)
![AI Agent](https://img.shields.io/badge/AI-Agent-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

### 🚀 Intelligent Command-Line AI Agent

*Memory • Tool Calling • Structured Output • Error Handling*

</div>

---

## 🌟 Overview

**Cortex_CLI** is a modular AI Agent built using **Python** and **Google Gemini**. It demonstrates the core building blocks of modern AI agents, including:

* 🧠 Conversational Memory
* 🛠️ Tool Calling
* 📄 Structured JSON Extraction
* ⚡ Error Handling
* 🤖 Intelligent Response Generation

This project was developed to understand and implement real-world AI Agent workflows.

---

## ✨ Features

### 💬 AI Chat

Interact naturally with Gemini-powered conversational AI.

### 🧠 Memory System

Stores the last 5 interactions and provides contextual responses.

### 🛠️ Tool Calling

#### Calculator Tool

```text
calculate  39093899*3298408
```

Output:

```text
128947629212792
```

#### Task Manager Tool

```text
/task add Complete Internship Report

/task list

/task delete 1
```

---

### 📄 Structured Output Extraction

Input:

```text
/extract NIKHIL is 21 and lives in surat
```

Output:

```json
{
    "name": "NIKHIL",
    "age": 21,
    "city": "Surat"
}
```

---

### ⚡ Robust Error Handling

* Invalid API Keys
* Invalid Mathematical Expressions
* Invalid Task Operations
* Unexpected Runtime Errors

---

## 🏗️ Architecture

```text
                 User Input
                      │
                      ▼
               ┌────────────┐
               │ Cortex_CLI │
               └─────┬──────┘
                     │
     ┌───────────────┼───────────────┐
     │               │               │
     ▼               ▼               ▼

 Calculator      Memory       JSON Extractor
    Tool         Handler          Mode

     │               │
     └───────┬───────┘
             ▼

        Gemini API
             │
             ▼

       Final Response
```

---

## 📂 Project Structure

```text
Cortex_CLI/
│
├── agent/
│   ├── agent.py
│   └── memory.py
│
├── config/
│   └── llm.py
│
├── modes/
│   └── extractor.py
│
├── tools/
│   ├── calculator.py
│   └── task_manager.py
│
├── data/
│   └── tasks.txt
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/NikDev345/Cortex_CLI.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run

```bash
python main.py
```

---

## 🎯 Example Usage

### General Chat

```text
What is Artificial Intelligence?
```

### Memory

```text
My name is Nikhil

What is my name?
```

### Calculator

```text
calculate (50+10)*5
```

### Task Management

```text
/ task add Complete Project Documentation

/ task list
```

### Structured JSON Output

```text
/ extract Sarah is 28 and lives in Delhi
```

---

## 🛠️ Technologies Used

* Python
* Google Gemini API
* python-dotenv
* JSON
* File Handling
* AST (Safe Expression Evaluation)

---

## 🎓 Key Concepts Demonstrated

✅ AI Agent Architecture

✅ Tool Calling

✅ Memory Management

✅ Prompt Engineering

✅ Structured Outputs

✅ Error Handling

✅ Modular Design

---

## 🔮 Future Improvements

* Weather Tool
* Web Search Tool
* File Reader Tool
* Long-Term Memory
* Database Integration
* Streamlit Web App
* Multi-Agent Collaboration

---

<div align="center">

### ⭐ Star this repository if you found it useful!

**Built with Python, Gemini, and Curiosity.**

</div>
