def max_clique(graphu, nnc):

    if c >= graphu.num_vertice:
        if graphu.num_sol > graphu.num_sol_best:
            graphu.num_sol_best = graphu.num_sol
            for i in range(graphu.num_vertice):
                graphu.solution_best[i] = graphu.solution[i]
        return

    add_in_solution = True

    for i in range(c+1):
        if graphu.solution[i] and graphu.adjmatrix[i][c] == 0:
            add_in_solution = False
            break

    if add_in_solution:
        graphu.solution[c] = 1
        graphu.num_sol += 1
        max_clique(graphu, c + 1)
        graphu.solution[c] = 0
        graphu.num_sol -= 1

    if (graphu.num_sol + graphu.num_vertice - c - 1) >= graphu.num_sol_best:
        graphu.solution[c] = 0
        max_clique(graphu, c + 1)
