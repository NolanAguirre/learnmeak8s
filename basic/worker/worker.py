import os
import threading
import select
from db import get_threaded_db_pool
from concurrent.futures import ThreadPoolExecutor

def process_event(payload):
    pool = get_threaded_db_pool()
    conn = pool.acquire()
    try:
        curs = conn.cursor()
        curs.execute('SELECT 1')
        conn.commit()
        print(f"Processing event: {payload}")
    except Exception as e:
        conn.rollback()
        print(f"Error processing event: {e}")
    finally:
        pool.release(conn)


def main():
    listen_pool = get_threaded_db_pool()
    listen_conn = listen_pool.acquire()
    listen_conn.set_isolation_level(0)
    
    curs = listen_conn.cursor()
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
        finally:
            curs.close()
            listen_pool.release(listen_conn)

if __name__ == "__main__":
    main()





