import most_queue.sim.rand_destribution as rd
import numpy as np
from most_queue.theory import network_calc
from most_queue.sim.network_im_prty import NetworkPrty


def test():
    """
    Тестирование ИМ СеМО с приоритетами в узлах
    Сравнение с численным расчетом методом декомпозиции
    """
    k_num = 3  # число классов
    n_num = 5  # число узлов

    n = [3, 2, 3, 4, 3]  # распределение числа каналов в узлах сети
    R = []  # список матриц вероятностей переходов между узлами сети для каждого класса.
    b = []  # список массивов начальных моментов распределения времени обслуживания [k, node, j]
    for i in range(k_num):
        # задаем одинаковые матрицы для всех классов звявок. Можно задать различные
        R.append(np.matrix([
            [1, 0, 0, 0, 0, 0],
            [0, 0.4, 0.6, 0, 0, 0],
            [0, 0, 0, 0.6, 0.4, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ]))
    L = [0.1, 0.3, 0.4]  # интенсивности поступления заявок в сеть по каждому из классов
    nodes_prty = []  # распределение приоритетов между заявками для каждого из узлов сети [m][x1, x2 .. x_k],
    # m - номер узла, xi- приоритет для i-го класса, k - число классов
    # Например: [0][0,1,2] - для первого узла задан прямой порядок приоритетов,
    # [2][0,2,1] - для третьего узла задан такой порядок приоритетов: для первого класса - самый старший (0),
    # для второго - младший (2), для третьего - средний (1)

    jobs_num = 100000  # число заявок для обслуживания в ИМ
    serv_params = []  #  параметры каналов обслуживания сети [m]{type: string, params: []},
    # где m - номер узла, type - тип распределения, params - параметры распределения.
    # Подробнее о параметрах распределения:
    #        Вид распределения                   Тип[types]     Параметры [params]
    #         Экспоненциальное                      'М'              mu
    #         Гиперэкспоненциальное 2-го порядка    'Н'         [y1, mu1, mu2]
    #         Эрланга                               'E'           [r, mu]
    #         Гамма-распределение                  'Gamma'        [mu, alpha]
    #         Кокса 2-го порядка                    'C'         [y1, mu1, mu2]
    #         Парето                                'Pa'         [alpha, K]
    #         Равномерное                         'Uniform'     [mean, half_interval]
    #         Детерминированное                      'D'         [b]


    h2_params = []
    for m in range(n_num):
        nodes_prty.append([])
        for j in range(k_num):
            if m % 2 == 0:
                nodes_prty[m].append(j)
            else:
                nodes_prty[m].append(k_num - j - 1)

        b1 = 0.9 * n[m] / sum(L)
        coev = 1.2
        h2_params.append(rd.H2_dist.get_params_by_mean_and_coev(b1, coev))

        serv_params.append([])
        for i in range(k_num):
            serv_params[m].append({'type': 'H', 'params': h2_params[m]})

    for k in range(k_num):
        b.append([])
        for m in range(n_num):
            b[k].append(rd.H2_dist.calc_theory_moments(*h2_params[m], 4))

    prty = ['NP'] * n_num  # список, содержащий тип приоритета для каждого узла сети.
    # "NP" - относительный приоритет. Также доступны абсолютные ("PR", "RW", "RS") и без приоритета "No"

    # Создаем экземпляр модели СеМО
    semo_im = NetworkPrty(k_num, L, R, n, prty, serv_params, nodes_prty)

    #  Запуск ИМ:
    semo_im.run(jobs_num)

    #  Получение нач. моментов пребывания в СеМО
    v_im = semo_im.v_semo

    #  Получение нач. моментов пребывания в СеМО с помощью метода инвариантов отношения
    semo_calc = network_calc.network_prty_calc(R, b, n, L, prty, nodes_prty)
    v_ch = semo_calc['v']

    #  получения коэфф загрузки каждого узла
    loads = semo_calc['loads']

    #  вывод результатов
    print("\n")
    print("-" * 60)
    print("{0:^60s}\n{1:^60s}".format("Сравнение данных ИМ и результатов расчета времени пребывания",
                                      "в СеМО с многоканальными узлами и приоритетами"))
    print("-" * 60)
    print("Количество каналов в узлах:")
    for nn in n:
        print("{0:^1d}".format(nn), end=" ")
    print("\nКоэффициенты загрузки узлов :")
    for load in loads:
        print("{0:^1.3f}".format(load), end=" ")
    print("\n")
    print("-" * 60)
    print("{0:^60s}".format("Относительный приоритет"))

    print("-" * 60)
    print("{0:^11s}|{1:^47s}|".format('', 'Номер начального момента'))
    print("{0:^10s}| ".format('№ кл'), end="")
    print("-" * 45 + " |")

    print(" " * 11 + "|", end="")
    for j in range(3):
        s = str(j + 1)
        print("{:^15s}|".format(s), end="")
    print("")
    print("-" * 60)

    for i in range(k_num):
        print(" " * 5 + "|", end="")
        print("{:^5s}|".format("ИМ"), end="")
        for j in range(3):
            print("{:^15.3g}|".format(v_im[i][j]), end="")
        print("")
        print("{:^5s}".format(str(i + 1)) + "|" + "-" * 54)

        print(" " * 5 + "|", end="")
        print("{:^5s}|".format("Р"), end="")
        for j in range(3):
            print("{:^15.3g}|".format(v_ch[i][j]), end="")
        print("")
        print("-" * 60)

    print("\n")

    #  Теперь для абсолютного приоритета:
    prty = ['PR'] * n_num
    semo_im = NetworkPrty(k_num, L, R, n, prty, serv_params, nodes_prty)

    semo_im.run(jobs_num)

    v_im = semo_im.v_semo

    semo_calc = network_calc.network_prty_calc(R, b, n, L, prty, nodes_prty)
    v_ch = semo_calc['v']

    print("-" * 60)
    print("{0:^60s}".format("Абсолютный приоритет"))

    print("-" * 60)
    print("{0:^11s}|{1:^47s}|".format('', 'Номер начального момента'))
    print("{0:^10s}| ".format('№ кл'), end="")
    print("-" * 45 + " |")

    print(" " * 11 + "|", end="")
    for j in range(3):
        s = str(j + 1)
        print("{:^15s}|".format(s), end="")
    print("")
    print("-" * 60)

    for i in range(k_num):
        print(" " * 5 + "|", end="")
        print("{:^5s}|".format("ИМ"), end="")
        for j in range(3):
            print("{:^15.3g}|".format(v_im[i][j]), end="")
        print("")
        print("{:^5s}".format(str(i + 1)) + "|" + "-" * 54)

        print(" " * 5 + "|", end="")
        print("{:^5s}|".format("Р"), end="")
        for j in range(3):
            print("{:^15.3g}|".format(v_ch[i][j]), end="")
        print("")
        print("-" * 60)

    print("\n")


if __name__ == "__main__":
    test()
