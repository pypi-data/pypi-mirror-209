

def Init(FML_TITLE,FML_WIDTH,FML_HIEGHT):
    #IMPORTS#
    import sdl2,sdl2.ext
    #CREATE WINDOW#
    sdl2.ext.init()

    WINDOW = sdl2.ext.Window(FML_TITLE, size=(FML_WIDTH,FML_HIEGHT))
    WINDOW.show()

    return WINDOW
def Render(FML_WINDOW):
    #IMPORTS#
    import sdl2,sdl2.ext
    #UPDATE WINDOW#
    processor = sdl2.ext.TestEventProcessor()
    FML_WINDOW.show()
    FML_WINDOW.refresh()
    #UPDATE UserExiting#

def UserExiting():
    #IMPORTS#
    import sdl2,sdl2.ext
    #CHECK FOR USER EXITING#
    EVENTS = sdl2.ext.get_events()
    for EVENT in EVENTS:
        if EVENT.type == sdl2.SDL_QUIT:
            return True
def Quit():
    #IMPORTS#
    import sdl2,sdl2.ext
    #QUITING#
    sdl2.ext.quit()

    

