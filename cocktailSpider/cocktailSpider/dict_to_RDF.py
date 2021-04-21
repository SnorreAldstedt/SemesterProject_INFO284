from rdflib import Graph, Literal, URIRef
from rdflib.namespace import RDF, XSD
from rdflib import Namespace
from cocktailcsv_to_dict import cocktail_listdict as cld


bevon = Namespace('http://rdfs.co/bevon/')
cocktail = Namespace('https://www.makemycocktail.com/cocktails/')

A = RDF.type
g = Graph()
alcoBev = URIRef('http://rdfs.co/bevon/latest/html#term-AlcoholicBeverage')
ingredient = URIRef('http://rdfs.co/bevon/latest/html#term-ingredient')

def normalize(text):
    return text.replace(' ','')
for e in cld:
    subj = URIRef(normalize(e['url']))

    print(subj)

    g.add((
        subj,
        A,
        alcoBev
    ))
    g.add((
        subj,
        A,
        Literal(normalize(e['drink']))
    ))
    for i in e['ingredients']:
        print(i)
        g.add((
            subj,
            ingredient,
            Literal(i)
        ))


print(g.serialize(format="n3").decode("utf-8"))

    #drink is a cocktail
