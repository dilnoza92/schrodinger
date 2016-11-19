 # -*- coding: utf-8 -*-
import numpy as np
import math
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy
from scipy.special import legendre
#!!!IMPORTANT:!!!
#both legendre and fourier variables have to have boolians
#if one wants to use fourier the variables should be:  fourier=True and legendre=False
#if one wants to use legendre it variables  be:  fourier=False and legendre=True

pe=1                 #potential energy
fourier_check=True               #tell to use fourier series for the basis set 
legendre_check=False             #tells to use legendre polynomials if it is true
constant=1                   #constant needed for hamiltonian operator
size_basis_set=20       #size of the basis set

parser=argparse.ArgumentParser()                  #parses command line inputs                                                                                                              
parser.add_argument('--fourier', nargs="?")       #adds a flag for fourier has to be a boolean                  
parser.add_argument('--legendre', nargs="?")      #adds a flag for legendre has to be a boolean
parser.add_argument('--constant', nargs="?")          #adds a flag for constant
parser.add_argument('--potential_energy', nargs="?")  #adds a flag for potential energy
parser.add_argument('--input_file', nargs="?")        #adds a flag for input file 
parser.add_argument('--basis_set_size', nargs="?")    #adds a flag for basis set size
parser.add_argument('schrodinger/schrodinger.py', nargs='?')#makes sure that parser doesn't give error when it reads the source code                                     
arguments=parser.parse_args()                 #arguments given in the command line                                                                                                        
filename="Pot_Example1.txt" 
print arguments
if (arguments.potential_energy!=None):
   pe=float(arguments.potential_energy)     
if (arguments.fourier!=None):            #potential energy
   fourier_check=arguments.fourier               #tell to use fourier series for the basis set
if (arguments.legendre!=None): 
   legendre_check=arguments.legendre             #tells to use legendre polynomials if it is true
if (arguments.constant!=None):
   constant=float(arguments.constant)                   #constant needed for hamiltonian operator
if (arguments.basis_set_size):
   size_basis_set=int(arguments.basis_set_size)       #size of the basis set
if (arguments.input_file!=None):
   filename=arguments.input_file
positions=np.arange(-1,1, 0.01)               #domain on which the wave function is defined
period=np.max(positions)-np.min(positions)    #period for fourier serier
alpha=100
def wavefunction(par):
   y_psi=np.array([(np.exp(-(t/par)**2)) for t in positions])  #Wave function
   return y_psi
def cn_fourier(n,par):
   ''' takes in an inndex n and returns the fourier series coeficient cn for that index
   Var:
        n-index in fourier series, is an integer
   Returns:
        cn-coefficient of the fourier serier for index n
   '''
   c = wavefunction(par)*np.exp(-1j*2*n*np.pi*positions/period)
   cn=c.sum()/c.size
   return cn


def fourier(x, Nh,par):
   '''
   a function that takes a point in the domain and the basis set size and returns fourier sum
   Var:
       x- a point in a domain 
       Nh-size of the basis set
   Returns:
       f.sum()- fourier series sum
   '''
   f = np.array([2*cn_fourier(i,par)*np.exp(1j*2*i*np.pi*x/period) for i in np.arange(1,Nh+1)])
   return f.sum()

def y_fourier_1(par):
   return  np.array([fourier(t,size_basis_set,par).real for t in positions])    #fourier approximation of the wave function


def cn_legendre(x,y):
   '''
   a function that takes in a domain and function that is defined in that domain and tries to get the coefficients of the legendre polynomials
   Var:
      x-independent variable (in our case the x domain in which the wave function exists)
      y-dependent variable (in our case the wave function represeted as a vector)
   Returns:
      cn-the coefficient of the legendre polynomail
      '''
   cn=np.polynomial.legendre.legfit(x,y, size_basis_set-1)
   return cn
def legendre_coeff(par):
   legendre_coeff=cn_legendre(positions,wavefunction(par))     #vector of legendre coefficients
   #return legendre_coeff
   for i in range(len(legendre_coeff)):
      if (abs(legendre_coeff[i])<1*10**(-10)):
         legendre_coeff[i]=0
   return legendre_coeff
#print tuple(map(tuple, legendre_coeff))
def fourier_coefficient(par):
   fourier_coeff=np.array([cn_fourier(size_basis_set,par) for i in np.arange(0.5,size_basis_set+0.5)])         #vector of fourier coefficients
   return fourier_coeff
def legendre_val(par):
   y_legendre=np.polynomial.legendre.legval(positions,legendre_coeff(par))     #legendre polynomial of the wave function
   return y_legendre
def fourier_deriv(x,Nh,par):
   '''                                                                                    
   a function that takes a point in the domain and the basis set size and returns fourier's second derivative                                                                                     
   Var:                                                                                   
       x- a point in a domain                                                             
       Nh-size of the basis set                                                           
   Returns:                                                                                                                                       
   '''
   f = np.array([2*-1*(2*i*np.pi/period)**2*cn_fourier(i,par)*np.exp(1j*2*i*np.pi*x/period) for i in np.arange(1,Nh+1)\
])
   sum=f.sum()
   return sum
def final_fourier_deriv(par):
   y_fourie_dev = np.array([fourier_deriv(x,size_basis_set,par).real for x in np.arange(0.5,size_basis_set+0.5)])         #fourier     
   return y_fourie_dev

def laplacian(leg_check,array_coeff):
   a=[]
   if(leg_check==True):
      a=np.polynomial.legendre.legder(array_coeff,2)
   return a
 

plt.plot(positions, y_fourier_1(1), 'g')   #fourier approximation shown in green
plt.plot(positions,wavefunction(1), '--r')      #the wave function shown in dashed red
plt.plot(positions,legendre_val(1), 'o')   #the legendre approximation in blue dots
plt.savefig('fourier1.png')           #saves the image that has the wavefunction,fourier approximation and legendre approximation

            #the name of the pot energy file

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
   
   """  a function that takes in the basis set coefficients for legendre  and gives the hamiltonian
   Variables:
   
      coef-fourier basis set coeffiecients

   Returns:
    
      hamiltonian_last- an array of length of size the basis set that contains hamiltonian 
   """   
   hamilton=laplacian(legendre_check,coef)  #the laplacian of the legendre polynomial       
      #hamilton=np.ndarray.tolist(hamilton)  
   hamilton.append(0)                       #due to the removal of two points from the basis for laplacian two more points need to be appended to make the array have the size of the basis set
   hamilton.append(0)                       #the second addition 
   hamilton=np.asarray(hamilton)            #converts the list to an array
   hamiltonian=np.zeros((len(hamilton)))    #initializes an array of the size of the basis set to keep the hamiltonian before it is multiplied by the basis set coefficients
   for i in np.arange(len(hamilton)):
      hamiltonian[i]=pe*coef[i]+hamilton[i]*(-constant) #computes the laplacian plus the potential energy term of basis set coefficient
   #hamiltonian_last=np.empty([len(hamilton), len(hamilton)])           #initializes an array to keep the final solution
   hamiltonian_last=np.zeros((len(hamilton)))
   for i in np.arange(len(hamilton)):
      hamiltonian_last[i]=hamiltonian[i]*coef[i]        #computes the hamiltonian on the basis set functions
   return hamiltonian_last                              #the final hamiltonian



def hamiltonian_fourier(par,coef):
   """  a function that takes in the basis set coefficients for fourier and gives the hamiltonian
   Variables:
   
      coef-fourier basis set coeffiecients

   Returns:
    
      hamiltonian_last- an array of length of size the basis set that contains hamiltonian 
   """
   hamilton=final_fourier_deriv(par)          #laplacian of the fourier 
 
   hamiltonian=np.zeros((len(hamilton)))   #initiation of an array that will keep the hamiltonians
   for i in np.arange(len(hamilton)):
      hamiltonian[i]=pe*coef[i]+hamilton[i]*(-constant)    #computes the laplacian plus the potential energy term of basis set coefficient
   
   hamiltonian_last=np.zeros((len(hamilton)))
   for i in np.arange(len(hamiltonian)):
      hamiltonian_last[i]=hamiltonian[i]*coef[i]           #computes the hamiltonian on the basis set functions
   return hamiltonian_last

def answer(check,par):
   """ takes a boolean for whether to set legendre polynomial true or false and gives the hamiltonians and a 1
   Variables:

      check-boolean for legendre polynomial

   Returns:

      a,1-hamiltonian matrix and number 1
   """
   a=[]#saves the hamiltonian coefficients
   if (check==False):#checks whether to use legendre polynomial or not
      a=hamiltonian_legendre(legendre_coeff(par))#get the hamiltonian using legendre polynomials
   else:
      a=hamiltonian_fourier(par, fourier_coefficient(par))#gets the hamiltonian using fourier transforms
   return a,1

def hamiltonian(par):
   hamiltonian_res=answer(fourier_check,par)  #hamiltonian
#print (answers[0][0],answers[0][1])
   hamiltonian_1d=hamiltonian_res[0]
   return hamiltonian_1d
#print 'The hamiltonian of is shown below for Legendre={} :\n {}'.format(legendre_check,hamiltonian())
def energy_calculator(hamiltonian, coeff):
   numerator=np.dot(hamiltonian, coeff)
   denominator=np.dot(coeff,coeff)
   return numerator/denominator
#energy=energy_calculator(hamiltonian_1d, fourier_coefficient(1))
#print energy

energy=np.empty((100,))
index=np.empty((100))
for i in np.arange(100):
   random1=np.random.rand(1)
   index[i]=random1
   energy[i]=energy_calculator(hamiltonian(random1),fourier_coefficient(random1))
minimum_energy=min(energy)
index0=energy.min()
print index[index0], minimum_energy,wavefunction(index[index0])
