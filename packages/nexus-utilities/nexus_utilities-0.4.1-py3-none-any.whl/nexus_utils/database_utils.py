"""Database-related utilities"""
#%%
from sqlalchemy import create_engine
# from . import config_reader as cr
# from . import password as pw
# from flat_file_loader.src.utils import config_reader as cr
# import config_utils as cr
# from flat_file_loader.src.utils import password as pw
import re

# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace

#%%
# def build_engine(config_path, config_entry, password_method="keyring"):
def build_engine(connect_type, server_address, server_port, database_name, user_name, password):#, schema=None):
    """Build SQL Alchemy Engine based on input parameters"""

    # db_config = cr.read_config_file(config_path)
    # connect_type = db_config[config_entry]['connect_type']
    # #environment = db_config[config_entry]['environment']
    # server_address = db_config[config_entry]['server_address']
    # server_port = db_config[config_entry]['server_port']
    # server_name = db_config[config_entry]['server_name']
    # schema = db_config[config_entry]['schema']
    # user_name = db_config[config_entry]['user_name']
    # secret_key = db_config[config_entry]['secret_key']

    # if password_method == 'keyring':
    #     from flat_file_loader.src.utils import password_keyring as pw
    # elif password_method == 'secretsmanager':
    #     from flat_file_loader.src.utils import password_aws as pw
    # elif password_method == 'ssm':
    #     from flat_file_loader.src.utils import password_ssm as pw
    # if password_method == 'custom':
    #     from flat_file_loader.src.utils import password_custom as pw
    # password = pw.get_password(user_name, secret_key)
    conn_string = f'{connect_type}://{user_name}:{password}@{server_address}:{server_port}/{database_name}'
    # if schema is not None:
        # conn_string += f'?schema={schema}'

    engine = create_engine(conn_string)

    # return engine, schema
    return engine

def clean_sql_statement(sql_statement):
    """Clean SQL strings to remove comments and separate statements into a list"""
    #%%

    #sql_statement = """/*\nSELECT *\nFROM nexus.imdb_title tgt, nexus_stg.stg_imdb_title stg\nWHERE tgt.titleid = stg.titleid\n*/\n\n--DELETE FROM nexus.imdb_title\n\n/*\n--Poor performance\nUPDATE nexus.imdb_title tgt\nSET\n\tremappedtitleid = coalesce(stg.remappedtitleid, tgt.remappedtitleid), \n\ttitlename = coalesce(stg.titlename, tgt.titlename), \n\ttitletype = coalesce(stg.titletype, tgt.titletype), \n\tepisodetitleid = coalesce(stg.episodetitleid, tgt.episodetitleid), \n\tseasontitleid = coalesce(stg.seasontitleid, tgt.seasontitleid), \n\tshowtitleid = coalesce(stg.showtitleid, tgt.showtitleid), \n\tprimarycompanyid = coalesce(stg.primarycompanyid, tgt.primarycompanyid), \n\tprimarydistributor = coalesce(stg.primarydistributor, tgt.primarydistributor), \n\tprimarygenre = coalesce(stg.primarygenre, tgt.primarygenre), \n\ttitleyear = coalesce(stg.titleyear, tgt.titleyear), \n\tprimaryreleasedate_us = coalesce(stg.primaryreleasedate_us, tgt.primaryreleasedate_us), \n\tseriestitleid = coalesce(stg.seriestitleid, tgt.seriestitleid), \n\tepisodenumber = coalesce(stg.episodenumber, tgt.episodenumber), \n\tseasonnumber = coalesce(stg.seasonnumber, tgt.seasonnumber), \n\tseriesstartyear = coalesce(stg.seriesstartyear, tgt.seriesstartyear), \n\tseriesendyear = coalesce(stg.seriesendyear, tgt.seriesendyear), \n\truntime_us = coalesce(stg.runtime_us, tgt.runtime_us), \n\timdb_url = coalesce(stg.imdb_url, tgt.imdb_url), \n\tuniversalproductflag = coalesce(stg.universalproductflag, tgt.universalproductflag), \n\tmatchconfirmedflag = coalesce(stg.matchconfirmedflag, tgt.matchconfirmedflag), \n\tisadultflag = coalesce(stg.isadultflag, tgt.isadultflag), \n\tproductnotes = coalesce(stg.productnotes, tgt.productnotes), \n\tcreatedtimestamp = coalesce(stg.createdtimestamp, tgt.createdtimestamp), \n\tsourcefilename = coalesce(stg.sourcefilename, tgt.sourcefilename), \n\tmodifydatetime = coalesce(stg.modifydatetime, tgt.modifydatetime)\n--SELECT *\nFROM nexus_stg.stg_imdb_title stg\nWHERE tgt.titleid = stg.titleid\n*/\n\n\nINSERT INTO nexus.imdb_title (titleid, remappedtitleid, titlename, titletype, episodetitleid, seasontitleid, showtitleid, primarycompanyid, primarydistributor, primarygenre, titleyear, primaryreleasedate_us, seriestitleid, episodenumber, seasonnumber, seriesstartyear, seriesendyear, runtime_us, imdb_url, universalproductflag, matchconfirmedflag, isadultflag, productnotes, createdtimestamp, sourcefilename, modifydatetime)\nSELECT \nstg.titleid AS titleid, \nstg.remappedtitleid AS remappedtitleid, \nstg.titlename AS titlename, \nstg.titletype AS titletype, \nstg.episodetitleid AS episodetitleid, \nstg.seasontitleid AS seasontitleid, \nstg.showtitleid AS showtitleid, \nstg.primarycompanyid AS primarycompanyid, \nstg.primarydistributor AS primarydistributor, \nstg.primarygenre AS primarygenre, \nstg.titleyear AS titleyear, \nstg.primaryreleasedate_us AS primaryreleasedate_us, \nstg.seriestitleid AS seriestitleid, \nstg.episodenumber AS episodenumber, \nstg.seasonnumber AS seasonnumber, \nstg.seriesstartyear AS seriesstartyear, \nstg.seriesendyear AS seriesendyear, \nstg.runtime_us AS runtime_us, \nstg.imdb_url AS imdb_url, \nstg.universalproductflag AS universalproductflag, \nstg.matchconfirmedflag AS matchconfirmedflag, \nstg.isadultflag AS isadultflag, \nstg.productnotes AS productnotes, \nstg.createdtimestamp AS createdtimestamp, \nstg.sourcefilename AS sourcefilename, \nstg.modifydatetime AS modifydatetime\nFROM nexus_stg.stg_imdb_title stg\nFROM nexus_stg.stg_imdb_title stg\nWHERE NOT EXISTS\n(\n\tSELECT 1\n\tFROM nexus.imdb_title tgt\n\tWHERE tgt.titleid = stg.titleid\n)\n  AND stg.isadultflag = 'N';\n  \nUPDATE nexus.imdb_titleadult tgt\nSET\n\tremappedtitleid = coalesce(stg.remappedtitleid, tgt.remappedtitleid), \n\ttitlename = coalesce(stg.titlename, tgt.titlename), \n\ttitletype = coalesce(stg.titletype, tgt.titletype), \n\tepisodetitleid = coalesce(stg.episodetitleid, tgt.episodetitleid), \n\tseasontitleid = coalesce(stg.seasontitleid, tgt.seasontitleid), \n\tshowtitleid = coalesce(stg.showtitleid, tgt.showtitleid), \n\tprimarycompanyid = coalesce(stg.primarycompanyid, tgt.primarycompanyid), \n\tprimarydistributor = coalesce(stg.primarydistributor, tgt.primarydistributor), \n\tprimarygenre = coalesce(stg.primarygenre, tgt.primarygenre), \n\ttitleyear = coalesce(stg.titleyear, tgt.titleyear), \n\tprimaryreleasedate_us = coalesce(stg.primaryreleasedate_us, tgt.primaryreleasedate_us), \n\tseriestitleid = coalesce(stg.seriestitleid, tgt.seriestitleid), \n\tepisodenumber = coalesce(stg.episodenumber, tgt.episodenumber), \n\tseasonnumber = coalesce(stg.seasonnumber, tgt.seasonnumber), \n\tseriesstartyear = coalesce(stg.seriesstartyear, tgt.seriesstartyear), \n\tseriesendyear = coalesce(stg.seriesendyear, tgt.seriesendyear), \n\truntime_us = coalesce(stg.runtime_us, tgt.runtime_us), \n\timdb_url = coalesce(stg.imdb_url, tgt.imdb_url), \n\tuniversalproductflag = coalesce(stg.universalproductflag, tgt.universalproductflag), \n\tmatchconfirmedflag = coalesce(stg.matchconfirmedflag, tgt.matchconfirmedflag), \n\tisadultflag = coalesce(stg.isadultflag, tgt.isadultflag), \n\tproductnotes = coalesce(stg.productnotes, tgt.productnotes), \n\tcreatedtimestamp = coalesce(stg.createdtimestamp, tgt.createdtimestamp), \n\tsourcefilename = coalesce(stg.sourcefilename, tgt.sourcefilename), \n\tmodifydatetime = coalesce(stg.modifydatetime, tgt.modifydatetime)\n--SELECT *\nFROM nexus_stg.stg_imdb_title stg\nWHERE tgt.titleid = stg.titleid;\n \n INSERT INTO nexus.imdb_titleadult (titleid, remappedtitleid, titlename, titletype, episodetitleid, seasontitleid, showtitleid, primarycompanyid, primarydistributor, primarygenre, titleyear, primaryreleasedate_us, seriestitleid, episodenumber, seasonnumber, seriesstartyear, seriesendyear, runtime_us, imdb_url, universalproductflag, matchconfirmedflag, isadultflag, productnotes, createdtimestamp, sourcefilename, modifydatetime)\nSELECT \nstg.titleid AS titleid, \nstg.remappedtitleid AS remappedtitleid, \nstg.titlename AS titlename, \nstg.titletype AS titletype, \nstg.episodetitleid AS episodetitleid, \nstg.seasontitleid AS seasontitleid, \nstg.showtitleid AS showtitleid, \nstg.primarycompanyid AS primarycompanyid, \nstg.primarydistributor AS primarydistributor, \nstg.primarygenre AS primarygenre, \nstg.titleyear AS titleyear, \nstg.primaryreleasedate_us AS primaryreleasedate_us, \nstg.seriestitleid AS seriestitleid, \nstg.episodenumber AS episodenumber, \nstg.seasonnumber AS seasonnumber, \nstg.seriesstartyear AS seriesstartyear, \nstg.seriesendyear AS seriesendyear, \nstg.runtime_us AS runtime_us, \nstg.imdb_url AS imdb_url, \nstg.universalproductflag AS universalproductflag, \nstg.matchconfirmedflag AS matchconfirmedflag, \nstg.isadultflag AS isadultflag, \nstg.productnotes AS productnotes, \nstg.createdtimestamp AS createdtimestamp, \nstg.sourcefilename AS sourcefilename, \nstg.modifydatetime AS modifydatetime\nFROM nexus_stg.stg_imdb_title stg\nWHERE NOT EXISTS\n(\n\tSELECT 1\n\tFROM nexus.imdb_titleadult tgt\n\tWHERE tgt.titleid = stg.titleid\n)\n  AND stg.isadultflag = 'Y';"""
    #sql_statement = """--DELETE FROM nexus.imdb_title_keyword\n\nDELETE\n--SELECT *\nFROM nexus.imdb_titlekeyword tgt\nWHERE EXISTS\n(\n\tSELECT 1\n\tFROM nexus_stg.stg_imdb_title_keyword stg\n\tWHERE stg.resource_id = tgt.titleid\n);\n\nINSERT INTO nexus.imdb_titlekeyword (titleid, titlekeyword, remappedtitleid, sourcefilename, modifydatetime)\nSELECT \nstg.resource_id AS titleid, \nstg.keyword AS titlekeyword, \nstg.remapped_to AS remappedtitleid, \nstg.sourcefilename AS sourcefilename, \nstg.modifydatetime AS modifydatetime\nFROM nexus_stg.stg_imdb_title_keyword stg\nWHERE NOT EXISTS\n(\n\tSELECT 1\n\tFROM nexus.imdb_titlekeyword tgt\n\tWHERE tgt.titleid = stg.resource_id\n)\n  AND stg.keyword IS NOT null;\n\n--SELECT * FROM nexus.imdb_titlekeyword tgt"""

    # Remove single-line comments
    sql_statement = re.sub('--(.*?)\n', '', sql_statement)
    sql_statement = re.sub('--(.*?)$', '', sql_statement)

    # Remove multi-line comments
    sql_statement = re.sub(r'/\*(.*?)\*/', '', sql_statement, flags = re.DOTALL)

    # Remove excess line breaks
    while '\n\n' in sql_statement:
        sql_statement = re.sub('\n\n', '\n', sql_statement, flags = re.DOTALL)

    sql_statement = re.sub('^\n', '', sql_statement, flags = re.DOTALL)
    sql_statement = re.sub('\n$', '', sql_statement, flags = re.DOTALL)
    #print(sql_statement)

    sql_statements = sql_statement.split(';')

    # Remove blank statements
    sql_statements.remove("")
    #print(len(sql_statements))

    # Add ';' to the end of each statement
    sql_statements_output = []
    for statement in sql_statements:
        statement_output = re.sub('^\n', '', statement)
        statement_output = re.sub('\n^', '', statement_output)
        sql_statements_output.append(statement_output + ';')

    return sql_statements_output

#%%
