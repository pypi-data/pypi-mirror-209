from functools import partial
from typing import Callable

from elasticai.creator.hdl.code_generation.template import (
    InProjectTemplate,
    module_to_package,
)
from elasticai.creator.hdl.design_base.design import Design, Port
from elasticai.creator.hdl.design_base.signal import Signal
from elasticai.creator.hdl.savable import Path


class _PrecomputedMonotonouslyIncreasingScalarFunction(Design):
    _template_package = module_to_package(__name__)

    def __init__(
        self,
        name: str,
        width: int,
        function: Callable[[int], int],
        inputs: list[int],
    ) -> None:
        super().__init__(name)
        self._width = width
        self._function = function
        self._inputs = inputs
        self._io_pairs: dict[int, int] = dict()
        self._template = InProjectTemplate(
            file_name="precomputed_monotonously_increasing_scalar_function.tpl.vhd",
            package=self._template_package,
            parameters=dict(name=self.name, data_width=str(width)),
        )

    def _compute_io_pairs(self) -> None:
        inputs_in_descending_order = sorted(self._inputs, reverse=True)
        for number in inputs_in_descending_order:
            self._io_pairs[number] = self._function(number)

    def _get_io_pairs(self) -> dict[int, int]:
        if len(self._io_pairs) == 0:
            self._compute_io_pairs()
        return self._io_pairs

    @property
    def port(self) -> Port:
        signal = partial(Signal, width=self._width)
        return Port(
            incoming=[signal(name="x")],
            outgoing=[signal(name="y")],
        )

    def save_to(self, destination: Path):
        process_content = []
        pairs = list(self._io_pairs.items())
        for input, output in pairs[0:1]:
            process_content.append(
                f"if signed_x <= {input} then signed_y <= to_signed({output},"
                f" {self._width});"
            )
        for input, output in pairs[1:-1]:
            process_content.append(
                f"if signed_x <= {input} then signed_y <= to_signed({output},"
                f" {self._width});"
            )
        for _, output in pairs[-2:-1]:
            process_content.append(
                f"else signed_y <= to_signed({output}, {self._width});\nend if;"
            )
        self._template.parameters.update(process_content=process_content)
        destination.as_file(".vhd").write(self._template)
