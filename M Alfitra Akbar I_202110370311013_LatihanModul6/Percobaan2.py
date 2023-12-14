from PIL import Image
# TODO 1 :
background_image = Image.open("E:\TUGAS\Kuliah\Semester 5\Pemrograman Fungsional K\Praktikum\Modul 6\Latihan\pemandangan.jpg")
overlay_image = Image.open("E:\TUGAS\Kuliah\Semester 5\Pemrograman Fungsional K\Praktikum\Modul 6\Latihan\pngtree-isolated-tree-on-transparent-background.-png-image_4414355.jpg")

# TODO 2 : Konversi overlay image ke mode RGB 
overlay_image = overlay_image.convert("RGB")

# TODO 3 :  Perkecil ukuran gambar overlay 
new_size = (overlay_image.width // 4, overlay_image.height // 4)
overlay_image = overlay_image.resize(new_size)

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2

# TODO 4 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center))

# TODO 5 : Simpan gambar hasil edit
background_image.save("hasil.jpg")

# TODO 6 : Tampilkan
background_image.show()
