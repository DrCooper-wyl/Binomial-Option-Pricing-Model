import numpy
def bopm(bitcoin_price,n):
    past_bitcoin_price = bitcoin_price[n]
    r=(bitcoin_price[n]/bitcoin_price[n-1])-1
    t_array=[]
    for i in range(1,n) :
        t_array=bitcoin_price[i]/bitcoin_price[i-1]-1
    vol=numpy.array(t_array).std(),\
    sigma=vol
    u=numpy.e**sigma
    d=1/u
    a=numpy.e**r
    p=(a-d)/(u-d)
    res=p*past_bitcoin_price*u+(1-p)*past_bitcoin_price*d
    return res