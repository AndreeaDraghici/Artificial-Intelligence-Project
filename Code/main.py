import time
import Code.service
from Code.model.implementation import *
from Code.model.generator_date_intrare import *


def main():
    # noinspection PyGlobalUndefined
    global file
    parking_size = generare_dimensiune_parcare()
    initialState = generare_stare_initiala(parking_size)
    goalState = generare_stare_finala(parking_size, initialState)
    # add absolut file path before you run the application
    try:
        file = open(r"D:\Data\Facultate\Sem2\APD\Lab\Artificial-Intelligence-Project\Code\date_experimentale\date2.txt", 'w')
    except FileExistsError:
        print("Eroare la deschiderea fisierului")
    except IOError:
        print("Eroare la procesarea fisierului")
    else:
        """file.write("\nFolosind Astar search\n")
        file.write("\nDimensiunea parcarii este : " + str(parking_size) + "x" + str(parking_size))
        file.write("\nStarea initiala este: " + str(initialState))
        file.write("\nObiectivul este: " + str(goalState))
        problem_m_Vehicle = m_Vehicle(parking_size, initialState, goalState)
        time1 = time.time()
        problem_Solution = search.astar_search(problem_m_Vehicle, problem_m_Vehicle.manhtDistance)
        print('\n')
        time2 = time.time()
        file.write("\nActiunile executate sunt: " + str(problem_Solution.solution()))
        file.write("\nTimpul executat este de " + str(time2 - time1) + " secunde")
        file.write("\nCostul caii este: " + str(problem_Solution.path_cost))
"""
        file.write("\nDimensiunea parcarii este : " + str(parking_size) + "x" + str(parking_size))
        file.write("\nStarea initiala este: " + str(initialState))
        file.write("\nObiectivul este: " + str(goalState))
        problem_m_Vehicle = m_Vehicle(parking_size, initialState, goalState)
        time1 = time.time()
        problem_Solution = Code.service.search.best_first_graph_search(problem_m_Vehicle, problem_m_Vehicle.manhtDistance)
        print('\n')
        time2 = time.time()
        file.write("\nActiunile executate sunt: " + str(problem_Solution.solution()))
        file.write("\nTimpul executat este de " + str(time2 - time1) + " secunde")
        file.write("\nCostul caii este: " + str(problem_Solution.path_cost))
    finally:
        file.close()


if __name__ == "__main__":
    main()

