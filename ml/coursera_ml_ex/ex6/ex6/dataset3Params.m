function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;
c_vals=[1 3];
s_vals=[0.01 0.03];
%[0.01 0.03 0.1 0.3 1 3 10 30];
n_res=length(c_vals)*length(s_vals);
res=zeros(n_res,3);
% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%
for i = 1:length(c_vals)
  for j = 1:length(s_vals)
    C = c_vals(i);
    sigma = s_vals(i);
    model=svmTrain(X, y, C, @(x1, x2) gaussianKernel(x1, x2, sigma));
    predictions=svmPredict(model,Xval);
    res(i,:)=[C sigma mean(double(predictions~=yval))];
  endfor
endfor
res
[min,index] = min(res(:,3));
C = res(index,1);
sigma = res(index,2);





% =========================================================================

end
