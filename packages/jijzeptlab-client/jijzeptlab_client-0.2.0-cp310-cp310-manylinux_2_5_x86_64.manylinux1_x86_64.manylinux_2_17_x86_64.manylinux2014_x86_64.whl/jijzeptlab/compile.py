import typing as typ
import dataclasses
import jijmodeling as jm

from jijzeptlab.jijzeptlab import (
    FixedVariables as FixedVariables,
    InstanceData as InstanceData,
)
from jijzeptlab.utils.baseclass import Option as Option
import jijmodeling.transpiler as jmt


class CompileOption(Option):
    needs_normalize: bool = False


class CompiledInstance:
    compile_option: CompileOption
    problem: jm.Problem
    instance_data: InstanceData
    fixed_variables: FixedVariables

    def __init__(
        self,
        engine_instance,
        compile_option: CompileOption,
        problem: jm.Problem,
        instance_data: InstanceData,
        fixed_variables: FixedVariables,
    ) -> None:
        self._instance = engine_instance
        self.compile_option = compile_option
        self.problem = problem
        self.instance_data = instance_data
        self.fixed_variables = fixed_variables

    def append_constraint(self, constraint: jm.Constraint, instance_data: InstanceData):
        pass


def compile_model(
    problem: jm.Problem,
    instance_data: InstanceData,
    fixed_variables: typ.Optional[FixedVariables] = None,
    option: typ.Optional[CompileOption] = None,
) -> CompiledInstance:
    """Compile a problem

    Args:
        problem (jm.Problem): Problem to be compiled
        instance_data (InstanceData): Instance data
        fixed_variables (FixedVariables, optional): Fixed variables. Defaults to None.
        option (CompileOption, optional): Compile option. Defaults to None.

    Returns:
        CompiledInstance: Compiled instance
    """

    from jijzeptlab.process.process import BackendProcess

    _option: CompileOption
    if option is not None:
        _option = option
    else:
        _option = CompileOption()

    _fixed_vars: FixedVariables
    if fixed_variables is None:
        _fixed_vars = FixedVariables()
    else:
        _fixed_vars = fixed_variables

    return BackendProcess.compile_model(problem, instance_data, _fixed_vars, _option)
