 # -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

from scipy.special import legendre
#!!!IMPORTANT:!!!
#both legendre and fourier variables have to have boolians
#if one wants to use fourier the variables should be:  fourier=True and legendre=False
#if one wants to use legendre it variables  be:  fourier=False and legendre=True

pe=1#potential energy
fourier_check=True               #tell to use fourier series for the basis set 
legendre_check=False             #tells to use legendre polynomials if it is true
constant=4                    #constant needed for hamiltonian operator
size_basis_set=150                      #size of the basis set
positions=np.arange(-1,1, 0.01)        #domain on which the wave function is defined
period=np.max(positions)-np.min(positions)                               #period for fourier serier
y_psi=np.array([(np.sin(2*np.pi*t)+t**3) for t in positions])  #Wave function

def cn_fourier(n):
   ''' takes in an inndex n and returns the fourier series coeficient cn for that index
   Var:
        n-index in fourier series, is an integer
   Returns:
        cn-coefficient of the fourier serier for index n
   '''
   c = y_psi*np.exp(-1j*2*n*np.pi*positions/period)
   cn=c.sum()/c.size
   return cn


def fourier(x, Nh):
   '''
   a function that takes a point in the domain and the basis set size and returns fourier sum
   Var:
       x- a point in a domain 
       Nh-size of the basis set
   Returns:
       f.sum()- fourier series sum
   '''
   f = np.array([2*cn_fourier(i)*np.exp(1j*2*i*np.pi*x/period) for i in np.arange(1,Nh+1)])
   return f.sum()


y_fourier = np.array([fourier(t,size_basis_set).real for t in positions])    #fourier 


def cn_legendre(x,y):
   '''
   a function that takes in a domain and function that is defined in that domain and tries to get the coefficients of the legendre polynomials
   Var:
      x-independent variable (in our case the x domain in which the wave function exists)
      y-dependent variable (in our case the wave function represeted as a vector)
   Returns:
      cn-the coefficient of the legendre polynomail
      '''
   cn=np.polynomial.legendre.legfit(x,y, size_basis_set)
   return cn

legendre_coeff=cn_legendre(positions,y_psi)     #vector of legendre coefficients
for i in range(len(legendre_coeff)):
   if (abs(legendre_coeff[i])<1*10**(-10)):
      legendre_coeff[i]=0
#print tuple(map(tuple, legendre_coeff))
fourier_coeff=np.array([cn_fourier(size_basis_set) for i in np.arange(0.5,size_basis_set+05)])         #vector of fourier coefficients

y_legendre=np.polynomial.legendre.legval(positions,legendre_coeff)     #legendre polynomial of the wave function

def fourier_deriv(x,Nh):
   '''                                                                                    
   a function that takes a point in the domain and the basis set size and returns fourier's second derivative                                                                                     
   Var:                                                                                   
       x- a point in a domain                                                             
       Nh-size of the basis set                                                           
   Returns:                                                                                                                                       
   '''
   f = np.array([2*-1*(2*i*np.pi/period)**2*cn_fourier(i)*np.exp(1j*2*i*np.pi*x/period) for i in np.arange(1,Nh+1)\
])
   sum=f.sum()
   return sum
def final_fourier_deriv():
   y_fourie_dev = np.array([fourier_deriv(x,size_basis_set).real for x in np.arange(0.5,size_basis_set+05)])         #fourier     
   return y_fourie_dev

def laplacian(leg_check,array_coeff):
   a=[]
   if(leg_check==True):
      a=np.polynomial.legendre.legder(array_coeff,2)
   return a
 

plt.plot(positions, y_fourier, 'g')   #fourier approximation shown in green
plt.plot(positions,y_psi, '--r')      #the wave function shown in dashed red
plt.plot(positions,y_legendre, 'o')   #the legendre approximation in blue dots
plt.savefig('fourier1.png')           #saves the image that has the wavefunction,fourier approximation and legendre approximation

filename="Pot_Example1.txt"            #the name of the pot energy file

def potential_force_data(potential_file):
   '''takes a name of the potential energy file and returns an array of potentials energy      data
   Var:
       potential_energy-name of the PE file
   Returns:
       data: an array that contains the positions and corresponding PE
   '''
   if(potential_file==None):
      raise ValueError("No file is given")        
   file=open(potential_file, 'r')        #opens the file in read mode

   data=[]
   for line in file:                     #line by line reading
      
      line=line.split()                  #splitting the lines by a whitespace
      
      numbers=[]                         #creates an empty array to hold the contents of lines
      for string in line:                #iterates through strings in the line
      
         number=float(string)            #converts string to a float
         
         numbers.append(number)          #appends the numbers to the array 
         
         data.append(numbers)            #appends the numbers array to the data array
   
   return data                           #returns the data array

pe_data=potential_force_data(filename)   #saves the data in the pe_data array

#def pe_force_reader(position):
 #   for datum in pe_data:
  #      if(position<=datum[1]):
   #         #print datum[3], datum[2]
    #        return datum[3]#PE_force 


def hamiltonian_legendre(coef):
      hamilton=laplacian(legendre_check,coef)       
      #hamilton=np.ndarray.tolist(hamilton)  
      hamilton.append(0)
      hamilton.append(0)
      hamilton=np.asarray(hamilton)
      hamiltonian=np.zeros((len(hamilton)))
      for i in np.arange(len(hamilton)):
         hamiltonian[i]=pe*coef[i]+hamilton[i]*(-constant)
      hamiltonian_last=np.zeros((len(hamilton)))
      for i in np.arange(len(hamiltonian)):
         hamiltonian_last[i]=hamiltonian[i]*coef[i]
      return hamiltonian_last


def hamiltonian_fourier( coef):
      hamilton=final_fourier_deriv()
      print len(hamilton), len(coef)
      ##hamilton=np.ndarray.tolist(hamilton)
      #hamilton.append(0)
      #hamilton.append(0)
      #hamilton=np.asarray(hamilton)
      
      #hamilton[len(hamilton)+1]=0
      #hamilton[len(hamilton)+1]=0
      hamiltonian=np.zeros((len(hamilton)))
      #print len(coef),len(hamilton)
      for i in np.arange(len(hamilton)):
         hamiltonian[i]=pe*coef[i]+hamilton[i]*(-constant)
      hamiltonian_last=np.zeros((len(hamilton)))
      for i in np.arange(len(hamiltonian)):
         hamiltonian_last[i]=hamiltonian[i]*coef[i]
      return hamiltonian_last
#print hamiltonian_fourier(fourier_coeff)
def answer(check):
   a=[]
   if (check==False):
      a=hamiltonian_legendre(legendre_coeff)
   else:
      a=hamiltonian_fourier(fourier_coeff)
   return a,1
answers=answer(legendre_check)  
print 'The hamiltonian of is shown below for Legendre={} :\n {}'.format(legendre_check,answers[0])
#plt.show()

