from PIL import Image, ImageDraw, ImageFont

class ImagesInputOutput():
    """
    Resize
    """
    def resize_image(self, input_image_path, output_image_path, size):
        original_image = Image.open(input_image_path)
        wpercent = (size / float(original_image.size[0]))
        hsize = int((float(original_image.size[1]) * float(wpercent)))
        resized_image = original_image.resize((size, hsize), Image.Resampling.LANCZOS)
        resized_image.save(output_image_path, quality=75)

    def watermark(self, input_image_path, input_font, input_text, output_image_path, fill, font_size):
        """
        Copyright

        """
     
        image_watermark = Image.open(input_image_path)
        width, height = image_watermark.size

        draw = ImageDraw.Draw(image_watermark)
        text =input_text

        font = ImageFont.truetype(input_font ,font_size)
        textwidth, textheight = draw.textsize(text, font)

        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        draw.text((x, y), text, font=font, fill=fill)

        image_watermark.save(output_image_path)