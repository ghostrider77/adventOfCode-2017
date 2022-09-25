import operator

from collections import namedtuple

Condition = namedtuple("Condition", ["register", "operator", "value"])
Instruction = namedtuple("Action", ["register", "instruction", "value", "condition"])


def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def get_operator(operator_string):
    if operator_string == "==":
        return operator.eq

    if operator_string == "!=":
        return operator.ne

    if operator_string == ">":
        return operator.gt

    if operator_string == ">=":
        return operator.ge

    if operator_string == "<":
        return operator.lt

    if operator_string == "<=":
        return operator.le

    raise ValueError(f"Unknown operator {operator_string}")


def read_instructions(data):
    instructions = []
    for instruction, condition in map(lambda x: x.split("if "), data):
        register, change, value = instruction.split()
        register_to_check, operator_string, comparison_value = condition.split()
        operator = get_operator(operator_string)
        item = Instruction(register, change, int(value), Condition(register_to_check, operator, int(comparison_value)))
        instructions.append(item)
    return instructions


def run_program(instructions):
    registers = {}
    max_value = 0
    for instruction in instructions:
        condition = instruction.condition
        if condition.operator(registers.get(condition.register, 0), condition.value):
            current_register_value = registers.get(instruction.register, 0)
            if instruction.instruction == "inc":
                value = current_register_value + instruction.value
            else:
                value = current_register_value - instruction.value

            registers[instruction.register] = value
            if value > max_value:
                max_value = value

    return max_value


def main():
    data = read_input_data("../resources/input_08.txt")
    instructions = read_instructions(data)
    result = run_program(instructions)
    print(result)


if __name__ == "__main__":
    main()
