from __future__ import division, absolute_import, print_function

from airflow.plugins_manager import AirflowPlugin

import operators
import helpers


class CapstonePlugin(AirflowPlugin):
    name = "udacity_plugin"
    operators = [
        operators.PreliminaryQueriesOperator,
        operators.PreprocessToS3Operator,
        operators.StagingQualityCheckOperator,
        operators.StagingToPrivateOperator
    ]
    helpers = [
        helpers.create_schemas,
        helpers.drop_statements,
        helpers.create_statements,
        helpers.practice_prescribing_schema,
        helpers.chemicals_schema,
        helpers.practices_schema,
        helpers.practice_size_schema,
        helpers.bnf_codes_schema,
    ]
