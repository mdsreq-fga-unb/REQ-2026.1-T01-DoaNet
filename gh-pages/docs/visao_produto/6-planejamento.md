# Planejamento da Equipe

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
    <svg id="tz-svg" xmlns="http://www.w3.org/2000/svg" style="display:block;"></svg>
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
    OE1:'am',OE2:'vd',OE3:'vd',OE4:'am',OE5:'am',OE6:'am',OE7:'am',
    CP1:'vd',CP2:'am',CP3:'am',CP4:'am',CP5:'vd',CP6:'vm',CP7:'am',CP8:'vm',
    RF01:'vm',RF02:'vd',RF03:'vm',RF04:'vd',RF05:'vm',RF06:'am',RF07:'am',
    RF08:'am',RF09:'vd',RF10:'vd',RF11:'vd',RF12:'vm',RF13:'vm',RF14:'vm',
    RF15:'vd',RF16:'vd',RF17:'vd',RF18:'vd',RF19:'vd',RF20:'vd',RF21:'vd',RF22:'vd',
    US01:'vm',US02:'vd',US03:'vm',US04:'vd',US05:'vm',US06:'am',US07:'am',
    US08:'am',US09:'vd',US10:'vd',US11:'vd',US12:'vm',US13:'vm',US14:'vm',
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
    RF05:'RF05 — Contactar administradores da organização',RF06:'RF06 — Filtrar feed por categoria',
    RF07:'RF07 — Buscar publicação pelo título',RF08:'RF08 — Inscrever-se como voluntário',
    RF09:'RF09 — Inscrever-se em evento',RF10:'RF10 — Realizar doação',
    RF11:'RF11 — Autenticar administradores',RF12:'RF12 — Cadastrar administrador da organização',
    RF13:'RF13 — Remover administrador da organização',RF14:'RF14 — Configurar dados de customização',
    RF15:'RF15 — Lançar doação externa ao aplicativo',RF16:'RF16 — Lançar despesa da organização',
    RF17:'RF17 — Publicar no feed',RF18:'RF18 — Deletar publicação no feed',
    RF19:'RF19 — Atualizar publicação no feed',RF20:'RF20 — Registrar oportunidade de voluntariado',
    RF21:'RF21 — Deletar oportunidade de voluntariado',RF22:'RF22 — Atualizar oportunidade de voluntariado',
    US01:'US01 — Visualizar histórico financeiro',US02:'US02 — Visualizar publicações no feed',
    US03:'US03 — Visualizar descrição da ONG',US04:'US04 — Visualizar oportunidades de voluntariado',
    US05:'US05 — Contactar a organização',US06:'US06 — Filtrar publicações do feed',
    US07:'US07 — Buscar publicações por título',US08:'US08 — Inscrever-se como voluntário',
    US09:'US09 — Inscrever-se em evento',US10:'US10 — Realizar doação',
    US11:'US11 — Autenticar administradores',US12:'US12 — Cadastrar administrador de organização',
    US13:'US13 — Remover administrador de organização',US14:'US14 — Configurar dados institucionais',
    US15:'US15 — Lançar doações manuais',US16:'US16 — Lançar despesas operacionais',
    US17:'US17 — Criar publicação no feed',US18:'US18 — Deletar publicação no feed',
    US19:'US19 — Atualizar publicação no feed',US20:'US20 — Registrar oportunidade de voluntariado',
    US21:'US21 — Deletar oportunidade de voluntariado',US22:'US22 — Atualizar oportunidade de voluntariado'
  };

  var LINKS={
    PROB:'../1-cenario/',
    OE1:'../2-solucao/#oe1',OE2:'../2-solucao/#oe2',OE3:'../2-solucao/#oe3',
    OE4:'../2-solucao/#oe4',OE5:'../2-solucao/#oe5',OE6:'../2-solucao/#oe6',OE7:'../2-solucao/#oe7',
    CP1:'../2-solucao/#cp1',CP2:'../2-solucao/#cp2',CP3:'../2-solucao/#cp3',
    CP4:'../2-solucao/#cp4',CP5:'../2-solucao/#cp5',CP6:'../2-solucao/#cp6',
    CP7:'../2-solucao/#cp7',CP8:'../2-solucao/#cp8',
    RF01:'../8-requisitos/#rf01',RF02:'../8-requisitos/#rf02',RF03:'../8-requisitos/#rf03',
    RF04:'../8-requisitos/#rf04',RF05:'../8-requisitos/#rf05',RF06:'../8-requisitos/#rf06',
    RF07:'../8-requisitos/#rf07',RF08:'../8-requisitos/#rf08',RF09:'../8-requisitos/#rf09',
    RF10:'../8-requisitos/#rf10',RF11:'../8-requisitos/#rf11',RF12:'../8-requisitos/#rf12',
    RF13:'../8-requisitos/#rf13',RF14:'../8-requisitos/#rf14',RF15:'../8-requisitos/#rf15',
    RF16:'../8-requisitos/#rf16',RF17:'../8-requisitos/#rf17',RF18:'../8-requisitos/#rf18',
    RF19:'../8-requisitos/#rf19',RF20:'../8-requisitos/#rf20',RF21:'../8-requisitos/#rf21',
    RF22:'../8-requisitos/#rf22',
    US01:'../../evidencias/sprint6/#us01',US02:'../../evidencias/sprint2/#us02',
    US03:'../../evidencias/sprint6/#us03',US04:'../../evidencias/sprint4/#us04',
    US05:'../../evidencias/sprint6/#us05',US06:'../../evidencias/sprint5/#us06',
    US07:'../../evidencias/sprint5/#us07',US08:'../../evidencias/sprint4/#us08',
    US09:'../../evidencias/sprint3/#us09',US10:'../../evidencias/sprint5/#us10',
    US11:'../../evidencias/sprint3/#us11',US12:'../../evidencias/sprint6/#us12',
    US13:'../../evidencias/sprint6/#us13',US14:'../../evidencias/sprint6/#us14',
    US15:'../../evidencias/sprint5/#us15',US16:'../../evidencias/sprint5/#us16',
    US17:'../../evidencias/sprint2/#us17',US18:'../../evidencias/sprint2/#us18',
    US19:'../../evidencias/sprint2/#us19',US20:'../../evidencias/sprint4/#us20',
    US21:'../../evidencias/sprint4/#us21',US22:'../../evidencias/sprint4/#us22'
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
  svg.setAttribute('width',W); svg.setAttribute('height',H);

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
  var cw=wrap.clientWidth||820;
  var sc=Math.min((cw-16)/W,1), tx0=(cw-W*sc)/2, ty0=8;
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

  document.getElementById('tz-in').addEventListener('click',function(){scale=Math.min(scale*1.2,4);txn=(cw-W*scale)/2;tyn=8;applyT();});
  document.getElementById('tz-out').addEventListener('click',function(){scale=Math.max(scale*0.8,0.2);txn=(cw-W*scale)/2;tyn=8;applyT();});
  document.getElementById('tz-reset').addEventListener('click',function(){scale=sc;txn=tx0;tyn=ty0;applyT();});
})();
</script>

| Cor | Status |
| :---: | :--- |
| 🟢 Verde | **Totalmente concluído** — entregue e validado com o cliente |
| 🟡 Amarelo | **Parcialmente concluído** — entregue com débito técnico ou dependente de itens incompletos |
| 🔴 Vermelho | **Não iniciado** — previsto em sprint futura ou em andamento sem entrega confirmada |

---

## Planejamento de Sprints

---

### Sprint 0 — Definição do Projeto

**Período:** 31/03/2026 – 14/04/2026  
**Status:** ✅ Concluída

**Objetivos:**

- Definição do projeto e do problema a resolver
- Levantamento das necessidades iniciais junto ao cliente
- Definição da arquitetura e stack tecnológica inicial

**User Stories:**

- Nenhuma US funcional nesta sprint — foco em entendimento do domínio e estruturação do projeto.

**Engenharia de Requisitos — Técnicas Aplicadas:**

- **Elicitação e Descoberta:** Entrevistas com o cliente (Paulo) para levantamento das necessidades reais das ONGs; brainstorming interno de domínio para entendimento do contexto do terceiro setor.
- **Análise e Consenso:** Definição do problema central e alinhamento sobre o escopo inicial da solução com o cliente; identificação dos perfis de usuário (apoiador, voluntário, administrador).
- **Representação de Requisitos:** Definição da arquitetura inicial do sistema e dos módulos principais (feed, transparência, colaboração); seleção da stack tecnológica de partida.

---

### Sprint 1 — Prototipagem e Story Map

**Período:** 14/04/2026 – 28/04/2026  
**Status:** ✅ Concluída

**Objetivos:**

- Elaboração do protótipo de baixa fidelidade no Figma
- Construção e validação do User Story Map

**User Stories:**

- Nenhuma US funcional nesta sprint — foco em representação de requisitos e validação de escopo com o cliente.

**Engenharia de Requisitos — Técnicas Aplicadas:**

- **Declaração de Requisitos:** US01–US22 escritas, refinadas e formalizadas com personas, objetivos e critérios de aceite.
- **Representação de Requisitos:** User Story Map (USM) construído como representação visual e estruturada do escopo completo, organizando as histórias por jornada do usuário e prioridade de entrega; protótipo de baixa fidelidade no Figma cobrindo os fluxos das três abas principais.
- **Análise e Consenso:** Priorização Valor × Esforço aplicada com a cliente para definição do escopo do MVP.
- **Validação de Requisitos:** USM e protótipo apresentados ao cliente em 27/04 — aprovação formal registrada em reunião com o stakeholder.

---

### Sprint 2 — Feed: CRUD de Postagens Normais

**Período:** 28/04/2026 – 12/05/2026  
**Status:** ✅ Concluída

**Objetivo:** Implementar as funcionalidades centrais do feed com criação, edição e deleção de postagens normais.

**User Stories:**

- [US17 - Criar publicação no feed](../evidencias/sprint2.md#us17) — Criar publicação no feed (post normal)
- [US18 - Deletar publicação no feed](../evidencias/sprint2.md#us18)
- [US19 - Atualizar publicação no feed](../evidencias/sprint2.md#us19)

**Engenharia de Requisitos — Técnicas Aplicadas:**

- **Verificação de Requisitos (INVEST):** Critérios INVEST aplicados no Sprint Planning para confirmar prontidão das histórias antes do início do desenvolvimento.
- **Critérios de Aceite:** Verificação formal dos critérios de US17, US18 e US19 na revisão da sprint.
- **Organização e Atualização do Backlog:** Escopo redefinido após pivoteamento (nova stack: FastAPI + MongoDB + Flutter + Streamlit); refinamento do USM realizado na semana intermediária da sprint.
- **Validação de Requisitos:** Feed com CRUD de posts demonstrado ao cliente em 12/05 — aprovação formal do incremento pelo stakeholder.

---

### Sprint 3 — Feed Completo, Eventos e Módulo Admin

**Período:** 12/05/2026 – 26/05/2026  
**Status:** ✅ Concluída

**Objetivo:** Implementar posts de eventos com inscrição, suporte a imagens em todos os tipos de post e iniciar o módulo de administração.

**User Stories:**

- [US17 - Criar publicação no feed](../evidencias/sprint2.md#us17) — Criar publicação no feed (evento)
- [US09 - Inscrever-se em evento](../evidencias/sprint3.md#us09)
- [US11 - Autenticar administradores](../evidencias/sprint3.md#us11)

**Engenharia de Requisitos — Técnicas Aplicadas:**

- **Verificação de Requisitos (INVEST):** Critérios INVEST aplicados no Sprint Planning para as três histórias da sprint.
- **Critérios de Aceite:** Verificação formal dos critérios de US17 (evento), US09 e US11 na revisão da sprint.
- **Organização e Atualização do Backlog:** Backlog atualizado com encaminhamentos da revisão da Sprint 2; refinamento do USM realizado na semana intermediária da sprint.
- **Validação de Requisitos:** Feed completo (posts normais + eventos), inscrição e módulo de autenticação admin demonstrados ao cliente em 26/05; protótipo final aprovado como referência para as próximas entregas.

---

### Sprint 4 — Colaboração: Voluntariado e Painel Admin

**Período:** 26/05/2026 – 09/06/2026  
**Status:** ⚠️ Concluída com débito técnico

**Objetivo:** Implementar o módulo de voluntariado (CRUD e inscrição) e expandir o painel de administração.

**User Stories:**

- [US04 - Visualizar oportunidades de voluntariado](../evidencias/sprint4.md#us04)
- [US08 - Inscrever-se como voluntário](../evidencias/sprint4.md#us08) *(débito técnico: formulário parcialmente implementado)*
- [US20 - Registrar oportunidade de voluntariado](../evidencias/sprint4.md#us20) (admin)
- [US21 - Deletar oportunidade de voluntariado](../evidencias/sprint4.md#us21) (admin)
- [US22 - Atualizar oportunidade de voluntariado](../evidencias/sprint4.md#us22) (admin)

**Engenharia de Requisitos — Técnicas Aplicadas:**

- **Verificação de Requisitos (INVEST):** Critérios INVEST aplicados no Sprint Planning para as cinco histórias da sprint.
- **Critérios de Aceite:** Verificação formal dos critérios de US04, US08, US20, US21 e US22 na revisão da sprint; débito técnico identificado no formulário de inscrição de US08.
- **Organização e Atualização do Backlog:** Backlog atualizado com encaminhamentos da revisão da Sprint 3; débito técnico formalizado e encaminhado para a sprint seguinte.
- **Validação de Requisitos:** Módulo de voluntariado (CRUD) e painel admin demonstrados ao cliente em 09/06 — aprovação formal do incremento e registro do débito técnico.

---

### Sprint 5 — Doações e Rastreabilidade

**Período:** 09/06/2026 – 23/06/2026  
**Status:** ✅ Concluída

**Objetivo:** Implementar o fluxo de doações no aplicativo, rastreabilidade e registro inicial no painel de transparência.

**User Stories:**

- [US06 - Filtrar publicações do feed](../evidencias/sprint5.md#us06)
- [US07 - Buscar publicações por título](../evidencias/sprint5.md#us07)
- [US10 - Realizar doação](../evidencias/sprint5.md#us10)
- [US15 - Lançar doações manuais](../evidencias/sprint5.md#us15)
- [US16 - Lançar despesas operacionais](../evidencias/sprint5.md#us16)

**Engenharia de Requisitos — Técnicas Aplicadas:**

- **Verificação de Requisitos (INVEST):** Critérios INVEST aplicados no Sprint Planning para as cinco histórias da sprint (US06, US07, US10, US15, US16).
- **Critérios de Aceite:** Verificação formal dos critérios de US06, US07, US10, US15 e US16 na revisão da sprint.
- **Organização e Atualização do Backlog:** Backlog atualizado com encaminhamentos da revisão da Sprint 4, incluindo o débito técnico herdado de US08; escopo refinado para histórias de filtro, busca, doação e transparência financeira.
- **Validação de Requisitos:** Funcionalidades de filtro, busca, doação e lançamento de registros de transparência demonstradas ao cliente ao final da sprint.

---

### Sprint 6 — Transparência, Admin e Customização

**Período:** 23/06/2026 – 07/07/2026  
**Status:** 🔄 Em andamento

**Objetivo:** Finalizar o painel de transparência, o painel de admin e a customização da organização, com a aba de descrição e contato funcionando.

**User Stories:**

- [US01 - Visualizar histórico financeiro](../evidencias/sprint6.md#us01)
- [US03 - Visualizar descrição da ONG](../evidencias/sprint6.md#us03)
- [US05 - Contactar a organização](../evidencias/sprint6.md#us05)
- [US12 - Cadastrar administrador de organização](../evidencias/sprint6.md#us12)
- [US13 - Remover administrador de organização](../evidencias/sprint6.md#us13)
- [US14 - Configurar dados institucionais](../evidencias/sprint6.md#us14)

**Engenharia de Requisitos — Técnicas Aplicadas:**

- **Verificação de Requisitos (INVEST):** Critérios INVEST aplicados no Sprint Planning para as seis histórias da sprint (US01, US03, US05, US12, US13, US14).
- **Critérios de Aceite:** Verificação formal dos critérios de US01, US03, US05, US12, US13 e US14 a ser concluída na revisão da sprint.
- **Organização e Atualização do Backlog:** Backlog ajustado com base nos encaminhamentos da Sprint 5; escopo da sprint contempla o fechamento das funcionalidades de transparência, perfil da organização e gestão administrativa.
- **Validação de Requisitos:** Painel de transparência, tela de descrição e contato, e gestão de administradores a serem demonstrados ao cliente ao final da sprint.

---

## **Considerações Importantes**

1. **Datas de Início e Fim:** O projeto é composto por uma Sprint 0 de definição e seis sprints de desenvolvimento, cada uma com duração de duas semanas. O ciclo inicia em **31/03/2026** com a Sprint 0 e finaliza em **07/07/2026**, com entregas incrementais ao longo do período.

2. **Validações ao Final de Cada Sprint:** Ao término de cada sprint, será realizada uma reunião com o cliente para validação das funcionalidades entregues, coleta de feedback e ajustes no backlog, garantindo alinhamento contínuo com os objetivos do projeto.

3. **Entregas Parciais:** O projeto contará com entregas parciais nas datas **26/05**, **23/06** e a entrega final em **07/07**, com o objetivo de promover a validação progressiva das principais funcionalidades da solução, como feed, colaboração e transparência.

---
