% Defining companies
company(sumsum).
company(appy).

% Beep boop technology
smartphonetechnology(galactica-s3).

% Defines relations between companies
competitor(X,Y) :- company(X), company(Y).
rival(X,Y) :- competitor(X,Y).

% Develop tech relations
develop(sumsum, galactica-s3).

develop(X,Y) :- company(X), smartphonetechnology(Y).

business(X) :- smartphonetechnology(X).
