# import numpy as np


# def uniform_distribution():
#     return np.random.uniform(low=0.0, high=1.0, size=100)

# def normal_distribution(mean: int, std_dev: int):
#     return np.random.normal(loc=mean, scale=std_dev, size=100)

# def exponential_distribution():
#     return np.random.exponential(scale=1, size=100)

# def poisson_distribution():
#     return np.random.poisson(lam=2, size=100)

# def binominal_distribution():
#     return np.random.binomial(n=10, p=0.5, size=100)

# def geometric_distribution():
#     return np.random.geometric(p=0.3, size=100)

# def hypergeometric_distribution(ngood: int, nbad: int):
#     return np.random.hypergeometric(ngood=ngood, nbad=nbad, 
#                     nsample=np.random.randint(low=0, high=ngood + nbad), size=100)

# def standard_t_distribution():
#     return np.random.standard_t(df=10, size=100)

# def fisher_distribution():
#     return np.random.f(dfnum=5, dfden=10, size=100)

# def pearson_distribution():
#     return np.random.chisquare(df=7, size=100)

# def bernoulli_distribution():
#     return np.random.binomial(n=1, p=0.5, size=100)

# print("Uniform:", uniform_distribution())
# print("Normal:", normal_distribution(0, 1))
# print("Exponential:", exponential_distribution())
# print("Poisson:", poisson_distribution())
# print("Binomial:", binominal_distribution())
# print("Geometric:", geometric_distribution())
# print("Hypergeometric:", hypergeometric_distribution(5, 15))
# print("Standard_t:", standard_t_distribution())
# print("Fisher's f-distribution:", fisher_distribution())
# print("Pearson distribution:", pearson_distribution())
# print("Bernoulli:", bernoulli_distribution())


# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.stats import uniform, norm, expon, poisson, binom, geom, hypergeom, t, f, pearson3, bernoulli

# def uniform_distribution():
#     return uniform(loc=0, scale=1)

# def normal_distribution():
#     return norm(loc=0, scale=1)

# def exponential_distribution():
#     return expon(loc=0, scale=1)

# def poisson_distribution():
#     return poisson(mu=3)

# def binomial_distribution():
#     return binom(n=10, p=0.5)

# def geometric_distribution():
#     return geom(p=0.5)

# def hypergeometric_distribution():
#     return hypergeom(M=20, n=7, N=12)

# def standard_t_distribution():
#     return t(df=5)

# def fisher_distribution():
#     return f(dfn=5, dfd=10)

# def pearson_distribution():
#     return pearson3(skew=0.5, loc=0, scale=1)

# def bernoulli_distribution():
#     return bernoulli(p=0.3)

# # Plotting
# distributions = [
#     uniform_distribution(),
#     normal_distribution(),
#     exponential_distribution(),
#     poisson_distribution(),
#     binomial_distribution(),
#     geometric_distribution(),
#     hypergeometric_distribution(),
#     standard_t_distribution(),
#     fisher_distribution(),
#     pearson_distribution(),
#     bernoulli_distribution()
# ]

# x = np.linspace(-5, 15, 1000)

# for distribution in distributions:
#     if hasattr(distribution, 'pdf'):
#         plt.plot(x, distribution.pdf(x), label=str(distribution.dist.name)+" (pdf)")
#     else:
#         plt.plot(range(int(min(x)), int(max(x))+1), distribution.pmf(range(int(min(x)), int(max(x))+1)), label=str(distribution.dist.name)+" (pmf)")

# plt.title('Probability Density Functions / Probability Mass Functions')
# plt.xlabel('Layout')
# plt.ylabel('Probability')
# plt.legend()
# plt.show()



import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform, norm, expon, poisson, binom, geom, hypergeom, t, f, pearson3, bernoulli
import seaborn as sns
print(np.random.uniform(low=0.0, high=1.0, size=10))
print(uniform(loc=0, scale=1).pmf(10))

def generate_dull_colors(num_colors):
    dull_palette = sns.color_palette("hls", n_colors=num_colors, desat=0.5)
    return dull_palette

print(generate_dull_colors(15))

class Probfunc:
    
    def uniform_distribution(self):
        return uniform(loc=0, scale=1)

    def normal_distribution(self):
        return norm(loc=0, scale=1)

    def exponential_distribution(self):
        return expon(loc=0, scale=1)

    def poisson_distribution(self):
        return poisson(mu=3)

    def binomial_distribution(self):
        return binom(n=10, p=0.5)

    def geometric_distribution(self):
        return geom(p=0.5)

    def hypergeometric_distribution(self):
        return hypergeom(M=20, n=7, N=12)

    def standard_t_distribution(self):
        return t(df=5)

    def fisher_distribution(self):
        return f(dfn=5, dfd=10)

    def pearson_distribution(self):
        return pearson3(skew=0.5, loc=0, scale=1)

    def bernoulli_distribution(self):
        return bernoulli(p=0.3)
    
    def plt_show(self, x: np.linspace):
        distributions = [getattr(self, name)() for name in dir(self) 
                             if name.endswith('_distribution')]
        colors = generate_dull_colors(len(distributions))
        
        for i, distribution in enumerate(distributions):
            if hasattr(distribution, 'pdf'):
                plt.plot(x, distribution.pdf(x), 
                         label=str(distribution.dist.name)+" (pdf)",
                         color=colors[i])
            else:
                plt.plot(range(int(min(x)), int(max(x))+1), 
                         distribution.pmf(range(int(min(x)), int(max(x))+1)), 
                         label=str(distribution.dist.name)+" (pmf)", color=colors[i])
        
        plt.title('Probability Density Functions / Probability Mass Functions')
        plt.xlabel('Layout')
        plt.ylabel('Probability')
        custom_legend = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) 
                         for color in colors]
        plt.legend(custom_legend, [str(distribution.dist.name) for distribution in distributions])

        plt.show()
        
def main():
    print(Probfunc().plt_show(np.linspace(-5, 15, 1000)))
    
if __name__ == "__main__":
    main()
    