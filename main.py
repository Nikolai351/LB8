import random
import deap.base
import deap.creator
import deap.tools

# Функция, которую мы хотим максимизировать
def fitness(individual):
    # Здесь должна быть логика вычисления функции
    # Например, сумма элементов списка
    return sum(individual)

# Создаем пространство решений
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, typecode='b', fitness=creator.FitnessMax)

# Создаем оператор селекции
toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 100)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", fitness)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Создаем начальную популяцию
population = toolbox.population(n=500)

# Выполняем 1000 итераций генетического алгоритма
toolbox.register("update", tools.selBest)
for g in range(1000):
    # Эволюционируем популяцию
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.5)
    # Выбираем лучших особей для следующей итерации
    population = toolbox.update(offspring, k=len(population))

# Выводим лучшую особь
best_ind = tools.selBest(population, k=1)[0]
print("Лучшая особь:", best_ind, "Функция:", fitness(best_ind))
