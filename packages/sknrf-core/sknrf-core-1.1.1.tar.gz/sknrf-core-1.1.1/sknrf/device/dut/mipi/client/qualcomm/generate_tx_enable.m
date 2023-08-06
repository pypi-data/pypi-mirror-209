fid = fopen('tx_enable.csv', 'wt');
D = et.txEnableSettings;
k = keys(D);
val = values(D);
for i = 1:length(D)
    fprintf(fid, '%s, %s\n', k{i}, val{i});
end
fclose(fid);

