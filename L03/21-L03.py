def nb_year(p0, percent, aug, p):
    n_day = 1
    total_bac = int(p0 + p0*percent/100 + aug)
    while p > total_bac:
        total_bac = int(total_bac + total_bac*percent/100 + aug)
        n_day+=1
    return n_day
    
