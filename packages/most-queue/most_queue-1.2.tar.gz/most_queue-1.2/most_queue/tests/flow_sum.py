from most_queue.theory.flow_sum import SummatorNumeric
from most_queue.sim import flow_sum_im
from most_queue.sim import rand_destribution as rd
import matplotlib.pyplot as plt


def test():
    """
    Тестирование суммирования потоков
    """

    # Задаем следующие параметры:
    n_nums = 10  # число суммируемых потоков
    coev = 0.74  # коэффициент вариации каждого потока
    mean = 1  # среднее каждого потока
    num_of_jobs = 400000  # количество заявок для ИМ
    is_semi = False  # True, если необходимо использовать метод семиинвариантов вместо H2
    distr_im = "Gamma"  # распределение, используемое для ИМ

    # число суммируемых потоков
    ns = [x + 2 for x in range(n_nums - 1)]

    # начальные моменты суммируемых потоков. В нашем случае все потоки одинаково распределены
    a = []
    for i in range(n_nums):
        params1 = rd.Gamma.get_mu_alpha_by_mean_and_coev(mean, coev)
        a1 = rd.Gamma.calc_theory_moments(*params1, 4)
        a.append(a1)

    # Численный расчет
    s = SummatorNumeric(a, is_semi=is_semi)
    s.sum_flows()  # в  s._flows[i][j] содержатся начальные моменты суммируемых потокоы,
    # i - кол-во суммируемых потоков, j - номер начального момента

    # ИМ
    s_im = flow_sum_im.SummatorIM(a, distr=distr_im, num_of_jobs=num_of_jobs)
    s_im.sum_flows()  # в  s_im._flows[i][j] содержатся начальные моменты суммируемых потокоы,
    # i - кол-во суммируемых потоков, j - номер начального момента

    # Расчет ошибок и отображение результатов
    coevs_im = s_im.coevs
    coevs_num = s.coevs
    errors1 = []
    errors2 = []
    errors_coev = []

    str_f = "{0:^18s}|{1:^10.3f}|{2:^10.3f}|{3:^10.3f}|{4:^10.3f}|{5:^10.3f}"
    print("{0:^18s}|{1:^10s}|{2:^10s}|{3:^10s}|{4:^10s}|{5:^10s}".format("-", "a1", "a2", "a3", "a4", "coev"))
    print("-" * 80)

    for i in range(n_nums - 1):
        print("{0:^80s}".format("Сумма " + str(i + 2) + " потоков"))
        print("-" * 80)
        print(str_f.format("ИМ", s_im.flows_[i][0], s_im.flows_[i][1], s_im.flows_[i][2], s_im.flows_[i][3],
                           coevs_num[i]))
        print("-" * 80)
        print(str_f.format("Числ", s.flows_[i][0].real, s.flows_[i][1].real, s.flows_[i][2].real, s.flows_[i][3].real,
                           coevs_im[i]))
        print("-" * 80)
        errors1.append(SummatorNumeric.get_error(s.flows_[i][0].real, s_im.flows_[i][0]))
        errors2.append(SummatorNumeric.get_error(s.flows_[i][1].real, s_im.flows_[i][1]))
        errors_coev.append(SummatorNumeric.get_error(coevs_num[i], coevs_im[i]))

    fig, ax = plt.subplots()
    linestyles = ["solid", "dotted", "dashed", "dashdot"]

    ax.plot(ns, s_im.a1_sum, label="ИМ a1", linestyle=linestyles[0])
    ax.plot(ns, s.a1_sum, label="Числ a1", linestyle=linestyles[1])

    plt.legend()
    str_title = "Среднее сумм-х потоков, %"
    if is_semi:
        str_title += ". Метод семиинвариантов"
    else:
        str_title += ". Метод H2"
    plt.title(str_title)
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(ns, errors1, label="error a1", linestyle=linestyles[0])
    ax.plot(ns, errors2, label="error a2", linestyle=linestyles[1])
    ax.plot(ns, errors_coev, label="error coev", linestyle=linestyles[2])

    plt.legend()
    str_title = "Отн. ошибка от числа сумм-х потоков, %"
    if is_semi:
        str_title += ". Метод семиинвариантов"
    else:
        str_title += ". Метод H2"
    plt.title(str_title)
    plt.show()


if __name__ == "__main__":
    test()
