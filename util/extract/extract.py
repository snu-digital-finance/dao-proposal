from .data import categories
from .regexp import _regex 


def extract_title_and_content(text):
    titles, contents = _regex(text)
    t, c = [], []
    for title, content in zip(titles, contents):
        if not categories["title"].limit.is_valid_length(len(title)): continue;
        if not categories["sentence"].limit.is_valid_length(len(content)): continue;
        t.append(title)
        c.append(content)
    return t, c


if __name__ == "__main__":
    print(categories)
    # 입력된 텍스트
    sample_text = """
Maginga

*Details:*
The last year has been a challenging one for the DAO, but also a year of tremendous growth, fun and learning. I remain as committed as ever to helping the DAO succeed, both as the center of gravity of the Pixel Vault community and as an independent entity with its own goals and aspirations.


1. Abstract
by

*Summary*
    This is a proposal to increase the AMPL capFactor from cap2 to cap3 ($3M > $10M) as outlined in the Balancer [whitelisting process](
    This is a proposal to increase the AMPL capFactor from cap2 to cap3 ($3M > $10M) as outlined in the Balancer [whitelisting process](
    This is a proposal to increase the AMPL capFactor from cap2 to cap3 ($3M > $10M) as outlined in the Balancer [whitelisting process](
    
#  Summary of Proposal
The Gas Refund Program is an initiative spearheaded by the DAO to alleviate the cost of gas for stakers using ParaSwap. As these refunds are done in PSP, three main limits were set during the initial proposal and budget allocation, as well as the later adjustment and renewals in the PSP 2.0 proposal:
* A per-address limit of USD 2500 per epoch
* A per-address yearly maximum of USD 30k
* A global budget limit of 30M PSP

Objective:
The Gas Refund Program is an initiative spearheaded by the DAO to alleviate the cost of gas for stakers using ParaSwap. As these refunds are done in PSP, three main limits were set during the initial proposal and budget allocation, as well as the later adjustment and renewals in the PSP 2.0 proposal:
-A per-address limit of USD 2500 per epoch
-A per-address yearly maximum of USD 30k
-A global budget limit of 30M PSP
"""

    titles, contents = extract_title_and_content(sample_text)
    for i, (title, content) in enumerate(zip(titles, contents), 1):
        print(f"Title {i}: {title}")
        print(f"Content {i}:\n{content}\n")
