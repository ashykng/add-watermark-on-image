from PIL import Image

margin_size = 20

# image's path
main_image = Image.open(r"")

# logo's path
watermark = Image.open("")

watermark_size = (int(watermark.size[0] * .3), int(watermark.size[1] * .3))

watermark = watermark.resize(watermark_size, resample=Image.LANCZOS)

position = (0, main_image.size[1] - watermark.size[1])
position = (margin_size, main_image.size[1] - watermark.size[1] - margin_size)
main_image.paste(watermark, position, mask=watermark)

main_image.save("watermarked_image.jpg")