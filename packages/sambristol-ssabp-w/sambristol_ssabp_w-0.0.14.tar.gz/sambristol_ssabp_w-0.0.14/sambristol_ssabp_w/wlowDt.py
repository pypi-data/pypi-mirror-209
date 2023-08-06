import numpy as np
import scipy.special as special


from .effectivepotential import twobody_value, twobody_derivative
from .effectivepotential import threebody_value, threebody_derivative_u


class wHardSphere():

    
    """
    Evaluate the w(r) function when D_t goes to 0 (is much smaller than D_r*sigma**2)


    Attributes
    ----------
    Pi : float (optional)
        value of the parameter Pi in eqn 1 above. Default value is 3.

    denom : float (optional)
        value of fitting parameter. No-fit parameter defaults to 3.

    

    as well as inherited attributes epsilon from parent class.

    Methods
    -------

    __init__(self,potentialclass)
        Initialise attributes.


    w(self,r)
        Compute the solution to the ode mentioned in the class doc.

    
    w_prime(self,r)
        Compute the derivative of the solution to the ode mentioned in
        the class doc.

    """


    def __init__(self,potentialclass,cutoff=1):

        """
        Initialise attributes.

        Parameters
        ----------
        potentialclass : potential
            class with potential that has attribute self.V_derivative(r) and
            self.V_doublederiv(r)
        """

        self.Vderiv = potentialclass.V_derivative
        self.Vdoublederiv = potentialclass.V_doublederiv
        self.cutoff = cutoff
        return



    def w(self,r):
        """

        Compute the solution to the ode mentioned in the class doc.

        Parameters
        ----------
        r : float or np.array
            Distance between particles.

        Returns
        -------
        value : float or np.array
            Value of the w-function.

        """
        
        return np.where(r<self.cutoff,-self.Vderiv(r)/(2*r),0)

    
    def w_prime(self,r):
        """

        Compute the derivative of the solution to the ode mentioned in
        the class doc.

        Parameters
        ----------
        r : float or np.array
            Distance between particles.

        Returns
        -------
        value : float or np.array
            Value of the w-function derivative.

        """

        return np.where(r<self.cutoff,-self.Vdoublederiv(r)/(2*r)+self.Vderiv(r)/(2*r*r),0)

    def Effective2Bod(self,r,fp):
        """

        Compute the effective two-body interaction.

        Parameters
        ----------
        r : float or np.array
            Distance between particles.
        fp : float
            value of the active force.

        Returns
        -------
        value : float or np.array
            Value of the effective interaction at r.

        """

        

        return twobody_value(r,fp,self.w,self.V_value)

    def Effective2Bod_prime(self,r,fp):
        """

        Compute the derivative of the effective
        two-body interaction.

        Parameters
        ----------
        r : float or np.array
            Distance between particles.
        fp : float
            value of the active force.

        Returns
        -------
        value : float or np.array
            Derivative of the effective interaction at r.

        """
        

        return twobody_derivative(r,fp,self.w,
                                  self.w_prime,
                                  self.V_derivative)

    def Effective3Bod(self,u,v,fp):
        """

        Compute the effective three-body interaction aside
        from a cosine factor.

        Parameters
        ----------
        u : float or np.array
            Distance between particles 1 and 2.
        v: float or np.array
            Distance between particles 1 and 3.
        fp : float
            value of the active force.

        Returns
        -------
        value : float or np.array
            Value of the effective interaction at u,v.

        """
        

        return threebody_value(self,u,v,fp,self.w)

    def Effective3Bod_prime_u(self,u,v,fp):

        """

        Compute the effective three-body interaction aside
        from a cosine factor.

        Parameters
        ----------
        u : float or np.array
            Distance between particles 1 and 2.
        v: float or np.array
            Distance between particles 1 and 3.
        fp : float
            value of the active force.

        Returns
        -------
        value : float or np.array
            Derivative of the effective interaction at u,v.

        """
        

        return threebody_derivative_u(self,u,v,fp,
                                      self.w,self.w_prime)

