from PIL import Image, ImageDraw, ImageFont
import os

class PreviewRenderer:
    @staticmethod
    def generate_preview(font_path: str, output_path: str, text: str = "MonFonts V1.0"):
        """Renders a text string using the newly synthesized font."""
        if not os.path.exists(font_path):
            raise FileNotFoundError("Compiled font not found.")

        # Create a blank 800x400 canvas
        img = Image.new('RGB', (800, 400), color=(15, 15, 15))
        draw = ImageDraw.Draw(img)

        try:
            # Load the dynamic font at 64px
            font = ImageFont.truetype(font_path, 64)
        except Exception:
            font = ImageFont.load_default()

        # Center the text on the canvas
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_w = text_bbox[2] - text_bbox[0]
        text_h = text_bbox[3] - text_bbox[1]
        
        x = (800 - text_w) / 2
        y = (400 - text_h) / 2

        # Draw the text in high-contrast white
        draw.text((x, y), text, font=font, fill=(255, 255, 255))
        img.save(output_path)
        return output_path
