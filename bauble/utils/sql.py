# util.sql
#
# Description: sql utility functions

from sqlalchemy import *

raise DeprecatedError

# def count_distinct_whereclause(table_column, whereclause):
#     return select([table_column], whereclause, distinct=True).alias('__dummy').count().scalar()


# def count(table, where_clause=None):
#     s = select([func.count('*')], from_obj=[table])
#     if where_clause is not None:
#         s.append_whereclause(where_clause)
#     return s.scalar()


# def count_select(sel):
#     return sel.alias('__dummy').count().scalar()
