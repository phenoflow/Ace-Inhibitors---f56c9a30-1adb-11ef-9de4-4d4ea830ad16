# David A Springate, Darren M Aschroft, Evangelos Kontopantelis, Tim Doran, Ronan Ryan, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"624","system":"gprdproduct"},{"code":"35189","system":"gprdproduct"},{"code":"19223","system":"gprdproduct"},{"code":"35007","system":"gprdproduct"},{"code":"37710","system":"gprdproduct"},{"code":"47006","system":"gprdproduct"},{"code":"35304","system":"gprdproduct"},{"code":"41746","system":"gprdproduct"},{"code":"47159","system":"gprdproduct"},{"code":"34710","system":"gprdproduct"},{"code":"45340","system":"gprdproduct"},{"code":"45300","system":"gprdproduct"},{"code":"43416","system":"gprdproduct"},{"code":"6217","system":"gprdproduct"},{"code":"756","system":"gprdproduct"},{"code":"1299","system":"gprdproduct"},{"code":"38367","system":"gprdproduct"},{"code":"32597","system":"gprdproduct"},{"code":"82","system":"gprdproduct"},{"code":"9693","system":"gprdproduct"},{"code":"34943","system":"gprdproduct"},{"code":"16701","system":"gprdproduct"},{"code":"33894","system":"gprdproduct"},{"code":"9915","system":"gprdproduct"},{"code":"32241","system":"gprdproduct"},{"code":"39786","system":"gprdproduct"},{"code":"6786","system":"gprdproduct"},{"code":"8830","system":"gprdproduct"},{"code":"65","system":"gprdproduct"},{"code":"41573","system":"gprdproduct"},{"code":"42894","system":"gprdproduct"},{"code":"34893","system":"gprdproduct"},{"code":"19208","system":"gprdproduct"},{"code":"37650","system":"gprdproduct"},{"code":"40384","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ace-inhibitors-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ace-inhibitors-100mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ace-inhibitors-100mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ace-inhibitors-100mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
