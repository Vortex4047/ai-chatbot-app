import os, json, time, threading, requests, customtkinter as ctk
from tkinter import filedialog

# Set up theme defaults
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Place your OpenRouter key here or set env var OPENROUTER_KEY
OPENROUTER_API_KEY = os.getenv("OPENROUTER_KEY", "or-XXXXXXXXXXXX")

MODELS = [
    "mistralai/mistral-7b-instruct",
    "meta-llama/llama-3-8b-instruct",
    "openchat/openchat-3.5-1210"
]

# Chat/style config
CHAT_BG = "#1E1E2E"; USER_BG = "#2E8B57"; BOT_BG = "#383A59"

# UI Setup
app = ctk.CTk()
app.geometry("700x600"); app.title("✨ AI Chat App")
app.grid_rowconfigure(1, weight=1); app.grid_columnconfigure(0, weight=1)

# Top bar: model selector + theme toggle + save btn
topbar = ctk.CTkFrame(app)
topbar.grid(row=0, column=0, sticky="ew", pady=10, padx=10)
model_var = ctk.StringVar(value=MODELS[0])
ctk.CTkOptionMenu(topbar, variable=model_var, values=MODELS).pack(side="left")
def toggle_theme():
    ctk.set_appearance_mode("Dark" if ctk.get_appearance_mode()=="Light" else "Light")
ctk.CTkButton(topbar, text="🌙/☀️", width=40, command=toggle_theme).pack(side="left", padx=10)
def save_chat():
    msgs = chat_data
    path = filedialog.asksaveasfilename(defaultextension=".json",
                                        filetypes=[("JSON","*.json"),("Text","*.txt")])
    if path:
        with open(path, "w") as f:
            if path.endswith(".json"):
                json.dump(msgs, f, indent=2)
            else:
                f.write("\n".join(f"{m['role']}: {m['content']}" for m in msgs))
        save_btn.configure(fg_color="green")
        threading.Timer(1.0, lambda: save_btn.configure(fg_color=None)).start()
save_btn = ctk.CTkButton(topbar, text="💾 Save Chat", command=save_chat)
save_btn.pack(side="left", padx=10)

# Chat history scrollbox
chat_frame = ctk.CTkScrollableFrame(app, fg_color=CHAT_BG)
chat_frame.grid(row=1, column=0, sticky="nsew", padx=10)
chat_widgets = []
chat_data = []

# Input entry + send
input_bar = ctk.CTkFrame(app)
input_bar.grid(row=2, column=0, sticky="ew", pady=10, padx=10)
entry = ctk.CTkEntry(input_bar, width=500, font=("Segoe UI", 14))
entry.pack(side="left", padx=5, fill="x", expand=True)
send_btn = ctk.CTkButton(input_bar, text="Send", width=80, command=lambda: threading.Thread(target=on_send).start())
send_btn.pack(side="left", padx=5)
entry.bind("<Return>", lambda e: send_btn.invoke())

def add_message(role, text):
    bubble = ctk.CTkLabel(chat_frame,
        text=text, wraplength=500, justify="left",
        fg_color=USER_BG if role=="user" else BOT_BG,
        text_color="white", corner_radius=10, padx=10, pady=6
    )
    bubble.pack(anchor="e" if role=="user" else "w", pady=4, padx=10)
    chat_frame.update()
    chat_frame._parent_canvas.yview_moveto(1.0)  # 👈 FIXED line
    chat_widgets.append(bubble)
    chat_data.append({"role": role, "content": text})

def ask_model(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"model": model_var.get(), "messages": [{"role":"user","content":prompt}]}
    resp = requests.post("https://openrouter.ai/api/v1/chat/completions",
                         headers=headers, json=data)
    try: return resp.json()["choices"][0]["message"]["content"]
    except: return f"Error: {resp.text}"

def on_send():
    text = entry.get().strip()
    if not text: return
    entry.delete(0, "end")
    add_message("user", text)
    bot_msg = ask_model(text)
    add_message("assistant", bot_msg)

app.mainloop()

#made by Vortex/Kritik
