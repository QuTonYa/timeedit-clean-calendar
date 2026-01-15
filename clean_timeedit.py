import requests
from ics import Calendar, Event


timeEDIT_URL = https://cloud.timeedit.net/usn/web/publikk/ri6Q28467l804WQQQWZq566Z7VyY051V9924XlY5W556XZW52612WZ7QQ713nqdnZuo00nm6nwonZl0Q3085Q6l7ZQ8kb9o13tZ889t3B43634AE29FF1DE65A663E319E8C99.ics
OUTPUT_FILE = "docs/clean.ics"  ## file we save new calander in?

raw = requests.get(timeEDIT_URL,timeout=30)
raw.raise_for_status()

source = Calendar(raw.text)
clean = Calandar()

for i in source.event:
  parts = [p.strip() for p in i.name.split("|")]
  
  title = part[0]
  details = "\n".join(parts[1:])
  
  new = Event()
  new.name = title
  new.begin = i.begin
  new.end = i.end
  new.location i.location
  new.description = details
  
  clean.events.add(new)
  
with open(OUTPUT_FILE, "w", encoding = "utf-8") as f:
  f.writelines(clean.serialize())


