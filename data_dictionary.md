
| File  | Column  | DataType  | References  | Description  |
|---|---|---|---|---|
| Practice prescribing data file  | SHA  |   |   | SHA (Strategic Health Authority) or AT (Area Team) code - 3 characters  |
|   | PCT  |   |   |  PCT (Primary Care Trust) or CCG (Clinical Commissioning Group) code - 3 characters |
|   | PRACTICE  |   |   | ANNNNN Practice code - 6 characters  |
|   | BNF_CODE |   |   | British National Formulary (BNF) code - 15 characters  |
|   | BNF_NAME |   |   | BNF presentation name - 40 characters  |
|   | ITEMS  |   |   | Prescription items dispensed - whole numbers  |
|   | NIC  |   |   | Net ingredient cost - pounds and pence  |
|   | ACT_COST  |   |   | Actual cost - pounds and pence  |
|   | QUANTITY  |   |   | Quantity - whole numbers  |
|   | PERIOD |   |   | YYYYMM  |
|   |  |   |   |  |
| Practice level prescribing - practice codes, names and addresses file | PERIOD |   |   | YYYYMM |
|   | Practice Code |   |   | ANNNNN practice code - 6 characters |
|   | Practice Name |   |   | Name of surgery |
|   | Address 1 |   |   | ANY VILLA SURGERY |
|   | Address 2 |   |   | 1 ANY ROAD |
|   | Address 3 |   |   | ANYTOWN |
|   | Address 4 |   |   | ANYSHIRE |
|   | Postcode |   |   | XX2 7XX |
|   |  |   |   |  |
| Practice level prescribing chemical names and bnf code file  | CHEM SUB |   |   | Practice level prescribing chemical names and bnf code file |
|   | NAME |   |   | Chemical Name - 60 characters |
|   |  |   |   |  |
| Practice list size and GP count file | Comm./Prov. |   |   |  |
|   | Practice Code |   |   |  |
|   | Practice Name |   |   | Name of the practice or doctor |
|   | Practice Address |   |   | Address of the practice or doctor |
|   | Code |   |   |  |
|   | GP Count |   |   | Number of General Practicioners or Doctors |
|   | Dispensing List Size |   |   | Shows the number of patients registered with a doctor who receive both medical services and dispensing services from their doctor |
|   | Prescribing List Size |   |   | Shows the number of patients registered with a doctor who receive medical services only. |
|   | Total List Size |   |   |  |
|   |  |   |   |  |