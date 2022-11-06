def test():
    import os
    import pandas as pd
    os.system('cls')
    tst = pd.read_csv('VolounteersData.csv')
    print(tst)
    
if __name__ == '__main__':
    test()