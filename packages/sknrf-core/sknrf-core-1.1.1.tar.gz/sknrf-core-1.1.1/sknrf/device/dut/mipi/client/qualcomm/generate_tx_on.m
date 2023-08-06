fid = fopen('tx_on.csv', 'wt');
D = et.txOnSettings;
k = keys(D);
val = values(D);
for i = 1:length(D)
    fprintf(fid, '%s, %s\n', k{i}, val{i});
end
fclose(fid);
