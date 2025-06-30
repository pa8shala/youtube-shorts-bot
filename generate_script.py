import datetime

def generate_script():
    today = datetime.date.today()
    short_text = f"🌞 {today.strftime('%B %d')} Motivation:\nBelieve in yourself. Start your day with purpose!"
    
    file_name = f"content/shorts_script_{today.strftime('%Y%m%d')}.txt"
    
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(short_text)
    
    print("Script generated and saved to", file_name)

if _name_ == "_main_":
    generate_script()
