class Solution:
    def alienOrder(self, words):
        all_letters = set()
        for word in words:
            for letter in word:
                all_letters.add(letter)
        relations = self.findRelation(words)
        relations = [r for r in relations if r is not None]
        if False in relations:
            return ""
        pres = {}
        depend = {}
        for letter in all_letters:
            pres[letter] = 0
            depend[letter] = []
        for relation in relations:
            small, large = relation
            pres[large] += 1
            depend[small].append(large)
        ans = []
        cur_turn = []
        next_turn = []
        for key in pres:
            if pres[key] == 0:
                cur_turn.append(key)
        while len(ans) < len(all_letters) and cur_turn:
            ans += cur_turn
            for smaller in cur_turn:
                for larger in depend[smaller]:
                    pres[larger] -= 1
                    if pres[larger] == 0:
                        next_turn.append(larger)
            cur_turn = next_turn
            next_turn = []
        if len(ans) < len(all_letters):
            return ""
        else:
            return "".join(ans)


    def findRelation(self, words):
        relations = []
        for i in range(len(words) - 1):
            relations.append(self.compare(words[i], words[i+1]))
        return relations

    def compare(self, w1, w2):
        index = 0
        while index < min(len(w1), len(w2)) and w1[index] == w2[index]:
            index += 1
        if index == len(w1):
            return None
        if index == len(w2):
            return False
        return [w1[index], w2[index]]