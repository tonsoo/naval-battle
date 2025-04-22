from pathlib import Path
import pygame


class FontWeight:
    def __init__(self, filename: str, font: 'Font'):
        self.filename = filename
        self.font = font

    def load(self, size: int = 24):
        full_path = Path(self.font.path) / self.filename
        if not full_path.exists():
            raise FileNotFoundError(f"Font file not found: {full_path}")
        return pygame.font.Font(str(full_path), size)


class FontWeights:
    def __init__(self, font: 'Font', **weights):
        self._font = font
        self.w100 = FontWeight(weights.get('w100', ''), font) if 'w100' in weights else None
        self.w200 = FontWeight(weights.get('w200', ''), font) if 'w200' in weights else None
        self.w300 = FontWeight(weights.get('w300', ''), font) if 'w300' in weights else None
        self.w400 = FontWeight(weights.get('w400', ''), font) if 'w400' in weights else None
        self.w500 = FontWeight(weights.get('w500', ''), font) if 'w500' in weights else None
        self.w600 = FontWeight(weights.get('w600', ''), font) if 'w600' in weights else None
        self.w700 = FontWeight(weights.get('w700', ''), font) if 'w700' in weights else None
        self.w800 = FontWeight(weights.get('w800', ''), font) if 'w800' in weights else None
        self.w900 = FontWeight(weights.get('w900', ''), font) if 'w900' in weights else None

    def get(self, weight: str) -> FontWeight:
        """Returns the requested weight, or fallback to closest available."""
        requested = getattr(self, weight, None)
        if requested:
            return requested

        # fallback search
        order = ['w100', 'w200', 'w300', 'w400', 'w500', 'w600', 'w700', 'w800', 'w900']
        if weight not in order:
            raise AttributeError(f"Unknown weight: {weight}")

        idx = order.index(weight)
        for offset in range(1, len(order)):
            for direction in (-1, 1):
                i = idx + direction * offset
                if 0 <= i < len(order):
                    fallback = getattr(self, order[i])
                    if fallback:
                        return fallback

        raise ValueError(f"No available fallback for weight '{weight}'.")


class Font:
    def __init__(self, path: str, **weights: str):
        self.path = path
        self.weights = FontWeights(self, **weights)

        # Provide direct shortcuts like .w400, .w700
        for key in ['w100', 'w200', 'w300', 'w400', 'w500', 'w600', 'w700', 'w800', 'w900']:
            setattr(self, key, getattr(self.weights, key))


class Fonts:
    DM_SANS = Font(
        'assets/fonts/dm-sans',
        w400='DMSans-Regular.ttf',
        w700='DMSans-Bold.ttf',
    )
