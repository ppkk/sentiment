import random

claims = [
    ("The market is sure to rise due to positive economic indicators.", 0.9),
    ("Analysts predict a downturn in the market due to recent geopolitical events.",-0.9),
    ("There's a strong likelihood of a bullish market in the coming months.", 0.4),
    ("Given the current economic climate, the market is likely to see a surge.", 0.3),
    ("The market could potentially face a decline, but it's too early to say for sure.",-0.2),
    ("Experts are confident in a market upswing due to robust corporate earnings.",0.4),
    ("There's a chance the market might dip due to regulatory changes.", -0.3),
    ("It's uncertain whether the market will rise or fall in the near future.", 0.0),
    ("There's a potential for the market to tank, but it's just a guess.", 0.1),
    ("There's a risk the market could contract, but it's just a speculation.", -0.2),
    ("Given the current economic climate, the market is almost certain to see a surge.", 0.7),
    ("There's a strong chance the market might dip due to regulatory changes.", -0.6),
    ("The market is poised for growth, according to leading economists.", 0.5),
    ("The market is projected to climb, but it's not a guarantee.", 0.1),
    ("The market is projected to thrive, but it's not a sure shot.", 0.3),
    ("The market is expected to prosper, but it's not a certain prediction.", 0.2),
    ("The market is set to increase, but it's not a certain outcome.", 0.1),
    ("The market is expected to rise due to positive economic indicators.", 0.7),
    ("The market may experience a bearish trend, but it's not set in stone.", -0.2),
    ("The market could potentially face a decline.", -0.4),
    ("I am sure the market will rise.", 0.9),
    ("I am sure the market will fall.", -0.9),
    ("Tomorrow the market will rise.", 1.0),
    ("Tomorrow the market will fall.", -1.0),
    ("I will buy more.", 0.8),
    ("I will sell more.", -0.8),
    ("I will borrow money and just buy, it is a sure thing.", 1.0),
    ("I will sell everyting, it is going to be a disaster.", -1.0),
    ("It is not going well.", -0.5),
    ("I expect extreme losses in a near future.", -0.9),
    

]

people = ["Petr", "Martin", "Pavel", "Tomas", "Mirek", "Vlada", "Jindra", "Michal", "Zuzana", "Jana", "Klara", "Katerina", "Eva", "Lucie", "Barbora", "Veronika", "Lenka", "Marie", "Alena", "Hana", "Ivana", "Tereza", "Simona", "Petra", "Michaela", "Marketa", "Sarka", "Nikola", "Karolina", "Kristyna", "Adela", "Daniela", "Martina", "Monika", "Vendula", "Aneta", "Andrea", "Kamila"]

def generate_statements_sum(names, claims):
    random.shuffle(names)
    statements = []
    sum_values = 0
    for i, name in enumerate(names):
        claim = random.choice(claims)
        statement = f"{name}: {claim[0]}"
        statements.append(statement)
        sum_values += claim[1]
    result = " ".join(statements)
    return result, sum_values

result, sum_values = generate_statements_sum(people, claims)
print(result)
print(f"Sum of values: {sum_values}")

def generate_statements_tomas(names, claims):
    random.shuffle(names)
    statements = []
    tomas_value = 0
    for i, name in enumerate(names):
        claim = random.choice(claims)
        statement = f"{name}: {claim[0]}"
        statements.append(statement)
        if name == "Tomas":
            tomas_value = claim[1]
    result = " ".join(statements)
    return result, tomas_value

result, tomas_value = generate_statements_tomas(people, claims)
print(result)
print(f"Value for Tomas: {tomas_value}")