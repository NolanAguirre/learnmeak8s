import os
import threading
import select
from db import get_threaded_db_pool
from concurrent.futures import ThreadPoolExecutor

def process_event(payload):
    pool = get_threaded_db_pool()
    with pool.connection() as conn:
        try:
            with conn.cursor() as curs:
                curs.execute('SELECT 1')
                conn.commit()
                print(f"Processing event: {payload}")
        except Exception as e:
            conn.rollback()
            print(f"Error processing event: {e}")


def main():
    pool = get_threaded_db_pool()
    with pool.connection() as listen_conn:
        listen_conn.autocommit = True
        
        with listen_conn.cursor() as curs:
            curs.execute('LISTEN events;')
            print("Listening for events on channel 'events'...")
            
            with ThreadPoolExecutor(max_workers=5) as executor:
                try:
                    while True:
                        if select.select([listen_conn], [], [], 5) == ([], [], []):
                            continue
                        listen_conn.poll()
                        while listen_conn.notifies:
                            notify = listen_conn.notifies.pop(0)
                            executor.submit(process_event, notify.payload)
                except KeyboardInterrupt:
                    print("Shutting down listener.")

if __name__ == "__main__":
    main()





