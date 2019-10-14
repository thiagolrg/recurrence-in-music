#se o diretorio existir e contiver arquivos midi retorna o diretorio
def diretorio(objetivo, arquivo):
   di=input('diretorio para '+objetivo+' '+arquivo+': ')
   import os
   if os.path.exists(di) == False:
      print('diretorio nao existe')
      return diretorio(objetivo, arquivo)
   elif objetivo == 'ler':
      for r, d, f in os.walk(di):
         for file in f:
            if arquivo in file:
               break
         else:
            continue
         break
      else:
         print('nao existem '+arquivo+' no diretorio')
         return diretorio(objetivo, arquivo)         
   return di

#retorna uma lista com o caminho de todos os arquivos midi de um diretório
def caminhos_arquivo(diretorio, extensao):
   import os
   caminhos = []
   # r=root, d=directories, f = files
   for r, d, f in os.walk(diretorio):
      for file in f:
         if extensao in file:
            caminhos.append(os.path.join(r, file))
   return caminhos

#recebe o caminho e tira o nome do arquivo
def nome_arquivo(caminho, extensao):
    for linha in caminho.split('\\'):
        if extensao in linha:
            nome = linha.replace(extensao,'')
            break
    return nome

def grava_arquivo(diretorio, arquivo, write):
   import pickle
   try:
      with open(diretorio, write) as f:
         pickle.dump(arquivo, f)
   except FileExistsError:
      raise FileExistsError(diretorio+" ja existe. para truncar arquivos passe write='wb'")
   if write == 'xb':
      return(diretorio+' arquivo criado')
   if write == 'wb':
      return(diretorio+' arquivo truncado ou criado')
   if write == 'ab':
      return(diretorio+' arquivo acrescentado')

def le_mapamus(caminho, read):
   import pickle
   with open(caminho, read) as arquivo:
      mapamus = pickle.loads(arquivo.read())
   return mapamus