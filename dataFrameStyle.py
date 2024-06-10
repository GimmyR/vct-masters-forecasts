def getBackgroundColor(row, colors: list, teams: list) :

    """
    This function gives the right background color for a row.
    """

    if len(colors) == len(teams) :
    
        if row["team"] in teams :

            i = teams.index(row["team"])
            return [f"background-color: {colors[i]}" for _ in row]
        
        else : raise Exception(f"{row['team']} is not Teams.")

    else : raise Exception("Colors and Teams must have the same size.")