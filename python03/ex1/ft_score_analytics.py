import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    size = len(sys.argv)
    count = 0
    if (size > 1):
        i = 1
        while (i < size):
            try:
                int(sys.argv[i])
                count += 1
            except ValueError:
                print(f"Invalid input! '{sys.argv[i]}'")
            i += 1
        if (count != 0):
            scores = [0] * count
            i = 1
            j = 0
            while (i < size):
                try:
                    score = int(sys.argv[i])
                    scores[j] = score
                    j += 1
                except ValueError:
                    pass
                i += 1
            print("Scores processed:", scores)
            print("Total players:", len(scores))
            print("Total score:", sum(scores))
            print(f"Average score: {sum(scores) / len(scores):.1f}")
            print("High score:", max(scores))
            print("Low score:", min(scores))
            print("Score range:", max(scores) - min(scores))
    else:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py",
            "<score1> <score2> ...")
