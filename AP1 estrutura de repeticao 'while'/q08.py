# Escreva um programa que deverá realizar a leitura do login e da senha de um usuário. Caso o login e a senha sejam inválidos, deverá informar ao usuário a mensagem “Login ou Senha inválido(s)” e devem ser solicitados novos valores para o login e a senha. O programa deverá parar quando for forem digitados login e senha corretos e o programa deverá apresentar “Login realizado com sucesso”. 

# 	O login e senha são os seguintes: 
# Login: admin
# Senha: admin123

logado = 0
while logado == 0:
    login = str(input('Digite seu login: '))
    senha = str(input('Digite sua senha: '))
    if login == 'admin' and senha  == 'admin123':
        print('Login realizado com sucesso')
        logado = 1
    else:
        print('Login e/ou Senha inválido(s)')