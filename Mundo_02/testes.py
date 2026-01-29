from random import choice
jokenpo = [1,2,3]
escolha_pc = choice(jokenpo)
escolha_usuario = int(input("""Escolha o que irá jogar:
[1] Pedra
[2] Papel
[3] Tesoura\n"""))
if(escolha_pc == 1 and escolha_usuario == 3):
    print('O computador escolheu pedra, você perdeu.')
elif(escolha_pc == 2 and escolha_usuario == 1):
    print('O computador escolheu papel, você perdeu.')
elif(escolha_pc == 3 and escolha_usuario == 2):
    print('O computador escolheu Tesoura, você perdeu.')
elif(escolha_pc == 1 and escolha_usuario == 2):
    print('O computador escolheu pedra, você ganhou.')
elif(escolha_pc == 2 and escolha_usuario == 3):
    print('O computador escolheu papel, você ganhou.')
elif(escolha_pc == 3 and escolha_usuario == 1):
    print('O computador escolheu tesoura, você ganhou.')
else:
    print('O computador escolheu o mesmo que você, empatou.')