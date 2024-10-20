


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        for ch in s:
            # print("current ch: " + ch)
            if ch.isdigit():
                # case: 100[
                if stack and isinstance(stack[-1], int):
                    stack[-1] = int(str(stack[-1]) + ch)
                else:
                    stack.append(int(ch))
            elif ch == "[":
                # case: 2[2
                stack.append(ch)
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
                if stack:
                    if isinstance(stack[-1], int):
                        stack.append([ch])
                    # case: 2[2
                    elif stack[-1] == "[":
                        stack.pop()
                        stack.append([ch])
                    else: 
                        stack[-1].append(ch)
                else:
                    res += ch
            # print(stack, res)

        return res

if __name__ == "__main__":
    solution = Solution()
    # result = solution.decodeString("3[aa]")
    # result = solution.decodeString("3[a2[c]]")
    # result = solution.decodeString("2[abc]3[cd]ef")
    # result = solution.decodeString("100[leetcode]")
    result = solution.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")
    print(result)