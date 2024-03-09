"""
    Scott Quashen
    CSC 309 SFSU Spring 2024
    Lab #06
    Created on Wednesday March 6 13:43 2024   
    Last Updated ....

    Description: 
        The program creates a bar plot comparing (mock) results in apparently milliseconds
        for what (assumedly) is a bubble sort runtime based on predefined problem sizes.
    
    Inputs: 
        createPlot( xData, yData, xAxisLab, yAxisLab, title )
        
            xData :
                List of Floats
                - values plugged into the calculation
                
            yDataRepresentingListTiming : 
                List of integers
                Representing mock time in what appears to be milleseconds 
                
            yDataRepresentingArrayTiming :
                List of integers
                Representing mock time in what appears to be milleseconds 

    Returns: 
        none

    Dependencies: time, mathhplotlib.pyplot, math

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.3.1
"""




#----Import all modules

import time
import matplotlib.pyplot as plt
import numpy as np


 

#----Define All Functions

def PrintNameDateTime():
    
    """
    
    Description
    ----------  
    Prints dev name and current time/ date

    Parameters
    ----------
    None.
            
    Returns
    -------
    None.

    """
    
    print( "Scott Quashen", time.asctime() )
    
# end PrintNameDateTime


def createPlot( xData, yDataRepresentingListTiming, yDataRepresentingArrayTiming ):
    
    """
    
    Description
    ----------  
    createPloat() uses mathPlot to create a chart representing the time taken 
    to perfrom an (assumedly) bubble sort calculation with given problem sizes.

    Parameters
    ----------
        
        xData : 
            List of integers
            Our problem sizes
            
        yDataRepresentingListTiming : 
            List of floats
            Our y-axis values for plotting

        yDataRepresentingArrayTiming : 
            List of floats
            Our y-axis values for plotting
            
    Returns
    -------
    None.

    """
    
    # string values for x ticks
    X = [ str( t ) for t in xData ]
    
    X_axis = np.arange( len( xData ) ) 
    
    plt.bar( X_axis - 0.2, yDataRepresentingListTiming, 0.4, label='List', color='darkblue' )
    plt.bar( X_axis + 0.2, yDataRepresentingArrayTiming, 0.4, label='Array', color='goldenrod' )
    
    plt.xticks( X_axis, X )    
    plt.title( "Bubble Sort Runtimes: Lists Vs. Arrays" )
    plt.xlabel( 'Problem Size' )
    plt.ylabel( 'Time (ms)' )
    plt.legend( ["Lists", "Arrays"], loc=2 )    
    plt.savefig( "Scott Quashen_Lab_6.png", dpi=600 )   
    plt.show()

# end createPlot() func


def main():
    
    """
    
    Description
    ----------  
    Calling main() function defines our constants and initiates our program when called.

    Parameters
    ----------
        
    None.
            
    Returns
    -------
    None.

    """
    
    # Best to define your variables here.
   
    # Problem sizes and string version of problem sizes, used for axis labels
    N = [ 128, 256,512, 1024, 2048, 4096, 8192 ]

    # "fake" timings for sorting Lists and Arrays
    listTimings = [ 100, 400, 1600, 6400, 12000, 40000, 160000 ]
    arrayTimings = [ 110, 440, 1800, 7000, 14000, 44000, 172000 ]

    PrintNameDateTime()
    createPlot( N, listTimings, arrayTimings )

    return None

# end of main function

 


#----Entry point

if __name__ == "__main__":
    main()









