import request
from ics import Calender, Event


timeEDIT_URL = "PASTE_YOUR_TIMEEDIT_ICS_URL_HERE"
OUTPUT_FILE = "docs/clean.ics"  ## file we save new calander in?

raw = request.get(timeEDIT_URL,timeout=30)
raw.raise_for_status()

source = Calender(raw.text)
clean = Calander()

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


