import spacy
import warnings
from nltk import Tree

from .qclassifier import classify_question
from .feature_extractor import extract_features
from .query_const import construct_query
from .fetch_wiki import fetch_wiki
from .doc_scorer import rank_docs
from .candidate_ans import get_candidate_answers


def tok_format_dep(tok):
    return "_".join([tok.orth_, tok.dep_])


def to_nltk_tree_dep(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(tok_format_dep(node), [to_nltk_tree_dep(child) for child in node.children])
    else:
        return tok_format_dep(node)


def construct_tree(en_doc):
    for word in en_doc.sents:
        # print(word.text, '-', word.lemma_, '(', word.tag_, ')', word.pos_)
        to_nltk_tree_dep(word.root).pretty_print()


def answer_question(input_question):

    intermediate_results = []

    warnings.filterwarnings("ignore", category=UserWarning)

    en_nlp = spacy.load('en_core_web_md')

    en_doc = en_nlp(u'' + input_question)
    intermediate_results.append("Question: " + input_question)

    # construct_tree(en_doc)

    question_class = classify_question(en_doc)
    intermediate_results.append("Class: " + question_class)
    print("Class:", question_class)

    question_keywords = extract_features(question_class, en_doc)
    intermediate_results.append("Question Features: " + str(question_keywords))
    print("Question Features:", question_keywords)

    question_query = construct_query(question_keywords, en_doc)
    intermediate_results.append("Question Query: " + str(question_query))
    print("Question Query:", question_query)

    print("Fetching Knowledge source...")
    intermediate_results.append("Fetching Knowledge source...")

    wiki_pages = fetch_wiki(question_keywords, number_of_search=3)
    intermediate_results.append("Pages Fetched: " + str(len(wiki_pages)))
    print("Pages Fetched:", len(wiki_pages))

    print("Pre-processing data...")
    intermediate_results.append("Pre-processing the raw data...Removing newline, html tags, sections, references...")

    # Anaphora Resolution

    ranked_wiki_docs = rank_docs(question_keywords)
    intermediate_results.append("Ranked Pages: " + str(ranked_wiki_docs))
    print("Ranked Pages:", ranked_wiki_docs)

    candidate_answers, split_keywords = get_candidate_answers(question_query, ranked_wiki_docs, en_nlp)
    intermediate_results.append("Candidate Answer: " + "(" + str(len(candidate_answers)) + ") " + str(candidate_answers))
    print("Candidate Answer:", "(" + str(len(candidate_answers)) + ")", candidate_answers)

    print("Answer:", " ".join(candidate_answers))

    answer = " ".join(candidate_answers)
    intermediate_results.append("Final Answer: " + answer)

    return answer, intermediate_results

# What's the only color Johnny Cash wears on stage ?

"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_files = os.path.join(BASE_DIR, "static")

dta = pandas.read_csv(static_files+'/data/qclassifier_trainer.csv', sep='|')
"""