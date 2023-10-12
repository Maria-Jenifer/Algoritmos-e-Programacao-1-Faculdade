# Reescreva o programa da questão anterior, considerando que o usuário só poderá realizar três tentativas de digitar o login e senha. No caso do usuário errar o usuário e senha na terceira tentativa o programa deverá apresentar a mensagem: “Você realizou três tentativas de acesso. Tente novamente mais tarde”

tentativas = 0
encerra = 0
while encerra == 0:        
    login = str(input('Digite seu login: '))
    senha = str(input('Digite sua senha: '))
    if login == 'admin' and senha  == 'admin123':
        print('Login realizado com sucesso')
        encerra = 1
    else:
        print('Login e/ou Senha inválido(s)')
        tentativas += 1
    
    if tentativas == 3:
        print('Você realizou três tentativas de acesso. Tente novamente mais tarde')
        encerra = 1