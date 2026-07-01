from dataclasses import dataclass, field

from .slide import Slide
from .statistics import Statistics


@dataclass(slots=True)
class Presentation:
    """
    Representa uma apresentação completa.
    """

    title: str = ""

    slides: list[Slide] = field(default_factory=list)

    statistics: Statistics = field(
        default_factory=Statistics
    )

    def add_slide(
        self,
        slide: Slide
    ):

        self.slides.append(slide)

    @property
    def total_slides(self):

        return len(self.slides)