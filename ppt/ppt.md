---
marp: true
math: mathjax
---

# The Comprehensive Analysis of Proposal in DAOs

---

# Motivation

- Analyze functions of DAO proposal by categorization and clustering
- Inspect effect of each functions to TVL or token price

#

- Key Paper: Decentralized Governance and Digital Asset Prices (Ian Appel, Jillian Grennan, 2023)

---

## 1. What we have done

1. Web scraping of spaces and proposals
2. Refining proposals
3. Constructing category of proposal
4. Labeling category in proposal dataset

## 2. What we will do

1.  Labeling category using LLM
2.  Robust Check
3.  Further Research

---

### 1-1. Proposal Dataset [Limit]

- Limit spaces
  - over 20 proposals
  - over 20 followers
  - over 0.1 percentile of vote counts
  - must have the proposal started in 2024
- Limit Proposals
  - remove when it has ..
    - duplicated content in title and body
    - empty content in title and body
    - body content length under 150
    - votes under 10

---

### 1-2. Proposal Dataset [Refine]

- Remove useless things
  - email
  - url: http, ipfs, image link (+ description)
  - wallet address
  - empty parentheses
- Remain validate content
  - eliminate when content is not written in English: https://pypi.org/project/langdetect/
  - regular expression pattern: [a-zA-Z0-9!@#$%^&*()_\-+{}\[\]:;≥"\'<>,.?/\\|`~\s]
- Remove useless footer/sentence in each protocol
  - by counting every paragraphs(splited by `#`) and scrutinizing uselessness
  - ex1) `This proposal appears on [Balancer's forum](`
  - ex2) `Please review the on-chain vote of the proposal in the link below:`

---

### 1-2. Proposal Dataset [Refine]

- Remove resubmitted proposal: 163
  - Levenshtein edit distance (string)

<div style="display:flex; justify-content:center;">

![image](https://devopedia.org/images/article/213/5510.1567535069.svg)

![image](https://www.ideserve.co.in/learn/img/editDistance_3.gif)

</div>

---

### 1-2. Proposal Dataset [Refine]

- Remove resubmitted proposal: 163
  - Levenshtein edit distance (string)
    - Set lower case in all the content
    - Sort on the content
    - $\text{String distance} = \cfrac{\text{Levenshtein distance}}{\max (\text{Length of content 1}, \text{Length of content 2})}$
    - Condition
      - grouped by space
      - created less than 5 days apart
      - identical title: $\text{String distance} = 0$
      - very similar body: $\text{String distance} < 0.5$
    - Remove previous proposal

---

### 1-2. Proposal Dataset [Refine]

- Remove resubmitted proposal: 163

  - Levenshtein edit distance (string)
    - etc
      - If title has 'resubmit', remove original one

---

### 1-2. Proposal Dataset [Description]

- Description of Dataset
  - 245 spaces
  - 20750 proposals
  - 3049 authors
  - proposals from 2020-07

---

![width:900px](proposal_date.png)

---

### 1-2. Proposal Dataset [Description]

<div style="display:flex; justify-content:space-between">
<div>

- Unit: Hour

- Remove the top and bottom 5%

</div>

| Duration of Proposal | Statistic  |
| -------------------- | ---------- |
| Count                | 18195      |
| Mean                 | 112.778851 |
| Std                  | 52.563157  |
| Min                  | 37.498611  |
| 25%                  | 72         |
| 50%                  | 96         |
| 75%                  | 167.960694 |
| Max                  | 335.995833 |

</div>

---

![alt text](proposal_duration.png)

---

### 1-2. Proposal Dataset [Description]

<div style="display:flex; justify-content:space-between">
<div>

- Spaces under 5 proposals: 21

- Spaces under 10 proposals: 28

</div>

| Proposal Count per Space | Statistic |
| ------------------------ | --------- |
| Count                    | 245       |
| Mean                     | 84.69     |
| Std                      | 194.12    |
| Min                      | 1         |
| 25%                      | 22        |
| 50%                      | 38        |
| 75%                      | 78        |
| Max                      | 2301      |

</div>

---

### 1-2. Proposal Dataset [Description]

<div style="display:flex; justify-content:space-between">

<div>

- Top 7 (sorted by vote count):

  - `stgdao.eth`: 17795924
  - `arbitrumfoundation.eth`: 5289055
  - `aave.eth`: 3103339
  - `cakevote.eth`: 431105
  - `aavegotchi.eth`: 396567
  - `gmx.eth`: 305324
  - `uniswapgovernance.eth`: 275334

- Table was divided by 100 due to large number

</div>

| Vote Count per Space | Statistic  |
| -------------------- | ---------- |
| Count                | 2.45       |
| Mean                 | 1262.5953  |
| Std                  | 11997.8151 |
| Min                  | 0.12       |
| 25%                  | 8.36       |
| 50%                  | 27.1       |
| 75%                  | 110.72     |
| Max                  | 177959.24  |

</div>

---

### 1-3. Category

- Business: `Fee`, `Expansion`, `User Expansion Strategy`, `New Business Proposal`, `Reward Adjustment`, `Rate`
- Operations: `Team`, `Liquidity Management`, `User Friendly Features`, `Risk Management`, `Feature improvement`, `Security`
- Governance: `Feature Improvement`, `Inclusive`, `Restrictive`, `Adjust`
- Reverse/Treasury: `Grant`, `Donation`, `Asset Management`, `Token Sale`, `Reduce/Increase Reserve/Treasury`, `Steward`, `Request Grant`
- Tokenomics: `Grant for Incentive`, `Token Reward Adjustment`, `Adjust Supply`, `Token Allocation`
- FALSE: `Request Money`, `Not Detailed`, `Off-topic`, `Info/Announcement`

---

### 1-4. Labeling

- Cosine Similarity to find similar proposal body

![width:800px](https://assets.zilliz.com/Vector_Similarity_Measures_Cosine_Zilliz_f3ebfcfd7e.png)

---

![img2](https://www.machinelearningplus.com/wp-content/uploads/2018/10/soft-cosine.png)

---

- the value between 0(different) ~ 1(similar)
  ![img3](https://blogs.sas.com/content/iml/files/2019/08/cosSim4.png)

---

### 1-4. Labeling

- Preprocessing
  - Set lower case
  - Remain only english
  - Remove stopwords: `the, a, I, my, me, is, ...`
  - Remove words appeard only once
    - Unless the word is not in dictionary
      - past, -s words converted to original shape
    - Bag of words(BoW): Just counting every words in body content on whole dataset

---

### 1-4. Labeling

- Result of cosine Similarity

![alt text](sample_result_cossim.png)

---

### 2. Next step

1. Labeling category using LLM(ChatGPT4o-mini)

2. Robust Check

- Validating meaningful categorization
- Check the effect on TVL or price
  - Test hypothesis statistically

3. Further Research

- Sincerity measure
  - Count Typos
- Unsupervised Learning
  - Topic modeling -> extract keywords

---

# Appendix

1. Proposal Sample

---

##### Proposal Sample

```
id 0x89f4f8ea61c728fbb6e60fc97826fd955dbeb9e3e7d6...
end 2023-06-27 20:46:00
app snapshot
ipfs bafkreidwgmggjxoxvlzhzy6fgxnzx3doxwifb3x6yzoug...
type single-choice
body Summary:\nThe proposal is to remove the old sd...
link https://snapshot.org/#/stakedao.eth/proposal/0...
title #SDGP 16 - Remove old sdTKN/TKN curve gauges f...
start 2023-06-22 20:46:51
state closed
votes 22
author 0x41717436744232Fb66E85fFAf388a8a33BC7397a
symbol veSDT
scores [2233745.925800096, 0, 0]
created 2023-06-22 20:47:52
updated NaN
network 1
choices ['Yes, remove it', 'No, don’t remove it', 'Abs...
flagged False
strategies [{'network': '1', 'params': {'symbol': 'veSDT'...
discussion NaN
scores_total 2233745.9258
scores_updated 1687866372
scores_by_strategy [[2233745.925800096], [0], [0]]
space_id stakedao.eth
```
