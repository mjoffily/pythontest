import mysql.connector
from mysql.connector import FieldType


sourceConnection = mysql.connector.connect(user='mjoffily', password='',
                                 host='localhost',
                                 database='c9')        # name of the data base

destinationConnection = mysql.connector.connect(user='mjoffily', password='',
                                 host='localhost',
                                 database='test1')        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
#cur = sourceConnection.cursor()

# Use all the SQL you like
#cur.execute("SELECT * FROM test")



class DBObj(object):
    def __init__(self, table, key_column, values):
        self.table = table
        self.key_column = key_column
        self.values = values

instr_file = open('./tables.txt', 'r')
#print instr_file.read()
#for line in instr_file:
#    print line.split('|')
line_words = [(line.split('|')) for line in instr_file]
print line_words
instr_file.close()
dbobjects = []
datasets = dict()
for line in line_words:
    
    if line[0][:2] != '##':
        if line[2][:2] == '##': # this is a pointer to a list
            values = datasets[line[2].rstrip()]
        else:
            values = line[2].rstrip().split(',')
        dbobjects.append(DBObj(line[0], line[1], values))
    else:
        dataset = line[0].rstrip().split('=')
        datasets[dataset[0]] = dataset[1].split(',')
        print 'DATASETS: ' , datasets
        
#initialise the array        
#accounts = ['AAA', 'BBB']
#dbobjects = [DBObj('test', 'a', ['7', '8']), DBObj('test2', 'account_code', accounts)]
query = 'select * from %s where %s in (%s)'

def describe_table(dbobj, src):
    cur = src.cursor()
#    cur.execute("SHOW columns FROM %s" % (table.table))
    cur.execute("select * FROM %s where 1 = 2" % (dbobj.table))
    cur.fetchall()
    cols = ([(k[0], FieldType.get_info(k[1])) for k in cur.description])
    for col in cols:
        if (col[0]) == dbobj.key_column:
            return [col[1], len(cols)]
    
    raise ValueError('No column found to match user defined %s' % dbobj.key_column)
    #types = [FieldType.get_info(k[1]) for k in cur.description]
    #print '?' * 30
    #print '%s %s %s' % (cols[0], cols[1], cols[2])
    #print types
#    return cols
    # for rows in cur.fetchall():
    #     print '\t\t' + ('*' * 30)
    #     print rows
    #     #cols = tuple([k for k in rows.keys()])
    #     # for col in cols:
    #     #     print col
    #     #     print '-' * 30

def format_in_clause(data_type_of_key_column, dbobj):
    s = ''
    print 'hey there: ', data_type_of_key_column
    if data_type_of_key_column == 'VAR_STRING' or data_type_of_key_column == 'STRING':
        for val in dbobj.values:
            s = s + ', "' + val + '"'
    else:
        for val in dbobj.values:
            s = s + ',' + val
    # cut the first comma from the list
    s = s[1:]
    return s

    
def processor(dbobjs, src, dest):
    dc = dest.cursor()
    sc = src.cursor()
    for dbobj in dbobjs:
        # table exists?
        cols = describe_table(dbobj, src)
        in_clause = format_in_clause(cols[0], dbobj)

        queryParsed = query % (dbobj.table, dbobj.key_column, in_clause)
        print "queryParsed : %s" % (queryParsed)
        sc.execute(queryParsed)
        ins = 'insert into %s values (%s)' % (dbobj.table, ','.join(['%s'] * cols[1]))
        print ins
        for row in sc:
            val = ()
            for c in xrange(cols[1]):
                val = val + (row[c],)
            print val
            dc.execute(ins, val)
        dest.commit()
            
processor(dbobjects, sourceConnection, destinationConnection)

sourceConnection.close()
destinationConnection.close()
