# Exercise 1: The Smart Phone Rivalry

> `sumsum`, a competitor of `appy`, developed some nice smart phone technology called `galactica-s3`, all of which was stolen by `stevey`, who is a boss of `appy`. It is unethical for a boss to steal business from rival companies. A competitor of is a rival. Smart phone technology is business.

## 1. Translation of natural language to First Order Logic (FOL)

> `sumsum`, a competitor of `appy`

> A competitor of is a rival.

This statement implies that both `sumsum` and `appy` are companies within the same industry. In the real world, not all companies are competitors to each other; however, this question only states two companies, thus we will be making the assumption that all companies are competitors with each other.

$$
\forall_{x}\forall_{y}\;Company(x) \land Company(y) \to Competitor(x,y)
$$

Furthermore, since competitors are rivals with each other, we can deduce the following equivilance relation. 

$$
\forall_x\forall_y\; Competitor(x,y) \iff Rival(x,y)
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

<div style="page-break-after: always;"></div>

## 2. Translating FOL Statements to Prolog

### Declaration of Facts

We first begin with declarative statements for the given facts.

```prolog
% Defining companies
company(sumsum).
company(appy).

% Beep boop technology
smartphonetechnology(galactica-s3).

% Develop tech relations
develop(sumsum, galactica-s3) :- company(sumsum), company(galactica-s3).

% Stevey is a bad guy
person(stevey).
boss(appy, stevey) :- company(appy), person(stevey).
steals(stevey, galactica-s3) :- person(stevey), business(galactica-s3).
```

### Translations

Defining competitors and rivals.

> $$
> \forall_{x}\forall_{y}\;Company(x) \land Company(y) \to Competitor(x,y) \\
\forall_x\forall_y\; Competitor(x,y) \iff Rival(x,y)
> $$

```prolog
competitor(X,Y) :- company(X), company(Y).
rival(X,Y) :- competitor(X,Y).
```

Defining the definition that smart phone technology is business.

> $$
> \forall_t\; SmartPhoneTechnology(t) \to Business(t)
> $$

```prolog
business(X) :- smartphonetechnology(X).
```

Defining the predicate `not_ethical`.

> $$
> \exist_x\exist_y\exist_t\exist_h \; Boss(x,h) \;\land\; Rival(x,y) \;\land\; Steals(h,t) \;\land\; Develop(y, t) \to \neg ethical
> $$

```prolog
not_ethical(H) :-
  rival(X,Y),
  boss(X,H),
  develop(Y,T),
  steals(H,T).
```

### Prolog Knowledge Base

Complete knowledge base containing the statements from above.

```prolog
% Defining companies
company(sumsum).
company(appy).

% Beep boop technology
smartphonetechnology(galactica-s3).

business(X) :- smartphonetechnology(X).

% Defines relations between companies
competitor(X,Y) :- company(X), company(Y).
rival(X,Y) :- competitor(X,Y).

% Develop tech relations
develop(sumsum, galactica-s3) :-
    company(sumsum),
    smartphonetechnology(galactica-s3).

% Stevey is a bad guy
person(stevey).
boss(appy, stevey) :- company(appy), person(stevey).
steals(stevey, galactica-s3) :- person(stevey), business(galactica-s3).

% Determining predicate
not_ethical(H) :-
  rival(X,Y),
  boss(X,H),
  develop(Y,T),
  steals(H,T).
```

<div style="page-break-after: always;"></div>

## 3. Trace Results

```prolog
?- not_ethical(X).
X = stevey ;
false.

?- trace.
true.

[trace]  ?- not_ethical(X).
   Call: (10) not_ethical(_11536) ? creep
   Call: (11) rival(_12820, _12822) ? creep
   Call: (12) competitor(_12820, _12822) ? creep
   Call: (13) company(_12820) ? creep
   Exit: (13) company(sumsum) ? creep
   Call: (13) company(_12822) ? creep
   Exit: (13) company(sumsum) ? creep
   Exit: (12) competitor(sumsum, sumsum) ? creep
   Exit: (11) rival(sumsum, sumsum) ? creep
   Call: (11) boss(sumsum, _11536) ? creep
   Fail: (11) boss(sumsum, _11536) ? creep
   Redo: (13) company(_12822) ? creep
   Exit: (13) company(appy) ? creep
   Exit: (12) competitor(sumsum, appy) ? creep
   Exit: (11) rival(sumsum, appy) ? creep
   Call: (11) boss(sumsum, _11536) ? creep
   Fail: (11) boss(sumsum, _11536) ? creep
   Redo: (13) company(_12820) ? creep
   Exit: (13) company(appy) ? creep
   Call: (13) company(_12822) ? creep
   Exit: (13) company(sumsum) ? creep
   Exit: (12) competitor(appy, sumsum) ? creep
   Exit: (11) rival(appy, sumsum) ? creep
   Call: (11) boss(appy, _11536) ? creep
   Call: (12) company(appy) ? creep
   Exit: (12) company(appy) ? creep
   Call: (12) person(stevey) ? creep
   Exit: (12) person(stevey) ? creep
   Exit: (11) boss(appy, stevey) ? creep
   Call: (11) develop(sumsum, _80) ? creep
   Call: (12) company(sumsum) ? creep
   Exit: (12) company(sumsum) ? creep
   Call: (12) smartphonetechnology(galactica-s3) ? creep
   Exit: (12) smartphonetechnology(galactica-s3) ? creep
   Exit: (11) develop(sumsum, galactica-s3) ? creep
   Call: (11) steals(stevey, galactica-s3) ? creep
   Call: (12) person(stevey) ? creep
   Exit: (12) person(stevey) ? creep
   Call: (12) business(galactica-s3) ? creep
   Call: (13) smartphonetechnology(galactica-s3) ? creep
   Exit: (13) smartphonetechnology(galactica-s3) ? creep
   Exit: (12) business(galactica-s3) ? creep
   Exit: (11) steals(stevey, galactica-s3) ? creep
   Exit: (10) not_ethical(stevey) ? creep
X = stevey .
```
