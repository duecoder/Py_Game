# CORES

CGREEN  = '\33[32m'
CRED    = '\33[31m'
CBEIGE  = '\33[36m'
CBLUE   = '\33[34m'
CEND = '\33[0m'

# CLASSE

class Pessoa:
    acertadas = 0
    chances = 27
        
    def __init__(self, name, job, fav_food, birth_month):
        self.name = name
        self.job = job
        self.fav_food = fav_food
        self.birth_month = birth_month   


    def palpite_logic(self, name):
        self.name = name
        while True:
            desafio = input('Escolha o desafio (Profissão, mês ou comida): ')
            if desafio.title() == 'Mês' or desafio.title() == 'Profissão' or desafio.title() == 'Comida':
                palpite = input('Digite seu palpite: ')
                if palpite.title() == self.birth_month or palpite.title() == self.job or palpite.title() == self.fav_food:
                    print()
                    print(CGREEN+"AEE! ACERTOU MIZERAVI!!!!!"+CEND)
                    var_pessoa.acertadas += 1
                    print(CBEIGE+f'Você já acertou {var_pessoa.acertadas} desafio(s). Falta(m) '+str((9 - (var_pessoa.acertadas)))+'!'+CEND)
                    break
                else:
                    print()
                    print(CRED+"UHHH! ERROU! Menos 1 chance!!"+CEND)
                    var_pessoa.chances -= 1
                    print(CBEIGE+f'Você ainda tem {var_pessoa.chances} chance(s)!'+CEND)
                    break
            else: 
                print(CRED+'Você precisa digitar algum dos desafios (Profissão, mês ou comida).'+CEND)
                continue
    

# PESSOAS

marcela = Pessoa('Marcela','Engenheira Civil','Sorvete','Outubro')
clebin = Pessoa('Clebin','Jardineiro','Sushi','Fevereiro')
rincon = Pessoa('Rincon','Programador','Lasanha','Dezembro')


# DICAS

dicas = {
    'Marcela': ['(Profissão): Capaz de construir um prédio.',
                '(Mês): As crianças adoram.'
                '(Comida): Adora se refrescar.', ],
    'Clebin': ['(Profissão): Sem ele, as plantas morreriam.',
                '(Mês): O ano só começa depois desse mês.',
                '(Comida): Come cru mesmo, nem liga.'],
    'Rincon': ['(Profissão): Se bobear foi ele quem fez esse jogo.',
                '(Mês): Depois desse só ano que vem.',
                '(Comida): Várias camadas, muito molho, NHAMMM.'],
}

var_pessoa = Pessoa
#var_chances = var_pessoa.chances
#var_acertadas = var_pessoa.acertadas

# GAME LOGIC

def action():
    while True:
        print(CBEIGE+'\n-------------------------------------------'+CEND)
        print(CBEIGE+'-------------AÇÕES DISPONÍVEIS-------------\n'+CEND)
        print(CBLUE+'a.'+CEND+' Mostrar as dicas;')
        print(CBLUE+'b.'+CEND+' Arriscar algum desafio;')
        #print(CBLUE+'c.'+CEND+' Mostrar quantas chances você tem;')
        #print(CBLUE+'d.'+CEND+' Mostrar quantas você já acertou;')
        print(CBLUE+'c.'+CEND+' Sair do jogo')
        print()
        
        action = input('Escolha a ação desejada (a, b ou c): ')
        if action == 'a':
            print(CBEIGE+'\n-------------------------------------------'+CEND)
            print(CBEIGE+'--------------------DICAS------------------\n'+CEND)
            for n, l in dicas.items():
                print(CBLUE+n+CEND)
                for items in l:
                    print(f'\t {items}')
        # DAQUI PRA BAIXO VOU REFAZER TUDO
        elif action == 'b':
            nome_input = input('Qual pessoa você vai arriscar? ')
            if nome_input.title() == 'Marcela':
                marcela.palpite_logic(marcela)
            elif nome_input.title() == 'Clebin':
                clebin.palpite_logic(clebin)
            elif nome_input.title() == 'Rincon':
                rincon.palpite_logic(rincon)
            else:
                print(CRED+'Você precisa digitar algum nome que tenha no jogo.'+CEND)
        elif action == 'c':
        #     print(CBEIGE+f'Você ainda tem {var_chances} chances!'+CEND)
        # elif action == 'd':
        #     print(CBEIGE+f'Você já acertou {var_acertadas} desafios. Faltam '+str((9 - (var_acertadas)))+'!'+CEND)
        # elif action == 'e':
            break
        
        if var_pessoa.acertadas >= 6:
            print(CGREEN+"BOA CARAI! Cê venceu o jogo!!!!"+CEND)
            break
        if var_pessoa.chances == 0:
            print(CRED+"PUTA MAN!! Suas chances já eram. :(((("+CEND)
            
                    
            
        
        
        
        
        
    
        