% Defining companies
company(sumsum).
company(appy).

% Beep boop technology
smartphonetechnology(galactica-s3).

business(X) :- smartphonetechnology(X).

% Defines relations between companies
competitor(X,Y) :- company(X), company(Y).
competitor(X,Y) :- rival(X,Y).
rival(X,Y) :- competitor(X,Y).

% Develop tech relations
develop(sumsum, galactica-s3) :- company(sumsum), smartphonetechnology(galactica-s3).


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

   