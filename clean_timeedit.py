import requests
from ics import Calendar, Event


timeEDIT_URL = "https://cloud.timeedit.net/usn/web/publikk/ri6QZ84Q7l804kQQQQZqqu0Z76yZ05w0n9d4ZlY5W55b1ZQ5Z5Qot00moD38l7n019Q38tDA89nDl0n6506727AZ8oA03B1nB33D47DAFD5C0074274.ics"
OUTPUT_FILE = "docs/clean.ics"  ## file we save new calander in?

raw = requests.get(timeEDIT_URL,timeout=30)
raw.raise_for_status()

source = Calendar(raw.text)
clean = Calandar()

for e in source.event:
  parts = [p.strip() for p in e.name.split("|")]
  
  title = part[0]
  details = "\n".join(parts[1:])
  
  new = Event()
  new.name = title
  new.begin = e.begin
  new.end = e.end
  new.location e.location
  new.description = details
  
  clean.events.add(new)
  
with open(OUTPUT_FILE, "w", encoding = "utf-8") as f:
  f.writelines(clean.serialize())


