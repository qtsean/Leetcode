class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        else:
            return " ".join(self.help(num))

    def help(self, num):
        if num == 0:
            return []
        below20 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                   "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        below100 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        if num < 20:
            return [below20[num - 1]]
        if num < 100:
            return [below100[num // 10 - 2]] + self.help(num % 10)
        if num < 1000:
            return [below20[num // 100 - 1]] + ["Hundred"] + self.help(num % 100)
        for i, e in enumerate(["Thousand", "Million", "Billion"]):
            if num < 1000 ** (i + 2):
                return self.help(num // (1000 ** (i + 1))) + [e] + self.help(num % (1000 ** (i + 1)))