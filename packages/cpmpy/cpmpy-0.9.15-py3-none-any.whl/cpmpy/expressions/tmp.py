
        # sum and wsum special handling
        if self.name == "-" and isinstance(other, Operator):
            if other.name == "-":
                # -x + -y
                w = [-1, -1]
                x = [self.args[0], other.args[0]]
                return Operator("wsum", [w, x])
            elif other.name == "mul" and is_num(other.args[0]):
                # -x + 3*z
                w = [-1, other.args[0]]
                x = [self.args[0], other.args[1]]
                return Operator("wsum", [w, x])
            elif other.name == "sum":
                # -x + (y + z)
                w = [-1] + [1]*len(other.args)
                x = [self.args[0]] + other.args
                return Operator("wsum", [w, x])
            elif other.name == "wsum":
                # -x + sum([1,2]*[y,z])
                w = [-1] + other.args[0]
                x = [self.args[0]] + other.args[1]
                return Operator("wsum", [w, x])
        elif self.name == "mul" and is_num(self.args[0]) and isinstance(other, Operator):
            if other.name == "-":
                # 2*x + -y
                w = [self.args[0], -1]
                x = [self.args[1], other.args[0]]
                return Operator("wsum", [w, x])
            elif other.name == "mul" and is_num(other.args[0]):
                # 2*x + 3*z
                w = [self.args[0], other.args[0]]
                x = [self.args[1], other.args[1]]
                return Operator("wsum", [w, x])
            elif other.name == "sum":
                # 2*x + (y + z)
                w = [self.args[0]] + [1]*len(other.args)
                x = [self.args[1]] + other.args
                return Operator("wsum", [w, x])
            elif other.name == "wsum":
                # 2*x + sum([1,2]*[y,z])
                w = [self.args[0]] + other.args[0]
                x = [self.args[1]] + other.args[1]
                return Operator("wsum", [w, x])
        elif self.name == 'sum' and isinstance(other, Operator):
            if other.name == "-":
                # (x+w) + -y
                w = [1]*len(self.args) + [-1]
                x = self.args + [other.args[0]]
                return Operator("wsum", [w, x])
            elif other.name == "mul" and is_num(other.args[0]):
                # (x+w) + 3*z
                w = [1]*len(self.args) + [other.args[0]]
                x = self.args + [other.args[1]]
                return Operator("wsum", [w, x])
            elif other.name == "sum":
                # (x+w) + (y + z)
                # SPECIAL CASE
                x = self.args + other.args
                return Operator("sum", x)
            elif other.name == "wsum":
                # (x+w) + sum([1,2]*[y,z])
                w = [1]*len(self.args) + other.args[0]
                x = self.args + other.args[1]
                return Operator("wsum", [w, x])
            else:
                # (x+w) + e
                # SPECIAL CASE
                x = self.args + [other]
                return Operator("sum", x)
        elif self.name == 'wsum' and isinstance(other, Operator):
            if other.name == "-":
                # sum([3,4]*[w,x]) + -y
                w = self.args[0] + [-1]
                x = self.args[1], other.args[0]]
                return Operator("wsum", [w, x])
            elif other.name == "mul" and is_num(other.args[0]):
                # sum([3,4]*[w,x]) + 3*z
                w = self.args[0] + [other.args[0]]
                x = self.args[1] + [other.args[1]]
                return Operator("wsum", [w, x])
            elif other.name == "sum":
                # sum([3,4]*[w,x]) + (y + z)
                w = self.args[0] + [1]*len(other.args)
                x = self.args[1] + other.args
                return Operator("wsum", [w, x])
            elif other.name == "wsum":
                # sum([3,4]*[w,x]) + ([1,2]*[y,z])
                w = self.args[0] + other.args[0]
                x = self.args[1] + other.args[1]
                return Operator("wsum", [w, x])

