import sys
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as LA

def main():
    with open(sys.argv[1], encoding='utf-8') as f:
        labels = f.readline().strip().split(',')
        years = list()
        duration = list()
        for line in f:
            data = line.strip().split(',')
            years.append(int(data[0]))
            duration.append(int(data[1]))
        
        #Q2
        plt.plot(years, duration) 
        plt.savefig("plot.jpg")
        
        #Q3
        n = len(years)
        column1 = np.array([1] * n)
        column2 = np.array(years)
        X = np.transpose(np.array((column1, column2)))
        print("Q3a:") 
        print(X)
        
        Y = np.array(duration)
        print("Q3b:") 
        print(Y)
        
        Z = np.dot(np.transpose(X), X)
        print("Q3c:") 
        print(Z)
        
        I = LA.inv(Z)
        print("Q3d:")
        print(I)
        
        PI = np.dot(I,np.transpose(X))
        print("Q3e:")
        print(PI)
        
        hat_beta =np.dot(PI,Y)
        print("Q3f:")
        print(hat_beta)
        
        #Q4
        print("Q4: " +str(np.dot(hat_beta,[1,2021])))   
        
        #Q5
        print("Q5a:", end = ' ')
        if hat_beta[1] > 0:
            print('>')
        elif hat_beta[1] == 0:
            print('=')
        else:
            print('<')
        print("Q5b: There is a negative correlation between years and the number of ice days.")
        
        #Q6
        print("Q6:" + str(-1*hat_beta[0]/hat_beta[1]))
        print("Q6b: Yes. Because the over all trend for the number of ice dyas is decreasing.")
    
if __name__ == "__main__":
    main()
