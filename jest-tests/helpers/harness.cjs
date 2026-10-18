const fs=require('fs'),path=require('path'),assert=require('assert/strict');
const {dependency}=require('./deps.cjs');
const {chromium}=dependency('playwright');const sqlite=dependency('sqlite3');
const root=path.resolve(__dirname,'../..'),run=process.env.HW02_RUN;
const delay=ms=>new Promise(r=>setTimeout(r,ms));
class Harness{
 constructor(fr){this.fr=fr;this.results={run_id:path.basename(run),cases:[]};this.demo=process.env.HW02_DEMO==='1';this.events=[];}
 async start(){
  this.db=new sqlite.Database(process.env.HW02_DB);this.db.configure('busyTimeout',5000);
  let executablePath=process.env.HW02_CHROMIUM;
  if(!executablePath&&!fs.existsSync(chromium.executablePath())){const cache=path.join(process.env.LOCALAPPDATA||'','ms-playwright');for(const f of fs.readdirSync(cache).filter(n=>/^chromium-\d+$/.test(n)).sort().reverse()){const p=path.join(cache,f,'chrome-win64/chrome.exe');if(fs.existsSync(p)){executablePath=p;break;}}}
  this.browser=await chromium.launch({headless:false,executablePath,args:['--window-size=1360,950']});
  this.context=await this.browser.newContext({viewport:{width:1280,height:850},locale:'vi-VN',...(this.demo?{recordVideo:{dir:path.join(run,'video'),size:{width:1280,height:850}}}:{})});
  this.page=await this.context.newPage();
  this.page.on('request',r=>{if(r.url().includes('/api/')){const h=r.headers();this.events.push({time:Date.now(),url:r.url(),method:r.method(),body:r.postData(),bearer:h.authorization?.startsWith('Bearer ')||false,authorization:h.authorization});}});
  this.page.on('dialog',async d=>{this.dialogs=(this.dialogs||[]).concat(d.message());await d.accept();});
  this.metadata=JSON.parse(fs.readFileSync(path.join(run,'environment.json'),'utf8'));this.metadata.browser=await this.browser.version();this.metadata.playwright=dependency('playwright/package.json').version;
  fs.writeFileSync(path.join(run,'environment-browser.json'),JSON.stringify(this.metadata,null,2));
 }
 sql(q,p=[]){return new Promise((res,rej)=>this.db.run(q,p,function(e){e?rej(e):res({changes:this.changes,id:this.lastID});}));}
 get(q,p=[]){return new Promise((res,rej)=>this.db.get(q,p,(e,row)=>e?rej(e):res(row)));}
 all(q,p=[]){return new Promise((res,rej)=>this.db.all(q,p,(e,row)=>e?rej(e):res(row)));}
 async user(){return this.get('SELECT id,email,login_attempts,locked_until FROM users WHERE email=?',['test@eshop.com']);}
 async resetUser(n=0,until=null){await this.sql('UPDATE users SET login_attempts=?,locked_until=? WHERE email=?',[n,until,'test@eshop.com']);}
 async request(route,body,token,method='POST'){
  const response=await fetch('http://localhost:3000'+route,{method,headers:{...(body===undefined?{}:{'Content-Type':'application/json'}),...(token?{Authorization:'Bearer '+token}:{})},...(body===undefined?{}:{body:JSON.stringify(body)})});
  let data;try{data=await response.json();}catch{data=null;}return {status:response.status,data};
 }
 async token(admin=false){const r=await this.request('/api/login',{email:admin?'admin@eshop.com':'test@eshop.com',password:admin?'Admin123!':'Test1234!'});assert.equal(r.status,200,'Fixture login must succeed');return r.data.token;}
 async banner(title,detail,color='#19334d'){
  await this.page.evaluate(({title,detail,color})=>{let e=document.getElementById('hw02-harness');if(!e){e=document.createElement('div');e.id='hw02-harness';document.body.append(e);}e.style.cssText='position:fixed;bottom:0;left:0;right:0;z-index:2147483647;min-height:110px;padding:14px 24px;background:'+color+';color:white;font:16px Arial;white-space:pre-wrap;border-top:4px solid #72b2ff;box-sizing:border-box;';e.replaceChildren();const t=document.createElement('b');t.textContent='HW02 TEST HARNESS — '+title;const p=document.createElement('div');p.style.cssText='margin-top:8px;line-height:1.4';p.textContent=detail;e.append(t,p);},{title,detail,color});
 }
 async loginPage(){await this.page.goto('http://localhost:5173/login');await this.page.waitForSelector('form input');}
 async submit(email,password){
  await this.page.locator('form input').nth(0).fill(email);await this.page.locator('form input').nth(1).fill(password);
  const pending=this.page.waitForResponse(r=>r.url().endsWith('/api/login')&&r.request().method()==='POST',{timeout:3500}).catch(()=>null);
  await this.page.getByRole('button',{name:'Sign In',exact:true}).click();const r=await pending;
  await delay(350);return r?{status:r.status(),data:await r.json()}:null;
 }
 check(label,actual,expected){this.checks.push({label,actual,expected,pass:JSON.stringify(actual)===JSON.stringify(expected)});}
 async runCase(tc,fn){
  this.checks=[];this.observations={};this.events=[];await this.context.clearCookies();await this.loginPage();await this.page.evaluate(()=>localStorage.clear());await this.loginPage();
  await this.banner(tc.id+' | '+tc.name,'Expected: '+tc.expected+'\nĐang thiết lập tiền điều kiện độc lập.');
  if(this.demo)await delay(1400);
  const started=new Date().toISOString();let infra;
  try{await fn.call(this,tc);}catch(e){infra=e;}
  const failed=this.checks.filter(c=>!c.pass);const status=infra?'Not Run':failed.length?'Fail':'Pass';
  const summary=this.checks.map(c=>(c.pass?'PASS':'FAIL')+' '+c.label+': '+JSON.stringify(c.actual)+(c.pass?'':' (expected '+JSON.stringify(c.expected)+')')).join('\n');
  await this.banner(tc.id+' — '+status,infra?'Infrastructure: '+infra.message:summary,status==='Pass'?'#14532d':status==='Fail'?'#7f1d1d':'#5b4612');
  if(this.demo)await delay(2600);
  const shot=path.join(run,tc.id+'.png');await this.page.screenshot({path:shot,fullPage:true});
  const result={id:tc.id,status,tested_at:new Date().toLocaleString('sv-SE',{timeZone:'Asia/Ho_Chi_Minh'})+' UTC+07:00',started_at:started,actual:summary,checks:this.checks,observations:this.observations,evidence:path.relative(root,shot).replaceAll('\\','/'),...(infra?{reason:infra.message}:{})};
  this.results.cases.push(result);fs.writeFileSync(path.join(run,'results.json'),JSON.stringify(this.results,null,2));
  // Record request metadata only; never persist bearer tokens or login response bodies.
  const safe=this.events.map(({authorization,body,...r})=>({...r,...(r.url.endsWith('/api/login')?{}:{body})}));
  fs.writeFileSync(path.join(run,tc.id+'-requests.json'),JSON.stringify(safe,null,2));
  if(infra)throw infra;if(failed.length)throw new Error(failed.map(c=>`${c.label}: expected ${JSON.stringify(c.expected)}, received ${JSON.stringify(c.actual)}`).join('; '));
 }
 async finish(){
  if(this.demo&&this.page){const pass=this.results.cases.filter(r=>r.status==='Pass').length,fail=this.results.cases.filter(r=>r.status==='Fail').length;await this.banner('FR-02 — Kết thúc video đầu tiên',`${this.results.cases.length} TC minh họa | Pass: ${pass} | Fail: ${fail}\nDừng tại đây và chờ sinh viên duyệt trước video FR-09/FR-15.`);await delay(4000);}
  const video=this.page?.video();await this.context?.close();
  if(video){const v=path.join(root,'videos',this.fr+'-demo.webm');await video.saveAs(v);fs.copyFileSync(v,path.join(run,this.fr+'-demo.webm'));this.results.video=path.relative(root,v).replaceAll('\\','/');}
  await this.browser?.close();if(this.db)await new Promise(res=>this.db.close(res));
  fs.writeFileSync(path.join(run,'results.json'),JSON.stringify(this.results,null,2));
 }
}
module.exports={Harness,delay};
