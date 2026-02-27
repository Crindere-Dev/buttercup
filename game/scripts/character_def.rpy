define im_anchor = (0.5, 1.0)

init python:
    import random, re

    renpy.music.register_channel("textsound", "sfx", False) # Add a new sound channel for the text sounds so that they don't overlap with anything else

    _TAG = re.compile(r'{cps=(\d+)}') # Use regex to find and store the first instance of the {cps=} tag in a character dialog block

   
    def m_adaptive_text_sounds(event, interact=True, **kw):
        if event == "show":
            renpy.sound.stop(channel="textsound")
            raw  = renpy.store._last_say_what or ""
            text = renpy.substitute(raw)
            cps  = (kw.get("slow_cps") or kw.get("cps") or renpy.store.preferences.text_cps)

            for chunk in _TAG.split(text):
                if chunk.isdigit():
                    cps = int(chunk)
                    continue
                pause = 0 if cps <= 0 else 1.0 / cps

                for char in chunk:
                    if not char.isspace():
                        renpy.sound.queue(f"audio/m_{random.randint(1,3)}.ogg",channel="textsound") # Replace "audio/popcat{random.randint(1,11)}.wav" with sound files of your choice
                    if pause:
                        renpy.sound.queue(f"<silence {pause}>", channel="textsound")

        elif event in ("slow_done", "end"):
            renpy.sound.stop(channel="textsound")

    def c_adaptive_text_sounds(event, interact=True, **kw):
        if event == "show":
            renpy.sound.stop(channel="textsound")
            raw  = renpy.store._last_say_what or ""
            text = renpy.substitute(raw)
            cps  = (kw.get("slow_cps") or kw.get("cps") or renpy.store.preferences.text_cps)

            for chunk in _TAG.split(text):
                if chunk.isdigit():
                    cps = int(chunk)
                    continue
                pause = 0 if cps <= 0 else 1.0 / cps

                for char in chunk:
                    if not char.isspace():
                        renpy.sound.queue(f"audio/c_{random.randint(1,3)}.ogg",channel="textsound") # Replace "audio/popcat{random.randint(1,11)}.wav" with sound files of your choice
                    if pause:
                        renpy.sound.queue(f"<silence {pause}>", channel="textsound")

        elif event in ("slow_done", "end"):
            renpy.sound.stop(channel="textsound")

    def a_adaptive_text_sounds(event, interact=True, **kw):
        if event == "show":
            renpy.sound.stop(channel="textsound")
            raw  = renpy.store._last_say_what or ""
            text = renpy.substitute(raw)
            cps  = (kw.get("slow_cps") or kw.get("cps") or renpy.store.preferences.text_cps)

            for chunk in _TAG.split(text):
                if chunk.isdigit():
                    cps = int(chunk)
                    continue
                pause = 0 if cps <= 0 else 1.0 / cps

                for char in chunk:
                    if not char.isspace():
                        renpy.sound.queue(f"audio/a_{random.randint(1,3)}.ogg",channel="textsound") # Replace "audio/popcat{random.randint(1,11)}.wav" with sound files of your choice
                    if pause:
                        renpy.sound.queue(f"<silence {pause}>", channel="textsound")

        elif event in ("slow_done", "end"):
            renpy.sound.stop(channel="textsound")



define m = Character("Malcolm", 
who_color ="#127844",
what_slow_cps=15,
callback=m_adaptive_text_sounds)
define dm = Character("Malcolm", 
who_color ="#127844",
what_slow_cps=30,
callback=m_adaptive_text_sounds)

define a = Character("Adeline", 
who_color ="#127844",
who_outline = "black",
callback=a_adaptive_text_sounds,
what_slow_cps=25,
what_suffix="-desu.")
define da = Character("Adeline", 
who_color ="#127844",
who_outline = "black",
callback=a_adaptive_text_sounds,
what_slow_cps=35)


define c = Character("Clerk",
who_color ="#127844",
who_outline = "black",
callback=c_adaptive_text_sounds,
what_slow_cps=25)

define i = Character("Intercom",
who_color ="#127844",
who_outline = "black",
callback=c_adaptive_text_sounds,
what_slow_cps=25)