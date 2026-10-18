"""Inspect local FR-02 state; optionally set one demo user's precondition."""
import argparse,json,sqlite3
from pathlib import Path
from datetime import datetime

def main():
    p=argparse.ArgumentParser();p.add_argument('--email',default='test@eshop.com');p.add_argument('--set-attempts',type=int,choices=[0,1,2]);p.add_argument('--db',type=Path,default=Path(__file__).resolve().parents[3]/'eshop-sut/backend/database.sqlite')
    a=p.parse_args();db=a.db.resolve()
    if not db.is_file():raise SystemExit('Database not found. Start the backend and verify the database path.')
    conn=sqlite3.connect(db.as_uri()+'?mode='+('ro' if a.set_attempts is None else 'rw'),uri=True,timeout=10)
    conn.row_factory=sqlite3.Row
    rows=conn.execute('SELECT id,email,login_attempts,locked_until FROM users WHERE email=?',(a.email,)).fetchall()
    if len(rows)!=1:
        print(json.dumps({'email':a.email,'matches':len(rows),'rows':[dict(x) for x in rows]},ensure_ascii=False));return
    if a.set_attempts is not None:
        dest=db.with_name('database.FR02-before-fixture-'+datetime.now().strftime('%Y%m%dT%H%M%S%f')+'.sqlite')
        backup=sqlite3.connect(dest);conn.backup(backup);backup.close()
        with conn:conn.execute('UPDATE users SET login_attempts=?,locked_until=NULL WHERE id=?',(a.set_attempts,rows[0]['id']))
        print('Fixture backup:',dest)
    after=conn.execute('SELECT id,email,login_attempts,locked_until FROM users WHERE id=?',(rows[0]['id'],)).fetchone()
    print(json.dumps(dict(after),ensure_ascii=False,indent=2));conn.close()

if __name__=='__main__':main()
