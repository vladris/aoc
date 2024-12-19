towels, patterns = open("input").read().split("\n\n")
towels = [towel.strip() for towel in towels.split(",")]
patterns = [pattern for pattern in patterns.split("\n")]

matched = {"": True}

def match(pattern):
    if pattern not in matched:
        matched[pattern] = any(match(pattern[len(towel):]) for towel in towels if pattern.startswith(towel))

    return matched[pattern]


print(sum(match(pattern) for pattern in patterns))
