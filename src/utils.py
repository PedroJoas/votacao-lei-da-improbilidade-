def get_sigla_partido(partido):
    sigla = partido.split('–')[0].strip()
    return sigla
