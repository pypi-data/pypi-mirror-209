import psycopg2
from azure.storage.blob import BlobServiceClient
import pandas as pd
import traceback
from asset_tracking_pepsico.dto.PostgresSchema import PostgresSchemaDto
from datetime import datetime, timedelta


class PostGresRepository:

    # Get a connection to a new postgres server using the connection string.
    def get_conn(self, postgre_conn_str):
        try:
            conn = psycopg2.connect(postgre_conn_str)
            cursor = conn.cursor()
            return cursor, conn
        except:
            traceback.print_exc()

    # Commit all transactions and close the connection
    def close_connection(self, conn):
        try:
            conn.commit()
            conn.close()
        except:
            traceback.print_exc()

    # convert the datetime string to extract date and time in the datetime format
    def convert_datetime(self, time_str):
        try:
            date_string, time_string, offset_string = time_str.split()
            date = datetime.strptime(date_string, "%m/%d/%Y").strftime("%m/%d/%Y")
            offset_hours, offset_minutes = map(int, offset_string.split(':'))
            offset = timedelta(hours=offset_hours, minutes=offset_minutes)
            datetime_obj = datetime.strptime(date_string + ' ' + time_string, "%m/%d/%Y %H:%M:%S") + offset
            return datetime_obj, date
        except:
            traceback.print_exc()

    # format the query to form an sql query
    def format_query(self, query):
        try:
            start_pos = query.find("None, '{") + len("None, '{")
            end_pos = query.find("}'")
            substring = query[start_pos:end_pos]
            new_substring = substring.replace("'", '"')
            updated_query = query[:start_pos] + new_substring + query[end_pos:]
            updated_query = updated_query.replace('None', 'NULL')
            return updated_query
        except:
            traceback.print_exc()

    # generate an insert query based on the table name and the columns
    def generate_insert_query(self, table_name, schema, columns):
        try:
            print('-'*120 + "\ncreating query for SCHEMA === \n", type(schema), schema, "\n" + '-'*120)
            query = f'''INSERT INTO {table_name} ({columns}) VALUES ({schema.__str__()})'''
            query = self.format_query(query)
            print("QUERY === ", query, type(query))
            return query
        except:
            traceback.print_exc()

    # write the data to postgres
    def write_data(self, postgre_conn_str, table_name, schema_list, columns):
        try:
            rows_affected = []
            cursor, conn = self.get_conn(postgre_conn_str)
            for schema in schema_list:
                print('-' * 100 + "\nwriting to postgres === ", schema.__str__() + "\n" + '-' * 100)
                query = self.generate_insert_query(table_name, schema, columns)
                cursor.execute(query)
                rows_affected.append(cursor.rowcount)
                conn.commit()
            self.close_connection(conn)
            return rows_affected
        except:
            traceback.print_exc()

    # read the data from postgres
    def read_data_from_db(self, postgre_conn_str):
        cursor, conn = self.get_conn(postgre_conn_str)
        sql1 = '''select * from rsrlocation_info limit 5;'''
        cursor.execute(sql1)
        for i in cursor.fetchall():
            print("result == ", i)

    # process the data got from log file.
    def process_data(self, data, event):
        try:
            log_list = []
            event_list = [i for i in data.split("\n") if event in i and "Monitoring" not in i and "Error" not in i]
            for i in event_list:
                temp = {}
                sub = i[i.index(event) + len(event) + 1:i.index('}') + 1]
                event_name = sub[:sub.index(':')]
                # print("event_name === ", event_name)
                sub = sub[sub.index('{') + 1:sub.index('}')]
                temp["event"] = event_name
                if event_name == "OnLocationChanged":
                    info_list = sub.split(',')
                    for info in info_list:
                        key, val = info[:info.index(':')], info[info.index(':') + 1:]
                        temp[key.strip()] = val.strip()
                else:
                    tags = sub[sub.index('Tags'):sub.index(']') + 1]
                    tags_type = str(tags[tags.index('[') + 1:-1]).replace('"', '').split(',')
                    temp["visit_type"] = tags_type[0]
                    temp["visit_id"] = tags_type[1].split("::")[1]
                    temp["cust_cis_id"] = tags_type[2].split("::")[1]
                    tags = tags + ', '
                    sub = sub.replace(tags, '')
                    info_list = sub.split(',')
                    for info in info_list:
                        key, val = str(info[:info.index(':')]).strip(), str(info[info.index(':') + 1:]).strip().replace('"',
                                                                                                                        '')
                        temp[key] = val
                # print("temp === ", temp)
                log_list.append(temp)
            df = pd.DataFrame(log_list)
            df.fillna('null', inplace=True)
            return df
        except:
            traceback.print_exc()

    # create the schema object in the form of dto defined in the PostgresSchemaDto class
    def create_schema_list(self, df, asset_type, gpid, data_source):
        try:
            schema_list = []
            for index, row in df.iterrows():
                # print("creating schema for \n" + str(row) + "\n" + "-"*200)
                event = {'event': row['event']}
                if event['event'] == "OnLocationChanged":
                    # print("Entered if condition for event === ", event)
                    speed = row['Speed']
                    updated_ts = None
                    store_id = None
                else:
                    speed = None
                    updated_ts = row['LastExitTime']
                    store_id = row['cust_cis_id']
                speed_acc = row['Accuracy']
                ts = row['Timestamp']
                _, dt = self.convert_datetime(row['Timestamp'])
                lat, long = float(row['Latitude']), float(row['Longitude'])
                schema = PostgresSchemaDto(asset_id=gpid, asset_type=asset_type, store_id=store_id, datasource=data_source, asset_latitude=lat,
                                           asset_longitude=long, speed=speed, speed_accuracy=speed_acc, event=str(event),
                                           created_ts=ts, updated_ts=updated_ts, created_dt=dt)
                schema_list.append(schema)
            return schema_list
        except:
            traceback.print_exc()

    # read the data from file.
    def read_data_from_logfile(self, filename):
        with open(filename, 'r') as f:
            data = f.read()
        f.close()
        return data

    # get block blob client from azure storage explorer.
    def get_block_blob_client(self, blob_conn_str, container_name, blob_name):
        try:
            print("conn str == ", blob_conn_str)
            blob_service_client = BlobServiceClient.from_connection_string(conn_str=blob_conn_str)
            container_client = blob_service_client.get_container_client(container_name)
            block_blob_client = container_client.get_blob_client(blob_name)
            return block_blob_client
        except:
            traceback.print_exc()

    # read data from downloaded blob
    def read_data_from_blob(self, blob_conn_str, container_name, blob_name):
        try:
            blob_client = self.get_block_blob_client(blob_conn_str, container_name, blob_name)
            file_name = blob_client.download_blob()
            data = file_name.readall()
            return data
        except:
            traceback.print_exc()
