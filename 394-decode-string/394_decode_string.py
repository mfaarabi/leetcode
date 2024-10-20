


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        for ch in s:
            if ch.isdigit():
                stack.append(int(ch))
            elif ch == "[":
                continue
            elif ch == "]":
                mult = ""
                arr = stack.pop()
                times = stack.pop()
                mult = mult.join(arr * times)
                if stack and isinstance(stack[-1], list):
                    stack[-1].append(mult)
                else:
                    res += mult
            else:
                if stack and isinstance(stack[-1], int):
                    stack.append([ch])
                elif stack:
                    stack[-1].append(ch)
                else:
                    res += ch

        return res

if __name__ == "__main__":
    solution = Solution()
    # result = solution.decodeString("3[aa]")
    # result = solution.decodeString("3[a2[c]]")
    result = solution.decodeString("2[abc]3[cd]ef")
    print(result)