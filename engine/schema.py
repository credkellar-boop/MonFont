from pydantic import BaseModel, Field

class FontParameters(BaseModel):
    font_name: str = Field(..., description="The unique name generated for the typeface.")
    weight: int = Field(..., description="Font weight value from 100 (Thin) to 900 (Black).", ge=100, le=900)
    slant: float = Field(..., description="Italic slant angle in degrees. 0 for upright, up to 15 for cursive.", ge=0, le=15)
    serif_style: str = Field(..., description="Type of serifs: 'sans-serif', 'serif', 'slab-serif', or 'display'.")
    contrast: float = Field(..., description="Ratio between thick and thin strokes, from 1.0 (monoline) to 4.0 (high contrast).", ge=1.0, le=4.0)
    x_height: float = Field(..., description="Height of lowercase letters relative to uppercase, from 0.5 to 0.8.", ge=0.5, le=0.8)
    roundness: float = Field(..., description="Corner rounding factor for glyph curves, from 0.0 (sharp) to 1.0 (fully round).", ge=0.0, le=1.0)
