class Solution:
    def parse_not(self, bool_list: List[str]) -> str:
        bool_map = {'t': True, 'f': False}
        if len(bool_list) == 1: result = not bool_map[bool_list.pop()]

        if len(bool_list) > 1: result = bool_map[bool_list.pop()]
        while bool_list:
            result != bool_map[bool_list.pop()]

        return 't' if result == True else 'f'

    def parse_and(self, bool_list: List[str]) -> str:
        bool_map = {'t': True, 'f': False}
        result = bool_map[bool_list.pop()]
        while bool_list:
            result &= bool_map[bool_list.pop()]
        return 't' if result == True else 'f'

    def parse_or(self, bool_list: List[str]) -> str:
        bool_map = {'t': True, 'f': False}
        result = bool_map[bool_list.pop()]
        while bool_list:
            result |= bool_map[bool_list.pop()]
        return 't' if result == True else 'f'
    
    def parse(self, first_stack: List[str], second_stack: List[str]) -> str:
        operator = first_stack.pop()
        bool_list = []
        
        for i in range(len(second_stack)-1, -1, -1):
            if second_stack[i] == '(':
                second_stack.pop()
                break
            bool_list.append(second_stack.pop())

        if operator == '!':
            parse_result = self.parse_not(bool_list)
        elif operator == '&':
            parse_result = self.parse_and(bool_list)
        else:
            parse_result = self.parse_or(bool_list)
        
        return parse_result


    def parseBoolExpr(self, expression: str) -> bool:
        first_stack = [] # contains the operators (&, |)
        second_stack = [] # contains the bools ('t', 'f', '(')

        for i in range(len(expression)):
            if expression[i] == '&' or expression[i] == '|' or expression[i] == '!':
                first_stack.append(expression[i])
            elif expression[i] == ',':
                continue
            else:
                if expression[i] == ')':
                    parse_result = self.parse(first_stack, second_stack)
                    second_stack.append(parse_result)
                else:
                    second_stack.append(expression[i])
        
        return True if second_stack[-1] == 't' else False
