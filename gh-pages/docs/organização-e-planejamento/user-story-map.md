

## User Story Map

<div style="position:relative;width:100%;max-width:100%;font-family:sans-serif;user-select:none;margin-top:8px;">
  <div style="display:flex;align-items:center;gap:6px;padding:8px 10px;background:rgba(128,128,128,0.08);border:1px solid rgba(128,128,128,0.2);border-bottom:none;border-radius:8px 8px 0 0;">
    <button id="sm-in" style="width:28px;height:28px;border:1px solid rgba(128,128,128,0.35);border-radius:4px;background:transparent;cursor:pointer;font-size:16px;line-height:1;">+</button>
    <button id="sm-out" style="width:28px;height:28px;border:1px solid rgba(128,128,128,0.35);border-radius:4px;background:transparent;cursor:pointer;font-size:16px;line-height:1;">−</button>
    <button id="sm-reset" style="height:28px;padding:0 10px;border:1px solid rgba(128,128,128,0.35);border-radius:4px;background:transparent;cursor:pointer;font-size:12px;">↺ Reset</button>
    <span style="font-size:11px;opacity:0.5;margin-left:4px;">Scroll para zoom · Arraste para mover · Passe o mouse nos cartões para detalhes · Clique no cartão para abrir evidências</span>
  </div>
  <div id="sm-wrap" style="width:100%;height:640px;overflow:hidden;border:1px solid rgba(128,128,128,0.2);border-radius:0 0 8px 8px;cursor:grab;box-sizing:border-box;">
    <svg id="sm-svg" xmlns="http://www.w3.org/2000/svg" style="display:block; width:100%; height:100%;"></svg>
  </div>
  <div id="sm-tip" style="position:absolute;background:#222;color:#fff;padding:7px 11px;border-radius:6px;font-size:13px;pointer-events:none;display:none;max-width:340px;z-index:200;line-height:1.5;box-shadow:0 2px 8px rgba(0,0,0,0.4);"></div>
</div>

<script>
(function(){
  var COL_W=120, COL_GAP=6, GRP_GAP=18, PAD=20;
  var PERSONA_H=22, OBJ_H=46, TASK_H=40, US_H=50, US_GAP=5;
  var PERSONA_Y=8;
  var OBJ_Y=PERSONA_Y+PERSONA_H+6;

  /* US que fazem parte do MVP (conforme tabela de priorizacao 10.2) */
  var MVP={US01:1,US02:1,US04:1,US08:1,US09:1,US10:1,US11:1,US12:1,
           US13:1,US14:1,US15:1,US16:1,US17:1,US18:1,US19:1,US20:1,US21:1,US22:1};

  var GROUPS=[
    {id:'G1',label:'Transparencia da organizacao',persona:'Usuario / Admin da Organizacao',
     lines:['Transparencia da','organizacao'],color:'#1565C0',
     tasks:[
       {label:'Historico financeiro',us:['US01']},
       {label:'Lancar doacoes e despesas',us:['US15','US16']}
     ]},
    {id:'G2',label:'Feed de Post das Organizacoes',persona:'Usuario / Admin da Organizacao',
     lines:['Feed de Post','das Organizacoes'],color:'#2E7D32',
     tasks:[
       {label:'Visualizar publicacoes',us:['US02']},
       {label:'Restringir exibicao',us:['US06']},
       {label:'Localizar publicacao',us:['US07']},
       {label:'Gerenciar publicacoes',us:['US17','US18','US19']}
     ]},
    {id:'G3',label:'Perfil geral da organizacao',persona:'Usuario / Admin da Organizacao',
     lines:['Perfil geral','da organizacao'],color:'#00695C',
     tasks:[
       {label:'Visualizar descricao',us:['US03']},
       {label:'Contactar organizacao',us:['US05']},
       {label:'Configurar dados inst.',us:['US14']}
     ]},
    {id:'G4',label:'Colaboracao com a Organizacao',persona:'Usuario / Admin da Organizacao',
     lines:['Colaboracao','com a Organizacao'],color:'#BF360C',
     tasks:[
       {label:'Visualizar voluntariado',us:['US04']},
       {label:'Inscrever voluntariado',us:['US08']},
       {label:'Inscrever em eventos',us:['US09']},
       {label:'Realizar doacao',us:['US10']},
       {label:'Gestao de voluntarios',us:['US20','US21','US22']}
     ]},
    {id:'G5',label:'Gerenciar o funcionamento da organizacao',persona:'Admin geral / Admin da Organizacao',
     lines:['Gerenciar o funcionamento','da organizacao'],color:'#4A148C',
     tasks:[
       {label:'Autenticar admins',us:['US11']},
       {label:'Gerenciar admins',us:['US12','US13']}
     ]}
  ];

  /* Labels exibidos no SVG (acentuados) */
  var LABEL={
    G1_0:'Transparência da',G1_1:'organização',
    G2_0:'Feed de Post',G2_1:'das Organizações',
    G3_0:'Perfil geral',G3_1:'da organização',
    G4_0:'Colaboração',G4_1:'com a Organização',
    G5_0:'Gerenciar o funcionamento',G5_1:'da organização',
    P1:'Usuário / Admin da Organização',P2:'Admin geral / Admin da Organização',
    T_G1_0:'Histórico financeiro',T_G1_1:'Lançar doações e despesas',
    T_G2_0:'Visualizar publicações',T_G2_1:'Restringir exibição',
    T_G2_2:'Localizar publicação',T_G2_3:'Gerenciar publicações',
    T_G3_0:'Visualizar descrição',T_G3_1:'Contactar organização',T_G3_2:'Configurar dados inst.',
    T_G4_0:'Visualizar voluntariado',T_G4_1:'Inscrever voluntariado',
    T_G4_2:'Inscrever em eventos',T_G4_3:'Realizar doação',T_G4_4:'Gestão de voluntários',
    T_G5_0:'Autenticar admins',T_G5_1:'Gerenciar admins'
  };

  /* Aplicar labels acentuados */
  GROUPS[0].lines=[LABEL.G1_0,LABEL.G1_1];
  GROUPS[1].lines=[LABEL.G2_0,LABEL.G2_1];
  GROUPS[2].lines=[LABEL.G3_0,LABEL.G3_1];
  GROUPS[3].lines=[LABEL.G4_0,LABEL.G4_1];
  GROUPS[4].lines=[LABEL.G5_0,LABEL.G5_1];
  GROUPS[0].persona=LABEL.P1; GROUPS[1].persona=LABEL.P1;
  GROUPS[2].persona=LABEL.P1; GROUPS[3].persona=LABEL.P1;
  GROUPS[4].persona=LABEL.P2;
  GROUPS[0].tasks[0].label=LABEL.T_G1_0; GROUPS[0].tasks[1].label=LABEL.T_G1_1;
  GROUPS[1].tasks[0].label=LABEL.T_G2_0; GROUPS[1].tasks[1].label=LABEL.T_G2_1;
  GROUPS[1].tasks[2].label=LABEL.T_G2_2; GROUPS[1].tasks[3].label=LABEL.T_G2_3;
  GROUPS[2].tasks[0].label=LABEL.T_G3_0; GROUPS[2].tasks[1].label=LABEL.T_G3_1; GROUPS[2].tasks[2].label=LABEL.T_G3_2;
  GROUPS[3].tasks[0].label=LABEL.T_G4_0; GROUPS[3].tasks[1].label=LABEL.T_G4_1;
  GROUPS[3].tasks[2].label=LABEL.T_G4_2; GROUPS[3].tasks[3].label=LABEL.T_G4_3; GROUPS[3].tasks[4].label=LABEL.T_G4_4;
  GROUPS[4].tasks[0].label=LABEL.T_G5_0; GROUPS[4].tasks[1].label=LABEL.T_G5_1;

  var UI={
    US01:{rf:'RF01',sprint:6,desc:'Visualizar histórico financeiro',link:'../planejamento/sprint-6/user-stories/#us01',st:'vd',persona:'Usuário',cl:['Histórico','financeiro']},
    US02:{rf:'RF02',sprint:2,desc:'Visualizar publicações no feed',link:'../planejamento/sprint-2/user-stories/#us02',st:'vd',persona:'Usuário',cl:['Visualizar','publicações']},
    US03:{rf:'RF03',sprint:6,desc:'Visualizar descrição da ONG',link:'../planejamento/sprint-6/user-stories/#us03',st:'vm',persona:'Usuário',cl:['Descrição','da ONG']},
    US04:{rf:'RF04',sprint:4,desc:'Visualizar oportunidades de voluntariado',link:'../planejamento/sprint-4/user-stories/#us04',st:'vd',persona:'Usuário',cl:['Visualizar','voluntariado']},
    US05:{rf:'RF05',sprint:6,desc:'Contactar a organização',link:'../planejamento/sprint-6/user-stories/#us05',st:'vm',persona:'Usuário',cl:['Contactar','organização']},
    US06:{rf:'RF06',sprint:5,desc:'Filtrar publicações do feed',link:'../planejamento/sprint-5/user-stories/#us06',st:'vd',persona:'Usuário',cl:['Filtrar','publicações']},
    US07:{rf:'RF07',sprint:5,desc:'Buscar publicações por título',link:'../planejamento/sprint-5/user-stories/#us07',st:'vd',persona:'Usuário',cl:['Buscar','publicações']},
    US08:{rf:'RF08',sprint:4,desc:'Inscrever-se como voluntário',link:'../planejamento/sprint-4/user-stories/#us08',st:'vd',persona:'Usuário',cl:['Inscrever-se','voluntário']},
    US09:{rf:'RF09',sprint:3,desc:'Inscrever-se em evento',link:'../planejamento/sprint-3/user-stories/#us09',st:'vd',persona:'Usuário',cl:['Inscrever-se','em evento']},
    US10:{rf:'RF10',sprint:5,desc:'Realizar doação',link:'../planejamento/sprint-5/user-stories/#us10',st:'vd',persona:'Usuário',cl:['Realizar','doação']},
    US11:{rf:'RF11',sprint:3,desc:'Autenticar administradores',link:'../planejamento/sprint-3/user-stories/#us11',st:'vd',persona:'Admin da org.',cl:['Autenticar','admins']},
    US12:{rf:'RF12',sprint:6,desc:'Cadastrar administrador de organização',link:'../planejamento/sprint-6/user-stories/#us12',st:'vd',persona:'Admin geral',cl:['Cadastrar','administrador']},
    US13:{rf:'RF13',sprint:6,desc:'Remover administrador de organização',link:'../planejamento/sprint-6/user-stories/#us13',st:'vd',persona:'Admin geral',cl:['Remover','administrador']},
    US14:{rf:'RF14',sprint:6,desc:'Configurar dados institucionais',link:'../planejamento/sprint-6/user-stories/#us14',st:'vd',persona:'Admin da org.',cl:['Configurar','dados inst.']},
    US15:{rf:'RF15',sprint:5,desc:'Lançar doações manuais',link:'../planejamento/sprint-5/user-stories/#us15',st:'vd',persona:'Admin da org.',cl:['Lançar','doações manuais']},
    US16:{rf:'RF16',sprint:5,desc:'Lançar despesas operacionais',link:'../planejamento/sprint-5/user-stories/#us16',st:'vd',persona:'Admin da org.',cl:['Lançar','despesas']},
    US17:{rf:'RF17',sprint:2,desc:'Criar publicação no feed',link:'../planejamento/sprint-2/user-stories/#us17',st:'vd',persona:'Admin da org.',cl:['Criar','publicação']},
    US18:{rf:'RF18',sprint:2,desc:'Deletar publicação no feed',link:'../planejamento/sprint-2/user-stories/#us18',st:'vd',persona:'Admin da org.',cl:['Deletar','publicação']},
    US19:{rf:'RF19',sprint:2,desc:'Atualizar publicação no feed',link:'../planejamento/sprint-2/user-stories/#us19',st:'vd',persona:'Admin da org.',cl:['Atualizar','publicação']},
    US20:{rf:'RF20',sprint:4,desc:'Registrar oportunidade de voluntariado',link:'../planejamento/sprint-4/user-stories/#us20',st:'vd',persona:'Admin da org.',cl:['Registrar','voluntariado']},
    US21:{rf:'RF21',sprint:4,desc:'Deletar oportunidade de voluntariado',link:'../planejamento/sprint-4/user-stories/#us21',st:'vd',persona:'Admin da org.',cl:['Deletar','voluntariado']},
    US22:{rf:'RF22',sprint:4,desc:'Atualizar oportunidade de voluntariado',link:'../planejamento/sprint-4/user-stories/#us22',st:'vd',persona:'Admin da org.',cl:['Atualizar','voluntariado']}
  };

  var CL={vd:{f:'#4CAF50',s:'#388E3C',t:'#fff'},am:{f:'#FFC107',s:'#F9A825',t:'#333'},vm:{f:'#F44336',s:'#C62828',t:'#fff'}};

  /* ── LAYOUT ── */
  var W, cx=PAD;
  GROUPS.forEach(function(grp){
    grp.x=cx;
    grp.tasks.forEach(function(t){ t.x=cx; cx+=COL_W+COL_GAP; });
    grp.w=cx-COL_GAP-grp.x;
    W=cx-COL_GAP+PAD;
    cx+=GRP_GAP-COL_GAP;
  });

  /* Maximo de US-MVP e US-nao-MVP em qualquer coluna */
  var maxMvpUS=0, maxNonMvpUS=0;
  GROUPS.forEach(function(grp){
    grp.tasks.forEach(function(t){
      var m=0,n=0;
      t.us.forEach(function(id){ if(MVP[id]) m++; else n++; });
      maxMvpUS=Math.max(maxMvpUS,m); maxNonMvpUS=Math.max(maxNonMvpUS,n);
    });
  });

  var TASK_Y=OBJ_Y+OBJ_H+8;
  var US_Y=TASK_Y+TASK_H+8;
  /* Linha MVP: logo abaixo do ultimo cartao MVP */
  var MVP_LINE_Y=US_Y+maxMvpUS*(US_H+US_GAP)-US_GAP+8;
  var MVP_BAND_H=20;
  var AFTER_MVP_Y=MVP_LINE_Y+MVP_BAND_H+4;

  /* ── BUILD SVG ── */
  var NS='http://www.w3.org/2000/svg';
  var svgEl=document.getElementById('sm-svg');
  var wrap=document.getElementById('sm-wrap');
  var tip=document.getElementById('sm-tip');
  svgEl.innerHTML='';
  var svgG=document.createElementNS(NS,'g');
  svgEl.appendChild(svgG);
  var didDrag=false;

  function mkRect(x,y,w,h,fill,stroke,sw,rx){
    var r=document.createElementNS(NS,'rect');
    r.setAttribute('x',x); r.setAttribute('y',y);
    r.setAttribute('width',w); r.setAttribute('height',h);
    r.setAttribute('fill',fill); r.setAttribute('stroke',stroke||'none');
    r.setAttribute('stroke-width',sw||0); r.setAttribute('rx',rx||4);
    return r;
  }
  function mkTxt(x,y,text,fs,fill,anchor,bold,ff){
    var t=document.createElementNS(NS,'text');
    t.setAttribute('x',x); t.setAttribute('y',y);
    t.setAttribute('text-anchor',anchor||'middle');
    t.setAttribute('dominant-baseline','middle');
    t.setAttribute('fill',fill||'#fff'); t.setAttribute('font-size',fs||10);
    t.setAttribute('font-family',ff||'sans-serif');
    if(bold) t.setAttribute('font-weight','bold');
    t.textContent=text;
    return t;
  }
  function splitLbl(text,maxL){
    if(text.length<=maxL) return [text];
    var mid=Math.floor(text.length/2);
    var idx=text.lastIndexOf(' ',mid);
    if(idx<0) idx=text.indexOf(' ',mid);
    if(idx<0) return [text];
    return [text.substring(0,idx),text.substring(idx+1)];
  }

  /* ── PERSONAS (agrupadas por persona consecutiva) ── */
  var pGroups=[], lastP=null, pX0=0, pX1=0;
  GROUPS.forEach(function(grp){
    if(grp.persona!==lastP){
      if(lastP!==null) pGroups.push({label:lastP,x:pX0,w:pX1-pX0});
      lastP=grp.persona; pX0=grp.x; pX1=grp.x+grp.w;
    } else { pX1=grp.x+grp.w; }
  });
  if(lastP!==null) pGroups.push({label:lastP,x:pX0,w:pX1-pX0});

  var pFill=['rgba(33,150,243,0.10)','rgba(156,39,176,0.10)'];
  var pStroke=['rgba(33,150,243,0.35)','rgba(156,39,176,0.35)'];
  var pText=['#1565C0','#6A1B9A'];
  pGroups.forEach(function(pg,i){
    svgG.appendChild(mkRect(pg.x,PERSONA_Y,pg.w,PERSONA_H,pFill[i%2],pStroke[i%2],0.8,4));
    svgG.appendChild(mkTxt(pg.x+pg.w/2,PERSONA_Y+PERSONA_H/2,pg.label,9,pText[i%2],'middle',true));
  });

  /* ── OBJECTIVES ── */
  GROUPS.forEach(function(grp){
    svgG.appendChild(mkRect(grp.x,OBJ_Y,grp.w,OBJ_H,grp.color,'none',0,6));
    var mx=grp.x+grp.w/2;
    if(grp.lines.length===1){
      svgG.appendChild(mkTxt(mx,OBJ_Y+OBJ_H/2,grp.lines[0],11,'#fff','middle',true));
    } else {
      svgG.appendChild(mkTxt(mx,OBJ_Y+14,grp.lines[0],11,'#fff','middle',true));
      svgG.appendChild(mkTxt(mx,OBJ_Y+27,grp.lines[1],11,'#fff','middle',true));
    }
  });

  /* ── TASKS ── */
  GROUPS.forEach(function(grp){
    grp.tasks.forEach(function(t){
      var x=t.x, w=COL_W, h=TASK_H;
      svgG.appendChild(mkRect(x,TASK_Y,w,h,'#f5f5f5','#ddd',1,4));
      svgG.appendChild(mkRect(x,TASK_Y,w,4,grp.color,'none',0,2));
      var lines=splitLbl(t.label,16), mx=x+w/2;
      if(lines.length===1){
        svgG.appendChild(mkTxt(mx,TASK_Y+h/2+2,lines[0],9,'#333','middle',true));
      } else {
        svgG.appendChild(mkTxt(mx,TASK_Y+h/2-5,lines[0],9,'#333','middle',true));
        svgG.appendChild(mkTxt(mx,TASK_Y+h/2+6,lines[1],9,'#333','middle',true));
      }
    });
  });

  /* ── US CARDS (MVP acima da linha, nao-MVP abaixo) ── */
  GROUPS.forEach(function(grp){
    grp.tasks.forEach(function(t){
      var mi=0, ni=0;
      t.us.forEach(function(usId){
        var info=UI[usId], c=CL[info.st], isMvp=!!MVP[usId];
        var y=isMvp ? US_Y+mi*(US_H+US_GAP) : AFTER_MVP_Y+ni*(US_H+US_GAP);
        if(isMvp) mi++; else ni++;
        var x=t.x+3, w=COL_W-6, h=US_H;
        var card=document.createElementNS(NS,'g');
        card.style.cursor='pointer';
        var r=mkRect(x,y,w,h,c.f,c.s,1.5,5);
        card.appendChild(r);
        card.appendChild(mkTxt(x+w/2,y+13,usId,10,c.t,'middle',true,'monospace'));
        if(info.cl.length===2){
          card.appendChild(mkTxt(x+w/2,y+28,info.cl[0],8,c.t,'middle',false));
          card.appendChild(mkTxt(x+w/2,y+38,info.cl[1],8,c.t,'middle',false));
        } else {
          card.appendChild(mkTxt(x+w/2,y+33,info.cl[0],8,c.t,'middle',false));
        }
        card.appendChild(mkTxt(x+w-4,y+8,'S'+info.sprint,7,c.t,'end',false));
        card.appendChild(mkTxt(x+4,y+8,info.rf,7,c.t,'start',false));
        card.addEventListener('mouseenter',function(){
          r.setAttribute('stroke-width','2.5');
          tip.innerHTML='<b>'+usId+'</b> \xb7 '+info.rf+'<br>'+info.desc+'<br><span style="opacity:0.7;font-size:11px">Persona: '+info.persona+' \xb7 Sprint '+info.sprint+'</span><br><span style="font-size:11px;font-style:italic;opacity:0.6">Clique para abrir evid\xeancias</span>';
          tip.style.display='block';
        });
        card.addEventListener('mousemove',function(ev){
          var br=wrap.getBoundingClientRect();
          var lx=ev.clientX-br.left+14, ly=ev.clientY-br.top-60;
          if(lx+345>br.width) lx=lx-360;
          tip.style.left=lx+'px'; tip.style.top=ly+'px';
        });
        card.addEventListener('mouseleave',function(){
          r.setAttribute('stroke-width','1.5'); tip.style.display='none';
        });
        card.addEventListener('click',function(){
          if(didDrag) return;
          window.open(info.link,'_blank','noopener');
        });
        svgG.appendChild(card);
      });
    });
  });

  /* ── FATIA MVP (linha divisoria horizontal) ── */
  /* banda de fundo */
  svgG.appendChild(mkRect(PAD/2,MVP_LINE_Y,W-PAD,MVP_BAND_H,'rgba(25,118,210,0.08)','rgba(25,118,210,0.22)',0.8,3));
  /* linha tracejada no topo da banda */
  var mvpLine=document.createElementNS(NS,'line');
  mvpLine.setAttribute('x1',PAD/2); mvpLine.setAttribute('x2',W-PAD/2);
  mvpLine.setAttribute('y1',MVP_LINE_Y); mvpLine.setAttribute('y2',MVP_LINE_Y);
  mvpLine.setAttribute('stroke','#1976D2'); mvpLine.setAttribute('stroke-width','1.5');
  mvpLine.setAttribute('stroke-dasharray','8,4');
  svgG.appendChild(mvpLine);
  /* badge "MVP" */
  svgG.appendChild(mkRect(PAD/2,MVP_LINE_Y,38,MVP_BAND_H,'#1976D2','none',0,3));
  svgG.appendChild(mkTxt(PAD/2+19,MVP_LINE_Y+MVP_BAND_H/2,'MVP',9,'#fff','middle',true));
  /* label zona abaixo */
  if(maxNonMvpUS>0){
    svgG.appendChild(mkTxt(PAD/2+46,MVP_LINE_Y+MVP_BAND_H/2,'Linha do MVP - Tudo abaixo dessa linha não será incluido dentro do MVP definido',9,'#1976D2','start',false));
  }

  /* ── ZOOM / PAN ── */
  var scale=1, txn=0, tyn=8, isDrg=false, sx, sy, stx, sty;
  function applyT(){ svgG.setAttribute('transform','translate('+txn+','+tyn+') scale('+scale+')'); }

  function fitToContainer(){
    var cw=wrap.clientWidth||820;
    scale=Math.min((cw-20)/W,1);
    txn=(cw-W*scale)/2; tyn=8;
    applyT();
  }
  fitToContainer();

  if(window.ResizeObserver){
    new ResizeObserver(function(){ if(!isDrg) fitToContainer(); }).observe(wrap);
  }

  wrap.addEventListener('wheel',function(ev){
    ev.preventDefault();
    var br=wrap.getBoundingClientRect();
    var mx=ev.clientX-br.left, my=ev.clientY-br.top;
    var ns=Math.min(Math.max(scale*(ev.deltaY<0?1.12:0.89),0.2),4);
    txn=mx-(mx-txn)*(ns/scale); tyn=my-(my-tyn)*(ns/scale); scale=ns; applyT();
  },{passive:false});
  wrap.addEventListener('mousedown',function(ev){
    isDrg=true; didDrag=false;
    sx=ev.clientX; sy=ev.clientY; stx=txn; sty=tyn;
    wrap.style.cursor='grabbing';
  });
  document.addEventListener('mousemove',function(ev){
    if(!isDrg) return;
    if(Math.abs(ev.clientX-sx)>3||Math.abs(ev.clientY-sy)>3) didDrag=true;
    txn=stx+(ev.clientX-sx); tyn=sty+(ev.clientY-sy); applyT();
  });
  document.addEventListener('mouseup',function(){ isDrg=false; wrap.style.cursor='grab'; });
  document.getElementById('sm-in').addEventListener('click',function(){
    scale=Math.min(scale*1.2,4); txn=(wrap.clientWidth-W*scale)/2; tyn=8; applyT();
  });
  document.getElementById('sm-out').addEventListener('click',function(){
    scale=Math.max(scale*0.8,0.2); txn=(wrap.clientWidth-W*scale)/2; tyn=8; applyT();
  });
  document.getElementById('sm-reset').addEventListener('click',fitToContainer);
})();
</script>

| Cor | Status |
| :---: | :--- |
| 🟢 Verde | **Totalmente concluído** — entregue e validado com o cliente |
| 🟡 Amarelo | **Parcialmente concluído** — entregue com débito técnico |
| 🔴 Vermelho | **Não iniciado / Em andamento** — previsto em sprint em andamento ou futura |
