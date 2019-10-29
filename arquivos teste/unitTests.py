import funcoes
assert funcoes.entrada_csv("localizacaocompassobpm3.csv")
assert funcoes.com_bpm()
assert funcoes.timesig_filtra("localizacaocompassobpm3.csv")==[int,int,int]


