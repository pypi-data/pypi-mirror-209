import FML
import FML.Graphics as Graphics

Window = FML.Graphics.Window.Init("Hello World",500,500)

while WindowRunning:
  FML.Graphics.Window.Render(Window)
  if FML.Graphics.Window.UserExiting():
    FML.Graphics.Window.Quit()
    WindowRunning = False