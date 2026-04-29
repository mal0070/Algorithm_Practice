def solution(polynomial): 
    polynomial = [n.strip() for n in polynomial.split('+')]
    constant = 0
    x_sum = 0
    
    for n in polynomial:
        if 'x' in n:
            if n=='x':
                x_sum += 1
            else:
                x_sum+=int(n.replace('x',''))
        else:
            constant += int(n)

    
    if constant !=0:
        if x_sum > 1:
            return str(x_sum)+'x + '+str(constant)
        if x_sum == 1:
            return 'x + '+str(constant)
        if x_sum == 0:
            return str(constant)
    else:
        if x_sum > 1:
            return str(x_sum)+'x'
        if x_sum == 1:
            return 'x'
        if x_sum == 0:
            return "0"