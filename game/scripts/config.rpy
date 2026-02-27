define black = "#00000"
transform rightish:
    xpos 600

define d = Dissolve(2.0)
define sd = Dissolve(4.0)
define morb = ImageDissolve("images/cooolio.png", 1.0, time_warp=_warper.easeout)
define rmorb = ImageDissolve("images/coool.png", 1.0, time_warp=_warper.easeout)
define wipe = ImageDissolve("images/woah.png", 1.0, time_warp=_warper.easeout)
define box = ImageDissolve("images/box.png", 1.0, time_warp=_warper.easeout)
