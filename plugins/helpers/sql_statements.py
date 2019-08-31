# drops queries
DROP_DIM_TABLE_BNF_CHAPTERS = """
    DROP TABLE IF EXISTS staging.bnf_chapters;
"""

DROP_DIM_TABLE_BNF_SECTIONS = """
    DROP TABLE IF EXISTS staging.bnf_sections;
"""

DROP_DIM_TABLE_BNF_PARAGRAPHS = """
    DROP TABLE IF EXISTS staging.bnf_paragraphs;
"""

DROP_DIM_TABLE_BNF_SUBPARAGRAPHS = """
    DROP TABLE IF EXISTS staging.bnf_subparagraphs;
"""

DROP_DIM_TABLE_BNF_CHEMICALS = """
    DROP TABLE IF EXISTS staging.bnf_chemicals;
"""

DROP_DIM_TABLE_BNF_PRODUCTS = """
    DROP TABLE IF EXISTS staging.bnf_products;
"""

DROP_DIM_TABLE_BNF_PRESENTATIONS = """
    DROP TABLE IF EXISTS staging.bnf_presentations;
"""

DROP_DIM_TABLE_PRACTICES = """
    DROP TABLE IF EXISTS staging.practices;
"""

DROP_FACT_TABLE_PRACTICE_SIZE = """
    DROP TABLE IF EXISTS staging.practice_size;
"""

DROP_DIM_TABLE_PRACTICE_GROUPS = """
    DROP TABLE IF EXISTS staging.groups;
"""

DROP_FACT_TABLE_PRESCRIPTIONS = """
    DROP TABLE IF EXISTS staging.prescriptions;
"""

# create queries
CREATE_TABLE_BNF_CHAPTERS = ("""
    CREATE TABLE staging.bnf_chapters (
        code varchar(2) not null,
        name varchar(255)
    );
""")

CREATE_TABLE_BNF_SECTIONS = ("""
    CREATE TABLE staging.bnf_sections (
        code varchar(4) not null,
        name varchar(255)
    );
""")

CREATE_TABLE_BNF_PARAGRAPHS = ("""
    CREATE TABLE staging.bnf_paragraphs (
        code varchar(6) not null,
        name varchar(255)
    );
""")

CREATE_TABLE_BNF_SUBPARAGRAPHS = ("""
    CREATE TABLE staging.bnf_subparagraphs (
        code varchar(7) not null,
        name varchar(255)
    );
""")

CREATE_TABLE_BNF_CHEMICALS = ("""
    CREATE TABLE staging.bnf_chemicals (
        code varchar(9) not null,
        name varchar(255)
    );
""")

CREATE_TABLE_BNF_PRODUCTS = ("""
    CREATE TABLE staging.bnf_products (
        code varchar(11) not null,
        name varchar(255)
    );
""")

CREATE_TABLE_BNF_PRESENTATIONS = ("""
    CREATE TABLE staging.bnf_presentations (
        code varchar(15) not null,
        name varchar(255)
    );
""")

CREATE_TABLE_PRACTICES = """
    CREATE TABLE staging.practices (
        code varchar(255) NOT NULL,
        name varchar(255),
        address_1 varchar(255),
        address_2 varchar(255),
        address_3 varchar(255),
        address_4 varchar(255),
        postcode varchar(255),
        year integer,
        month integer
    );
"""

CREATE_TABLE_PRACTICE_SIZE = """
    CREATE TABLE staging.practices_size (
        practice_code varchar(255),
        group_code varchar(255),
        gp_count integer,
        dispensing_list_size integer,
        prescribing_list_size integer,
        total_list_size integer
    );
"""

CREATE_TABLE_PRACTICE_GROUPS = """
    CREATE TABLE staging.groups (
        code varchar(255),
        comm_prov varchar(255)
    );
"""

CREATE_TABLE_PRESCRIPTIONS = """
    CREATE TABLE staging.prescriptions (
        id integer not null,
        sha varchar(255),
        pct varchar(255),
        practice varchar(255),
        bnf_code varchar(15),
        bnf_chapter varchar(2),
        bnf_section varchar(4),
        bnf_paragraph varchar(6),
        bnf_subparagraph varchar(7),
        bnf_chemical varchar(9),
        bnf_product varchar(11),
        items integer,
        nic double precision,
        act_cost double precision,
        quantity integer,
        year integer,
        month integer
    );
"""

drop_statements = [
    DROP_DIM_TABLE_BNF_CHAPTERS,
    DROP_DIM_TABLE_BNF_SECTIONS,
    DROP_DIM_TABLE_BNF_PARAGRAPHS,
    DROP_DIM_TABLE_BNF_SUBPARAGRAPHS,
    DROP_DIM_TABLE_BNF_CHEMICALS,
    DROP_DIM_TABLE_BNF_PRODUCTS,
    DROP_DIM_TABLE_BNF_PRESENTATIONS,
    DROP_DIM_TABLE_PRACTICES,
    DROP_FACT_TABLE_PRACTICE_SIZE,
    DROP_DIM_TABLE_PRACTICE_GROUPS,
    DROP_FACT_TABLE_PRESCRIPTIONS,
]

create_statements = [
    CREATE_TABLE_BNF_CHAPTERS,
    CREATE_TABLE_BNF_SECTIONS,
    CREATE_TABLE_BNF_PARAGRAPHS,
    CREATE_TABLE_BNF_SUBPARAGRAPHS,
    CREATE_TABLE_BNF_CHEMICALS,
    CREATE_TABLE_BNF_PRODUCTS,
    CREATE_TABLE_BNF_PRESENTATIONS,
    CREATE_TABLE_PRACTICES,
    CREATE_TABLE_PRACTICE_SIZE,
    CREATE_TABLE_PRACTICE_GROUPS,
    CREATE_TABLE_PRESCRIPTIONS,
]
