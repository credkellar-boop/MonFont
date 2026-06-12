import math
from fontTools.pens.ttGlyphPen import TTGlyphPen
from engine.schema import FontParameters

class GlyphSynthesizer:
    def __init__(self, parameters: FontParameters):
        self.params = parameters
        self.upm = 1000  # Standard Units Per Em

    def apply_slant(self, x: float, y: float) -> tuple[float, float]:
        """Applies mathematical shear based on the requested italic slant."""
        if self.params.slant == 0:
            return x, y
        radians = math.radians(self.params.slant)
        new_x = x + (y * math.tan(radians))
        return new_x, y

    def draw_glyph(self, letter: str, base_topology: dict) -> object:
        """Draws a specific glyph using the FontTools Pen."""
        pen = TTGlyphPen(None)
        
        # Example logic: scaling the stem width based on the 'weight' parameter
        stem_width = (self.params.weight / 400.0) * 100 

        # The base_topology dict would contain the raw anchor points for 'letter'
        # Here we map them through the pen to create the vector paths
        for contour in base_topology.get(letter, []):
            pen.moveTo(self.apply_slant(*contour[0]))
            for point in contour[1:]:
                pen.lineTo(self.apply_slant(*point))
            pen.closePath()

        return pen.glyph()
