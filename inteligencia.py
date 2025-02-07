import google.generativeai as genai

def identificar_especie(chave, imagem):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    prompt = '''Identifique qual a espécie presente nesta imagem.
    A espécie deve inicialmente ser classificada em grandes grupos (Planta, animal,
    fungo, bactéria, outro).
    Posteriormente a espécie deve ser classificada ao menor nível taxonômico possível, 
    listando as classificações anteriores.
    Nenhum texto adicional deve ser gerado como resposta além da identificação da espécie.
    As classificações devem ser separadas por vírgulas.
    #exemplo de saída:
    É um animal possivelmente da espécie *Corbicula fluminea*,
    Reino: Animalia, Filo: Mollusca, Classe: Bivalvia, Ordem: Veneroida, Família: Corbiculidae'''
    resposta = modelo.generate_content([prompt, imagem])
    especie =resposta.text.split(",")
    return especie


def outras_especies(chave, especie):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f'''cite outras principais espécies do mesmo gênero
    da especie identificada.
    #especie
   {especie}
    '''
    resposta = modelo.generate_content(prompt)
    outras=resposta.text
    return outras


opcoes_lista = ("Área de distribuição", "Status de conservação", "Ciclo de vida", "Como identificar", "Curiosidades")

def sobre_especie(chave, especie, opcoes_lista):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f'''Traga informações relevantes de alguma das opcoes listadas, sobre 
    a especie identificada
    #especie
    {especie}
    #opcoes_lista
    {opcoes_lista}
    '''
    resposta = modelo.generate_content(prompt)
    return resposta.text