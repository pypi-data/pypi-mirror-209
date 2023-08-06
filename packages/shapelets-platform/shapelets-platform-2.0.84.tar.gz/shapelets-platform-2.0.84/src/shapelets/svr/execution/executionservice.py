# Copyright (c) 2022 Shapelets.io
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
import base64
from typing import Any
import dill

from .iexecutionrepo import IExecutionRepo
from .iexecutionservice import IExecutionService

from ..model.function import FunctionProfile


class ExecutionService(IExecutionService):
    __slots__ = ('_execution_repo',)

    def __init__(self, execution_repo: IExecutionRepo) -> None:
        self._execution_repo = execution_repo

    def execute_function(self, fn: FunctionProfile) -> Any:
        callable_fn = dill.loads(base64.decodebytes(bytes(fn.body, encoding="utf-8")))
        arg_values = []
        for arg in fn.parameters:
            if arg.get('pickled'):
                arg_values.append(dill.loads(base64.decodebytes(bytes(arg.get('value'), encoding="utf-8"))))
            else:
                # Value was not serialized
                arg_values.append(arg.get('value'))
        result = callable_fn(*arg_values)
        return result
