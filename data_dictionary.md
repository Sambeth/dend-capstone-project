
| File  | Column  | DataType  | References  | Description  |
|---|---|---|---|---|
| practices_prescriptions  | id  |   |   |   |
|  | sha  |   |   | SHA (Strategic Health Authority) or AT (Area Team) code - 3 characters  |
|   | pct |   |   |  PCT (Primary Care Trust) or CCG (Clinical Commissioning Group) code - 3 characters |
|   | practice  |   |   | ANNNNN Practice code - 6 characters  |
|   | bnf_code |   |   | British National Formulary (BNF) code - 15 characters  |
|   | bnf_chapter |   |   | BNF presentation name - 40 characters  |
|   | bnf_section |   |   | BNF presentation name - 40 characters  |
|   | bnf_paragraph |   |   | BNF presentation name - 40 characters  |
|   | bnf_subparagraph |   |   | BNF presentation name - 40 characters  |
|   | bnf_chemical |   |   | BNF presentation name - 40 characters  |
|   | bnf_product |   |   | BNF presentation name - 40 characters  |
|   | items  |   |   | Prescription items dispensed - whole numbers  |
|   | nic |   |   | Net ingredient cost - pounds and pence  |
|   | act_cost  |   |   | Actual cost - pounds and pence  |
|   | quantity |   |   | Quantity - whole numbers  |
|   | year |   |   | YYYY  |
|   | month |   |   | MM  |
|   |  |   |   |  |
| practices - practice codes, names and addresses file | PERIOD |   |   | YYYYMM |
|   | code |   |   | ANNNNN practice code - 6 characters |
|   | name |   |   | Name of surgery |
|   | address 1 |   |   | ANY VILLA SURGERY |
|   | address 2 |   |   | 1 ANY ROAD |
|   | address 3 |   |   | ANYTOWN |
|   | address 4 |   |   | ANYSHIRE |
|   | postcode |   |   | XX2 7XX |
|   | year |   |   | XX2 7XX |
|   | month |   |   | XX2 7XX |
|   |  |   |   |  |
| practices_size | Comm./Prov. |   |   |  |
|   | practice code |   |   |  |
|   | group code |   |   |  |
|   | gp count |   |   | Number of General Practicioners or Doctors |
|   | dispensing list Size |   |   | Shows the number of patients registered with a doctor who receive both medical services and dispensing services from their doctor |
|   | prescribing list Size |   |   | Shows the number of patients registered with a doctor who receive medical services only. |
|   | total list size |   |   |  |
|   |  |   |   |  |
| groups | code |   |   |  |
|   | comm_prov |   |   |  |
|   |  |   |   |  |
| bnf_chapters | code |   |   |  |
|   | name |   |   |  |
| bnf_sections | code |   |   |  |
|   | name |   |   |  |
| bnf_paragraphs | code |   |   |  |
|   | name |   |   |  |
| bnf_subparagraphs | code |   |   |  |
|   | name |   |   |  |
| bnf_chemicals | code |   |   |  |
|   | name |   |   |  |
| bnf_products | code |   |   |  |
|   | name |   |   |  |
| bnf_presentations | code |   |   |  |
|   | name |   |   |  |
|   |  |   |   |  |