# ⚙️ Installation Guide — Simple CLI and GUI Weather Map

This guide will walk you through setting up and running the project locally.

---

## 🐍 Step 1: Install Python

Make sure you have **Python 3.8 or higher** installed.  
You can download it from the official site: [https://www.python.org/downloads](https://www.python.org/downloads)

To check your version:

```bash
python --version
```

---

## 🧪 Step 2: Create a Virtual Environment (venv)

A **virtual environment** is an isolated Python environment that keeps your project dependencies separate from your system-wide Python installation.

### 🔒 Why use venv?

- Prevents conflicts between different Python projects
- Keeps your system clean
- Ensures reproducibility
- **Important:** Never share or upload your `venv/` folder — it contains machine-specific paths and binaries.

### 🛠️ How to create venv

```bash
python -m venv venv
```

This will create a folder named `venv/` in your project directory.

### ▶️ How to activate venv

#### On Windows:

```bash
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
source venv/bin/activate
```

Once activated, your terminal will show `(venv)` at the beginning of the prompt.

---

## 📦 Step 3: Install Dependencies

Install required Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install:

- `requests` — for making HTTP requests to OpenWeather API

---

## 🔑 Step 4: Get Your OpenWeather API Key

1. Go to [https://home.openweathermap.org/users/sign_in](https://home.openweathermap.org/users/sign_in)
2. Sign in or create an account
3. Copy your **API key (APPID)**

You can either:

- Save it in a file named `appid.txt`  
  *(the app will read it automatically)*

**OR**

- Enter it manually when prompted in CLI or GUI

---

## 🚀 Step 5: Run the Application

### GUI Mode

```bash
python general.py
# Select "GUI" in the popup window
```

### CLI Mode

```bash
python general.py
# Select "CLI" in the popup window
# Follow the interactive prompts
```

---

## 🧹 Optional: Deactivate venv

When you're done working:

```bash
deactivate
```

---

## 🛑 Reminder: Do NOT upload `venv/` to GitHub

Add this line to your `.gitignore` file:

```
venv/
```

This ensures your virtual environment is excluded from version control.

---

## ✅ You're Ready!

Enjoy using Simple CLI and GUI Weather Map!  
If you run into issues, feel free to open an issue or reach out.