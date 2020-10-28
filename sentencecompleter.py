def sentence_maker(phrase):
    interrogatives = ("what", "how", "why", "where", "when", "who")
    exclamation = ("wow", "awesome", "cool")
    capatilized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capatilized)
    elif phrase.endswith(exclamation):
        return "{}!".format(capatilized)
    else:
        return "{}.".format(capatilized)


results = []
while True:
    x = input("Say Something: ")
    if x != "\end":
        results.append(sentence_maker(x))
        continue
    else:
        break

print(" ".join(results))
