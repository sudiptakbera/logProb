from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class WienerProcess:

      def __init__(self, path):
        self.path = path

      def setPrior(self, theta):
        '''priors for parameters'''
        return - np.log(theta)
      def logProb(self, theta):
        '''analytical expression for the logarithm of the posterior'''
        N = np.size(self.path[:, 1])
        x= self.path[:,0]
        t = self.path[:,1]
        dt = t[1] -t[0]
       # dx2 = sum((self.path[0, 1:] - self.path[0, :-1])**2)
        dx2=sum((x[1:] - x[:-1])**2)
        
        s = -dx2/(4*theta*dt)  + setPrior -0.5*(N-1)*np.log(4*theta*np.pi*(dt))
        return s


      def mapEstimate(self, method):
        '''analytical or numerical maximum aposteriori estimate of parameters'''
        N = np.size(self.path[:, 1])
        x= self.path[:,0]
        t = self.path[:,1]
        dt = t[1] -t[0]
        sigma = np.sqrt(np.sum((x[1:]-x[:-1])**2)/(dt*(N+1)))
        D = sigma*sigma/2
        return D
        print ()   
      def normalEstimate(self):
        '''analytical estimate of parameters assuming asymptotic normality'''

      def posteriorInterval(self, percent):
        '''domain containing p percent of the probability'''

      def plotLogProb(self, extent):
        '''plot of the posterior probability'''
        th = extent*0     # initializing x to be zeros of same size as extent
        
        for i in range(np.size(extent)):
            '''call logProb method and update x'''
            th[i] = self.logProb(extent[i])

        #plotting logProb with extent
        plt.plot(extent, th)
        plt.xlabel('Theta')
        plt.ylabel('logProb')
        plt.show()


class OrnsteinUhlenbeckProcess:

      def __init__(self, path):
        self.path = path

      def setPrior(self, prior):
        '''priors for parameters'''

      def logProb(self,theta1,theta2):
        '''analytical expression for the logarithm of the posterior'''
        N = np.size(self.path[:, 1])
        x= self.path[:,0]
        t = self.path[:,1]
        dt = t[1] -t[0]
        mu = theta1
        sigma = theta2
        dx2 = np.sum((x[1:]-x[:-1]*np.exp(-mu*dt))**2)
        I = 1-np.exp(-2*mu*dt)
        s1 = 0.5*(N-1)*np.log(mu/(np.pi*sigma*sigma*I))-mu*dx2/(sigma*sigma*I)
        return s1
      def mapEstimate(self, method):
        '''analytical or numerical maximum aposteriori estimate of parameters'''

      def normalEstimate(self):
        '''analytical estimate of parameters assuming asymptotic normality'''
        N = np.size(self.path[:, 1])
        x= self.path[:,0]
        t = self.path[:,1]
        dt = t[1] -t[0]
        mu =( 1/dt)*np.log((np.sum(x[0:]**2)/N)/(np.sum(x[1:]*x[:-1])/N))
        sigma = np.sqrt(2*(mu*(np.sum((x[1:]-x[:-1]*np.exp(-mu*dt))**2)/N)/(1-np.exp(-2*mu*dt))))
        D=sigma*sigma/2
        kB = 1.38e-23
        T = 300
        gamma = kB*T/D
        k=mu*gamma
        return k, D
        print (k,D) 

      def posteriorInterval(self, percent):
        '''domain containing p percent of the probability'''

      def plotLogProb(self, extent):
        '''plot of the posterior probability'''
        #th = extent*0     # initializing x to be zeros of same size as extent
        th = np.zeros((np.size(extent[:,0]),np.size(extent[:,1])))
        for l in range(np.size(extent[:,0])):
                for m in range(np.size(extent[:,1])):
            #'''call logProb method and update x'''
                     th[l,m] = self.logProb(extent[l,0],extent[m,1])
        #np.savetxt('output.txt', th, delimiter=" ")
        #print np.shape(th)
        plt.clf()
        mu=extent[:,0]
        sigma = extent[:,1]
        mu, sigma = np.meshgrid(mu,sigma) 
        np.savetxt('output.txt', th, delimiter=" ")
        np.savetxt('mu.txt', mu, delimiter=" ")
        np.savetxt('sigma.txt', sigma, delimiter=" ")  
        #plt.axis([mu.min(), mu.max(),sigma.min(),sigma.max()])
        #plt.pcolor(mu, sigma,th)
	#plt.colorbar()
	#plt.hold('on')
        #[i, j] = np.where(th == np.max(th))
        #plt.plot(mu[i,j],sigma[i,j],'gs')
	#plt.axis('tight')
        #plt.xlabel(r'$\mu$')
        #plt.ylabel('sigma')
        #plt.show()
	
        #print (mu[i,j],sigma[i,j])
        D=sigma*sigma/2
        kB = 1.38e-23
        T = 300
        gamma = kB*T/D
        k=mu*gamma
        plt.axis([k.min(), k.max(),D.min(),D.max()])
        plt.pcolor(k, D,th)
	plt.colorbar()
	plt.hold('on')
        [i, j] = np.where(th == np.max(th))
        plt.plot(k[i,j],D[i,j],'gs')
	plt.axis('tight')
        plt.xlabel('k')
        plt.ylabel('D')
        plt.ticklabel_format(style='sci',axis = 'x', scilimits=(0,0))
	
        print (k[i,j],D[i,j])




