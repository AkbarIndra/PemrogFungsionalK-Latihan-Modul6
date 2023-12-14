from PIL import Image, ImageEnhance

image = Image.open("E:\TUGAS\Kuliah\Semester 5\Pemrograman Fungsional K\Praktikum\Modul 6\Latihan\pemandangan.jpg")

brightness_enhancer = ImageEnhance.Brightness(image)
brightened_image = brightness_enhancer.enhance(1.5)

contrast_enhancer = ImageEnhance.Contrast(brightened_image)
final_image = contrast_enhancer.enhance(1.2)

final_image.save("brightness_contrast_image.jpg")

final_image.show()
