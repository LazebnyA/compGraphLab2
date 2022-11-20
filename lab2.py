from PIL import Image, ImageDraw

image = Image.new("RGBA", (960, 540), 'white')    

draw = ImageDraw.Draw(image)

with open('C:\compGraphics\compGraphLab2\DS4.txt', 'r') as file:  # в першому аргументі потрібно змінити шлях, на відповідний шлях до файлу DS4.txt

    for line in file:
        coordinatesTuple = (int(line[0:3]), int(line[4:7]))
        draw.point(coordinatesTuple, (0, 0, 0))

del draw
image.save("C:\compGraphics\compGraphLab2\img.png", "PNG")  # в першому аргументі потрібно змінити/поставити шлях, по якому ви хочете зберегти зображення і відповідно назву файлу
        





