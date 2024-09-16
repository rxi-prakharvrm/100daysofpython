country = "India"
name = "Prakhar"
txt = "Hello, I am {0} from {1}"
print(txt.format(name, country))

print(f"Hello, I am {name} from {country}")
print(f"We can write f-strings in this way: f\"Hello, I am {{name}} from {{country}}\"")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.90234))

price = 49.90234
print(f"For only {price:.2f} dollars!")

