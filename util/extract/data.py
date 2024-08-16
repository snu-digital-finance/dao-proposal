from math import inf
from dataclasses import dataclass

@dataclass
class Limit:
    lower: int
    upper: int | float = inf

    def is_valid_length(self, value):
        return self.lower <= value <= self.upper

@dataclass
class Category:
    name: str
    limit: Limit
    words: tuple[str]
    not_words: tuple[str] = tuple()
    other_words: tuple[str] = tuple()
    

title_words = (
    "in short", "result",
    "summary", "objective",  "keyword",
    "key points", "category",
    "motivation", "rationale", "background", 
    "tl;dr", "tldr", "tl,dr", "tl;dr:"
    "benefit", "recommendation", "purpose", 
    "the proposal",
    "goal", " aim ", "conclusion",
    "synopsis", "abstract", 
    # "therefore" <-> here
    # "solution",
    # aim <-> claim
)


other_title_words = (
    "problem", "disclaimer", "introduction", "method", "methodology",
    "result", "discussion", "acknowledgement", "reference",
    "appendix", "appendices", "author",
    "detail", "specification", "requirement", "implementation",
    "contribution", "analysis", "evaluation", 
    "content", "overview", "review", "means", "mechanism",
    "drawback", "limitation", "challenge", "issue", "concern",
    "vote", "overall cost", "risk", "candidate",
    "responssibilit",  "description", "why", "when",
    "parameter", "solution"
)

not_title_words = (
    "other", "detail"
)

sentence_words = (
    "i propose", "we propose", "i suggest", "we suggest",
    "i recommend", "we recommend",
    "proposes to", "suggests to", "recommends to",
    "to propose", "to suggest", "to recommend",
    # "we should", "we must",
    "therefore",
)

not_sentence = (
    "Link to proposed Governance Update",
    "[Read the original proposal on Discourse](",
    "Read the formatted version of this proposal at",
    "[This proposal is also on Balancer's forum](",
    "[Link to proposal discussion](",
)

categories = dict(
    title=Category(
        name="title",
        words=title_words,
        not_words=not_title_words,
        other_words=other_title_words,
        limit=Limit(lower=2, upper=30)
    ),
    sentence=Category(
        name="sentence",
        words=sentence_words,
        limit=Limit(lower=30)
    ),
)
