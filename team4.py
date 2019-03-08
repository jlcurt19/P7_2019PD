team_name = 'ThotPatrol'
strategy_name = 'Determine by recent move'
strategy_description = 'For the first move collude, then if my last move is b return b if their last move was c, else return c. If my last move was collude then if their last move was collude then collude else betray.'

def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return 'c'
    else:
        if my_history[-1] == 'b':
            if their_history[-1] == 'c':
                return 'b'
            else:
                return 'c'
        else:
            if their_history[-1] == 'c':
                return 'c'
            else:
                return 'b'