import numpy as np


def uniform_distribution():
    return np.random.uniform(low=0.0, high=1.0, size=100)

def normal_distribution(mean: int, std_dev: int):
    return np.random.normal(loc=mean, scale=std_dev, size=100)

def exponential_distribution():
    return np.random.exponential(scale=1, size=100)

def poisson_distribution():
    return np.random.poisson(lam=2, size=100)

def binominal_distribution():
    return np.random.binomial(n=10, p=0.5, size=100)

def geometric_distribution():
    return np.random.geometric(p=0.3, size=100)

def hypergeometric_distribution(ngood: int, nbad: int):
    return np.random.hypergeometric(ngood=ngood, nbad=nbad, 
                    nsample=np.random.randint(low=0, high=ngood + nbad), size=100)

def standard_t_distribution():
    return np.random.standard_t(df=10, size=100)

def fisher_distribution():
    return np.random.f(dfnum=5, dfden=10, size=100)

def pearson_distribution():
    return np.random.chisquare(df=7, size=100)

def bernoulli_distribution():
    return np.random.binomial(n=1, p=0.5, size=100)

print("Uniform:", uniform_distribution())
print("Normal:", normal_distribution(0, 1))
print("Exponential:", exponential_distribution())
print("Poisson:", poisson_distribution())
print("Binomial:", binominal_distribution())
print("Geometric:", geometric_distribution())
print("Hypergeometric:", hypergeometric_distribution(5, 15))
print("Standard_t:", standard_t_distribution())
print("Fisher's f-distribution:", fisher_distribution())
print("Pearson distribution:", pearson_distribution())
print("Bernoulli:", bernoulli_distribution())


# class bernoulli():
#     def pmf(x,p):
#         """
#         probability mass function        
#         """
#         f = p**x*(1-p)**(1-x)
#         return f
    
#     def mean(p):
#         """
#         expected value of bernoulli random variable
#         """
#         return p
    
#     def var(p):
#         """
#         variance of bernoulli random variable
#         """
#         return p*(1-p)
    
#     def std(p):
#         """
#         standart deviation of bernoulli random variable
#         """
#         return bernoulli.var(p)**(1/2)
    
#     def rvs(p,size=1):
#         """
#         random variates
#         """
#         rvs = np.array([])
#         for i in range(0, size):
#             if np.random.rand() <= p:
#                 a=1
#                 rvs = np.append(rvs,a)
#             else:
#                 a=0
#                 rvs = np.append(rvs,a)
#         return rvs

# t1 = bernoulli.rvs(0.2, size=5)
# t2 = np.random.binomial(n=1, p=0.2, size=5)
# print(f"t1 = {t1}, \nt2 = {t2}")

