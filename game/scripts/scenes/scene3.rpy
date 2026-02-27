
define config.layers = [ 'master', 'transient', 'screens', 'overlay']
label date:
    camera at cam_reset
    scene black
    "On a cold but refreshing winter day,"
    "Malcolm stood there {w=0.25}slightly bored but content."
    show test with dissolve 
    pause(1)
    show m_neu with dissolve
    "It seemed liked he’d been stood there the whole time.."
    show test with hpunch
    a"huff  huff huff"
    "The sound of rapid footsteps slowly ramped up as a certain barista approached.."
    
    a"ohh—{w=0.25} huff— {w=0.25}you’re{w=0.25}—huff—{w=0.25}already here"
    hide m_neu
    show m_neu at ts_moveinX(-1, 1, 300)
    
    "Adeline ran up to meet him before stopping for a moment to catch her breath…"
    show a_neu_ec_mo at ts_moveinX(600,0.8, 800)
    a "Hey!— oh wow"#
    hide a_neu_ec_mo
    show a_neu_eo_mo at ajump(600)
    a "How—How are you,{w=0.25} waoww I love your coat!"
    hide a_neu_eo_mo
    show a_blush_ec_mo at ajump(600)
    a "You look great :3"
    hide m_neu
    show m_neu_open at mjump(-1)
    m "Thank you."
    hide m_neu_open
    show m_neu at mjump(-1)
    "Malcolm looked down at her with a plain but strangely heart-warming expression."
    hide m_neu 
    show m_think at mjump(-1)

    m "“You look…cute”"
    hide m_think
    show m_neu at left
    hide a_blush_ec_mo
    hide m_neu_open
    show a_blush_flap at ajump(600)
    a "“Ah this?"
    hide a_blush_flap
    show a_blush_flap at ts_acShake(600,5,0.1)
    a "Noo it's just something I threw together hehehe"
    hide m_neu
    show m_neu_open at mjump(-1)
    m "Are you not cold?"
    hide m_neu_open
    show m_neu at mjump(-1)
    hide a_blush_flap
    show a_neu_ec_mo at ajump(600)
    a"No!"
    hide a_neu_ec_mo
    show a_neu_eo_mo at ajump(600)
    a"Are you?"
    hide m_neu
    show m_neu_open at mjump(-1)
    m "...{w=.25} No."
    hide m_neu_open

    show m_think at mjump(-1)
    hide m_neu
    m "Our tickets is for 12:30…"   
    hide m_think

    show m_neu at mjump(-1)
    m "We should go."

    hide a_blush_flap

    show a_neu_eo_mo at ajump(600)
    a "Ahh, Yes!"
    hide a_neu_eo_mo
    show a_neu_ec_mo at ajump(600)
    a "Took the words right out of my mouth, haha"
    show m_neu at ts_moveX(1025, 2)
    hide a_neu_ec_mo
    show a_neu_ec_mc at rightish
    pause 1.5
    hide a_neu_ec_mc
    show a_neu_ec_mc at ts_flipX(600, -1, 1)
    hide a_neu_ec_mc
    show flip_witch at ts_moveinX(1025, 1, 600)
    "And with that, they began to walk"
    "— side by side.."#insert cg here       


    scene black
    show street:
        linear 60 zoom 0.9
        
        
    # walk scene
    
    show m_neu at ts_acFloat(-200,10) with dissolve:
        zoom 1.2
    show a_neu_ec_mo at ts_acFloat(150,10) with dissolve:
        zoom 1.2
    a "I wanted to ask, how long have you been standing there for {w=0.25}"
    hide a_neu_ec_mo
    show a_neu_eo_mo at ts_acFloat(150,10):
        zoom 1.2
    a "— like I thought I was early,,"
    hide a_neu_eo_mo
    show a_neu at ts_acFloat(150,10):
        zoom 1.2
    hide m_neu
    show m_neu_open at ts_acFloat(-200,10):
        zoom 1.2
    m "Since 10."
    hide a_neu
    hide m_neu_open
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    a "10??{w=.25} Wow you're really on point aren't you."
    hide m_neu
    show m_neu_open at ts_acFloat(-200,10):
        zoom 1.2
    m "Yeah."
    hide a_explain
    hide m_neu_open
    show a_shame_c at ts_acFloat(150,10):
        zoom 1.2
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    a "..."
    hide a_shame_c
    show a_shame_o at ts_acFloat(150,10):
        zoom 1.2
    a "Haha,{w=.25} anyways.."
    hide a_shame_o
    show a_shame_c at ts_acFloat(150,10):
        zoom 1.2
    "Adeline looked down at the floor, slightly embarrassed by his short, dry replies."
    a "{i}Think—{w=.25}Addy—{w=.25}think...{/i}"
    hide a_shame_c
    show a_neu_ec_mo at ts_acFloat(150,10):
        zoom 1.2
    a "Ah!"
    hide a_neu_ec_mo
    show a_neu_eo_mo at ts_acFloat(150,10):
        zoom 1.2
    a "So uhhh, {w=.25} how old are you?"
    hide a_neu_eo_mo
    hide m_neu
    show a_neu_ec_mc at ts_acFloat(150,10):
        zoom 1.2
    show m_neu_open at ts_acFloat(-200,10):
        zoom 1.2
    m "I’m 21... {w=.25} 4th of October is my birthday."
    hide a_neu_ec_mc
    hide m_neu_open
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    a "Oh wow, I’m a year younger!!"
    hide a_explain
    show a_ec_explain at ts_acFloat(150,10):
        zoom 1.2
    a "I’m 20 — haha — my birthday was a few months ago..."
    hide a_ec_explain
    show a_neu at ts_acFloat(150,10):
        zoom 1.2
    a "Jan 6..."
    m "..."
    hide a_neu
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    a "What do you work as?"
    hide a_explain
    show a_neu_ec_mo at ts_acFloat(150,10):
        zoom 1.2
    a "You looked so important with your cardigan and your messenger bag!"
    a "I bet it’s important.."
    hide a_neu_ec_mo
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    a "Ooh Ooh!"
    hide a_explain
    show a_ec_explain at ts_acFloat(150,10):
        zoom 1.2
    a "Let me guess!"
    hide a_ec_explain
    show a_neu_ec_mo at ts_acFloat(150,10):
        zoom 1.2
    a"uhh, business executive… "
    hide a_neu_ec_mo
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    a"no— wait, maybe you're an intern at a big bank!"
    hide a_explain
    show a_blush_flap at ts_acFloat(150,10):
        zoom 1.2
    a "or maybe..{w=.25} you're a spy oooh >:3 "
    hide m_neu
    show m_smile_o at ts_acFloat(-200,10):
        zoom 1.2
    m"You have a big imagination."
    hide a_blush_flap
    hide m_smile_o
    show m_neu_eye_close_mouth_open at ts_acFloat(-200,10):
        zoom 1.2
    show a_neu_ec_mc at ts_acFloat(150,10):
        zoom 1.2

    m "I'm in University."
    hide m_neu_eye_close_mouth_open
    
    hide a_neu_ec_mc
    show a_blush_flap at ts_acFloat(150,10):
        zoom 1.2
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    a "SAME!!"
    hide a_blush_flap
    hide m_neu_open
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    a "What degree and year??"
    hide a_explain
    show a_ec_explain at ts_acFloat(150,10):
        zoom 1.2
    a "I’m in my second year of History :0"
    hide a_ec_explain
    show a_neu_ec_mc at ts_acFloat(150,10):
        zoom 1.2
    hide m_neu
    show m_neu_open at ts_acFloat(-200,10):
        zoom 1.2
    m"Third year, mathematics and philosophy."
    hide a_neu_ec_mc
    hide m_neu_open
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    a"Wow you're degree fits you perfectly.."
    hide m_neu
    show m_neu_open at ts_acFloat(-200,10):
        zoom 1.2
    m"What do you mean."
    hide m_neu_open
    hide a_explain
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    show a_ec_explain at ts_acFloat(150,10):
        zoom 1.2
    a"Well you're cool and mysterious"
    a" — logical suave types are usually drawn to maths {w=.25} no?"
    hide m_neu
    show m_smile_o at ts_acFloat(-200,10):
        zoom 1.2
    m"Are you calling me boring.?"
    hide a_ec_explain
    hide m_smile_o
    show m_smile_c at ts_acFloat(-200,10):
        zoom 1.2
    show a_worry_mo at ts_acShake(430,5,0.1):
        zoom 1.2
    a "No no!"
    a"Not at all—{w=.25} Actually you're really interesting to talk too, yes!"
    hide a_worry_mo
    hide m_smile_c
    show m_smile_ec_mo at ts_acFloat(-200,10):
        zoom 1.2
    show a_worry at ts_acFloat(150,10):
        zoom 1.2
    m"I'm kidding."
    hide m_smile_ec_mo
    hide a_worry
    show m_smile_ec_mc at ts_acFloat(-200,10):
        zoom 1.2
    show a_shame_c at ts_acFloat(150,10):
        zoom 1.2
    a "{i}He's so Colddd, {w=.25} I couldn't even tell sobbb{/i}"
    hide a_shame_c
    show a_shame_o at ts_acFloat(150,10):
        zoom 1.2
    a "Haha— you remind me of some of the stem guys at my uni.."
    a "Why do you all act like that... ;_;"
    hide a_shame_o
    hide m_smile_ec_mc
    show a_shame_c at ts_acFloat(150,10):
        zoom 1.2
    show m_neu_open at ts_acFloat(-200,10):
        zoom 1.2
    m"What university do you go too..?"
    hide a_shame_c
    hide m_neu_open
    show a_shame_o at ts_acFloat(150,10):
        zoom 1.2
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    a"...{w=.25}Camterbridge."
    hide m_neu
    hide a_shame_o
    show a_shame_c at ts_acFloat(150,10):
        zoom 1.2
    show m_eyeopen_think at ts_acFloat(-200,10):
        zoom 1.2
    m"You go CU?"
    m"So do I..."
    hide m_eyeopen_think
    hide a_shame_c
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    show a_shocked at ts_acFloat(150,10):
        zoom 1.2
    a"WHATT!"
    hide a_shocked
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    a"How come I never see you?!"
    hide m_neu 
    show m_explain at ts_acFloat(-200,10):
        zoom 1.2
    m"I live on another campus."
    hide m_explain
    hide a_explain
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    show a_ec_explain at ts_acFloat(150,10):
        zoom 1.2
    a"Right...!"
    a"I knew I recognised your lanyard from somewhere.."
    hide m_neu
    show m_think at ts_acFloat(-200,10):
        zoom 1.2
    m "..."
    m "I'm suprised you're enrolled."
    hide a_ec_explain
    show a_tsun at ts_acFloat(150,10):
        zoom 1.2
    a "Hmph!"
    hide a_tsun
    show a_tsuno at ts_acFloat(150,10):
        zoom 1.2
    a" Are you calling me dumb?"
    hide a_tsuno
    hide m_think 
    show a_tsun at ts_acFloat(150,10):
        zoom 1.2
    show m_smile_o at ts_acFloat(-200,10):
        zoom 1.2
    m "A bit."
    hide m_smile_o
    show m_smile_ec_mo at ts_acFloat(-200,10):
        zoom 1.2
    m "You did pour...{w=.25} boiling hot coffee on me."
    hide m_smile_ec_mo
    hide a_tsun
    show m_smile_ec_mc at ts_acFloat(-200,10):
        zoom 1.2
    show a_tsuno at ts_acFloat(150,10):
        zoom 1.2
    a "I think you simply lack providence."
    hide a_tsuno
    hide m_smile_ec_mc
    show a_tsun at ts_acFloat(150,10):
        zoom 1.2
    show m_neu_open at ts_acFloat(-200,10):
        zoom 1.2
    m "Ok."
    hide m_neu_open
    hide a_tsun 
    show m_think at ts_acFloat(-200,10):
        zoom 1.2
    show a_shame_c at ts_acFloat(150,10):
        zoom 1.2
    a"{i}Anddd back to the one worded answers...{w=.25} when will it end.{/i}"
    a"{i}He has a certain type of humor doesn't he..{/i}"
    a"{i}Bit of a deadpanner..{/i}"
    hide a_shame_c
    show a_blush_ec_mc at ts_acFloat(150,10):
        zoom 1.2
    a"{i}Oh wow...{w=.25} I never realised how big his hands were..{/i}"
    a"{i}and veiny...{/i}"
    hide m_neu 
    hide m_think
    show m_neu_open at ts_acFloat(-200,10):
        zoom 1.2
    m "I like puzzles."
    hide m_neu_open
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    hide a_blush_ec_mc
    show a_neu_eo_mo at ts_acFloat(150,10):
        zoom 1.2
    a "Huh?"
    hide a_neu_eo_mo
    show a_neu_ec_mo at ts_acFloat(150,10):
        zoom 1.2
    a "Oh Cute!"
    hide m_neu
    hide a_neu_ec_mo
    show m_blushed_close at ts_acFloat(-200,10):
        zoom 1.2
    show a_blush_ec_mo at ts_acFloat(150,10):
        zoom 1.2
    a "{i}{cps=30}oh did I really just call him cute oh my goddfsk{/cps}{/i}"
    hide a_blush_ec_mo
    hide m_blushed_close 
    show a_blush_eo_mc at ts_acFloat(150,10):
        zoom 1.2
    show m_blushed_open at ts_acFloat(-200,10):
        zoom 1.2
    m "Thank you..."
    m "What do you like.."
    hide a_blush_eo_mc
    hide m_blushed_open
    show a_blush_ec_mo at ts_acFloat(150,10):
        zoom 1.2
    show m_blushed_close at ts_acFloat(-200,10):
        zoom 1.2
    a "uhhh,{w=.25} I loveee sweets!"
    hide a_blush_ec_mo
    show a_speak_explain at ts_acFloat(150,10):
        zoom 1.2
    a "Macaroons are the best!"
    a"and sometimes, {w=.25} when SFE drops,{w=.25} I spend half on luxury cream cakes…"
    hide a_speak_explain
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    a "Oh I alsooo like scrolling through forums,"
    a "you'd be surprised on how much information you can get from anon’s online…"
    hide a_explain
    show a_ec_explain at ts_acFloat(150,10):
        zoom 1.2
    a "Yeah!"
    hide a_ec_explain
    show a_neu at ts_acFloat(150,10):
        zoom 1.2
    hide m_blushed_close
    show m_neu_open at ts_acFloat(-200,10):
        zoom 1.2
    m "I enjoy writing documentation and explaining mathematic formulas that can solve these puzzles.."
    hide m_neu_open
    hide a_neu
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    show a_blush_ec_mc at ts_acFloat(150,10):
        zoom 1.2
    a"{i}Godd that's adorable he's like a little nerdd inside.{/i}"
    hide a_blush_ec_mc
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    a"Woah that sounds hard.."
    hide m_neu
    show m_explain at ts_acFloat(-200,10):
        zoom 1.2
    m "Some of them sound complex but are rather simple."
    hide a_explain
    hide m_explain
    show a_ec_explain at ts_acFloat(150,10):
        zoom 1.2
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    a"Ok...{w=.25}hit me!"
    hide m_neu 
    hide a_ec_explain
    show a_neu_ec_mc at ts_acFloat(150,10):
        zoom 1.2
    show m_think at ts_acFloat(-200,10):
        zoom 1.2
    m "Well, let’s say you have been given three transformations over Z₁₀₀₀ and asked whether (0,0) can reach (1,1). With this we need to open 2 locks."
    
    hide a_neu_ec_mc
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    a "Okay.."
    hide m_think
    show m_eyeopen_think at ts_acFloat(-200,10):
        zoom 1.2
    m"Well, In order to solve this, you would have to first eliminate a variable."
    m "Which gives you 28x - 687y (triple bar) 912 mod 1000."
    hide m_eyeopen_think
    show m_explain at ts_acFloat(-200,10):
        zoom 1.2
    m "Since every term is divisible by four, reduce the modulus to 250."
    m"That gives you: 7x - 187t (triple bar) 288 mod 250."
    m"Then invert the 7 modulo 250."
    hide m_explain
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    a "Ok… Wait a sec."
    a "You're um {w=.25} shrinking the modulus so its easy to isolate the x right?"
    hide m_neu 
    show m_neu_open at ts_acFloat(-200,10):
        zoom 1.2
    m"Oh."
    m"Yes."
    hide a_explain
    hide m_neu_open
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    show a_ec_explain at ts_acFloat(150,10):
        zoom 1.2
    a "I forgot how, something something factors."
    hide m_neu
    show m_eyeopen_think at ts_acFloat(-200,10):
        zoom 1.2
    m "Correct..."
    hide m_eyeopen_think
    show m_explain at ts_acFloat(-200,10):
        zoom 1.2
    m"Z becomes 809,"
    m "So then the correct solution to the locks is X = 104 and Z = 809."
    hide m_explain
    show m_smile_o at ts_acFloat(-200,10):
        zoom 1.2
    m "So not the hardest problem {w=.25}but it’s common when you want to flex your intellect."
    hide a_ec_explain
    hide m_smile_o
    show a_neu_ec_mc at ts_acFloat(150,10):
        zoom 1.2
    show m_smile_c at ts_acFloat(-200,10):
        zoom 1.2
    a"{i}I thought I recognised it from somewhere..{/i}"
    hide a_neu_ec_mc
    
    show a_speak_explain at ts_acFloat(150,10):
        zoom 1.2
    a "That’s from Pretty Princess Nanako,{w=.25} no?"
    hide m_smile_c
    show m_neu_open at ts_acFloat(-200,10):
        zoom 1.2
    m "What."
    hide m_neu_open
    show m_neu at ts_acFloat(-200,10):
        zoom 1.2
    a"Yeah! I knew I recognised it."
    hide a_ec_explain
    hide a_speak_explain
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    a "Basically episode 8, {w=.25} she was trying to break into the observatory to save her familiar right.."
    hide a_explain
    show a_ec_explain at ts_acFloat(150,10):
        zoom 1.2
    a "But then she was like the locks were impossible!"
    hide a_ec_explain
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    a "So this guy on the AniNet thread literally posted theory.{w=.5} Like literal mathematic theory that he wrote himself"
    a"— proving that it could be solved by reducing the congruence."
    hide a_explain
    show a_ec_explain at ts_acFloat(150,10):
        zoom 1.2
    a "And they literally did the same thingy you were talking about, omg!"
    a "And I remember it because basically someone replied calling him a virgin."
    a "Something like: Nanako isn't gonna fuck you anon."
    hide a_ec_explain
    hide a_neu
    hide m_neu
    show a_neu_ec_mc at ts_acFloat(150,10):
        zoom 1.2
    show m_smile_o at ts_acFloat(-200,10):
        zoom 1.2
    m "You learnt number theory from a Moe forum?"
    hide m_smile_o
    hide a_neu_ec_mc
    show m_smile_c at ts_acFloat(-200,10):
        zoom 1.2
    show a_tsuno at ts_acFloat(150,10):
        zoom 1.2
    a "Hmph, it was a very,{w=.25} very rigorous discussion."
    hide a_tsuno
    show a_explain at ts_acFloat(150,10):
        zoom 1.2
    a "WITH citations I may add."
    "Malcolm's eyes laid fixed for a second, slightly perplexed but also greatly amused."
    hide m_smile_c
    hide m_neu
    hide a_explain
    show a_neu_ec_mc at ts_acFloat(150,10):
        zoom 1.2
    show m_blushed_close at ts_acFloat(-200,10):
        zoom 1.2
    m"{i}She's {w=.5}Wonderful...{/i}"
    hide m_blushed_close
    show m_blushed_open at ts_acFloat(-200,10,rot=2):
        zoom 1.2
    m "You’re wonderfully weird Adeline."#
    hide m_blushed_open
    show m_blushed_close at ts_acFloat(-200,10,rot=2):
        zoom 1.2
    "He moved slightly closer to her without her noticing.. almost feeling drawn to her in a sense."
    hide a_neu_ec_mc
    show a_blush_ec_mo at ts_acFloat(150,10, rot=3):
        zoom 1.2
    a "o-oh..{w=.25} thank you :3"
    hide a_blush_ec_mo
    show a_blush_eo_mc at ts_acFloat(150,10, rot=3):
        zoom 1.2
    "Third times the charm she thought as her eyes quickly darted to the floor again before slowly beginning to fixate on his hands again."
    hide a_blush_eo_mc
    show a_blush_ec_mc at ts_acFloat(150,10, rot=3):
        zoom 1.2
    a"{i}Wow, I really think were going somewhere.{/i}"
    a"{i}He’s so charming in his own weird apathetic way..{/i}"
    a "{i}Ok I’m gonna go for it,{w=.5} im going,{w=.25} im going im—{/i}"
    a"Can I hold your h—"
    hide m_blushed_close
    hide a_blush_ec_mc
    show a_shocked at ajump(500):
        zoom 1.2
    show m_neu_open at mjump(110):
        zoom 1.2
    m"We are here."
    hide a_shocked
    hide m_neu_open
    show a_shame_o at ajump(500):
        zoom 1.2
    show m_neu at mjump(110):
        zoom 1.2
    a"oh.."
    hide a_shame_o
    show a_shame_c at ajump(500):
        zoom 1.2
    "Malcolm digs into his pocket,{w=.25} pulling out his sleek wallet before taking 2 unwrinkled tickets out of the cash slot."
    "Adeline takes a deep breath to reset herself.."
    hide m_neu with dissolve
    hide a_shame_c with dissolve
    jump aqua

    
    return