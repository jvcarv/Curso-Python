# SECRETS GERA NÚMEROS ALEATORIOS SEGUROS
import secrets
# import string as s

print(secrets.randbelow(100))
print(secrets.choice([1, 2, 3, 4, 5, 6, 6, 7]))

random = secrets.SystemRandom()
# COM ESSE COMANDO, O RANDOM FICA CONFIÁVEL
# python -c "import string as s;from secrets import SystemRandom as Sr; print
# (''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"
# CRIA SENHAS ALEATÓRIAS

r_range = random.randrange(10, 20)
print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print(f'{r_uniform:.2f}')

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['João', 'André', 'André Diel', 'Felipe']

random.shuffle(nomes)
print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)

new_names = random.sample(nomes, k=2)
print(new_names)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
print(random.choices(new_names, k=3))

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(new_names))
