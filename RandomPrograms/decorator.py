def beautifyGreet(greet):
    def inner(name, gf_name):
        name = name.capitalize()  # Capitalize the name
        gf_name = gf_name.capitalize()
        return greet(name) + f". Nice to meet you and your girl friend {gf_name}!"
    return inner

def greet(name):
    return f"Hello, {name}"

# Use the decorated greet function
beautified_greet = beautifyGreet(greet)("shUBhaM", "ShruTI")
print(beautified_greet)
