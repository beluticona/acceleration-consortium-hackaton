import matplotlib.pyplot as plt

def box(data):
    
    df = data.copy()
    
    df.plot(kind='hist',subplots=True,layout=(4,3),grid=True,figsize=(10,10))
    plt.tight_layout()
    plt.show()
    
def hist(df, densidad = False, tiempo = True):
    '''Hace los histogramas de datos para la base con conc de TEOS, NH3, agua,
    Temperatura, tiempo y diámetro. Si se aclara que tiempo es FALSE, entonces
    no hace el histograma de tiempo (puede que no tenga esa columna la base)'''
    
    
    data = df.copy()
    
    plt.figure(figsize = (23,14) ,dpi=200)

    plt.subplot(2, 3, 1)
    plt.hist(data['TEOS concentration'],density = densidad,bins = 20)
    plt.xlabel('TEOS (M)',fontsize = 30)
    plt.ylabel('Conteo de datos',fontsize = 30)
    plt.grid(False)
    
    ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    #plt.ylim(0,ylim)
    
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(25)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
    
    plt.subplot(2, 3, 2)
    plt.hist(data['Ammonia concentration'],density = densidad,bins = 20)
    plt.xlabel('Amoníaco (M)',fontsize = 30)
    plt.grid(False)
    
    ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    #plt.ylim(0,ylim)

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(20)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
    
    plt.subplot(2, 3, 3)
    plt.hist(data['Water concentration'],density = densidad,bins = 20)
    plt.xlabel('Agua (M)',fontsize = 30)
    plt.grid(False)
    
    ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    #plt.ylim(0,ylim)

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(25)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
     
    if tiempo:
        plt.subplot(2, 3, 4)
        plt.hist(data['Time'],density = densidad,bins = 50)
        plt.xlabel('Tiempo (min)',fontsize = 30)
        plt.ylabel('Conteo de datos',fontsize = 30)
        plt.grid(False)
        
        ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        #plt.ylim(0,ylim)
    
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontsize(25)
            label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
        
    if tiempo:
        plt.subplot(2, 3, 5)
    else:
        plt.subplot(2, 3, 4)
        
    plt.hist(data['Temperature'],density = densidad,bins = 15)
    plt.xlabel('Temperatura (°C)',fontsize = 30)
    plt.grid(False)
    
    ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    #plt.ylim(0,ylim)

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(25)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
        
    plt.subplot(2, 3, 6)
    plt.hist(data['Size'],density = densidad,bins = 25)
    plt.xlabel('Diámetro (nm)',fontsize = 30)
    plt.grid(False)
        
    ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    #plt.ylim(0,ylim)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(25)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
        
    plt.show()    
