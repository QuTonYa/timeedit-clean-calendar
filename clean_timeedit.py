import request;
from ics import Calender, Event:


TimeEdit_URL = https://cloud.timeedit.net/usn/web/publikk/ri6Q28467l804WQQQWZq566Z7VyY051V9924XlY5W556XZW52612WZ7QQ713nqdnZuo00nm6nwonZl0Q3085Q6l7ZQ8kb9o13tZ889t3B43634AE29FF1DE65A663E319E8C99.ics ## paste your TimeEdit link here
NEW_TimeEdit_file = "output/clean.ics"  ## file we save new calander in?

raw = request.get(TimeEdit_URL,timeout=30)
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
with open(NEW_TimeEdit_file, "w", encoding = "utf-8") as f:
  f.writelines(clean.serialize())


