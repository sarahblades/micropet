def play():
    global lonely, times_played_with, dead, sleeping
    if not dead and not sleeping:
        soundExpression.happy.play()
        lonely = False
        times_played_with += 1
input.on_button_pressed(Button.A, play)

def sleep():
    global sleeping, lonely, happy, dead, hungry, hunger_level
    if sleeping == True:
        sleeping = False
        music.stop_all_sounds()
        dead = False 
        lonely = False
        hungry = False
        happy = True
    elif sleeping == False:
        sleeping = True
        hunger_level = 0
input.on_button_pressed(Button.AB, sleep)

def feed():
    global dead, hungry, hunger_level, sleeping, times_fed
    if not sleeping:
        if dead:
            basic.show_icon(IconNames.HEART)
            music.play_melody("C D E F G A B C5 ", 500)
        else:
            basic.show_icon(IconNames.SMALL_HEART)
            if hunger_level <= 1:
                music.play_melody("C D E - - - - - ", 500)
            if hunger_level == 2:
                music.play_melody("C D E F - - - - ", 500)
            if hunger_level == 3:
                music.play_melody("C D E F G - - - ", 500)
            if hunger_level == 4:
                music.play_melody("C D E F G A - - ", 500)
        dead = False
        hungry = False
        hunger_level = 0
        times_fed += 1
input.on_button_pressed(Button.B, feed)

def reset_guesses():
    global guesses
    guesses = 0
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, reset_guesses)

def game():
    global guesses
    global playing
    random_number = 0
    if not dead and not sleeping:
        playing = True
        random_number = randint(1, 9)
        guesses += 1
    if random_number == 1:
        images.create_image("""
         . # # . .
         # . # . .
         . . # . .
         . . # . .
         . . # . .
         """).show_image(0)
        
    
    elif random_number == 2:
        images.create_image("""
            . # # . .
            # . . # .
            . . # . .
            . # . . .
            # # # # .
            """).show_image(0)

    elif random_number == 3:
            images.create_image("""
            . # # . .
            # . . # .
            . . # . .
            # . . # .
            . # # . .
            """).show_image(0)

    elif random_number == 4:
            images.create_image("""
            # . . . .
            # . # . .
            # # # # .
            . . # . .
            . . # . .
            """).show_image(0)
    elif random_number == 5:
            images.create_image("""
            # # # # .
            # . . . .
            # # # . .
            . . . # .
            # # # . .
            """).show_image(0)

    elif random_number == 6:
            images.create_image("""
            . . . # .
            . . # . .
            . # # # .
            # . . . #
            . # # # .
            """).show_image(0)

    elif random_number == 7:
            images.create_image("""
            # # # # #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            """).show_image(0)

    elif random_number == 8:
            images.create_image("""
            . # # # .
            # . . . #
            . # # # .
            # . . . #
            . # # # .
            """).show_image(0)

    elif random_number == 9:
            images.create_image("""
            . # # # .
            # . . . #
            . # # # .
            . . # . .
            . # . . .
            """).show_image(0)

input.on_logo_event(TouchButtonEvent.PRESSED, game)

def shake():
    global dead, sleeping, shaking
    if not dead and not sleeping:
        shaking = True
        images.create_image("""
                    . . . . .
                            . . . . .
                            . # # # .
                            . # . # .
                            . # # # .
            """).show_image(0)
        soundExpression.giggle.play_until_done()
input.on_gesture(Gesture.SHAKE, shake)

def tilt_left():
    global dead, sleeping
    if not dead and not sleeping:
        images.create_image("""
                        . . . . .
                        . . . . .
                        . . . . .
                        . # . # .
                        # . # . #
                    """).show_image(0)
        soundExpression.mysterious.play()
input.on_gesture(Gesture.TILT_LEFT, tilt_left)

def tilt_right():
    global dead, sleeping
    if not dead and not sleeping:
        images.create_image("""
                        . . . . .
                        . . . . .
                        . . . . .
                        . # . # .
                        # . # . #
                    """).show_image(0)
        soundExpression.mysterious.play()
input.on_gesture(Gesture.TILT_RIGHT, tilt_right)


number_of_deaths = 0
hunger_level = 0
times_played_with = 0
times_fed = 0
guesses = 0

playing = False
shaking = False

dead = False
hungry = False
sleeping = True
lonely = False
happy = True

startup = True

def on_forever():
    global happy, startup, playing, sleeping, lonely, hungry, dead
    while sleeping == True:
        images.create_image("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # # # # #
        """).show_image(0)
        soundExpression.yawn.play()
    if lonely == False and hungry == False:
        happy = True
    else:
        happy = False
    if playing == True or shaking == True:
            basic.pause(3000)
            playing = False
            shaking = False
    if dead == True:
        basic.show_icon(IconNames.GHOST)
    elif happy == True:
        images.create_image("""
            . . . . .
                        . . . . .
                        . . . . .
                        # . . . #
                        . # # # .
        """).show_image(0)
    else:
        images.create_image("""
            . . . . .
                        . . . . .
                        . . . . .
                        . # # # .
                        # . . . #
        """).show_image(0)
    startup = False
basic.forever(on_forever)

def on_every_interval():
    global lonely, startup, dead
    if startup == True:
        pass
    else:
        if not dead:
            lonely = True
            soundExpression.sad.play()
loops.every_interval(15000, on_every_interval)

def on_every_interval2():
    global sleeping
    sleeping = True
loops.every_interval(1000000, on_every_interval2)

def on_every_interval3():
    global hunger_level, dead, number_of_deaths, hungry
    if not dead:
        hunger_level += 1
    if hunger_level >= 5:
        dead = True
        number_of_deaths += 1
    elif hunger_level >= 3:
        hungry = True
loops.every_interval(5000, on_every_interval3)

