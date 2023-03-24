% Define gender
female(queen_elizabeth).
female(future_princess).
female(princess_ann).
male(prince_charles).
male(prince_andrew).
male(prince_edward).

% Define parent relationships
parent_of(queen_elizabeth, prince_charles).
parent_of(queen_elizabeth, princess_ann).
parent_of(queen_elizabeth, prince_andrew).
parent_of(queen_elizabeth, prince_edward).
parent_of(queen_elizabeth, future_princess).



% Define birth order
% born_after(X,Y) --> X is born before Y --> X is older than Y
born_after(prince_charles, princess_ann).
born_after(princess_ann, prince_andrew).
born_after(prince_andrew, prince_edward).



% Define the old Royal succession rule
succession(X) :-
    male_succession(MaleList),
    member(X, MaleList),
    parent_of(queen_elizabeth, X).

    


succession(X) :-
  female_succession(FemaleList),
  member(X, FemaleList),
  parent_of(queen_elizabeth, X).



male_succession([prince_charles, prince_andrew, prince_edward]).
female_succession([princess_ann, future_princess]).


order([prince_charles, prince_andrew, prince_edward, princess_ann, future_princess]).

