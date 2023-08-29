# Orbital ClickBot
GD ClickBot, continuation/rewrite of TCB++

## Quickstart

There's no console version (yet), but it's planned.
Just download GUI version from [releases](https://github.com/thisisignitedoreo/orbitalcb/releases)

## For users

Current supported macros:
- EchoBot
- TasBot

_Planned_:
- ReplayBot
- ReplayEngine
- MHReplay
- MacroBot
- much more (i dont have that much time \'^\' you can [help me](https://github.com/thisisignitedoreo/orbitalcb#for-developers)...)

Clickpacks can be either a folder or a zip with such structure:

```
clickpack/
├─ p1/
│  ├─ softclicks/  # optional
│  │  ├─ holds/
│  │  ├─ releases/
│  ├─ hardclicks/  # optional
│  │  ├─ holds/
│  │  ├─ releases/
│  ├─ holds/
│  ├─ releases/
├─ p2/             # optional
│  ├─ softclicks/  # optional
│  │  ├─ holds/
│  │  ├─ releases/
│  ├─ hardclicks/  # optional
│  │  ├─ holds/
│  │  ├─ releases/
│  ├─ holds/
│  ├─ releases/
```

## For developers

Clickbot is split into two parts: logic and interface.
Logic is some kind of library on top of which you can write any interface you want.
This overcomes the problem with TCB++ in which I had a completly different console
version with its own logic and such. It was really hard to maintain.

Forks are allowed by the [LICENSE](/LICENSE) (GNU GPL v3 only) and are greatly
appreciated by me. Just follow license (opensource your code under GPL v3 license).

Adding bot-parsers is as easy as adding such key-value pair to macro_types:
    ("Human readable bot name", "Wildcard to match file with"): MacroClass

Class should have:
- Function `__init__` with arguments self and path where path is path to the macro
- Variable self.path with path to the macro
- Variable self.data with macro's data in this format:
	- `{ "fps": MACRO_FPS (*int),`<br>
	  `  "replay": [`<br>
	  `    { "frame": ACTION_FRAME (*int), "hold": ACTION_ISHOLD (True, False), "player": ACTION_PLAYER (1, 2) },`<br>
	  `    ... ] }`<br>

You can take a look at existing classes for help if you need to (i think ya need haha)

## History

This project evolved from [clickbot for ReplayEngine](https://github.com/tovyadd/clicks), which was written
almost entirely by me for TobyAdd (he wrote small portion of initial implementation,
which didn't support hard/soft clicks). It was published under MIT license, but toby
strictly forbid any forks. Don't get me wrong - he's great programmer and just a
cool guy (no he does not put any rats/stillers/other malware in his cracks, stop
spreding mis-info), but after I seen how many people wanted to get his, now
deleted, ACB crack, I thought about making FOSS alternative to ACB/GCB/other CB's,
with GUI, support for many bots and much more.
