def get_sentence_list(text):

    from natasha import Segmenter, Doc

    doc = Doc(text)
    segmenter = Segmenter()

    doc.segment(segmenter)

    sentence_list = []
    for i in doc.sents:
        sentence_list.append(i.text)
    return sentence_list


def get_lemmatized_text(text):

    from natasha import Segmenter, Doc, NewsEmbedding, NewsMorphTagger, MorphVocab

    doc = Doc(text)
    segmenter = Segmenter()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    morph_vocab = MorphVocab()

    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)

    lemmatized_text = ''

    for token in doc.tokens:
        token.lemmatize(morph_vocab)
        lemmatized_text = lemmatized_text + token.lemma + " "

    return lemmatized_text

def get_entities(text):

    from natasha import Segmenter, Doc, NewsEmbedding, NewsNERTagger, NewsSyntaxParser, NewsMorphTagger, MorphVocab
    from ipymarkup import format_span_box_markup

    doc = Doc(text)
    segmenter = Segmenter()
    emb = NewsEmbedding()
    ner_tagger = NewsNERTagger(emb)
    syntax_parser = NewsSyntaxParser(emb)
    morph_tagger = NewsMorphTagger(emb)
    morph_vocab = MorphVocab()

    doc.segment(segmenter)
    doc.parse_syntax(syntax_parser)
    doc.tag_morph(morph_tagger)
    doc.tag_ner(ner_tagger)

    locations = []
    people = []
    organizations = []
    spans = []

    for span in doc.spans:
        span.normalize(morph_vocab)
        spans.append((span.start, span.stop, span.type))
        match span.type:
            case "LOC":
                if span.normal not in locations:
                    locations.append(span.normal)
            case "PER":
                if span.normal not in people:
                    people.append(span.normal)
            case "ORG":
                if span.normal not in organizations:
                    organizations.append(span.normal)

    annotated_text = "".join(list(format_span_box_markup(text, spans)))

    return locations, people, organizations, annotated_text

def get_syntax(text):

    from natasha import Segmenter, Doc, NewsEmbedding, NewsNERTagger, NewsSyntaxParser
    from ipymarkup import format_dep_ascii_markup

    doc = Doc(text)
    segmenter = Segmenter()
    emb = NewsEmbedding()
    syntax_parser = NewsSyntaxParser(emb)

    doc.segment(segmenter)

    if len(doc.sents) > 1:
        return ["Пожалуйста, введите одно предложение."]

    doc.parse_syntax(syntax_parser)
    print(doc.tokens)
    words = ["Дерево зависимостей:"] ## просто гениальное решение
    deps= []

    for token in doc.tokens:
        deps.append((int((token.head_id.split("_"))[1]), int((token.id.split("_"))[1]), token.rel))
        words.append(token.text)
    print(words)
    print(deps)
    return list(format_dep_ascii_markup(words, deps))



#from natasha import Segmenter, Doc, NewsEmbedding, NewsMorphTagger, MorphVocab, NewsSyntaxParser

text = 'Посол Израиля на Украине Йоэль Лион признался, что пришел в шок, узнав о решении властей Львовской области объявить 2019 год годом лидера запрещенной в России Организации украинских националистов (ОУН) Степана Бандеры.'

def get_grammar(text):
    from natasha import Segmenter, Doc, NewsEmbedding, NewsMorphTagger, MorphVocab

    doc = Doc(text)
    segmenter = Segmenter()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    morph_vocab = MorphVocab()

    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)

    grammar = []

    for token in doc.tokens:
        grammar.append([token.text, token.pos, token.feats])

    return grammar


#spans = []
#spans.append((doc.spans[0].start, doc.spans[0].stop, doc.spans[0].type))
