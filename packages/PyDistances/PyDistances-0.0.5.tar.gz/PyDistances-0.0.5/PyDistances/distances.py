def Dist_Euclidea(x_i, x_r): 
    """
    Calcula la distancia Euclidea entre dos vectores de observaciones.

    Parametros (inputs)
    ----------
    x_i , x_r: vectores de observaciones. Arrays de una dimension.       

    Devuelve (outputs)
    -------
    d: la distancia Euclidea entre x_i y x_r.
    """
    Dist_Euclidea = ( ( x_i - x_r )**2 ).sum()
    Dist_Euclidea = np.sqrt(Dist_Euclidea)
    return Dist_Euclidea

def Matrix_Dist_Euclidea(Data):
    """
    Calcula la matriz de distancias Euclideas para un conjunto de datos.

    Parametros (inputs)
    ----------
    Data: un data-frame Pandas o un array Numpy.       

    Devuelve (outputs)
    -------
    M: la matriz de distancias Euclideas entrelas observaciones (filas) del data-frame Data.
    """
    if isinstance(Data, pd.DataFrame):
        Data = Data.to_numpy()
    else:
        pass
    n = len(Data)
    M =  np.zeros((n , n))   
    for i in range(0, n):
        for r in range(i+1, n):        
                M[i,r] = Dist_Euclidea(Data[i,:], Data[r,:])
    M = M + M.T
    return M 