def normalize_path_params(cidade=None,
                        estrelas_min = 0,
                        estrelas_max = 8,
                        diaria_min = 0,
                        diaria_max = 566666600005666666000056666660000,
                        limit = 50,
                        offset =0, **dados):
    if cidade:
        return {
        'estrelas_min': estrelas_min,
        'estrelas_max': estrelas_max,
        'diaria_min': diaria_min,
        'diaria_max': diaria_max,
        'cidade':cidade,
        'limit': limit,
        'offset':offset        }
    return {
    'estrelas_min': estrelas_min,
    'estrelas_max': estrelas_max,
    'diaria_min': diaria_min,
    'diaria_max': diaria_max,
    'limit': limit,
    'offset':offset }

consulta_sem_cidade = "SELECT * FROM hoteis \
WHERE (estrelas > %s and estrelas <  %s)\
and (diaria > %s  and diaria < %s)\
LIMIT  %s OFFSET %s"


consulta = "SELECT * FROM hoteis \
WHERE (estrelas > %s and estrelas <  %s)\
and (diaria > %s  and diaria < %s)\
and cidade =%s LIMIT %s OFFSET %s"
