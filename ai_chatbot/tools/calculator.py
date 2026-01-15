from langchain.tools import BaseTool
from math import sqrt, pi
from typing import Union


class CalculatorTool(BaseTool):
    name = "calculator"
    description = (
        """
        Use this tool to perform simple math operations like 
        "addition, subtraction, multiplication, division, square root 
        and circle circumference.
        """
    )

    def _run(
        self,
        operation: str,
        a: Union[int, float],
        b: Union[int, float] | None = None
    ) -> float:
        operation = operation.lower()

        if operation == "add":
            return a + b

        if operation == "subtract":
            return a - b

        if operation == "multiply":
            return a * b

        if operation == "divide":
            return a / b

        if operation == "sqrt":
            return sqrt(a)

        if operation == "circumference":
            return 2 * pi * a

        raise ValueError("Unsupported operation")

    async def _arun(self, *args, **kwargs):
        raise NotImplementedError("Async not supported")

tool = CalculatorTool()

tool._run("add", 2, 3)              
tool._run("sqrt", 16)               
tool._run("circumference", 7.81)    

