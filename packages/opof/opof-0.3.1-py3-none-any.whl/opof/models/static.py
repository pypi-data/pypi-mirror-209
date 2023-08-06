from typing import Any, Generic, List, Optional, Tuple, TypeVar

from torch import Tensor

from ..generator import Generator

Problem = TypeVar("Problem")


class StaticGenerator(Generic[Problem], Generator[Problem]):
    """
    :class:`StaticGenerator` represents a generator :math:`G_\\theta(c)` that returns
    fixed parameters :math:`x \\in \\mathcal{X}` and extra objects for any
    given problem instance.
    """

    parameters: List[Tensor]
    extras: List[Any]

    def __init__(self, parameters: List[Tensor], extras: List[Any]):
        """
        Constructs a :class:`StaticGenerator` with fixed parameters and extra objects.

        :param parameters: Fixed parameters
        :param extras: Fixed extra objects.
        """
        super(StaticGenerator, self).__init__()
        self.parameters = parameters
        self.extras = extras

    def forward(
        self, problem: List[Problem]
    ) -> Tuple[List[Tensor], Optional[Tensor], List[List[Any]]]:
        parameters = []
        extras = []
        for p in self.parameters:
            parameters.append(p.repeat(len(problem), *[1 for _ in p.shape]))
        if len(self.extras) > 0:
            for e in self.extras:
                extras.append([e for _ in problem])
        return (parameters, None, extras)
