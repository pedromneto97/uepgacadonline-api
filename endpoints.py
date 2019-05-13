from utils.map import Map

acadonline = Map({
    "home": "https://sistemas.uepg.br/academicoonline/login/index",
    "auth": "https://sistemas.uepg.br/academicoonline/login/authenticate",
    "grades": "https://sistemas.uepg.br/academicoonline/avaliacaoDesempenho/index",
    "password": "https://sistemas.uepg.br/academicoonline/academico/index",
    "perfil_get": "https://sistemas.uepg.br/academicoonline/academico_pessoa/show",
    "perfil_set": "https://sistemas.uepg.br/academicoonline/academico_pessoa/index",
    "activities": "https://sistemas.uepg.br/academicoonline/atividadeComplementar/index",
    "remember_password": "https://sistemas.uepg.br/academicoonline/recuperarSenha/index",
    "extract": "https://sistemas.uepg.br/academicoonline/documentos/generate?reportName=ExtratoMatricula"
})

pergamum = Map({
    "home": "https://sistemas.uepg.br/pergamum/biblioteca/index.php",
    "auth": "https://sistemas.uepg.br/pergamum///biblioteca/index.php?rs=ajax_valida_acesso_novo&rst=&rsargs[]={login}&rsargs[]={password}",
    "renew": "https://sistemas.uepg.br/pergamum///biblioteca_s/meu_pergamum/index.php?rs=ajax_renova&rsrnd=1508281073663&rsargs[]={book}&rsargs[]=4&rsargs[]=4&rsargs[]=15411",
    "search": "https://sistemas.uepg.br/pergamum///biblioteca/index.php",
    "validate": "https://sistemas.uepg.br/pergamum/biblioteca_s/php/login_usu.php?flag=index.php",
    "books": "https://sistemas.uepg.br/pergamum/biblioteca_s/meu_pergamum/index.php?flag=index.php",
    "collection": "https://sistemas.uepg.br/pergamum///biblioteca/index.php?rs=ajax_dados_acervo&rst=&rsrnd=1544500507731&rsargs[]={book}&rsargs[]="
})

ru = Map({
    "menu": "https://sistemas.uepg.br/producao/pro-reitorias/proad/diser/ru/cardapio/cardapio_semanal.php"
})

portal = Map({
    "featured": "https://portal.uepg.br",
    "news_item": "https://portal.uepg.br/selnoticia.php",
    "news": "https://portal.uepg.br/noticias.php"
})

eventos = Map({
    "home": "https://siseve.apps.uepg.br"
})
