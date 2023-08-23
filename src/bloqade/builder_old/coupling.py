from bloqade.ir.control.pulse import detuning
from .base import Builder


class LevelCoupling(Builder):
    @property
    def detuning(self):
        """
        - Specify the Detuning field
        - Next-step: <SpacialModulation>
        - Possible Next:

            -> `...detuning.location(int)`
                :: Address atom at specific location

            -> `...detuning.uniform`
                :: Address all atoms in register

            -> `...detuning.var(str)`
                :: Address atom at location labeled by variable

        """
        from .field import Detuning

        self.__build_cache__.field_name = detuning
        return Detuning(self)

    @property
    def rabi(self):
        """
        - Specify the Rabi term/field.
        - Possible Next:

            -> `...rabi.amplitude`
                :: address rabi amplitude

            -> `...rabi.phase`
                :: address rabi phase


        """
        from .field import Rabi

        return Rabi(self)


class Rydberg(LevelCoupling):
    """
    This node represent level coupling of rydberg state.

    Examples:

        - To reach the node from the start node:

        >>> node = bloqade.start.rydberg
        >>> type(node)
        <class 'bloqade.builder.coupling.Rydberg'>

        - Rydberg level coupling have two reachable field nodes:

            - detuning term (See also [`Detuning`][bloqade.builder.field.Detuning])
            - rabi term (See also [`Rabi`][bloqade.builder.field.Rabi])

        >>> ryd_detune = bloqade.start.rydberg.detuning
        >>> ryd_rabi = bloqade.start.rydberg.rabi

    """

    pass


class Hyperfine(LevelCoupling):
    """
    This node represent level coupling between hyperfine state.

    Examples:

        - To reach the node from the start node:

        >>> node = bloqade.start.hyperfine
        >>> type(node)
        <class 'bloqade.builder.coupling.Hyperfine'>

        - Hyperfine level coupling have two reachable field nodes:

            - detuning term (See also [`Detuning`][bloqade.builder.field.Detuning])
            - rabi term (See also [`Rabi`][bloqade.builder.field.Rabi])

        >>> hyp_detune = bloqade.start.hyperfine.detuning
        >>> hyp_rabi = bloqade.start.hyperfine.rabi

    """

    pass