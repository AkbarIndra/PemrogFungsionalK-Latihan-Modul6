# TODO 0: Import necessary libraries
from PIL import Image, ImageDraw, ImageFont

# TODO 1: Load the image
gambarku = Image.open("E:\TUGAS\Kuliah\Semester 5\Pemrograman Fungsional K\Praktikum\Modul 6\Latihan\pemandangan.jpg")

# TODO 2: GrayScale IMG
gambarBW = gambarku.convert("L")

# TODO 3: Add text to the image
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype("arial.ttf", 24)
text = "M Alfitra Akbar I_202110370311013"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
text_x = (gambarBW.width - text_width) // 2
text_y = (gambarBW.height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill=255)

# TODO 4: Save the edited image
gambarBW.save("percobaan_satu.jpg")

# TODO 5: Show the final image
gambarBW.show()
