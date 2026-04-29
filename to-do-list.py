# usuário "cadastrado"
usuario_correto = "admin"
senha_correta = "123"

# entrada do usuário
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

# validação
if usuario == usuario_correto and senha == senha_correta:
    print("Login realizado com sucesso 🚀")
else:
    print("Usuário ou senha incorretos ❌")
