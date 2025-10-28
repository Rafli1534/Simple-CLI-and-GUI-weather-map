# 🌦️ Simple CLI and GUI Weather Map

A Python application for retrieving current weather and 5-day forecasts using the OpenWeather API. It supports both **Command Line Interface (CLI)** and **Graphical User Interface (GUI)** modes, with multilingual output in English, Russian, and Ukrainian.

---

## 🚀 Features

- 🌍 Multilingual output: English, Russian, Ukrainian
- 📏 Unit selection: Metric (°C), Imperial (°F), Standard (Kelvin)
- 🖥️ GUI mode with styled interface
- 🧪 CLI mode with interactive prompts
- 📡 Fetches current weather and 5-day forecast
- ✅ Error handling and formatted output
- 🔑 API key management via `appid.txt`

---

## 📁 Project Structure & File Overview

### `general.py`
**Main entry point** of the application.  
- Prompts user to choose between CLI and GUI.
- In CLI mode: guides through input of APPID, city, units, language, and mode.
- Delegates to `run_current()` and `run_forecast()` from `weather_api.py`.

### `gui.py`
**Graphical interface using Tkinter.**  
- Builds a two-panel GUI: left for input, right for output.
- Handles user input via radio buttons and text fields.
- Calls API functions and formats output using `language.py`.
- Includes a splash screen (`choose_mode_gui()`) for mode selection.

### `language.py`
**Handles multilingual output formatting.**  
- Defines `english()`, `russian()`, and `ukrainian()` functions to print weather data.
- Includes `wind_direction()` to convert wind degrees to compass directions.
- Provides `print_forecast_by_lang()` to format forecast output per language.

### `utils.py`
**CLI helpers and APPID management.**  
- `hello()` — prints welcome message with OpenWeather link.
- `appid()` — prompts user for valid 32-character API key.
- `save_appid()` / `load_appid()` — manage API key persistence.
- `choose_units()`, `choose_language()`, `choose_mode_cli()` — interactive CLI selectors.
- `get_city()` — prompts and normalizes city name.

### `weather_api.py`
**Handles API interaction and data parsing.**  
- `build_weather_request()` — constructs URL and parameters for OpenWeather.
- `fetch_weather()` — performs HTTP GET request.
- `error()` — checks response status and prints error if needed.
- `parse_weather()` — extracts current weather data.
- `parse_forecast()` — aggregates 5-day forecast into daily summaries.
- `run_current()` / `run_forecast()` — high-level functions to fetch and display data.
- `do_current()` / `do_forecast()` — alternative CLI-style output functions.

### `appid.txt`
Stores the user's OpenWeather API key.  
Used for persistent access without re-entering the key each time.

### `requirements.txt`
Lists Python dependencies.  
Currently includes:
```
requests
```

---

## 🖥️ How to Run

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

## 📌 Input Guidelines

- **City**: Use real city names (e.g. `Kyiv`, `London`, `New York`)
- **Units**:
  - `metric` → Celsius
  - `imperial` → Fahrenheit
  - `standard` → Kelvin
- **Language**:
  - `en` → English
  - `ru` → Russian
  - `ua` → Ukrainian

---

## 🛠️ Technologies Used

- Python 3.8+
- `requests` — for HTTP requests
- `tkinter` — for GUI (built-in)

---

## 📄 License

This project is open-source and free to use. Feel free to fork, modify, and share!

---

## ✨ Author

Created by **null** — a developer who values clean code, visual clarity, and a touch of personality in every project.