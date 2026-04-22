define l = Character("Lin")

define n = Character("Nil")

define c = Character("Customer")

define e = Character("Eileen")

$linSign = ""

label start:

    "what a beautiful day..."

    show nil
    with fade

    c "Hello, I'd like an espresso"

    l "Ok, sir.."

    "....isn't he..."

    with fade

    l "..."

    l "here's your Espresso, sir..."

    show espresso

    c "Thank you!"

    menu:
        "that is a unique pendant":
            jump talk
        "that'll be 30 keas":
            jump noTalk

    
label noTalk:
    c "okay, here"

    l "Thank you, have a nice day..."

    hide nil
    show nil happy

    c "you too!"

    hide nil
    return

label talk:
    c "..."

    hide nil
    hide espresso
    show nil looking down
    show espresso

    c "oh"

    hide nil looking down
    hide espresso
    show nil
    show espresso

    c "thanks, it's dear to me"

    l "Oh, i see..."

    c "..."

    c "this is break time, right?"

    l "yes, sir"

    c "okay..."

    # nil sits down

    l "..."

    l "what is your name sir?"

    c "oh, it's Nil"

    l "oh"

    l "oh, Nil.."

    hide nil
    hide espresso
    show nil looking down
    show espresso

    n "yup"

    n "what is your name?"

    hide nil looking down
    hide espresso
    show nil
    show espresso

    l "I'm.."

    l "..."

    l "..Lin"

    hide nil
    hide espresso
    show nil happy
    show espresso

    n "Nice to meet you Lin"

    l "Nice to meet you too, Nil"

    hide nil happy
    hide espresso
    show nil
    show espresso

    n "..."

    n "say.."

    n "..what would you choose as a sign of you?"

    n "Moon or a star?"

    $linSign = renpy.input(default = "Moon" , prompt = "What would you choose as your sign?")

    n "%(linSign)s , nice.."

    n "..."

    n "you know..."

    n "...this pendant"

    n "your choice of sign matters..."

    n "..."

    hide nil
    hide espresso
    show nil looking down

    n "well..."

    e "....lin..."

    e "...Lin.."

    e "Lin!"

    l "..oh?.."

    hide nil looking down
    show eiln
    with fade

    e "what are you doing?"

    l "Sorry, i was just talking to..Nil.."

    hide eiln
    with fade

    "..."

    play music "./music/theme-song.mp3" fadein 1.0 loop

    l "..."

    l "....."

    l ".."

    e "Huh? anyways, i need your help with the new machine"

    l "..."

    l "..sure.."




    

