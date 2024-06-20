from faker import Faker

fake = Faker()

# Generate a fake name
name = fake.name()
print(name)

# Generate a fake address
address = fake.address()
print(address)

# Generate a fake text
text = fake.text()
print(text)
