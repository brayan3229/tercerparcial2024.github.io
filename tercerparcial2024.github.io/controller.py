import time

import sqlite3 as sql

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print("Base de datos de autoconocimientos creada")
    conn.close()
    
def createTable():
    conn = sql.connect("autoconocimiento.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE progress_metrics (
    metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER,
    metric_type TEXT, -- 'financial', 'time', 'impact'
    current_value DECIMAL(10,2),
    target_value DECIMAL(10,2),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plan_id) REFERENCES strategic_plan(plan_id)
);
    """)
    print("Table creada")
    conn.commit()    
    conn.close()

if __name__== "__main__":
    createDB()
    createTable()