def precond_dfa(str):
    state = 'q0'  
    for sym in str:
        match state:
            case 'q0': state = 'q1' if sym == '1' else 'q0'
            case 'q1': state = 'q2' if sym == '1' else 'q1'
            case 'q2': state = 'q3' if sym == '1' else 'q2'
            case 'q3': state = 'q1' if sym == '1' else 'q3'
    return state == 'q3'  

print(precond_dfa(''))        
print(precond_dfa('111'))     
print(precond_dfa('111111'))  
print(precond_dfa('10101'))   
print(precond_dfa('11011'))   
print(precond_dfa('000'))     