import numpy as np
from optimisers import MultiSurrogateOptimiser, MonoSurrogateOptimiser
from pymoo.core.problem import ElementwiseProblem
from scalarisations import Tchebicheff, PBI, ModifiedTchebicheff, WeightedSum, IPBI, ExponentialWeightedCriterion, WeightedNorm, WeightedPower, WeightedProduct, AugmentedTchebicheff
from util_functions import ei_over_decomposition
import matplotlib.pyplot as plt

class MyProblem(ElementwiseProblem):

    def __init__(self):
        super().__init__(n_var=2,
                         n_obj=2,
                         xl=np.array([-2,-2]),
                         xu=np.array([2,2]))

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = 100 * (x[0]**2 + x[1]**2)
        f2 = (x[0]-1)**2 + x[1]**2
        out["F"] = [f1, f2]

# problem = MyProblem()
# optimi = MultiSurrogateOptimiser(problem, [0,0], [700,12])
# out = optimi.solve(n_iterations=100, display_pareto_front=True, n_init_samples=20, sample_exponent=3, acquisition_func=Tchebicheff([0,0],[700,12]))
# out = optimi.solve(n_iterations=30, display_pareto_front=True, n_init_samples=10)

# from pymoo.problems import get_problem
# problem = get_problem("dtlz5", n_obj=2, n_var=5)
# optimi = MultiSurrogateOptimiser(problem, [0,0], [2.0,2.0])
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, sample_exponent=3, acquisition_func=WeightedSum())
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, sample_exponent=3, acquisition_func=Tchebicheff([0,0], [2.0,2.0]))
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, sample_exponent=3, acquisition_func=ModifiedTchebicheff([0,0], [2.0,2.0]))
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, sample_exponent=3, acquisition_func=AugmentedTchebicheff([0,0], [2.0,2.0]))
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, sample_exponent=3, acquisition_func=ExponentialWeightedCriterion())
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, sample_exponent=3, acquisition_func=WeightedNorm())
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, sample_exponent=3, acquisition_func=WeightedPower())
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, sample_exponent=3, acquisition_func=WeightedProduct())
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, sample_exponent=3, acquisition_func=PBI([0,0], [2.0,2.0]))
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, sample_exponent=3, acquisition_func=IPBI([0,0], [2.0,2.0]))

# optimi = MonoSurrogateOptimiser(problem, [0,0], [2.0,2.0])
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, aggregation_func=WeightedSum())
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, aggregation_func=Tchebicheff([0,0], [2.0,2.0]))
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, aggregation_func=ModifiedTchebicheff([0,0], [2.0,2.0]))
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, aggregation_func=AugmentedTchebicheff([0,0], [2.0,2.0]))
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, aggregation_func=ExponentialWeightedCriterion())
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, aggregation_func=WeightedNorm())
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, aggregation_func=WeightedPower())
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, aggregation_func=WeightedProduct())
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, aggregation_func=PBI([0,0], [2.0,2.0]))
# out = optimi.solve(n_iterations=10, display_pareto_front=True, n_init_samples=20, aggregation_func=IPBI([0,0], [2.0,2.0]))



# ei_over_decomposition([0,0], models, weights, agg_func, minimum, ideal_point, max_point)


####################################################################
nx, ny = (75, 75)
# x = np.linspace(-1.76, 3, nx)
# y = np.linspace(-1.9, 3, ny)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = np.meshgrid(x, y)
obj = list(zip(xv.flatten(), yv.flatten()))
obj = np.asarray([list(i) for i in obj])

import pdb; pdb.set_trace()

fig, axs = plt.subplots(2,5, sharex=True, sharey=True)
fig.supxlabel(r'$f_1(x)$')
fig.supylabel(r'$f_2(x)$')

dec = IPBI([0,0], [1,1])
cheb_outputs = [dec(i, [0.5,0.5]) for i in obj]
axs[0,0].scatter(obj[:,0], obj[:,1], c=cheb_outputs)
axs[0,0].set_xlabel('IPBI')
print(dec(obj[5], [0.5,0.5]))

dec = WeightedNorm()
cheb_outputs = [dec(i, np.asarray([0.5,0.5])) for i in obj]
axs[0,1].scatter(obj[:,0], obj[:,1], c=cheb_outputs)
axs[0,1].set_xlabel('WN')
print(dec(obj[5], [0.5,0.5]))


dec = WeightedPower()
cheb_outputs = [dec(i, np.asarray([0.5,0.5])) for i in obj]
axs[0,4].scatter(obj[:,0], obj[:,1], c=cheb_outputs)
axs[0,4].set_xlabel('WPO')
print(dec(obj[5], [0.5,0.5]))

dec = WeightedProduct()
cheb_outputs = [dec(i, np.asarray([0.5,0.5])) for i in obj]
axs[1,0].scatter(obj[:,0], obj[:,1], c=cheb_outputs)
axs[1,0].set_xlabel('WPR')
print(dec(obj[5], [0.5,0.5]))

dec = AugmentedTchebicheff([0,0], [1,1])
cheb_outputs = [dec(i, np.asarray([0.5,0.5])) for i in obj]
axs[1,1].scatter(obj[:,0], obj[:,1], c=cheb_outputs)
axs[1,1].set_xlabel('ATCH')
print(dec(obj[5], [0.5,0.5]))

dec = ModifiedTchebicheff([0,0], [1,1])
cheb_outputs = [dec(i, np.asarray([0.5,0.5])) for i in obj]
axs[0,2].scatter(obj[:,0], obj[:,1], c=cheb_outputs)
axs[0,2].set_xlabel('MTCH')
print(dec(obj[5], [0.5,0.5]))

dec = PBI([0,0], [1,1])
cheb_outputs = [dec(i, np.asarray([0.5,0.5])) for i in obj]
axs[1,2].scatter(obj[:,0], obj[:,1], c=cheb_outputs)
axs[1,2].set_xlabel('PBI')
print(dec(obj[5], [0.5,0.5]))

dec = ExponentialWeightedCriterion(p=1)
cheb_outputs = [dec(i, np.asarray([0.5,0.5])) for i in obj]
axs[1,3].scatter(obj[:,0], obj[:,1], c=cheb_outputs)
axs[1,3].set_xlabel('EWC')
print(dec(obj[5], np.asarray([0.5,0.5])))

dec = Tchebicheff([0,0],[1,1])
cheb_outputs = [dec(i, np.asarray([0.5,0.5])) for i in obj]
axs[0,3].scatter(obj[:,0], obj[:,1], c=cheb_outputs)
axs[0,3].set_xlabel('TCH')
print(dec(obj[5], [0.5,0.5])[0])

dec = WeightedSum()
cheb_outputs = [dec(i, np.asarray([0.5,0.5])) for i in obj]
axs[1,4].scatter(obj[:,0], obj[:,1], c=cheb_outputs)
axs[1,4].set_xlabel('WS')
print(dec(obj[5], [0.5,0.5])[0])

plt.show()
####################################################################

dec = PBI([0,0], [1,1])
cheb_outputs = [dec(i, np.asarray([0.5,0.5])) for i in obj]
plt.scatter(obj[:,0], obj[:,1], c=cheb_outputs)
# plt.xlabel('PBI')
plt.show()