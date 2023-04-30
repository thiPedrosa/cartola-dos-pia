import requests
import pandas as pd
import json
import os
from PIL import Image

def rodada():
    url = 'https://api.cartolafc.globo.com/partidas'

    response = requests.request("GET", url)

    rodada_atual = response.json()['rodada']
    return rodada_atual
rodada_atual = rodada()

def numero_escalacoes():
    escala = []

    url = f'https://api.cartolafc.globo.com/mercado/destaques'

    response = requests.request("GET", url)
    resultado = response.json()
    # print(json.dumps(resultado, indent=4))

    for jogador in resultado:
        nome_jogador = jogador['Atleta']['apelido']
        escalacoes = jogador['escalacoes']
        clube = jogador['clube_nome']
        dic = {
            'nome':nome_jogador,
            'escalacoes':escalacoes,
            'clube':clube
        }
        escala.append(dic)
    return escala
quantos_escalaram = numero_escalacoes()

#Api cartola para obter dados jogadores
url = 'https://api.cartolafc.globo.com/atletas/mercado'

headers1 = {
            "Content-Type": "application/json",
            "Authorization" : "Bearer live_b369006f0f1166d9ce7b9641a3cdfd",
}

response = requests.get(url)
data = response.json()

def clubes():
    clubes = data['clubes']
    lista_clubes = []

    for clube in clubes:
        infos_clube = clubes[f'{clube}']
        nome_time = infos_clube['nome_fantasia'] 
        if nome_time == "Athlético-PR":
            nome_time = "Athletico-PR"
        objeto = {'clube_id':infos_clube['id'], 'clube_nome':nome_time}
        lista_clubes.append(objeto)
    return lista_clubes
lista_clubes = clubes()

def posicoes():
    posicoes = data['posicoes']
    lista_posicoes = []

    for posicao in posicoes:
        infos_posicao = posicoes[f'{posicao}']
        objeto = {'posicao_id':infos_posicao['id'], 'posicao_nome':infos_posicao['nome']}
        lista_posicoes.append(objeto)
    return lista_posicoes
lista_posicoes = posicoes()

def status():
    status = data['status']
    lista_status = []

    for stats in status:
        infos_status = status[f'{stats}']
        objeto = {'status_id':infos_status['id'], 'status_nome':infos_status['nome']}
        lista_status.append(objeto)
    return lista_status
lista_status = status()

def jogadores():
    jogadores = data['atletas']
    lista_jogadores = []

    for info in jogadores:
        nome = info['apelido']
        clube_id = info['clube_id']
        posicao_id = info['posicao_id']
        status_id = info['status_id']
        preco = info['preco_num']
        pontos_ultima_rodada = info['pontos_num']
        variacao_preco = info['variacao_num']
        minimo_para_valorizar = info['minimo_para_valorizar']
        numero_de_jogos = info['jogos_num']
        media = info['media_num']
        
        scout = info['scout']
        #Defesa
        try:
            ds = scout['DS']
        except:
            ds = ''
        try:
            fc = scout['FC']
        except:
            fc = ''
        try:
            gc = scout['GC']
        except:
            gc = ''
        try:
            ca = scout['CA']
        except:
            ca = ''
        try:
            cv = scout['CV']
        except:
            cv = ''
        try:
            sg = scout['SG']
        except:
            sg = ''
        try:
            de = scout['DE']
        except:
            de = ''
        try:
            dp = scout['DP']
        except:
            dp = ''
        try:
            gs = scout['GS']
        except:
            gs = ''
        try:
            pc = scout['PC']
        except:
            pc = ''

            #Ataque
        try:
            fs = scout['FS']
        except:
            fs = ''
        try:
            pe = scout['PE']
        except:
            pe = ''
        try:
            a = scout['A']
        except:
            a = ''
        try:
            ft = scout['FT']
        except:
            ft = ''
        try:
            fd = scout['FD']
        except:
            fd = ''
        try:
            ff = scout['FF']
        except:
            ff = ''
        try:
            g = scout['G']
        except:
            g = ''
        try:
            i = scout['I']
        except:
            i = ''
        try:
            pp = scout['PP']
        except:
            pp = ''
        try:
            ps = scout['PS']
        except:
            ps = ''
        
        objeto = {'nome':nome,
                'clube_id':clube_id,
                'posicao_id':posicao_id,
                'status_id':status_id,
                'preco':preco,
                'pontos_ultima_rodada':pontos_ultima_rodada,
                'variacao_preco':variacao_preco,
                'minimo_para_valorizar':minimo_para_valorizar,
                'numero_de_jogos':numero_de_jogos,
                'media':media,
                'ds':ds,
                'fc':fc,
                'gc':gc,
                'ca':ca,
                'cv':cv,
                'sg':sg,
                'de':de,
                'dp':dp,
                'gs':gs,
                'pc':pc,
                'fs':fs,
                'pe':pe,
                'a':a,
                'ft':ft,
                'fd':fd,
                'ff':ff,
                'g':g,
                'i':i,
                'pp':pp,
                'ps':ps}
        lista_jogadores.append(objeto)
    return lista_jogadores
lista_jogadores = jogadores()

#Api Brasileirao para obter a tabela e confrontos
def tabela_brasileirao():

    url = "https://api.api-futebol.com.br/v1/campeonatos/10/tabela"  
    response = requests.request(
        "GET",
        url,
        headers=headers1,
    )

    data = response.json()

    tabela_brasileirao = []

    for time in data:

        posicao = time['posicao']
        pontos = time['pontos']
        nome = time['time']['nome_popular']
        jogos = time['jogos']
        vitorias = time['vitorias']
        empates = time['empates']
        derrotas = time['derrotas']
        gols_pro = time['gols_pro']
        gols_contra = time['gols_contra']
        saldo_gols = time['saldo_gols']
        aproveitamento = time['aproveitamento']

        objeto = {'posicao':posicao,
                'pontos':pontos,
                'nome':nome,
                'jogos':jogos,
                'vitorias':vitorias,
                'empates':empates,
                'derrotas':derrotas,
                'gols_pro':gols_pro,
                'gols_contra':gols_contra,
                'saldo_gols':saldo_gols,
                'aproveitamento':aproveitamento}
        tabela_brasileirao.append(objeto)
    return tabela_brasileirao
tabela_brasileiro = tabela_brasileirao()

def proxima_rodada():
    url = f"https://api.api-futebol.com.br/v1/campeonatos/10/rodadas/{rodada_atual}"  

    response = requests.request(
        "GET",
        url,
        headers=headers1,
    )

    data = response.json()
    partidas = data['partidas']

    proximas_partidas = []

    for partida in partidas:
        time_mandante = partida['time_mandante']['nome_popular']
        time_visitante = partida['time_visitante']['nome_popular']
        objeto = {'time_mandante':time_mandante, 'time_visitante':time_visitante}
        proximas_partidas.append(objeto)
    return proximas_partidas
proximas_partidas = proxima_rodada()

def criar_data_base():
    data_base = []
    
    for jogador in lista_jogadores:
        qts_escalaram = 0
        media = jogador['media']
        for posicao in lista_posicoes:
            if jogador['posicao_id'] == posicao['posicao_id']:
                posicao_ = posicao['posicao_nome']
        for clube in lista_clubes:
            if jogador['clube_id'] == clube['clube_id']:
                nome_clube = clube['clube_nome']  
        for status in lista_status:
            if jogador['status_id'] == status['status_id']:
                status_ = status['status_nome']
        for partida in proximas_partidas:
            if nome_clube == partida['time_mandante'] or nome_clube == partida['time_visitante']:
                mandante = partida['time_mandante']
                visitante = partida['time_visitante']
                proximo_jogo = f'{mandante} x {visitante}'
        for escalacao in quantos_escalaram:
            if jogador['nome'] == escalacao['nome'] and nome_clube == escalacao['clube']:
                qts_escalaram = escalacao['escalacoes']
        
        objeto = {'nome':jogador['nome'],
            'clube':nome_clube,
            'posicao':posicao_,
            'status':status_,
            'preco':jogador['preco'],
            'pontos_ultima_rodada':jogador['pontos_ultima_rodada'],
            'variacao_preco':jogador['variacao_preco'],
            'minimo_para_valorizar':jogador['minimo_para_valorizar'],
            'numero_de_jogos':jogador['numero_de_jogos'],
            'media':media,
            'proximo_jogo':proximo_jogo,
            'qts_escalaram':qts_escalaram,
            'ds':jogador['ds'],
            'fc':jogador['fc'],
            'gc':jogador['gc'],
            'ca':jogador['ca'],
            'cv':jogador['cv'],
            'sg':jogador['sg'],
            'de':jogador['de'],
            'dp':jogador['dp'],
            'gs':jogador['gs'],
            'pc':jogador['pc'],
            'fs':jogador['fs'],
            'pe':jogador['pe'],
            'a':jogador['a'],
            'ft':jogador['ft'],
            'fd':jogador['fd'],
            'ff':jogador['ff'],
            'g':jogador['g'],
            'i':jogador['i'],
            'pp':jogador['pp'],
            'ps':jogador['ps']
            }
        
        data_base.append(objeto)
    return data_base
data_base = criar_data_base()

class_gols_pro = sorted(tabela_brasileiro, key=lambda x:x['gols_pro'], reverse=True)
classificacao_gols_pro = []
for i, time in enumerate(class_gols_pro):
    dicionario = {'nome':time['nome'], 'classificacao':(i+1)}
    classificacao_gols_pro.append(dicionario)

class_gols_sofridos = sorted(tabela_brasileiro, key=lambda x:x['gols_contra'], reverse=False)
classificacao_gols_sofridos = []
for i, time in enumerate(class_gols_sofridos):
    obj = {'nome':time['nome'], 'classificacao':(i+1)}
    classificacao_gols_sofridos.append(obj)

def definir_time_adversario(clube_do_jogador):
    for partida in proximas_partidas:
        if clube_do_jogador == partida['time_mandante']:
            time_adversario = partida['time_visitante']
            fator_casa = 1
        elif clube_do_jogador == partida['time_visitante']:
            time_adversario = partida['time_mandante']
            fator_casa = 0
    return time_adversario, fator_casa
    
fator_ataque = 0
fator_defesa = 0 

def metricas_atacante(data_base):
    formula = 0
    for jogador in data_base:
        media_jogador = jogador['media']
        time_adversario, fator_casa = definir_time_adversario(jogador['clube'])
        if jogador['posicao'] == "Atacante" or jogador['posicao'] == "Meia":
            for time in classificacao_gols_pro:
                if jogador['clube'] == time['nome']:
                    fator_ataque = time['classificacao']
            for time in classificacao_gols_sofridos:
                if time_adversario == time['nome']:
                    fator_defesa = time['classificacao']
            formula = (60*media_jogador + 20*fator_ataque + 20*fator_defesa)/100 + fator_casa
            jogador['formula'] = "{:.2f}".format(formula)
    return
metricas_atacante(data_base)

def metricas_goleiro(data_base):
    formula = 0
    class_gols_sofridos = sorted(tabela_brasileiro, key=lambda x:x['gols_contra'], reverse=True)
    pontos_gols_sofridos = []
    for i, time in enumerate(class_gols_sofridos):
        obj = {'nome':time['nome'], 'classificacao':(i+1)}
        pontos_gols_sofridos.append(obj)

    for jogador in data_base:
        media_jogador = jogador['media']
        time_adversario, fator_casa = definir_time_adversario(jogador['clube'])
        if jogador['posicao'] == "Goleiro" or jogador['posicao'] == "Zagueiro" or jogador['posicao'] == "Lateral":
            for time in pontos_gols_sofridos:
                if jogador['clube'] == time['nome']:
                    fator_defesa = time['classificacao']
            for time in classificacao_gols_pro:
                if time_adversario == time['nome']:
                    fator_ataque = time['classificacao']
            formula = (60*media_jogador + 20*fator_ataque + 20*fator_defesa)/100 + fator_casa
            jogador['formula'] = "{:.2f}".format(formula)
    return
metricas_goleiro(data_base)

def metricas_tecnico(data_base):
    formula = 0
    for jogador in data_base:
        media_jogador = jogador['media']
        time_adversario, fator_casa = definir_time_adversario(jogador['clube'])
        if jogador['posicao'] == "Técnico":
            for time in classificacao_gols_pro:
                if jogador['clube'] == time['nome']:
                    fator_ataque = time['classificacao']
            for time in classificacao_gols_sofridos:
                if jogador['clube'] == time['nome']:
                    fator_defesa = time['classificacao']
            formula = (60*media_jogador + 20*fator_ataque + 20*fator_defesa)/100 + fator_casa
            jogador['formula'] = "{:.2f}".format(formula)
    return
metricas_tecnico(data_base)

df = pd.DataFrame(data_base)
df = pd.DataFrame(proximas_partidas)

base_de_dados = df[[
                    'nome',
                    'clube',
                    'posicao',
                    'status',
                    'pontos_ultima_rodada',
                    'preco',
                    'minimo_para_valorizar',
                    'media',
                    'proximo_jogo',
                    'qts_escalaram',
                    'formula'
                    ]].to_dict('records')

proximo_jogo = df[['time_mandante','time_visitante']].to_dict('records')

