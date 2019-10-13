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

def grava_mapamus(diretorio, mapamus, nome, truncar=False):
   import pickle
   if truncar == False:
      write = 'xb'
   elif truncar == True:
      write = 'wb'
   try:
      with open(diretorio+'\\'+nome+'.mapamus', write) as arquivo:
         pickle.dump(mapamus, arquivo)
   except FileExistsError:
      raise FileExistsError(nome+'.mapamus ja existe. para truncar arquivos passe truncar=True')
   if truncar == False:
      return(nome+' mapamus criado')
   if truncar == True:
      return(nome+' mapamus truncado ou criado')

def le_mapamus(caminho):
   import pickle
   with open(caminho, 'rb') as arquivo:
      mapamus = pickle.loads(arquivo.read())
   return mapamus