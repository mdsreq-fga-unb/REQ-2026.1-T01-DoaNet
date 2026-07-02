# 9 MVP

## 9.1 Priorização do User Story Map e MVP

> 🗺️ O mapa interativo completo está disponível em [User Story Map](../organização-e-planejamento/user-story-map.md).

Para a priorização foram utilizados os seguintes critérios:

- **VN** = Valor de negócio (1 a 5)

    - **O que significa:** O impacto positivo que a funcionalidade traz para a organização (ONG) ou para o usuário final. Mede o quanto aquela entrega resolve uma dor real, gera engajamento, traz segurança jurídica/financeira ou atende ao objetivo central do aplicativo.

    - **Como mensurar:**

        - **1 a 2 (Baixo):** Recursos cosméticos, relatórios secundários ou funções que poucos usuários vão usar.

        - **3 (Médio):** Funcionalidades de suporte importantes, mas que não impedem a operação principal se estiverem    ausentes.

        - **4 a 5 (Alto):** Funcionalidades críticas e core do sistema (Ex: Autenticação de admins, realização de doações,    transparência financeira). Sem elas, o produto perde o propósito.

- **CT** = Complexidade técnica (1 a 5)

    - **O que significa:** O nível de dificuldade intelectual, incerteza, novidade ou risco envolvido no desenvolvimento da história. Avalia se a equipe já sabe como fazer ou se exigirá muita pesquisa, integrações com terceiros (APIs externas) ou arquiteturas robustas.

    - **Como mensurar:**

        - **1 a 2 (Baixo):** Telas estáticas, cadastros simples (CRUDs) e comportamentos que a equipe já domina amplamente.

        - **3 (Médio):** Regras de negócio moderadas, filtros dinâmicos ou consultas que exigem maior atenção na modelagem.

        - **4 a 5 (Alto):** Recursos que envolvem criptografia, gateway de pagamento externo, regras de White Label dinâmicas ou alta exigência de segurança e performance.

- **EI** = Esforço de implementação (1 a 5)

    - **O que significa:** O volume de trabalho bruto e o tempo necessário para codificar, testar e homologar a funcionalidade. Uma tarefa pode ser conceitualmente simples (baixa complexidade), mas muito repetitiva ou longa (alto esforço).

    - **Como mensurar:**

        - **1 a 2 (Baixo):** Alterações rápidas, mensagens de erro, criação de botões ou fluxos de cliques curtos.

        - **3 (Médio):** Desenvolvimento padrão que consome alguns dias de trabalho de um desenvolvedor focado.

        - **4 a 5 (Alto):** Fluxos longos que exigem muitas telas, validações extensas de dados, e cenários complexos de testes manuais ou automatizados.


### 1. Esforço Técnico

Para metrificar o esforço técnico como um todo, utilizamos:

**ET = (CT + EI)/2**

Escala continua de 1 a 5.

### 2. Indice de prioridade

Para calcular o indice de prioridade:

**IP = VN / ET**

Quanto maior for o valor do IP, maior a prioridade.

Sendo:

- **IP Alto** = alto valor de negócio para baixo custo técnico
- **IP Médio** = Equilibrio entre valor de negócio e custo técnico
- **IP Baixo** = pouco valor de negócio para alto custo técnico

A partir dessas informações, foi gerada a seguinte tabela:

<style>
.usmap-table{border-collapse:collapse;width:100%;font-family:-apple-system,Segoe UI,Roboto,sans-serif;font-size:13px;border-radius:8px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,0.12);}
.usmap-table thead tr{background:#1f2937;color:#fff;}
.usmap-table th{padding:8px 6px;text-align:center;font-weight:600;}
.usmap-table td{padding:6px;text-align:center;border-bottom:1px solid #e5e7eb;}
.usmap-table tbody tr:nth-child(even){background:#f9fafb;}
.usmap-table tbody tr:hover{background:#eef2ff;}
.usmap-table a{color:#4f46e5;text-decoration:none;font-weight:600;}
.usmap-table a:hover{text-decoration:underline;}
.badge{display:inline-block;padding:2px 8px;border-radius:12px;font-size:11px;font-weight:700;color:#fff;}
.q1{background:#16a34a;}
.q2{background:#2563eb;}
.q3{background:#eab308;color:#1f2937;}
.q4{background:#f22824;}
.mvp-yes{color:#16a34a;font-weight:700;}
.mvp-no{color:#d1d5db;}
.legend{margin-top:12px;font-family:-apple-system,Segoe UI,Roboto,sans-serif;font-size:13px;border:1px solid #e5e7eb;border-radius:8px;padding:12px 16px;background:#fafafa;}
.legend-title{font-weight:700;margin-bottom:8px;color:#1f2937;}
.legend-item{display:flex;align-items:center;gap:8px;margin-bottom:6px;}
.legend-item:last-child{margin-bottom:0;}
</style>

<table class="usmap-table">
<thead>
<tr>
<th>US</th><th>VN</th><th>CT</th><th>EI</th><th>ET</th><th>IP</th><th>Quad.</th><th>Prior.</th><th>MVP</th>
</tr>
</thead>
<tbody>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-3/user-stories/#us11">US11</a></td><td>5</td><td>2</td><td>2</td><td>2</td><td>2,5</td><td><span class="badge q1" title="Alto valor / Baixa carga técnica">Q1</span></td><td>1</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-6/user-stories/#us01">US01</a></td><td>5</td><td>2</td><td>2</td><td>2</td><td>2,5</td><td><span class="badge q1" title="Alto valor / Baixa carga técnica">Q1</span></td><td>1</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-2/user-stories/#us02">US02</a></td><td>5</td><td>2</td><td>2</td><td>2</td><td>2,5</td><td><span class="badge q1" title="Alto valor / Baixa carga técnica">Q1</span></td><td>1</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-5/user-stories/#us10">US10</a></td><td>5</td><td>2</td><td>2</td><td>2</td><td>2,5</td><td><span class="badge q1" title="Alto valor / Baixa carga técnica">Q1</span></td><td>1</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-6/user-stories/#us14">US14</a></td><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td><span class="badge q1" title="Alto valor / Baixa carga técnica">Q1</span></td><td>1</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-5/user-stories/#us15">US15</a></td><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td><span class="badge q1" title="Alto valor / Baixa carga técnica">Q1</span></td><td>1</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-2/user-stories/#us17">US17</a></td><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td><span class="badge q1" title="Alto valor / Baixa carga técnica">Q1</span></td><td>1</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-6/user-stories/#us12">US12</a></td><td>5</td><td>4</td><td>4</td><td>4</td><td>1,25</td><td><span class="badge q2" title="Alto valor / Alta carga técnica">Q2</span></td><td>2</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-6/user-stories/#us13">US13</a></td><td>4</td><td>4</td><td>4</td><td>4</td><td>1</td><td><span class="badge q2" title="Alto valor / Alta carga técnica">Q2</span></td><td>2</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/observacoes-gerais/#us03">US03</a></td><td>3</td><td>1</td><td>1</td><td>1</td><td>3</td><td><span class="badge q3" title="Baixo valor / Baixa carga técnica">Q3</span></td><td>3</td><td class="mvp-no">—</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-4/user-stories/#us08">US08</a></td><td>3</td><td>2</td><td>2</td><td>2</td><td>1,5</td><td><span class="badge q3" title="Baixo valor / Baixa carga técnica">Q3</span></td><td>3</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-3/user-stories/#us09">US09</a></td><td>3</td><td>2</td><td>2</td><td>2</td><td>1,5</td><td><span class="badge q3" title="Baixo valor / Baixa carga técnica">Q3</span></td><td>3</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-5/user-stories/#us16">US16</a></td><td>3</td><td>2</td><td>2</td><td>2</td><td>1,5</td><td><span class="badge q3" title="Baixo valor / Baixa carga técnica">Q3</span></td><td>3</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-2/user-stories/#us19">US19</a></td><td>3</td><td>2</td><td>2</td><td>2</td><td>1,5</td><td><span class="badge q3" title="Baixo valor / Baixa carga técnica">Q3</span></td><td>3</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-4/user-stories/#us20">US20</a></td><td>3</td><td>2</td><td>2</td><td>2</td><td>1,5</td><td><span class="badge q3" title="Baixo valor / Baixa carga técnica">Q3</span></td><td>3</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-4/user-stories/#us22">US22</a></td><td>3</td><td>2</td><td>2</td><td>2</td><td>1,5</td><td><span class="badge q3" title="Baixo valor / Baixa carga técnica">Q3</span></td><td>3</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-4/user-stories/#us04">US04</a></td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td><span class="badge q3" title="Baixo valor / Baixa carga técnica">Q3</span></td><td>3</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/observacoes-gerais/#us05">US05</a></td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td><span class="badge q3" title="Baixo valor / Baixa carga técnica">Q3</span></td><td>3</td><td class="mvp-no">—</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-2/user-stories/#us18">US18</a></td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td><span class="badge q3" title="Baixo valor / Baixa carga técnica">Q3</span></td><td>3</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-4/user-stories/#us21">US21</a></td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td><span class="badge q3" title="Baixo valor / Baixa carga técnica">Q3</span></td><td>3</td><td class="mvp-yes">✔</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-5/user-stories/#us07">US07</a></td><td>2</td><td>2</td><td>2</td><td>2</td><td>1,5</td><td><span class="badge q4" title="Baixo valor / Baixa carga técnica">Q4</span></td><td>4</td><td class="mvp-no">—</td></tr>
<tr><td><a href="../../organização-e-planejamento/planejamento/sprint-5/user-stories/#us06">US06</a></td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td><span class="badge q4" title="Baixo valor / Baixa carga técnica">Q4</span></td><td>4</td><td class="mvp-no">—</td></tr>
</tbody>
</table>

<div class="legend">
<div class="legend-title">Legenda dos Quadrantes</div>
<div class="legend-item"><span class="badge q1">Q1</span> Alto valor / Baixa carga técnica</div>
<div class="legend-item"><span class="badge q2">Q2</span> Alto valor / Alta carga técnica</div>
<div class="legend-item"><span class="badge q3">Q3</span> Médio valor / Baixa carga técnica</div>
<div class="legend-item"><span class="badge q4">Q4</span> Baixo valor / Baixa carga técnica</div>
</div>
