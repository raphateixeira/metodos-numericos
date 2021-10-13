class bissec( ):

    def bisection(f,a,b,N):
    '''
    Aproxima a solução de f(x) = 0 em um intervalo [a, b] pelo método da bissecção.

    Parâmetros:
    f   : função (lambda function);
    a,b : Limites do intervalo;
    N   : Número de iterações;

    Retorno:
    xn  : Número. Solução aproximada com N iterações de f(x) = 0 no intervalo dado.
    '''
    # Avalia se o intervalo possui raiz:
    if f(a)*f(b) >= 0:
        print('O intervalo dado não possui raiz.')
        return None

    a_n = a
    b_n = b
    for n in range(1,N+1):
        xn = (a + b)/2
        fxn = f(xn)
        if f(a)*fxn < 0:
            b = xn
        elif f(b)*fxn < 0:
            a = xn
        elif fxn == 0:
            print("Solução exata.")
            return xn
        else:
            print("Bissecção falhou.")
            return None
    return xn