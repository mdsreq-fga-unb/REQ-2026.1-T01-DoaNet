## Rastreabilidade do Projeto

O grafo abaixo representa a cadeia completa de rastreabilidade do DoaNet — do problema central até cada User Story — com indicação visual do status de execução por cor.

<div style="position:relative;width:100%;font-family:sans-serif;user-select:none;">
  <div style="display:flex;align-items:center;gap:6px;padding:8px 10px;background:rgba(128,128,128,0.08);border:1px solid rgba(128,128,128,0.2);border-bottom:none;border-radius:8px 8px 0 0;">
    <button id="tz-in" style="width:28px;height:28px;border:1px solid rgba(128,128,128,0.35);border-radius:4px;background:transparent;cursor:pointer;font-size:16px;line-height:1;">+</button>
    <button id="tz-out" style="width:28px;height:28px;border:1px solid rgba(128,128,128,0.35);border-radius:4px;background:transparent;cursor:pointer;font-size:16px;line-height:1;">−</button>
    <button id="tz-reset" style="height:28px;padding:0 10px;border:1px solid rgba(128,128,128,0.35);border-radius:4px;background:transparent;cursor:pointer;font-size:12px;">↺ Reset</button>
    <span style="font-size:11px;opacity:0.5;margin-left:4px;">Scroll para zoom · Arraste para mover · Passe o mouse nos nós para detalhes · Clique no texto para abrir documentação</span>
  </div>
  <div id="tz-wrap" style="width:100%;height:640px;overflow:hidden;border:1px solid rgba(128,128,128,0.2);border-radius:0 0 8px 8px;cursor:grab;box-sizing:border-box;">
    <svg id="tz-svg" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;height:100%;"></svg>
  </div>
  <div id="tz-tip" style="position:absolute;background:#222;color:#fff;padding:7px 11px;border-radius:6px;font-size:13px;pointer-events:none;display:none;max-width:340px;z-index:200;line-height:1.5;box-shadow:0 2px 8px rgba(0,0,0,0.4);"></div>
</div>

<script>
(function(){
  var R=23, PAD=42, SP=52, GRP_GAP=78, OE_MIN=54, H=600;
  var LY=[55,160,265,380,500];

  var CP_RF={
    CP1:['RF10'],
    CP2:['RF01','RF15','RF16'],
    CP3:['RF02','RF06','RF07','RF17','RF18','RF19'],
    CP4:['RF04','RF08','RF20','RF21','RF22'],
    CP5:['RF09'],
    CP6:['RF03','RF05'],
    CP7:['RF11','RF12','RF13'],
    CP8:['RF14']
  };
  var RF_US={
    RF01:'US01',RF02:'US02',RF03:'US03',RF04:'US04',RF05:'US05',RF06:'US06',
    RF07:'US07',RF08:'US08',RF09:'US09',RF10:'US10',RF11:'US11',RF12:'US12',
    RF13:'US13',RF14:'US14',RF15:'US15',RF16:'US16',RF17:'US17',RF18:'US18',
    RF19:'US19',RF20:'US20',RF21:'US21',RF22:'US22'
  };
  var OE_CP={
    OE1:['CP2'],OE2:['CP1'],OE3:['CP1'],
    OE4:['CP4','CP7'],
    OE5:['CP2','CP5','CP6','CP8'],
    OE6:['CP3','CP5'],
    OE7:['CP4','CP7','CP8']
  };
  var CP_ORDER=['CP1','CP2','CP3','CP4','CP5','CP6','CP7','CP8'];
  var OE_ORDER=['OE1','OE2','OE3','OE4','OE5','OE6','OE7'];

  var EDGES=[
    ['PROB','OE1'],['PROB','OE2'],['PROB','OE3'],['PROB','OE4'],['PROB','OE5'],['PROB','OE6'],['PROB','OE7'],
    ['OE1','CP2'],['OE2','CP1'],['OE3','CP1'],['OE4','CP4'],['OE4','CP7'],
    ['OE5','CP2'],['OE5','CP5'],['OE5','CP6'],['OE5','CP8'],['OE6','CP3'],['OE6','CP5'],
    ['OE7','CP4'],['OE7','CP7'],['OE7','CP8'],
    ['CP1','RF10'],
    ['CP2','RF01'],['CP2','RF15'],['CP2','RF16'],
    ['CP3','RF02'],['CP3','RF06'],['CP3','RF07'],['CP3','RF17'],['CP3','RF18'],['CP3','RF19'],
    ['CP4','RF04'],['CP4','RF08'],['CP4','RF20'],['CP4','RF21'],['CP4','RF22'],
    ['CP5','RF09'],['CP6','RF03'],['CP6','RF05'],
    ['CP7','RF11'],['CP7','RF12'],['CP7','RF13'],['CP8','RF14'],
    ['RF01','US01'],['RF02','US02'],['RF03','US03'],['RF04','US04'],['RF05','US05'],
    ['RF06','US06'],['RF07','US07'],['RF08','US08'],['RF09','US09'],['RF10','US10'],
    ['RF11','US11'],['RF12','US12'],['RF13','US13'],['RF14','US14'],['RF15','US15'],
    ['RF16','US16'],['RF17','US17'],['RF18','US18'],['RF19','US19'],['RF20','US20'],
    ['RF21','US21'],['RF22','US22']
  ];

  var ST={
    PROB:'am',
    OE1:'vd',OE2:'vd',OE3:'vd',OE4:'vd',OE5:'am',OE6:'vd',OE7:'vd',
    CP1:'vd',CP2:'vd',CP3:'vd',CP4:'vd',CP5:'vd',CP6:'vm',CP7:'vd',CP8:'vd',
    RF01:'vd',RF02:'vd',RF03:'vm',RF04:'vd',RF05:'vm',RF06:'vd',RF07:'vd',
    RF08:'vd',RF09:'vd',RF10:'vd',RF11:'vd',RF12:'vd',RF13:'vd',RF14:'vd',
    RF15:'vd',RF16:'vd',RF17:'vd',RF18:'vd',RF19:'vd',RF20:'vd',RF21:'vd',RF22:'vd',
    US01:'vd',US02:'vd',US03:'vm',US04:'vd',US05:'vm',US06:'vd',US07:'vd',
    US08:'vd',US09:'vd',US10:'vd',US11:'vd',US12:'vd',US13:'vd',US14:'vd',
    US15:'vd',US16:'vd',US17:'vd',US18:'vd',US19:'vd',US20:'vd',US21:'vd',US22:'vd'
  };
  var CL={
    vd:{f:'#4CAF50',s:'#388E3C',t:'#fff'},
    am:{f:'#FFC107',s:'#F9A825',t:'#333'},
    vm:{f:'#F44336',s:'#C62828',t:'#fff'}
  };
  var DESC={
    PROB:'Problema DoaNet — dados dispersos e gestão desordenada de ONGs',
    OE1:'OE1 — Aumentar a transparência financeira',OE2:'OE2 — Desburocratizar o processo de doação',
    OE3:'OE3 — Fomentar a recorrência de contribuições',OE4:'OE4 — Facilitar a captação e gestão de voluntários',
    OE5:'OE5 — Ampliar a visibilidade do impacto social',OE6:'OE6 — Impulsionar o engajamento contínuo da comunidade',
    OE7:'OE7 — Otimizar acesso a informação',
    CP1:'CP1 — Gestão de doações',CP2:'CP2 — Painel de transparência financeira',
    CP3:'CP3 — Feed de comunicação',CP4:'CP4 — Gestão de voluntários',
    CP5:'CP5 — Gestão de eventos',CP6:'CP6 — Perfil público da organização',
    CP7:'CP7 — Controle de acesso administrativo',CP8:'CP8 — Customização da organização',
    RF01:'RF01 — Visualizar histórico de doações e despesas',RF02:'RF02 — Visualizar publicações no feed',
    RF03:'RF03 — Visualizar descrição da organização',RF04:'RF04 — Visualizar oportunidades de voluntariado',
    RF05:'RF05 — Contactar administradores da organização',RF06:'RF06 — Filtrar o feed por tipo de publicação',
    RF07:'RF07 — Buscar publicação no feed por título',RF08:'RF08 — Inscrever-se como voluntário',
    RF09:'RF09 — Inscrever-se em evento',RF10:'RF10 — Realizar doação',
    RF11:'RF11 — Autenticar administradores',RF12:'RF12 — Cadastrar administrador da organização',
    RF13:'RF13 — Remover administrador da organização',RF14:'RF14 — Configurar dados de customização',
    RF15:'RF15 — Lançar doação externa ao aplicativo',RF16:'RF16 — Lançar despesa da organização',
    RF17:'RF17 — Publicar no feed',RF18:'RF18 — Deletar publicação no feed',
    RF19:'RF19 — Atualizar publicação no feed',RF20:'RF20 — Registrar oportunidade de voluntariado',
    RF21:'RF21 — Deletar oportunidade de voluntariado',RF22:'RF22 — Atualizar oportunidade de voluntariado',
    US01:'US01 — Visualizar histórico financeiro',US02:'US02 — Visualizar publicações no feed',
    US03:'US03 — Visualizar descrição da ONG',US04:'US04 — Visualizar oportunidades de voluntariado',
    US05:'US05 — Contactar a organização',US06:'US06 — Filtrar o feed por tipo de publicação',
    US07:'US07 — Buscar publicação no feed por título',US08:'US08 — Inscrever-se como voluntário',
    US09:'US09 — Inscrever-se em evento',US10:'US10 — Realizar doação',
    US11:'US11 — Autenticar administradores',US12:'US12 — Cadastrar administrador de organização',
    US13:'US13 — Remover administrador de organização',US14:'US14 — Configurar dados institucionais',
    US15:'US15 — Lançar doações manuais',US16:'US16 — Lançar despesas operacionais',
    US17:'US17 — Criar publicação no feed',US18:'US18 — Deletar publicação no feed',
    US19:'US19 — Atualizar publicação no feed',US20:'US20 — Registrar oportunidade de voluntariado',
    US21:'US21 — Deletar oportunidade de voluntariado',US22:'US22 — Atualizar oportunidade de voluntariado'
  };

  var LINKS={
    PROB:'../../visao_produto/1-cenario/',
    OE1:'../../visao_produto/2-solucao/#oe1',OE2:'../../visao_produto/2-solucao/#oe2',OE3:'../../visao_produto/2-solucao/#oe3',
    OE4:'../../visao_produto/2-solucao/#oe4',OE5:'../../visao_produto/2-solucao/#oe5',OE6:'../../visao_produto/2-solucao/#oe6',OE7:'../../visao_produto/2-solucao/#oe7',
    CP1:'../../visao_produto/2-solucao/#cp1',CP2:'../../visao_produto/2-solucao/#cp2',CP3:'../../visao_produto/2-solucao/#cp3',
    CP4:'../../visao_produto/2-solucao/#cp4',CP5:'../../visao_produto/2-solucao/#cp5',CP6:'../../visao_produto/2-solucao/#cp6',
    CP7:'../../visao_produto/2-solucao/#cp7',CP8:'../../visao_produto/2-solucao/#cp8',
    RF01:'../../visao_produto/8-requisitos/#rf01',RF02:'../../visao_produto/8-requisitos/#rf02',RF03:'../../visao_produto/8-requisitos/#rf03',
    RF04:'../../visao_produto/8-requisitos/#rf04',RF05:'../../visao_produto/8-requisitos/#rf05',RF06:'../../visao_produto/8-requisitos/#rf06',
    RF07:'../../visao_produto/8-requisitos/#rf07',RF08:'../../visao_produto/8-requisitos/#rf08',RF09:'../../visao_produto/8-requisitos/#rf09',
    RF10:'../../visao_produto/8-requisitos/#rf10',RF11:'../../visao_produto/8-requisitos/#rf11',RF12:'../../visao_produto/8-requisitos/#rf12',
    RF13:'../../visao_produto/8-requisitos/#rf13',RF14:'../../visao_produto/8-requisitos/#rf14',RF15:'../../visao_produto/8-requisitos/#rf15',
    RF16:'../../visao_produto/8-requisitos/#rf16',RF17:'../../visao_produto/8-requisitos/#rf17',RF18:'../../visao_produto/8-requisitos/#rf18',
    RF19:'../../visao_produto/8-requisitos/#rf19',RF20:'../../visao_produto/8-requisitos/#rf20',RF21:'../../visao_produto/8-requisitos/#rf21',
    RF22:'../../visao_produto/8-requisitos/#rf22',
    US01:'../planejamento/sprint-6/user-stories/#us01', US02:'../planejamento/sprint-2/user-stories/#us02',
    US03:'../planejamento/observacoes-gerais/#us03', US04:'../planejamento/sprint-4/user-stories/#us04',
    US05:'../planejamento/observacoes-gerais/#us05', US06:'../planejamento/sprint-5/user-stories/#us06',
    US07:'../planejamento/sprint-5/user-stories/#us07', US08:'../planejamento/sprint-4/user-stories/#us08',
    US09:'../planejamento/sprint-3/user-stories/#us09', US10:'../planejamento/sprint-5/user-stories/#us10',
    US11:'../planejamento/sprint-3/user-stories/#us11', US12:'../planejamento/sprint-6/user-stories/#us12',
    US13:'../planejamento/sprint-6/user-stories/#us13', US14:'../planejamento/sprint-6/user-stories/#us14',
    US15:'../planejamento/sprint-5/user-stories/#us15', US16:'../planejamento/sprint-5/user-stories/#us16',
    US17:'../planejamento/sprint-2/user-stories/#us17', US18:'../planejamento/sprint-2/user-stories/#us18',
    US19:'../planejamento/sprint-2/user-stories/#us19', US20:'../planejamento/sprint-4/user-stories/#us20',
    US21:'../planejamento/sprint-4/user-stories/#us21', US22:'../planejamento/sprint-4/user-stories/#us22'
  };

  /* ── LAYOUT (bottom-up): RF grouped by CP, US directly below RF ── */
  var cpX={}, rfX={}, cx=PAD;
  CP_ORDER.forEach(function(cp){
    var rfs=CP_RF[cp], gw=(rfs.length-1)*SP;
    rfs.forEach(function(rf,i){rfX[rf]=cx+i*SP;});
    cpX[cp]=cx+gw/2;
    cx+=gw+GRP_GAP;
  });
  var W=cx-GRP_GAP+PAD;

  var oeIdeal={};
  OE_ORDER.forEach(function(oe){
    var cps=OE_CP[oe];
    oeIdeal[oe]=cps.reduce(function(s,c){return s+cpX[c];},0)/cps.length;
  });
  var sortedOEs=OE_ORDER.slice().sort(function(a,b){return oeIdeal[a]-oeIdeal[b];});
  var oeX={};
  sortedOEs.forEach(function(oe){oeX[oe]=oeIdeal[oe];});
  var j;
  for(j=1;j<sortedOEs.length;j++){
    var pr=sortedOEs[j-1],cu=sortedOEs[j];
    if(oeX[cu]<oeX[pr]+OE_MIN) oeX[cu]=oeX[pr]+OE_MIN;
  }
  for(j=sortedOEs.length-2;j>=0;j--){
    var cu2=sortedOEs[j],nx=sortedOEs[j+1];
    if(oeX[cu2]>oeX[nx]-OE_MIN) oeX[cu2]=oeX[nx]-OE_MIN;
  }

  var pos={};
  pos['PROB']={x:W/2,y:LY[0]};
  OE_ORDER.forEach(function(oe){pos[oe]={x:oeX[oe],y:LY[1]};});
  CP_ORDER.forEach(function(cp){pos[cp]={x:cpX[cp],y:LY[2]};});
  CP_ORDER.forEach(function(cp){
    CP_RF[cp].forEach(function(rf){pos[rf]={x:rfX[rf],y:LY[3]};});
  });
  CP_ORDER.forEach(function(cp){
    CP_RF[cp].forEach(function(rf){
      var us=RF_US[rf]; pos[us]={x:rfX[rf],y:LY[4]};
    });
  });

  /* ── BUILD SVG ── */
  var NS='http://www.w3.org/2000/svg';
  var svg=document.getElementById('tz-svg');
  var wrap=document.getElementById('tz-wrap');
  var tip=document.getElementById('tz-tip');
  /* O SVG preenche o contêiner (100%/100%) — dimensões fixas aqui fariam o
     desenho ser recortado na borda do próprio SVG durante zoom/pan. */

  var g=document.createElementNS(NS,'g');
  svg.appendChild(g);

  var didDrag=false;

  /* ── EDGES ── */
  EDGES.forEach(function(e){
    var p1=pos[e[0]], p2=pos[e[1]];
    var dx=p2.x-p1.x, dy=p2.y-p1.y, d=Math.sqrt(dx*dx+dy*dy);
    var ln=document.createElementNS(NS,'line');
    ln.setAttribute('x1',p1.x+dx/d*R); ln.setAttribute('y1',p1.y+dy/d*R);
    ln.setAttribute('x2',p2.x-dx/d*R); ln.setAttribute('y2',p2.y-dy/d*R);
    ln.setAttribute('stroke','#888'); ln.setAttribute('stroke-width','1.4');
    ln.setAttribute('opacity','0.5');
    g.appendChild(ln);
  });

  /* ── NODES ── */
  Object.keys(pos).forEach(function(id){
    var p=pos[id], c=CL[ST[id]];
    var grp=document.createElementNS(NS,'g');

    var ci=document.createElementNS(NS,'circle');
    ci.setAttribute('cx',p.x); ci.setAttribute('cy',p.y); ci.setAttribute('r',R);
    ci.setAttribute('fill',c.f); ci.setAttribute('stroke',c.s); ci.setAttribute('stroke-width','2.2');
    ci.style.cursor='pointer';

    var tx=document.createElementNS(NS,'text');
    tx.setAttribute('x',p.x); tx.setAttribute('y',p.y);
    tx.setAttribute('text-anchor','middle'); tx.setAttribute('dominant-baseline','middle');
    tx.setAttribute('fill',c.t); tx.setAttribute('font-size','9');
    tx.setAttribute('font-weight','bold'); tx.setAttribute('font-family','monospace');
    tx.style.cursor='pointer';
    tx.textContent=id;

    grp.addEventListener('mouseenter',function(){
      ci.setAttribute('r',R+3); ci.setAttribute('stroke-width','3');
      tx.setAttribute('text-decoration','underline');
      tip.innerHTML=DESC[id]+'<br><span style="font-size:11px;opacity:0.6;font-style:italic;">Clique no texto para abrir documentação</span>';
      tip.style.display='block';
    });
    grp.addEventListener('mousemove',function(ev){
      var br=wrap.getBoundingClientRect();
      var lx=ev.clientX-br.left+14, ly=ev.clientY-br.top-60;
      if(lx+345>br.width) lx=lx-360;
      tip.style.left=lx+'px'; tip.style.top=ly+'px';
    });
    grp.addEventListener('mouseleave',function(){
      ci.setAttribute('r',R); ci.setAttribute('stroke-width','2.2');
      tx.setAttribute('text-decoration','none');
      tip.style.display='none';
    });

    tx.addEventListener('click',function(e){
      if(didDrag) return;
      window.open(LINKS[id],'_blank','noopener');
    });

    grp.appendChild(ci);
    grp.appendChild(tx);
    g.appendChild(grp);
  });

  /* ── ZOOM / PAN ── */
  var cw=wrap.clientWidth||820, ch=wrap.clientHeight||640;
  var CH=LY[LY.length-1]+R+PAD; /* altura real do conteúdo (última linha + raio + margem) */
  var sc=Math.min((cw-16)/W,(ch-16)/CH,1);
  var tx0=(cw-W*sc)/2, ty0=Math.max((ch-CH*sc)/2,8);
  var scale=sc, txn=tx0, tyn=ty0, isDragging=false, sx,sy,stx,sty;

  function applyT(){g.setAttribute('transform','translate('+txn+','+tyn+') scale('+scale+')');}
  applyT();

  wrap.addEventListener('wheel',function(ev){
    ev.preventDefault();
    var br=wrap.getBoundingClientRect();
    var mx=ev.clientX-br.left, my=ev.clientY-br.top;
    var ns=Math.min(Math.max(scale*(ev.deltaY<0?1.12:0.89),0.2),4);
    txn=mx-(mx-txn)*(ns/scale); tyn=my-(my-tyn)*(ns/scale); scale=ns; applyT();
  },{passive:false});

  wrap.addEventListener('mousedown',function(ev){
    isDragging=true; didDrag=false;
    sx=ev.clientX; sy=ev.clientY; stx=txn; sty=tyn;
    wrap.style.cursor='grabbing';
  });
  document.addEventListener('mousemove',function(ev){
    if(!isDragging) return;
    if(Math.abs(ev.clientX-sx)>3||Math.abs(ev.clientY-sy)>3) didDrag=true;
    txn=stx+(ev.clientX-sx); tyn=sty+(ev.clientY-sy); applyT();
  });
  document.addEventListener('mouseup',function(){isDragging=false; wrap.style.cursor='grab';});

  document.getElementById('tz-in').addEventListener('click',function(){scale=Math.min(scale*1.2,4);txn=(cw-W*scale)/2;tyn=Math.max((ch-CH*scale)/2,8);applyT();});
  document.getElementById('tz-out').addEventListener('click',function(){scale=Math.max(scale*0.8,0.2);txn=(cw-W*scale)/2;tyn=Math.max((ch-CH*scale)/2,8);applyT();});
  document.getElementById('tz-reset').addEventListener('click',function(){scale=sc;txn=tx0;tyn=ty0;applyT();});
})();
</script>

| Cor | Status |
| :---: | :--- |
| 🟢 Verde | **Totalmente concluído** — entregue e validado com o cliente |
| 🟡 Amarelo | **Parcialmente concluído** — entregue com débito técnico ou dependente de itens incompletos |
| 🔴 Vermelho | **Não iniciado** — previsto em sprint futura ou em andamento sem entrega confirmada |

