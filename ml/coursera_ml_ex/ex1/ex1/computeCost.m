function J = computeCost(X, y, theta)

m = length(y); % number of training examples
J = 0;
s=sum(((X*theta).-y).^2);
J=(1/(2*m))*s;
end
