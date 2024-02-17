from PIL import Image, ImageDraw, ImageFont

print('Генератор мемов запущен!')
print('Список картинок: ')
print('1. Кот в ресторане ')
print('2. Кот в очках')
image = int(input('Введи номер нужной картинки: '))
if image == 1:
    image_file = 'Кот в ресторане.png'
elif image == 2:
    image_file = 'Кот в очках.png'

top_text = input('Введи верхний текст: ')
bottom_text = input('Введи нижний текст: ')


image = Image.open(image_file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=70)

text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]
text_height = text[3]


draw.text(((width - text_width) / 2, 30), top_text, font=font, fill='black')

text = draw.textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]


draw.text(((width - text_width) / 2,height - text_height - 60), bottom_text, font=font, fill = 'black')


image.save('new_meme.jpg')
