import 'package:flutter/material.dart';

class Transacao {
  final String titulo;
  final String dataString;
  final DateTime dataReal;
  final double valor;
  final String tipo;

  Transacao({
    required this.titulo,
    required this.dataString,
    required this.dataReal,
    required this.valor,
    required this.tipo,
  });
}

class TransparenciaPage extends StatefulWidget {
  const TransparenciaPage({super.key});

  @override
  State<TransparenciaPage> createState() => _TransparenciaPageState();
}

class _TransparenciaPageState extends State<TransparenciaPage> {
  // Dados temporários para a interface
  final List<Transacao> transacoes = [
    Transacao(titulo: 'Doação anônima', dataString: '20 Maio de 2026', dataReal: DateTime(2026, 5, 20), valor: 50.00, tipo: 'entrada'),
    Transacao(titulo: 'Compra de materiais', dataString: '8 Agosto de 2026', dataReal: DateTime(2026, 8, 8), valor: 423.00, tipo: 'saida'),
    Transacao(titulo: 'Eduardo Franscisco', dataString: '2 Setembro de 2026', dataReal: DateTime(2026, 9, 2), valor: 854.00, tipo: 'entrada'),
    Transacao(titulo: 'Compra de Roupas', dataString: '27 Abril de 2026', dataReal: DateTime(2026, 4, 27), valor: 570.00, tipo: 'saida'),
  ];

  String _filtroSelecionado = 'todos';

  @override
  void initState() {
    super.initState();
    _ordenarTransacoes();
  }

  // Ordenação cronológica decrescente
  void _ordenarTransacoes() {
    transacoes.sort((a, b) => b.dataReal.compareTo(a.dataReal));
  }

  @override
  Widget build(BuildContext context) {
    final corAzulMoveEduca = const Color(0xFF0088FF);
    final corVerdeEntrada = const Color(0xFF4CAF50);
    final corVermelhoSaida = const Color(0xFFE53935);

    return Scaffold(
      backgroundColor: Colors.white,
      body: SingleChildScrollView(
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
                      valor: 'R\$ 15.251,45',
                      corValor: corVerdeEntrada,
                      isSelecionado: _filtroSelecionado == 'entrada',
                      corBorda: corAzulMoveEduca,
                      onTap: () => setState(() => _filtroSelecionado = 'entrada'),
                    ),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    child: _buildResumoCard(
                      titulo: 'Gasto',
                      valor: 'R\$ 4.887,68',
                      corValor: corVermelhoSaida,
                      isSelecionado: _filtroSelecionado == 'saida',
                      corBorda: corAzulMoveEduca,
                      onTap: () => setState(() => _filtroSelecionado = 'saida'),
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
                ),
              ),
              const SizedBox(height: 16),

              ListView.separated(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: transacoes.length,
                separatorBuilder: (context, index) => const Divider(height: 1, color: Colors.black12),
                itemBuilder: (context, index) {
                  final transacao = transacoes[index];
                  final isEntrada = transacao.tipo == 'entrada';
                  final cor = isEntrada ? corVerdeEntrada : corVermelhoSaida;

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
                        transacao.titulo,
                        style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14),
                      ),
                      subtitle: Text(
                        transacao.dataString,
                        style: const TextStyle(fontSize: 12, color: Colors.black54),
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
      ),
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
            color: isSelecionado ? corBorda : Colors.grey[200]!,
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
            Text(titulo, style: TextStyle(color: Colors.grey[600], fontSize: 14)),
            const SizedBox(height: 8),
            Text(valor, style: TextStyle(color: corValor, fontSize: 18, fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }
}