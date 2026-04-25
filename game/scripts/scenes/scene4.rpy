
label aqua:
    scene black
    play music "aquarium.ogg" fadein 1.0 loop 
    "The two stepped into the aquarium.."
    
    show till with d
    show till_desk 
    "Adeline absentmindedly twirled her hair as she fixated on the tuna doing loops in front of her."
    show m_neu behind till_desk at mjump(50) with d 
    show cash with d
    pause 0.5
    
    c "How many people are coming today, sir?"
    #bg with fish in the background and couter ladhy
    hide m_neu 
    show m_neu_open behind till_desk at mjump(50)
    m "Two."
    hide m_neu_open
    show m_neu behind till_desk at mjump(50)
    c "And what kind of ticket?"
    hide m_neu 
    show m_neu_open behind till_desk at mjump(50)
    m "Both adults."
    hide m_neu_open
    show m_neu behind till_desk at mjump(50)
    "He laid the tickets on the table and waited patiently as they get scanned in."
    c"And would you like a map, sir?"
    c"They’re £3.99 per booklet."
    hide m_neu
    show m_neu_open  behind till_desk at mjump(50)
    m "No."
    hide m_neu_open
    show m_neu  behind till_desk at mjump(50)
    c"O-Okay.. Have a good time, sir!"
    hide m_neu 
    show m_smile_o  behind till_desk at mjump(50)
    m"Hey,{w=.25} Adeline it’s time to go."
    show a_neu_ec_mo  behind till_desk at ajump(400) with d
    a "Ahh—Yay! :333"
    hide a_neu_ec_mo with d 
    hide m_smile_o with d
    "Adeline following shortly after him, they both stepped into the first tank."
    #basic fish halway
    scene tank_1 with dissolve
    show tint  zorder 100 with dissolve
    "Adeline looked through the glass in awe, mesmerised by the natural show the fish put on for them."
    
    show a_explain at ajump(600) with dissolve
    show m_neu at mjump(50)  with dissolve
    a"Woah...."
    "Malcolm looked down at her."
    hide a_explain
    show a_neu_ec_mo at ajump(600) 
    a"They're soo cute, aren't they?!"
    hide a_neu_ec_mo
    show a_neu_ec_mc at ajump(600)
    hide m_neu 
    show m_neu_open at mjump(50)
    m"Yeah."
    hide m_neu_open
    show m_neu at mjump(50)
    hide m_neu
    show m_neu at ts_moveX(1025, 5)
    "He nodded,{w=.25} looking back at the show in front of him while slowly treading deeper through the tank."
    hide a_neu_ec_mc
    show a_shocked at ajump(600)
    a"Wahh! Wait for me!"
    show a_shocked at ts_flipX(600, -1, 1)
    pause 1
    hide a_shocked
    show a_shocked_f at ts_moveinX(1025, 1, 600)
    pause 1
    scene aquaside with dissolve
    show tint  zorder 100 with dissolve
    show overlay zorder 100
    a"You're so impatient.."
    show a_tsuno at ajump(500) with dissolve
    a "I like aquariums because they don’t rush you.."
    hide a_tsuno
    show a_ec_explain at ajump(500)
    a"It’s a nice change of pace — especially if you work in food.."
    hide a_ec_explain
    show a_blush_flap at ajump(500)
    a "also—{w=.25} fishies!!"
    hide a_blush_flap
    show a_blush_ec_mc at ajump(500)
    show m_smile_o at mjump(200) with dissolve
    m "Which one is your favorite so far?"
    hide m_smile_o
    show m_smile_c at loc(200)
    hide a_blush_ec_mc
    show a_blush_ec_mo at ajump(500)
    a "The tuna—{w=.25} he’s an amazing performer!"
    hide m_smile_c
    show m_smile_ec_mc at mjump(200)
    m "Hmm.. :)"
    "Adeline looked up, hypnotized by the fish," 
    "before lightly jogging closer to the tank in order to read the plaque that accompanied it."
    hide a_blush_ec_mo
    show a_explain at ajump(500)
    a "The Mola Mola fish… "
    hide m_smile_ec_mc
    show m_neu at loc(200)
    hide a_explain 
    show a_ec_explain at ajump(500)

    a"He looks like he’d be in Roncario 64,{w=.25} hehe.."
    hide m_neu 
    show m_blushed_close at mjump(200)
    "She grabbed Malcolm’s hand, pulling him closer - his eyes softened."
    hide a_ec_explain 
    show a_neu_ec_mc at loc(500)
    hide m_blushed_close
    show m_midly_concerned at mjump(200)
    m "Uhm... Did you know that they can weight over 2000 kilograms? And their skeletons are mostly cartilaginous."
    hide m_midly_concerned
    show m_smile_ec_mc at loc(200)
    hide a_neu_ec_mc
    show a_explain at ajump(500)
    a "Uwahhh! really??"
    hide a_explain
    show a_ec_explain at ajump(500)
    a "You’re so smart Malcolm!"
    a "I bet it would make yummy Mola Mola stock..."
    hide a_ec_explain
    show a_neu_ec_mc at loc(500)
    hide m_smile_ec_mc 
    show m_smile_o at mjump(200)
    m "Yum."
    hide m_smile_o 
    show m_smile_c at loc(200)
    hide a_neu_ec_mc
    show a_blush_ec_mo at ajump(500)
    a "You know, sometimes, I feel like a mola mola fish."
    "Her hand remained in Malcolm's.. "
    hide a_blush_ec_mo
    show a_blush_ec_mc at ajump(500)
    a"{i}He’s so warm, that's so ironic…{/i}"
    a"{i}He's such a cold, stoic man and yet I feel so warm around him..{/i}"
    a"{i}His hands are so much bigger than mine…{/i}"
    hide m_smile_c 
    show m_neu_open at mjump(200)
    m "Do you want to go deeper?"
    hide a_blush_ec_mc
    show a_blush_ec_mo at ajump(500)
    a "Oh{w=.25} sure!…"
    "She doesn't let go."
    scene turtle with d 
    "They kept walking before arriving at the touch tank."
    "Adeline bend down before starting a small conversation with a tortoise."
    a "How are you today mate."
    a "What are you saying you good yeah?"
    a "I hear dat i hear dat still."
    m "Adeline, {w=.25} what are you doing."
    a "Chatting to my man, I call him T1."
    m "Adeline, {w=.25} you don't speak like that."
    a "Hehe I know I’m cute but that's how we speak in back in London."
    a"He’s one of the {w=.25} groundem."
    "Malcolm took a deep sigh, before joining her." 
    "Slowly he bent down, getting level with the tortoise."
    m "Hello."
    "STAREEEEEEEEEEEE."
    
    "The tortoise took a long, hard look at Malcolm," 
    show turtlel1 with dissolve 
    "Before deciding to walk away."
    pause 1
    show turtlel2 with dissolve 
    m "Oh.."
    a "Hey it’s okay, maybe he was overstimulated.."
    a "You know, they're actually super sensitive to environmental stimuli — like light."
    a "Maybe you unknowingly signalled for him to leave.."
    m "That makes me feel worse."
    a "..."
    a "sorry…"
    "Her hand absentmindedly traced circles on to his back, creating a sort of comfort in him."
    show otter with dissolve
    "As more animals came to play with Adeline,"
    "Malcolm couldn't help but fixate on how cute he found her."
    "It’s ridiculous how earnest and authentic she can be."
    "He doesn’t know if is the something in her or if she's just dumb."
    "No, No she isn't dumb not at all."
    "She’s intelligent, so much she doesn't need to try. Clearly."
    "She wasn't even trying to impress him; she barely looked at him the whole time she was playing with the creatures."
    "She’s... just like this - cute, gentle, open."
    "He felt something tighten in his chest, as he gazed further at the blonde.."
    m"{i}If I want something more.{/i}"
    m "{i}I would have to tell her.{/i}"
    m "{i}Is it reasonable..?{/i}" 
    hide otter with d
    a "They walked away…:("
    m "I guess play time is over."
    m "Let’s keep going."
    a "Okay! ^^"
    show black with d
    scene black
    # black bg with jellyfish
    "The lights slowly dimmed as they made their way into the jellyfish room."
    show jelu  with dissolve
    show dark zorder 100 with dissolve
    "Their voices slowly softened as the room lit up with what seemed like a million little jellyfish..."
    show a_blush_ec_mo at loc(500) with dissolve
    a "You know what I love about Jellies.."
    hide a_blush_ec_mo
    show a_blush_eo_mo at ajump(500)
    a "They're so effortlessly free... And really beautiful."
    hide a_blush_eo_mo
    show a_blush_eo_mc at ajump(500)  
    "They leaned further onto the glass, getting a deeper look into the jellyfish."

    "Malcolm watched her intensely.. "
    show m_neu at loc(200) with dissolve
    hide a_blush_eo_mc
    show a_shame_o at ajump(500) 

    a "Sorry Mr. Jellyfish…"
    hide a_shame_o
    show a_explain at ajump(500) 
    a "But..."
    hide a_explain
    show a_ec_explain at ajump(500) 
    a"They kinda just glide without any thoughts, aimlessly through space.."
    a"It’s kind of inspiring.."
    hide a_ec_explain
    show a_blush_ec_mc at loc(500)
    pause 0.5
    hide m_neu
    show m_smile_c at ts_moveinX(250, 1, 200)
    "He nodded, and shuffled slightly closer to her."
    "Their faces got closer and closer as he attempted to get a better look.."
    a"{i}He's so close..{/i}"
    a"{i}I can.. I can feel his breath on me..{/i}"
    hide a_blush_ec_mc
    show a_blush_eo_mc at loc(500)
    "She unconsciously shifted closer towards him.."
    "Shoulders brushed up on one another.."
    "Slowly, Adeline tilted her head making eye contact with the rigid boy.. "
    hide a_blush_eo_mc
    show a_blush_ec_mo at ajump(500)
    a "Malcolm.."
    hide a_blush_ec_mo
    hide m_smile_c
    show a_blush_eo_mc at ajump(500)
    show m_neu_open at mjump(250)
    
    m "Adeline?.."
    hide m_neu_open
    show m_neu at mjump(250)
    show a_shame_o at ajump(500)
    hide a_blush_eo_mc
    a "Y—you’re close.."
    hide m_neu
    show m_blushed_open at mjump(250)
    m "O—oh.."
    m "I think this is the last tank - should we leave?"
    hide m_blushed_open
    show m_blushed_close at loc(250)
    hide a_shame_o
    show a_flus at ajump(500)
    a "y-yeah.."
    scene black 
    #arch bench
    "Sat side by side on the bench, Adeline rocked her legs back and forth as a way of passing the time." 
    show sit with dissolve 
    show tint zorder 100 with  dissolve
    "It wasn’t like they were bored, it was more like their was nothing much left to see. "
    show a_explain at ajump(500) with dissolve
    a "Wow,"
    a"This aquarium sure is short."
    show m_neu_open at mjump(200) with dissolve 
    m"Yeah.."
    hide m_neu_open
    show m_neu_eye_close_mouth_open at mjump(200)
    m"It was the cheapest one."
    hide m_neu_eye_close_mouth_open
    show m_neu at loc(200)
    hide a_explain
    show a_blush_ec_mo at ajump(500)
    a"I never took you as the frugal type!"
    hide a_blush_ec_mo
    show a_blush_ec_mc at loc(500)
    "His eyes softened at the jest, mirroring her actions."
    hide m_neu 
    hide m_neu_eye_close_mouth_open
    show m_smile_ec_mo at mjump(200)
    m"You’ve known me for 2 weeks."
    hide m_smile_ec_mo
    show m_smile_ec_mc at mjump(200)
    show a_ec_explain at ajump(500)
    a "I’m a peoples' person, I can read you like a book! "
    hide m_smile_ec_mc
    hide a_ec_explain
    show m_smile_ec_mo at mjump(200)
    show a_blush_ec_mc at loc(500)
    m"You’re very attentive."
    "He turned away too."
    hide a_blush_ec_mc
    show a_blush_eo_mo at ajump(500)
    hide m_smile_ec_mo
    show m_smile_c at loc(200)
    a "T—thanks.."
    hide a_blush_eo_mo
    show a_neu at loc(500)
    "The silenced felt like it was panning on for eternity."
    hide a_neu
    show a_shame_c at loc(500)
    "They both sat slightly awkward but relaxed.."
    hide m_smile_c
    show m_think at mjump(200)
    "Both snuck looks at each other, maybe as a poor attempt of pushing the conversation forward."
    pause 2
    hide m_think
    show m_eyeopen_think at mjump(200)
    m"I’m transgender."
    "His voice softened,"
    hide a_shame_c
    show a_neu_ec_mc at loc(500) 
    "Gaze remaining fixated on a pair of clownfish circling each other slowly," 
    "In a sort of synchronized dance."
    hide m_eyeopen_think
    show m_neu_eye_close_mouth_open at mjump(200)
    m"I don’t usually disclose this.."
    hide m_neu_eye_close_mouth_open
    show m_think at loc(200)
    "His voice lowered, that apathetic tone which Adeline quickly grew accustomed to dissipated."
    hide m_think
    show m_neu_open at mjump(200)
    m"I thought you’d deserve to know…{w=.5} if this goes any further."
    hide m_neu_open
    show m_neu at loc(200)
    "The ceiling lamp buzzed around them."
    hide m_neu
    show m_neu_eye_close_mouth_open at mjump(200)
    m"If that alters your perception of me, I understand."
    hide m_neu_eye_close_mouth_open
    show m_think at loc(200)
    a "..."
    m "..."
    hide m_think
    show m_blushed_close at mjump(200)
    show a_blush_eo_mc at loc(500) with dissolve
    hide a_neu_ec_mc with dissolve
    "A soft hand laid itself on top of Malcolm's."
    "Instinctively, he slghtly froze."
    hide a_blush_eo_mc
    show a_blush_eo_mo at ajump(500)
    a "It doesn’t."
    "She was gentle."
    hide a_blush_eo_mo
    show a_blush_ec_mo at ajump(500)
    a "Not at all.."
    hide a_blush_ec_mo
    show a_blush_ec_mc at loc(500)
    a "..."
    hide a_blush_ec_mc

    show a_neu_ec_mo at ajump(500)
    a "'Cause I’m.. trans too."
    show a_blush_ec_mc at loc(500) with dissolve
    hide a_neu_ec_mo with dissolve

    "He slowly turned to look at her," 
    "Hand tightening in her tender grasp."
    "Their eyes met, softened by the moment of unity."
    "She smiled a little, genuine and warm."
    hide a_blush_ec_mc
    show a_blush_eo_mo at ajump(500)
    a "I was kind of hoping you were as well..."
    hide a_blush_eo_mo
    show a_blush_eo_mc at loc(500)
    hide m_blushed_close
    show m_blushed_open at mjump(200)
    m "Adeline.."
    hide m_blushed_open
    show m_blushed_close at loc(200)
    hide a_blush_eo_mc
    show a_explain at ajump(500)
    a "Do you want to talk about it..?"
    m "…"
    hide m_blushed_close
    show m_neu_open at mjump(200)
    m "I don’t have much to say."
    hide m_neu_open
    show m_neu at loc(200)
    "She squeezed his hand lightly.."
    hide a_explain
    show a_ec_explain at ajump(500)
    a "I’m 3 years on HRT." 
    a "I started at 17.."
    hide a_ec_explain
    show a_neu_ec_mc at loc(500)
    hide m_neu
    show m_blushed_open at mjump(200)
    m "16."
    hide m_blushed_open
    show m_blushed_close at loc(200)
    show a_neu_ec_mo at ajump(500)
    a "Do you feel like it was worth it."
    m"..."
    hide a_neu_ec_mo 
    show a_neu_ec_mc at loc(500)
    hide m_blushed_close
    show m_midly_concerned at mjump(200)
    m "Yes."
    hide a_neu_ec_mc
    hide a_neu_eo_mo
    show a_blush_ec_mo at ajump(500)
    a "It feels good not having to explain much, doesn't it."
    "She giggled again, melting any tension left between them."
    hide a_blush_ec_mo
    show a_blush_ec_mc at loc(500)
    hide m_midly_concerned
    show m_smile_ec_mo at mjump(200)
    m "I’m glad I met you."
    hide m_smile_ec_mo
    show m_smile_ec_mc at loc(200)   
    "They stayed still for a moment."
    "Her fingers still rested over his."
    "He didn’t pull away, instead he laced his fingers in hers."
    "Finally holding hands."
    hide a_blush_ec_mc
    show a_blush_eo_mo at ajump(500)
    a "Malcolm.."
    hide a_blush_eo_mo
    show a_blush_ec_mc at loc(500)
    hide m_smile_ec_mc
    show m_smile_o at mjump(200)
    m "Do you want to go to the gift shop."
    hide m_smile_o
    show m_smile_c at loc(200)
    "She beamed at him before nodding."
    "They both hopped back to their feet, getting ready to go to the gift shop."
    hide m_smile_c with dissolve 
    hide a_blush_ec_mc with dissolve    
    "Adeline skipped excitedly to the shop,"
    "Malcolm slowly stalling behind, smilingly softly at the girl."
    scene gif with dissolve
    show light zorder 100 with  dissolve
    "For a gift shop, it was surprisingly large." 
    "The walls were covered head to toe with tall wooden shelves filled to the brim with overpriced fish themed souvenirs. "
    "Cups, stationary, flimsy tote bags, 95 percent polyester hoodies."
    "Buckets also littered the floors full of plushies of various types of fish."
    show a_blush_flap at ts_acShake(500,5,0.1) with dissolve
    a "Uwahhh, Look at him!"
    show m_neu at loc(200) with dissolve
    "Malcolm's watched her in front the small, pink stuffed shark that was being pushed into his face."
    hide a_blush_flap
    show a_ec_explain at ajump(500)
    a "Isn’t he soooo cute?!"
    hide a_ec_explain with dissolve
    hide m_neu
    show m_disappointed at mjump(200)
    "Clumsily, she pushed the shark into his arms before diving headfirst into a pile of stuffed sharks."
    show a_blush_flap at ajump(500)
    a "Tada!"
    hide a_blush_flap
    show a_explain at ajump(500)
    a "I have grabbed the best shark plush."
    a "Look!"
    hide m_disappointed
    show m_smile_c at mjump(200)
    "Malcolm leaned in, inspecting the stitching."
    hide a_explain
    show a_ec_explain at ajump(500)
    a"The stitching is uniform and tight, without sacrificing the bounciness and cuddliness of the plush!"
    hide m_smile_c
    show m_smile_o at mjump(200)
    m "Really?"
    hide a_ec_explain
    show a_explain at ajump(500)
    a "Huh."
    "Malcolm lifted the previous plush in his arms, "
    m"Yours.{w=.25} The polyester fiberfill is clumped."
    hide m_smile_o

    show m_explain at mjump(200)
    m "Low quality filling compacts over the time."
    m "This one has a more even fibre dispersion... which means it can maintain its shape for longer."
    hide m_explain
    show m_think at mjump(200)#
    hide a_explain
    show a_tsun at ajump(500)
    "Malcolm points to the poor shark in the girls hands."
    m "He will develop... asymmetry."
    "Adeline stares at him, delightfully baffled."
    show a_tsuno at ajump(500)
    a "What, are you some plushie God or something?"
    m "..."
    hide m_think
    show m_smile_c at mjump(200)
    "Slowly, Malcolm leans into her face, holding the superior shark in her face." 
    scene a_kiss_neu with dissolve
    m "Rawr."
    a "AH!"
    a "Hehe ;3"
    "She fake screamed, giggling heavily as she grabbed his wrist instinctively."
    "It lingered there, much longer than she needed."
    "They stopped for a second."
    "Eyes lost into an endless maze of comfort and longing."
    show a_kiss_blush with dissolve
    a "Oh wow you’re smiling."
    m "Possibly."
    m "Am I incapable of showing joy..?"
    a "Ok I never said that!"
    "Her hand still remained on his wrist, her thumb slowly rubbing shapes against his pulse."
    "Her eyes watched him carefully as his gazed dropped for a second to capture a glimpse of her full lips."
    hide a_kiss_blush with dissolve
    a "Malcolm.."
    "Slowly, he leaned closer, intentionally this time."
    "Her breath warmly lingering on his skin, lips parting as if on command…"
    show a_kiss_neu:
        linear 60 zoom 1
    pause 2
    c "Seal Life aquarium once again asks you to not take flash photography in the exhibits."
    c "Thank you and Have a hydrated day."
    m "Is this all you want."
    a "Huh?"
    m "The shark..."
    a "OH! hehe" 
    "Her grasp loosened as she came back to her senses."
    a"Can I get that lobster too..."
    m "Sure."
    "He lips pulled into a warm smile before taking the 2 little creatures to the self serve till.."
    scene gif with dissolve
    show light zorder 100 with dissolve
    show a_blush_eo_mo
    a"{i}He was so close… I wish.{/i}"
    a "{i}I want to kiss him..{/i}"
    "He turned back to her, indicating it was time to go.."
    "Side by Side, they left the aquarium."
    scene black with dissolve
    show street_m  with dissolve
    show light zorder 100 with dissolve
    show m_smile_o at mjump (-1)
    m "That was fun."
    hide m_smile_o
    show m_smile_c at mjump(-1)
    m "..."
    hide m_smile_c
    show m_smile_o at mjump (-1)
    m "Thank you."
    hide m_smile_o
    show  m_smile_c at mjump(-1)
    "Adeline's hands gripped onto the hem of her blouse."
    show a_blush_ec_mo at ajump(600) with dissolve
    a "Yeah…. I really enjoyed m—myself and the fishies."
    a "Um."
    "..."
    hide a_blush_ec_mo
    show a_shame_c at ajump(600)
    "He looked away, rubbing the back of his head.."
    hide m_smile_c
    show m_disappointed at mjump(-1)
    m "I guess this is goodbye then. "
    m"I hope this made up for the café incident."
    hide m_disappointed
    show m_neu at ts_flipX(-1, -1, 1)
    "He turns around, getting ready to leave - but -"
    hide a_shame_c
    show a_shame_c at ajump(250)
    "tug."
    hide a_shame_c
    show a_flus at ajump(250)
    "Adeline looked down blushing heavily.."
    "Her knocked knees rubbing up against each other as the nerves threatened to overtake her."
    a "I— Uhm." 

    hide a_flus
    show a_flus at ts_acShake(250,5,0.1)
    a"I really hand fun.. we don’t need to end so early."
    
    "He looks down, extremely glad."
    hide m_neu
    show m_blushed_open at mjump(-1)
    m "Do you want to come over?"
    scene black with dissolve


    




    




    jump fuck