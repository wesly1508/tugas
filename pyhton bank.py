name = input ("Hi")

match name:
    case "Hello" | "Hello, Newman":
        print("0$")
    case "How you doing?":
        print("20$")
    case "what's happening":
        print("100$")
    case _:
        print("????")