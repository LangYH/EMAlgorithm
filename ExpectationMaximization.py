import numpy as np

def gaussianEM( data, clusters = 2, iteration = 6 ):
    N = data.size
    data.reshape( 1, N )
    #Initialization
    Pz = np.zeros( (clusters,1), dtype="float64" )
    Pz += 1.0 / clusters

    sample_index = np.array( np.percentile(data, range(100/(clusters+1),100,100/(clusters+1))[:clusters]), dtype="int" ).reshape(clusters,1)
    mu = data[np.zeros((clusters,1), dtype="int" ), sample_index]
    print "mu:"
    print mu
    np.random.seed(1)
    sample_matrix = np.random.randint( N, size=(clusters, N / 10  ) )
    samples = data[ np.zeros((clusters, N/10), dtype="int"), sample_matrix ]
    variance = samples.var( axis=1 ).reshape( clusters, 1 )
    print "variance:"
    print variance

    #E-step
    for i in range( iteration ):
        squareDistane = ( data - mu ) ** 2
        Pxz = 1 / ( np.sqrt( 2 * np.pi ) * np.sqrt(variance)) * np.exp( -squareDistane / ( 2 * variance) ) * Pz
        PzOfx = Pxz / Pxz.sum( axis = 0 )

        #m-step
        sumPz = PzOfx.sum( axis=1 ).reshape( clusters, 1 )
        Pz = 1. / N * sumPz
        mu_new = ( PzOfx * data ).sum( axis = 1 ).reshape(clusters,1) / sumPz
        print ""
        print "mu:"
        print mu_new
        variance_new = ( ( ( data - mu_new ) ** 2 * PzOfx ).sum( axis = 1 ) ).reshape( clusters, 1 ) / sumPz
        print ""
        print "variance:"
        print variance_new
        if( ( np.abs(mu_new - mu) < 1e-6 ).sum() == 2 & ( np.abs( variance_new - variance) < 1e-6 ).sum() == 2 ):
            return Pz, mu_new, variance_new
        else:
            mu = mu_new
            variance = variance_new

    return Pz, mu, variance

mail = np.random.normal( 170, 7, (1, 100) )
femail = np.random.normal( 160, 5, (1, 100) )
child = np.random.normal( 100, 10, (1, 100) )
data = np.c_[mail, femail,child]
np.random.shuffle( data )
Pz, u, variance = gaussianEM( data, clusters=3, iteration=10)



