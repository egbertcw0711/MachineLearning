close all;
clear all;
X = double(rgb2gray(imread('harvey-saturday-goes7am.jpg')));
original_size = numel(X);
[U,S,V] = svd(X);
fig = imagesc(X);
set(gca, 'YTick', []);
set(gca, 'XTick', []);
saveas(fig, 'original.jpg');
errors = [];
compression_ratios = [];

for i = [2,10,40]
    
    X_compressed = U(:,1:i) * S(1:i, 1:i) * V(:,1:i).';
    
    error = norm(X_compressed - X, 'fro') / norm(X, 'fro');
    % number of singular values + numel of corresponding U + numel of
    % corresonding V
    number = (i+numel(U(:,1:i))+numel(V(:,1:i)));  
    compression_ratio = number/original_size;
    errors = [errors, error];
    compression_ratios = [compression_ratios, compression_ratio];
    
    fprintf('For k=%i singluar vectors, the error is %.4f\n', i, error);
    fprintf('For k=%i, numbers required for storage: %i, compression ratio is %.4f\n ',...
        i, number, number/original_size);
    
    fig = imagesc(X_compressed);
    set(gca, 'YTick', []);
    set(gca, 'XTick', []);
    saveas(fig, sprintf('%i_singular_vectors.jpg', i));
end 
  
fig = figure;
yyaxis right
plot([2,10,40], errors, '-^')
ylabel('Errors')
yyaxis left
plot([2,10,40], compression_ratios, '-o');
ylabel('Compression_ratio')
saveas(fig, 'Compression_vs_error.jpg')

