from dataclasses import dataclass, field
from typing import List, Optional

from .slide import Slide
from .statistics import SpeechStatistics


@dataclass
class Presentation:
    """
    Representa toda a apresentação.
    """

    title: Optional[str] = None

    slides: List[Slide] = field(default_factory=list)

    statistics: SpeechStatistics = field(
        default_factory=SpeechStatistics
    )

    def add_slide(self, slide: Slide):
        self.slides.append(slide)

    def get_slide(self, index: int) -> Optional[Slide]:
        if 0 <= index < len(self.slides):
            return self.slides[index]
        return None

    def total_slides(self) -> int:
        return len(self.slides)