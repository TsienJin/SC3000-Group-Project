# Exercise 1

> `sumsum`, a competitor of `appy`, developed some nice smart phone technology called `galactica-s3`, all of which was stolen by `stevey`, who is a boss of `appy`. It is unethical for a boss to steal business from rival companies. A competitor of is a rival. Smart phone technology is business.

## 1. Translation of natural language to First Order Logic (FOL)

> `sumsum`, a competitor of `appy`

> A competitor of is a rival.

This statement implies that both `sumsum` and `appy` are companies within the same industry. The following logical deduction can be made, with the assumption that not all companies are competitors to each other.

$$
\exist_{x}\exist_{y}\;Company(x) \land Company(y) \to Competitor(x,y)
$$

Furthermore, since competitors are rivals with each other, we can deduce the following equivilance relation. 

$$
\exist_x\exist_y\; Competitor(x,y) \iff Rival(x,y)
$$

> ...developed some nice smart phone technology called `galactica-s3`...

A company can develop smart phone technology, but not all the smart phone technology used by the company is developed from the same company.

$$
\exist_{x} \exist_{t} \; Company(x) \;\land\; SmartPhoneTechnology(t) \to Develop(x,t)
$$

> Smart phone technology is business.

We can further deduce a logical statement that all smart phone technology is business.

$$
\forall_t\; SmartPhoneTechnology(t) \to Business(t)
$$

> ...all of which was stolen by `stevey`...

We can infer that `stevey` is a person. This suggests that a person can steal technology.

$$
\exist_t\exist_h\; SmartPhoneTechnology(t) \;\land\; Person(h) \to Steals(h, t)
$$

> ...`stevey`, who is a boss of `appy`.

From the earlier deduction that `stevey` is a person, this informs us that the boss of `appy` (a company) is a person. Thus, for every company, there is a person as its boss.

$$
\forall_x\; Company(x) \to (\exist_h\;Person(h) \to Boss(x, h))
$$

> It is unethical for a boss to steal businsess from rival companies.

A boss is a person, who is the boss of a company. This statement suggests that it is only unethical if the two companies involved are rivals.

We can break this statement down into smaller logical statements to follow. Statements (2) and (3) are transitive, as the boss is a person, and a person can steal technology.

1. There are two companies that are rivals.

2. The boss of one of these comapnies is a person.

3. The boss can steal busines from rival companies.

4. Stealing business from rival comapnies is always unethical.

Therefore these statements can be expressed in natural language -- there are two companies which are rivals, where the boss of one company steals business from the rival company; this is unethical.

$$
\exist_x\exist_y\exist_t\exist_h \; Boss(x,h) \;\land\; Rival(x,y) \;\land\; Steals(h,t) \;\land\; Develop(y, t) \to \neg ethical

$$
