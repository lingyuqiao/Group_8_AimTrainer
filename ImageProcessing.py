from PIL import Image
from PIL.ImageQt import ImageQt

# Resize the image to use
length = 1500
width = 800
# Resize the lobby the background
Lobby = Image.open('Lobby_background.png')
Lobby = Lobby.resize((length, width))
Lobby.save('Lobby_background.png')

Range = Image.open('shooting_range.png')
Range = Range.resize((length, width))
Range.save('shooting_range.png')

end = Image.open('game_over.png')
end = end.resize((length, width))
end.save('game_over.png')
