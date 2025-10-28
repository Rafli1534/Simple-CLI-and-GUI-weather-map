import tkinter as tk
from tkinter import ttk
import sys
from io import StringIO
import traceback
from project.language import print_weather_by_lang
from project.weather_api import (
    build_weather_request,
    fetch_weather,
    error,
    parse_weather,
    parse_forecast,
    
    )


class WeatherAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Informer OpenWeather")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f4fa")

        # Переменные
        self.api_key_var = tk.StringVar()
        self.city_var = tk.StringVar()
        self.unit_var = tk.StringVar(value="metric")
        self.lang_var = tk.StringVar(value="en")
        self.mode_var = tk.StringVar(value="current")

        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg="#f4f4fa")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Левая панель — ввод
        left_frame = tk.Frame(main_frame, bg="#f4f4fa")
        left_frame.pack(side="left", fill="y", padx=5, pady=5)

        # Правая панель — вывод
        right_frame = tk.Frame(main_frame, bg="#f4f4fa")
        right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        # API Key
        tk.Label(left_frame, text="🔑 APPID:", bg="#f4f4fa").pack(anchor="w", pady=(0, 2))
        tk.Entry(left_frame, textvariable=self.api_key_var, width=30).pack(pady=(0, 10))

        # City
        tk.Label(left_frame, text="🏙️ City:", bg="#f4f4fa").pack(anchor="w", pady=(0, 2))
        tk.Entry(left_frame, textvariable=self.city_var, width=30).pack(pady=(0, 10))

        # Units
        tk.Label(left_frame, text="📏 Units:", bg="#f4f4fa").pack(anchor="w")
        for text, val in [("Metric (°C, m/s)", "metric"), ("Standard (K, m/s)", "standard"), ("Imperial (°F, mph)", "imperial")]:
            tk.Radiobutton(left_frame, text=text, variable=self.unit_var, value=val, bg="#f4f4fa").pack(anchor="w")

        # Language
        tk.Label(left_frame, text="🗣️ Language:", bg="#f4f4fa", pady=5).pack(anchor="w")
        for text, val in [("English", "en"), ("Russian", "ru"), ("Ukrainian", "ua")]:
            tk.Radiobutton(left_frame, text=text, variable=self.lang_var, value=val, bg="#f4f4fa").pack(anchor="w")

        # Mode
        tk.Label(left_frame, text="🌦️ Mode:", bg="#f4f4fa", pady=5).pack(anchor="w")
        for text, val in [("Current weather", "current"), ("Forecast", "forecast"), ("Both", "both")]:
            tk.Radiobutton(left_frame, text=text, variable=self.mode_var, value=val, bg="#f4f4fa").pack(anchor="w")

        # Button
        tk.Button(left_frame, text="📡 Show weather", command=self.get_weather, bg="#4a90e2", fg="white").pack(pady=10)

        # Output Text Field
        tk.Label(right_frame, text="📋 Result:", bg="#f4f4fa").pack(anchor="w")
        self.text_out = tk.Text(right_frame, wrap="word", font=("Consolas", 11), bg="#ffffff", fg="#333333")
        self.text_out.pack(fill="both", expand=True)
        scrollbar = tk.Scrollbar(right_frame, command=self.text_out.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_out.config(yscrollcommand=scrollbar.set)

    def show_result(self, text):
        self.text_out.config(state="normal")
        self.text_out.delete(1.0, tk.END)
        self.text_out.insert(tk.END, text)
        self.text_out.config(state="disabled")

    def get_weather(self):
        appid = self.api_key_var.get().strip()
        city = self.city_var.get().strip()
        units = self.unit_var.get()
        lang = self.lang_var.get()
        mode = self.mode_var.get()

        if not appid:
            self.show_result("⚠️ Please enter your OpenWeather APPID.")
            return
        if not city:
            self.show_result("⚠️ Please enter a city name.")
            return

        def format_weather_by_lang(city, data, unit, lang) -> str:
            buffer = StringIO()
            sys_stdout = sys.stdout
            sys.stdout = buffer
            try:
                print_weather_by_lang(city, data, unit, lang)
            finally:
                sys.stdout = sys_stdout
            return buffer.getvalue()

        def format_forecast_by_lang(forecast: dict, lang: str = 'en') -> str:
            header = {'ru': 'Прогноз:', 'ua': 'Прогноз:', 'en': 'Forecast:'}.get(lang, 'Forecast:')
            lines = [f"\n{header}"]
            for day, info in sorted(forecast.items()):
                min_t = info.get('min')
                max_t = info.get('max')
                desc = info.get('desc') or ''
                lines.append(f"{day}: {min_t}..{max_t}, {desc}")
            return "\n".join(lines)

        result = ""

        try:
            if mode == "current":
                url, params = build_weather_request(appid, mode="current", city=city, units=units, lang=lang)
                resp = fetch_weather(url, params)
                if error(resp):
                    data = parse_weather(resp)
                    result = format_weather_by_lang(city.title(), data, units, lang)

            elif mode == "forecast":
                url, params = build_weather_request(appid, mode="forecast", city=city, units=units, lang=lang)
                resp = fetch_weather(url, params)
                if error(resp):
                    forecast = parse_forecast(resp)
                    result = format_forecast_by_lang(forecast, lang)

            elif mode == "both":
                result = ""

                url, params = build_weather_request(appid, mode="current", city=city, units=units, lang=lang)
                resp = fetch_weather(url, params)
                if error(resp):
                    data = parse_weather(resp)
                    result += format_weather_by_lang(city.title(), data, units, lang) + "\n"

                url, params = build_weather_request(appid, mode="forecast", city=city, units=units, lang=lang)
                resp = fetch_weather(url, params)
                if error(resp):
                    forecast = parse_forecast(resp)
                    result += format_forecast_by_lang(forecast, lang)

            else:
                result = "Unknown mode selected."

        except Exception as e:
            result = f"Error:\n{traceback.format_exc()}"

        self.show_result(result)

    def run(self):
        self.root.mainloop()

def run_gui():
    root = tk.Tk()
    app = WeatherAppGUI(root)
    app.run()

def choose_mode_gui():
        choice = {}
        splash = tk.Tk()
        splash.title("Выбор режима")
        splash.geometry("275x115")
        splash.resizable(False, False)
        ttk.Label(
            splash, text="Выберите режим работы:", 
            font=("Arial", 12, "bold"),
        ).pack(pady=10)
        btn_frame = ttk.Frame(splash)
        btn_frame.pack(pady=5, fill="x", expand=True)
        def cli_select():
            choice['mode'] = 'cli'
            splash.destroy()
        def gui_select():
            choice['mode'] = 'gui'
            splash.destroy()
        ttk.Button(
            btn_frame,
            text="CLI", 
            width=13, 
            command=cli_select
        ).pack(side=tk.LEFT, padx=13)
        ttk.Button(
            btn_frame, 
            text="Графика (GUI)", 
            width=13, 
            command=gui_select
        ).pack(side=tk.RIGHT, padx=13)
        splash.mainloop()
        return choice.get('mode')
