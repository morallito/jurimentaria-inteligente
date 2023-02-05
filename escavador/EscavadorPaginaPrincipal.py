import requests
import selenium


class EscavadorPaginaPrincipal ():

    def __init__(self) -> None:
        self.__url ='https://jurisprudencia.stf.jus.br/pages/search?base=acordaos&pesquisa_inteiro_teor=false&sinonimo=true&plural=true&radicais=false&buscaExata=true&page=1&pageSize=10&queryString=<QUERY_STRING>&sort=_score&sortBy=desc'

    def __formatar_url (self, palavras_chave:str)-> str:
        insercao = palavras_chave.replace(' ','%')
        return self.__url.replace('<QUERY_STRING>', insercao )


    def fazer_pesquisa(self, palavras_chave):
        query_url = self.__formatar_url(palavras_chave=palavras_chave)
        print(f'searching for: {query_url}')
        """
        O site do STF requer que o agente do usuario seja repassado no cabecalho da requisicao. 
        Pode-se mudar este de acordo com sua plateforma
        """
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        resposta_pesquisa = requests.get(query_url,headers=headers)
        mfile = open('response.html', 'a')
        mfile.write(resposta_pesquisa.text)
        



if __name__ == '__main__':
    ep = EscavadorPaginaPrincipal()
    ep.fazer_pesquisa('teste')

