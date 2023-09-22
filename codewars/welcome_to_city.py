def say_hello(name, city, state):
    return f'Hello, {" ".join(name)}! Welcome to {city}, {state}!'


print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))
print(say_hello(['Franklin','Delano','Roosevelt'], 'Chicago', 'Illinois'))
print(say_hello(['Wallace','Russel','Osbourne'],'Albany','New York'))