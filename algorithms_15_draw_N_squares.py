def draw_n_squares(n):    
    result = ("+" + "---+" * n + "\n")
    for i in range(n):            
        result += ("|" + "   |" * n + "\n")
        result += ("+" + "---+" * n + "\n")
    return result
        

# def draw_n_squares(n):                # PROSTSZE ROZWIĄZANIE
#   if n == 0: return ''
#   return ('+---' * n + '+\n' + '|   ' * n + '|\n')* n + '+---' * n + '+'

print(draw_n_squares(5))
