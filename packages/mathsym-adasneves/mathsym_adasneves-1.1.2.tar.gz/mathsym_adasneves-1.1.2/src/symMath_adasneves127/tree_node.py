      
class tree_node:
    def __init__(self, type, value, precedence):
        self.value = value
        self.type = type
        self.prec = precedence
        self.parent: None | tree_node = None
        self.left_child: None | tree_node  = None
        self.right_child: None | tree_node = None
        
    def print(self):
        if self.left_child is None or self.right_child is None:
            print(self.value, end="")
            return
        else:
            print("(", end="")
            self.left_child.print()
            print(self.value, end="")
            self.right_child.print()
            print(")", end="")
            
    def evaluate(self, x: int | float) -> float | None:
        """Evaluate the function at some given value of X
        :param x: The value to evaluate the function at
        :returns: Float value of the function at X, or None if the operation was undefined at X."""
        if self.left_child is None and self.right_child is None:
            if self.type == "VARIABLE":
                return x
            return float(self.value)
        else:
            if self.left_child is None or self.right_child is None:
                raise TypeError(f"Node {self.type} has invalid children. Was the equation valid?")
            
            left_result = self.left_child.evaluate(x)
            right_result = self.right_child.evaluate(x)
            if left_result is None or right_result is None:
                return None
            
            match self.type:
                case "PLUS":
                    return left_result + right_result
                case "MINUS":
                    return left_result - right_result
                case "MULTIPLICATION":
                    return left_result * right_result
                case "DIVISION":
                    try:
                        return left_result / right_result
                    except ZeroDivisionError:
                        return None                         # If the process results in: n/0, return None, as it is not a valid operation.
                case "EXPONENT":
                    return left_result ** right_result
                case other:  # noqa: F841
                    return 0
                
    def instantaneous_slope(self, x):
        y_1 = self.evaluate(x + 0.0000000001) # Evaluate the function at a x value to the right.
        y_2 = self.evaluate(x) # Evaluate the function at the current X pos
        
        if y_2 is not None and y_1 is not None:
            return (y_2 - y_1)/(0.0000000001)
        else:
            return None
        