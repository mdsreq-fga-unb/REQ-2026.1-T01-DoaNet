import 'package:flutter/material.dart';
import '../info_fetch/transparencia/fetch_transparencia.dart';
import '../info_fetch/transparencia/transparencia_model.dart';

class TransparenciaPage extends StatefulWidget {
  const TransparenciaPage({super.key});

  @override
  State<TransparenciaPage> createState() => _TransparenciaPageState();
}

class _TransparenciaPageState extends State<TransparenciaPage> {
  String _filtroSelecionado = 'todos';

  String _formatarData(DateTime data) {
    const meses = [
      '', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
      'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ];
    return '${data.day} ${meses[data.month]} de ${data.year}';
  }

  @override
  Widget build(BuildContext context) {
    final corAzulMoveEduca = const Color(0xFF0088FF);
    final corVerdeEntrada = const Color(0xFF4CAF50);
    final corVermelhoSaida = const Color(0xFFE53935);

    return Container(
      color: Colors.white,
      child: FutureBuilder<List<TransacaoModel>>(
        future: FetchTransparencia().fetchTransacoes(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(
              child: Text(
                'Erro ao carregar transações: ${snapshot.error}',
                style: const TextStyle(color: Colors.red),
              ),
            );
          }

          List<TransacaoModel> transacoes = snapshot.data ?? [];
          
          // Ordenação cronológica decrescente
          transacoes.sort((a, b) => b.data.compareTo(a.data));

          double totalArrecadado = 0;
          double totalGasto = 0;

          for (var t in transacoes) {
            if (t.tipo == 'doacao_externa' || t.tipo == 'doacao_interna') {
              totalArrecadado += t.valor;
            } else if (t.tipo == 'despesa') {
              totalGasto += t.valor;
            }
          }

          // Filtragem
          List<TransacaoModel> transacoesFiltradas = transacoes.where((t) {
            if (_filtroSelecionado == 'entrada') {
              return t.tipo == 'doacao_externa' || t.tipo == 'doacao_interna';
            } else if (_filtroSelecionado == 'saida') {
              return t.tipo == 'despesa';
            }
            return true;
          }).toList();

          return SingleChildScrollView(
            child: Padding(
              padding: const EdgeInsets.all(20.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Center(
                    child: Text(
                      'Transparência',
                      style: TextStyle(fontSize: 22, fontWeight: FontWeight.w800),
                    ),
                  ),
                  const SizedBox(height: 32),

                  Row(
                    children: [
                      Expanded(
                        child: _buildResumoCard(
                          titulo: 'Arrecadado',
                          valor: 'R\$ ${totalArrecadado.toStringAsFixed(2).replaceAll('.', ',')}',
                          corValor: corVerdeEntrada,
                          isSelecionado: _filtroSelecionado == 'entrada' || _filtroSelecionado == 'todos',
                          corBorda: const Color(0xFFD9D9D9),
                          onTap: () {
                            setState(() {
                              _filtroSelecionado = _filtroSelecionado == 'entrada' ? 'todos' : 'entrada';
                            });
                          },
                        ),
                      ),
                      const SizedBox(width: 16),
                      Expanded(
                        child: _buildResumoCard(
                          titulo: 'Gasto',
                          valor: 'R\$ ${totalGasto.toStringAsFixed(2).replaceAll('.', ',')}',
                          corValor: corVermelhoSaida,
                          isSelecionado: _filtroSelecionado == 'saida' || _filtroSelecionado == 'todos',
                          corBorda: const Color(0xFFD9D9D9),
                          onTap: () {
                            setState(() {
                              _filtroSelecionado = _filtroSelecionado == 'saida' ? 'todos' : 'saida';
                            });
                          },
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 32),

                  const Text(
                    'Últimas Transações',
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.w600,
                      fontFamily: 'Times New Roman',
                      color: Color(0xFF171616),
                    ),
                  ),
                  const SizedBox(height: 8),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                    decoration: BoxDecoration(
                      color: const Color(0xFFF4F7FB),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        _legendaItem(const Color(0xFF16A34A), 'Doação externa', 'recebida de terceiros (pessoa, empresa ou evento)'),
                        const SizedBox(height: 5),
                        _legendaItem(const Color(0xFF2563EB), 'Doação interna', 'gerada dentro do aplicativo'),
                        const SizedBox(height: 5),
                        _legendaItem(const Color(0xFFE53935), 'Despesa', 'saída de recurso da organização'),
                      ],
                    ),
                  ),
                  const SizedBox(height: 16),

                  if (transacoesFiltradas.isEmpty)
                    const Padding(
                      padding: EdgeInsets.only(top: 20.0),
                      child: Center(
                        child: Text(
                          'Nenhuma transação encontrada.',
                          style: TextStyle(color: Colors.black54),
                        ),
                      ),
                    )
                  else
                    ListView.separated(
                      shrinkWrap: true,
                      physics: const NeverScrollableScrollPhysics(),
                      itemCount: transacoesFiltradas.length,
                      separatorBuilder: (context, index) => const Divider(height: 1, color: Color(0xFFD9D9D9)),
                      itemBuilder: (context, index) {
                        final transacao = transacoesFiltradas[index];
                        final isEntrada = transacao.tipo == 'doacao_externa' || transacao.tipo == 'doacao_interna';
                        final cor = isEntrada ? corVerdeEntrada : corVermelhoSaida;

                        String tipoLabel = '';
                        Color corTipo;
                        if (transacao.tipo == 'doacao_externa') {
                          tipoLabel = 'Doação Externa';
                          corTipo = const Color(0xFF16A34A);
                        } else if (transacao.tipo == 'doacao_interna') {
                          tipoLabel = 'Doação Interna';
                          corTipo = const Color(0xFF2563EB);
                        } else {
                          tipoLabel = 'Despesa';
                          corTipo = const Color(0xFFE53935);
                        }

                        return Padding(
                          padding: const EdgeInsets.symmetric(vertical: 8.0),
                          child: ListTile(
                            contentPadding: EdgeInsets.zero,
                            leading: CircleAvatar(
                              backgroundColor: cor.withValues(alpha: 0.1),
                              child: Icon(
                                isEntrada ? Icons.arrow_upward : Icons.arrow_downward,
                                color: cor,
                                size: 20,
                              ),
                            ),
                            title: Text(
                              transacao.descricao,
                              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14, color: Color(0xFF171616)),
                            ),
                            subtitle: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                const SizedBox(height: 4),
                                Container(
                                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                                  decoration: BoxDecoration(
                                    color: corTipo.withValues(alpha: 0.12),
                                    borderRadius: BorderRadius.circular(999),
                                  ),
                                  child: Text(
                                    tipoLabel,
                                    style: TextStyle(fontSize: 11, color: corTipo, fontWeight: FontWeight.w700),
                                  ),
                                ),
                                const SizedBox(height: 3),
                                Text(
                                  _formatarData(transacao.data),
                                  style: const TextStyle(fontSize: 12, color: Color(0xFF505050)),
                                ),
                              ],
                            ),
                            trailing: Text(
                              '${isEntrada ? '+' : '-'} R\$ ${transacao.valor.toStringAsFixed(2).replaceAll('.', ',')}',
                              style: TextStyle(
                                fontWeight: FontWeight.w900,
                                color: cor,
                                fontSize: 14,
                              ),
                            ),
                          ),
                        );
                      },
                    ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }

  Widget _legendaItem(Color cor, String label, String descricao) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: const EdgeInsets.only(top: 3),
          child: CircleAvatar(radius: 4, backgroundColor: cor),
        ),
        const SizedBox(width: 6),
        Expanded(
          child: RichText(
            text: TextSpan(
              style: const TextStyle(fontSize: 11, color: Color(0xFF505050)),
              children: [
                TextSpan(text: '$label ', style: TextStyle(fontWeight: FontWeight.w700, color: cor)),
                TextSpan(text: '— $descricao'),
              ],
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildResumoCard({
    required String titulo,
    required String valor,
    required Color corValor,
    required bool isSelecionado,
    required Color corBorda,
    required VoidCallback onTap,
  }) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 20),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(12),
          border: Border.all(
            color: isSelecionado ? corBorda : const Color(0xFFD9D9D9),
            width: isSelecionado ? 2 : 1,
          ),
          boxShadow: [
            if (!isSelecionado)
              BoxShadow(
                color: Colors.black.withValues(alpha: 0.05),
                blurRadius: 10,
                offset: const Offset(0, 4),
              ),
          ],
        ),
        child: Column(
          children: [
            Text(titulo, style: const TextStyle(color: Color(0xFF171616), fontSize: 14)),
            const SizedBox(height: 8),
            Text(valor, style: TextStyle(color: corValor, fontSize: 18, fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }
}