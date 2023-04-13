import numpy as np

def string_to_roots(w,z):
    # w,z are lists, representing strings of \pm1s
    # this function will return the roots of the 
    # corresponding polynomial to the preperiodic itinerary wz^\infty
    ell=len(w)
    p=len(z)
    alpha=w+z
    f=[]
    # f will be the coefficients of the polynomial ordered wrt the
    # numpy.roots solver
    for i in range(ell):
        f.append(alpha[p+ell-1-i]-alpha[ell-1-i])
    for i in range(ell,p+ell):
        f.append(alpha[ell+p-1-i])
    rs=np.roots(f) 
    list_rs=[] #np array type is annoying so convert to list
    for i in range(len(rs)):
        lam=rs[i]
        if abs(lam.imag)>.0001 and abs(lam)<1: 
            # remove elements (almost) 
            # on real axis, keep only elements in D
            list_rs.append(lam)
    return list_rs


w=[1,-1,1]
z=[1,1,-1,1]
print(string_to_roots(w,z))





