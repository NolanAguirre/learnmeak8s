#!/usr/bin/env python3

import os
from db import get_db_connection, get_db_pool

def test_direct_connection():
    """Test direct database connection"""
    try:
        conn = get_db_connection()
        with conn.cursor() as curs:
            curs.execute('SELECT version()')
            version = curs.fetchone()
            print(f"✓ Direct connection successful: {version[0]}")
        conn.close()
        return True
    except Exception as e:
        print(f"✗ Direct connection failed: {e}")
        return False

def test_connection_pool():
    """Test connection pool"""
    try:
        pool = get_db_pool(minconn=1, maxconn=3)
        with pool.connection() as conn:
            with conn.cursor() as curs:
                curs.execute('SELECT 1 as test')
                result = curs.fetchone()
                print(f"✓ Connection pool successful: {result[0]}")
        pool.close()
        return True
    except Exception as e:
        print(f"✗ Connection pool failed: {e}")
        return False

def main():
    print("Testing psycopg3 database connections...")
    print("=" * 50)
    
    success = True
    success &= test_direct_connection()
    success &= test_connection_pool()
    
    print("=" * 50)
    if success:
        print("✓ All tests passed! psycopg3 is working correctly.")
    else:
        print("✗ Some tests failed. Please check your database configuration.")
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main()) 