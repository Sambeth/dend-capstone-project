
| Table  | Column  | DataType  | References  | Description  |
|---|---|---|---|---|
| prescriptions  | id  | int |   | unique identifier  |
|  | sha  | string |   | SHA (Strategic Health Authority) or AT (Area Team) code - 3 characters  |
|   | pct | string |   |  PCT (Primary Care Trust) or CCG (Clinical Commissioning Group) code - 3 characters |
|   | practice  | string  | practices  | ANNNNN Practice code - 6 characters  |
|   | bnf_code | string  |  bnf_presentations | British National Formulary (BNF) code - 15 characters  |
|   | bnf_chapter | string  | bnf_chapters  | BNF presentation name - 40 characters  |
|   | bnf_section | string  | bnf_sections  | BNF presentation name - 40 characters  |
|   | bnf_paragraph |  string | bnf_paragraphs  | BNF presentation name - 40 characters  |
|   | bnf_subparagraph | string  |  bnf_subparagraphs | BNF presentation name - 40 characters  |
|   | bnf_chemical | string  | bnf_chemicals  | BNF presentation name - 40 characters  |
|   | bnf_product | string  | bnf_products  | BNF presentation name - 40 characters  |
|   | items  | int  |   | Prescription items dispensed - whole numbers  |
|   | nic | float  |   | Net ingredient cost - pounds and pence  |
|   | act_cost  | float  |   | Actual cost - pounds and pence  |
|   | quantity | int  |   | Quantity - whole numbers  |
|   | year | int  |   | YYYY  |
|   | month | int  |   | MM  |
|   |  |   |   |  |
| practices | code | string | practices_size  | ANNNNN practice code - 6 characters |
|   | name | string  |   | Name of surgery |
|   | address 1 | string  |   | ANY VILLA SURGERY |
|   | address 2 | string  |   | 1 ANY ROAD |
|   | address 3 | string  |   | ANYTOWN |
|   | address 4 | string  |   | ANYSHIRE |
|   | postcode | string  |   | XX2 7XX |
|   | year | int |   | 20XX |
|   | month | int  |   | XX |
|   |  |   |   |  |
| practices_size | practice_code | string  | practices  | unique_identifier of gp practices |
|   | group_code | string  | groups  | unique identifier for gp groups |
|   | gp_count | int  |   | Number of General Practicioners or Doctors |
|   | dispensing_list_Size | int  |   | Shows the number of patients registered with a doctor who receive both medical services and dispensing services from their doctor |
|   | prescribing_list_Size | int  |   | Shows the number of patients registered with a doctor who receive medical services only. |
|   | total_list_size | int  |   | a sum of dispensing_list_size and prescribing_list_size |
|   |  |   |   |  |
| groups | code | string  | practices_size  | unique identifier |
|   | comm_prov | string  |   | name of gp group or organization |
|   |  |   |   |  |
| bnf_chapters | code |  string |  prescriptions | unique identifier |
|   | name | string  |   | the part of a chapter a drug is from in the bnf reference book |
|   |  |   |   |  |
| bnf_sections | code | string  | prescriptions  | unique identifier |
|   | name | string  |   | the part of a section a drug is from in the bnf reference book |
|   |  |   |   |  |
| bnf_paragraphs | code | string  |  prescriptions | unique identifier |
|   | name | string  |   | the part of a paragraph a drug is from in the bnf reference book |
|   |  |   |   |  |
| bnf_subparagraphs | code | string  | prescriptions  | unique identifier |
|   | name | string  |   | the part of a subparagraph a drug is from in the bnf reference book |
|   |  |   |   |  |
| bnf_chemicals | code | string  | prescriptions  | unique identifier |
|   | name | string  |   | the part of a chemicals a drug is from in the bnf reference book |
|   |  |   |   |  |
| bnf_products | code |  string | prescriptions  | unique identifier |
|   | name | string  |   | the part of a products a drug is from in the bnf reference book |
|   |  |   |   |  |
| bnf_presentations | code | string  | prescriptions  | unique identifier |
|   | name | string  |   | the part of a presentation a drug is from in the bnf reference book |
|   |  |   |   |  |